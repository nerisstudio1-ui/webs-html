#!/usr/bin/env python3
"""
Genera la versión de la web para pegar en un bloque de HTML personalizado de
WordPress (o de cualquier gestor).

    python3 build/build_widget.py

Escribe en `wordpress/`:

    widget-ca.html                 catalán, con los archivos por URL
    widget-es.html                 castellano, con los archivos por URL
    widget-ca-autocontenido.html   catalán, con tipografías y fotos dentro
    widget-es-autocontenido.html   castellano, ídem

El problema de pegar una web entera en un tema es que las dos hojas de estilo se
pisan: el tema define `.card`, `.section`, `.btn`, `body`… igual que nosotros.
Aquí se resuelve así:

1. Todo va dentro de `<div id="laconic-app">` y **cada** selector del CSS se
   prefija con ese id. Un `#laconic-app .card` (especificidad 1,1,0) gana a
   cualquier `.card` del tema (0,1,0), y a la vez nuestras reglas no salen del
   contenedor.
2. Las reglas globales (`html`, `body`, `*`, `p`, `a`…) se reescriben para
   aplicarse solo dentro del contenedor.
3. Los identificadores de las secciones se prefijan con `lac-` para no chocar
   con los del tema.
4. La cabecera pasa de `fixed` a `sticky` y las secciones se sacan a todo el
   ancho de la ventana, porque el tema las mete en una columna estrecha.
5. El JavaScript solo mira dentro del contenedor.
"""
import base64
import io
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEST = ROOT / 'wordpress'
APP = '#laconic-app'

# Marcador que el usuario sustituye por la URL donde suba la carpeta assets
BASE = '__BASE__'


# --------------------------------------------------------------------------- #
# CSS
# --------------------------------------------------------------------------- #

def scope_css(css):
    # 1. Reglas globales -> el contenedor
    css = css.replace(':root {', APP + ' {', 1)

    # El bloque html{} deja de tener sentido: el scroll suave lo hace el JS
    css = re.sub(r'\nhtml \{[^}]*\}\n', '\n', css, count=1)

    css = re.sub(r'\nbody \{', '\n' + APP + ' {', css, count=1)
    css = css.replace('*,\n*::before,\n*::after {',
                      APP + ',\n' + APP + ' *,\n' + APP + ' *::before,\n' + APP + ' *::after {')
    css = css.replace('body.menu-open', APP + '.is-menu-open')
    css = css.replace('body.cursor-on', APP + '.cursor-on')
    # Estas clases van en el propio contenedor, no en un ancestro: el selector
    # tiene que ir pegado al id, no separado por un espacio.
    css = css.replace('.has-js ', APP + '.has-js ')
    css = css.replace('.is-loaded ', APP + '.is-loaded ')
    css = css.replace('::selection {', APP + ' ::selection {')
    css = css.replace(':focus-visible {', APP + ' :focus-visible {')
    css = re.sub(r'\nhtml \{[^}]*\}', '', css)  # por si queda alguno en media queries

    # 2. Prefijar el resto de selectores
    fuera = ('@', '}', '/*', '*/')
    salida = []
    dentro_de_arroba = 0
    saltar_bloque = False
    for linea in css.split('\n'):
        strip = linea.strip()

        if strip.startswith('@font-face') or strip.startswith('@keyframes'):
            saltar_bloque = True
        if saltar_bloque:
            salida.append(linea)
            if strip == '}':
                saltar_bloque = False
            continue
        if strip.startswith('@media') or strip.startswith('@supports'):
            dentro_de_arroba += 1
            salida.append(linea)
            continue
        if strip == '}' and dentro_de_arroba and not linea.startswith('  '):
            dentro_de_arroba -= 1
            salida.append(linea)
            continue

        # ¿Es una línea de selector? Termina en , o en {
        if strip and not strip.startswith(fuera) and (strip.endswith(',') or strip.endswith('{')):
            partes = []
            for sel in strip.rstrip('{').rstrip().split(','):
                sel = sel.strip()
                if not sel:
                    continue
                if sel.startswith(APP) or sel.startswith('from') or sel.startswith('to') or sel.endswith('%'):
                    partes.append(sel)
                else:
                    partes.append(APP + ' ' + sel)
            indent = linea[:len(linea) - len(linea.lstrip())]
            cierre = ' {' if strip.endswith('{') else ','
            salida.append(indent + ',\n'.join(partes) + cierre)
        else:
            salida.append(linea)
    css = '\n'.join(salida)

    # 3. La cabecera no puede ser fixed dentro de un tema: pasa a sticky, por
    #    encima de la del tema y desplazada su altura con --lac-top.
    css = css.replace(APP + ''' .header {
  position: fixed;
  inset: 0 0 auto 0;
  z-index: 50;''', APP + ''' .header {
  position: sticky;
  top: var(--lac-top, 0px);
  width: 100%;
  z-index: 1000;''')

    # El escenario del hero se queda pegado justo debajo
    css = css.replace('''.hero__stage {
  position: sticky;
  top: 0;
  height: 100svh;''', '''.hero__stage {
  position: sticky;
  top: var(--lac-top, 0px);
  height: calc(100svh - var(--lac-top, 0px));''')
    css = css.replace('''.svc__media {
    position: sticky;
    top: 15vh;''', '''.svc__media {
    position: sticky;
    top: calc(15vh + var(--lac-top, 0px));''')
    css = css.replace('''  .process__head {
    position: sticky;
    top: 20vh;''', '''  .process__head {
    position: sticky;
    top: calc(20vh + var(--lac-top, 0px));''')

    # 4. El grano cubre el contenedor, no toda la ventana
    css = css.replace(APP + ''' .grain {
  position: fixed;''', APP + ''' .grain {
  position: absolute;''')

    # 5. Reinicio dentro del contenedor
    #
    #    Cualquier propiedad que el tema declare y nosotros no, se cuela: fondos,
    #    bordes, subrayados, viñetas… Por eso el contenedor arranca con su propio
    #    reinicio. Va con especificidad baja (el * suma 1,0,0 con el id) para que
    #    todas nuestras reglas, que llevan clase, lo pisen sin esfuerzo.
    reinicio = (
        APP + ',\n' + APP + ' *,\n' + APP + ' *::before,\n' + APP + ' *::after {\n'
        '  background: none;\n'
        '  border: 0;\n'
        '  border-radius: 0;\n'
        '  box-shadow: none;\n'
        '  outline: 0;\n'
        '  text-decoration: none;\n'
        # Estas se heredan, y ahí está la trampa: si aquí les damos un valor
        # fijo, el hijo (que también encaja con el *) deja de heredar lo que
        # declara el padre, y una regla que encaja siempre gana a la herencia.
        # Así se perdían las mayúsculas de .slab__meta en sus <span>. Con
        # `inherit` el valor del tema no entra y el nuestro sigue bajando: eso
        # tapa además las que el tema pone por etiqueta (`h2 { color }`,
        # `.entry-content p { color }`, `.btn { font-family }`…), que si no se
        # cuelan en cuanto nosotros heredamos en vez de declarar.
        '  color: inherit;\n'
        '  font-family: inherit;\n'
        '  font-style: inherit;\n'
        '  font-variant: inherit;\n'
        '  line-height: inherit;\n'
        '  letter-spacing: inherit;\n'
        '  text-transform: inherit;\n'
        '  text-shadow: inherit;\n'
        '  list-style: none;\n'
        '  float: none;\n'
        '  clear: none;\n'
        '  min-width: 0;\n'
        '  max-height: none;\n'
        '  transition: none;\n'
        '  animation: none;\n'
        '}\n'
        # El contenedor sí las fija, para no heredarlas del tema. El resto
        # (font-family, color, line-height, letter-spacing) las pone la regla
        # que sale del `body` de nuestra hoja, que va después de este reinicio.
        + APP + ' {\n'
        '  font-style: normal;\n'
        '  font-variant: normal;\n'
        '  text-align: left;\n'
        '  text-transform: none;\n'
        '  text-shadow: none;\n'
        '}\n'
        + ',\n'.join(APP + ' ' + e for e in
                     ('h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'figure',
                      'blockquote', 'form', 'fieldset'))
        + ' {\n  margin: 0;\n  padding: 0;\n}\n'
        # El énfasis sí va en cursiva: títulos de libro, por ejemplo
        + APP + ' em {\n  font-style: italic;\n}\n'
        + APP + ' img {\n  display: block;\n  max-width: 100%;\n  height: auto;\n}\n\n'
    )
    css = reinicio + css

    # 6. Salida a todo el ancho: una sola vez, en el contenedor
    css += '''

/* ---------- Ajustes para vivir dentro de un tema ---------- */
''' + APP + ''' {
  position: relative;
  isolation: isolate;
  margin: 0;
  padding: 0;
  text-align: left;
  /* Si el tema tiene cabecera fija o pegada, poner aquí su altura para que la
     nuestra y el hero queden justo debajo. Con 0px se comporta como la web
     suelta. */
  --lac-top: 0px;
  /* El tema mete el contenido en una columna estrecha. El contenedor sale a todo
     el ancho de la ventana una sola vez y dentro todo funciona igual que en la
     web suelta; clip evita que aparezca barra horizontal. */
  width: 100vw;
  max-width: 100vw;
  margin-inline: calc(50% - 50vw);
  overflow-x: clip;
}
''' + APP + ''' .wrap {
  box-sizing: border-box;
}
'''
    return css


# --------------------------------------------------------------------------- #
# HTML
# --------------------------------------------------------------------------- #

IDS = ['estudi', 'serveis', 'treball', 'proces', 'recursos', 'contacte',
       'estudio', 'servicios', 'trabajo', 'proceso', 'contacto',
       'mobile-menu', 'top', 'nombre', 'marca', 'email', 'mensaje', 'servicios-label',
       'lg-zero', 'lg-word', 'lg-lockup']


def scope_html(html, lang, prefix_assets):
    cuerpo = html[html.index('<body>') + len('<body>'):html.index('</body>')]

    # Fuera las hojas y el script: van dentro del widget
    cuerpo = re.sub(r'<script src="[^"]*main\.js"[^>]*></script>', '', cuerpo)

    # Rutas de los archivos
    rel = 'assets/' if lang == 'ca' else '../assets/'
    cuerpo = cuerpo.replace('"' + rel, '"' + prefix_assets + 'assets/')
    cuerpo = cuerpo.replace(' ' + rel, ' ' + prefix_assets + 'assets/')  # srcset

    # Identificadores propios, para no chocar con los del tema
    for i in IDS:
        cuerpo = cuerpo.replace('id="%s"' % i, 'id="lac-%s"' % i)
        cuerpo = cuerpo.replace('href="#%s"' % i, 'href="#lac-%s"' % i)
        cuerpo = cuerpo.replace('for="%s"' % i, 'for="lac-%s"' % i)
        cuerpo = cuerpo.replace('aria-controls="%s"' % i, 'aria-controls="lac-%s"' % i)
        cuerpo = cuerpo.replace('aria-labelledby="%s"' % i, 'aria-labelledby="lac-%s"' % i)
        cuerpo = cuerpo.replace('href="#%s"' % i, 'href="#lac-%s"' % i)
        cuerpo = cuerpo.replace('#%s"/>' % i, '#lac-%s"/>' % i)  # <use href="#lg-zero"/>

    # Los vídeos nunca se meten dentro del archivo, ni en la versión
    # autocontenida: siempre se sirven por URL. Su póster va con ellos.
    if not prefix_assets:
        cuerpo = cuerpo.replace('"assets/video/', '"' + BASE + 'assets/video/')
        cuerpo = re.sub(r'poster="assets/', 'poster="' + BASE + 'assets/', cuerpo)

    # El cambio de idioma apunta a la otra página de WordPress. En la versión
    # autocontenida no dejamos marcador: se pega y funciona, con la ruta más
    # probable (/es/ y /). Si la página de castellano acaba en otra dirección,
    # se cambia ese enlace y ya está.
    if prefix_assets:
        otra = '__URL_ES__' if lang == 'ca' else '__URL_CA__'
    else:
        otra = '/es/' if lang == 'ca' else '/'
    cuerpo = re.sub(r'href="(es/|\.\./)" hreflang', 'href="%s" hreflang' % otra, cuerpo)

    return cuerpo.strip()


# --------------------------------------------------------------------------- #
# JS
# --------------------------------------------------------------------------- #

def scope_js(js):
    js = js.replace('(function () {\n  "use strict";',
                    '''(function () {
  "use strict";

  // Todo se busca dentro del contenedor del widget, nunca en el resto del tema
  var APP = document.getElementById("laconic-app");
  if (!APP) return;''')
    js = js.replace('document.documentElement.classList.add("is-loaded")',
                    'APP.classList.add("is-loaded")')
    js = js.replace('document.documentElement.classList.add("has-js")',
                    'APP.classList.add("has-js")')
    js = js.replace('document.querySelectorAll(', 'APP.querySelectorAll(')
    js = js.replace('document.querySelector(', 'APP.querySelector(')
    js = js.replace('document.body.classList.toggle("menu-open", open)',
                    'APP.classList.toggle("is-menu-open", open)')
    js = js.replace('document.body.classList.contains("menu-open")',
                    'APP.classList.contains("is-menu-open")')
    js = js.replace('document.body.classList.add("cursor-on")', 'APP.classList.add("cursor-on")')
    js = js.replace('document.body.classList.remove("cursor-on")', 'APP.classList.remove("cursor-on")')
    js = js.replace('document.documentElement.dataset.on = entry.target.dataset.theme;',
                    'APP.dataset.on = entry.target.dataset.theme;')

    # Dentro de una página, la cabecera no está en la parte alta de la ventana:
    # el widget empieza más abajo. Así que "pegada" y color de la cabecera se
    # deciden por la posición real de la cabecera, no por window.scrollY ni por
    # qué sección cruza el borde de la ventana.
    js = js.replace('''      header.classList.toggle("is-stuck", y > 60);''',
                    '''      var caja = header.getBoundingClientRect();
      header.classList.toggle("is-stuck", caja.top <= 1);''')
    js = js.replace('''        header.classList.toggle("is-hidden", y > lastY && y > 400);''',
                    '''        header.classList.toggle("is-hidden", y > lastY && caja.top <= 1);''')

    # El color de la cabecera lo da la sección que hay justo detrás de ella
    inicio = js.index('    if (temas.length && "IntersectionObserver" in window) {')
    fin = js.index('  /* ---- Menú móvil ---- */')
    js = js[:inicio] + '''    if (temas.length) {
      var pintarCabecera = function () {
        var linea = header.getBoundingClientRect().bottom - 2;
        for (var i = 0; i < temas.length; i++) {
          var r = temas[i].getBoundingClientRect();
          if (r.top <= linea && r.bottom > linea) {
            header.dataset.on = temas[i].dataset.theme;
            APP.dataset.on = temas[i].dataset.theme;
            return;
          }
        }
      };
      window.addEventListener("scroll", pintarCabecera, { passive: true });
      window.addEventListener("resize", pintarCabecera);
      pintarCabecera();
    }
  }

''' + js[fin:]

    # El contenedor arranca con has-js, y el scroll suave lo hacemos aquí porque
    # ya no tocamos el html del tema
    js = js.replace('})();', '''
  /* ---- Scroll suave de los enlaces internos, con margen para la cabecera ---- */
  APP.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var destino = document.getElementById(a.getAttribute("href").slice(1));
      if (!destino) return;
      e.preventDefault();
      var top = destino.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top: top, behavior: reduced ? "auto" : "smooth" });
    });
  });
})();''')
    return js


# --------------------------------------------------------------------------- #
# Empaquetado
# --------------------------------------------------------------------------- #

def fuentes_css(inline):
    css = (ROOT / 'assets/css/fonts.css').read_text(encoding='utf-8')
    if inline:
        return re.sub(
            r'url\(\.\./fonts/([^)]+)\)',
            lambda m: 'url(data:font/woff2;base64,'
                      + base64.b64encode((ROOT / 'assets/fonts' / m.group(1)).read_bytes()).decode()
                      + ')', css)
    return css.replace('url(../fonts/', 'url(' + BASE + 'assets/fonts/')


def inline_imagenes(html):
    """Sustituye las fotos por data URI y quita el srcset."""
    html = re.sub(r'\s*srcset="[^"]*"', '', html)
    html = re.sub(r'\s*sizes="[^"]*"', '', html)
    from PIL import Image
    for stem in sorted(set(re.findall(r'proyectos/([a-z0-9-]+)-1100\.jpg', html))):
        im = Image.open(ROOT / f'assets/img/proyectos/{stem}-1100.jpg').convert('RGB')
        w = 900
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'JPEG', quality=80, optimize=True, progressive=True)
        uri = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
        html = re.sub(r'src="[^"]*proyectos/' + stem + r'-1100\.jpg"', 'src="%s"' % uri, html)
    return html


def construir(lang, autocontenido):
    src = ROOT / ('index.html' if lang == 'ca' else 'es/index.html')
    html = src.read_text(encoding='utf-8')
    css = scope_css((ROOT / 'assets/css/main.css').read_text(encoding='utf-8'))
    js = scope_js((ROOT / 'assets/js/main.js').read_text(encoding='utf-8'))
    cuerpo = scope_html(html, lang, '' if autocontenido else BASE)
    if autocontenido:
        cuerpo = inline_imagenes(cuerpo)

    aviso = ('<!-- Laconic Studio — bloque de HTML personalizado (%s).\n'
             '     Pegar tal cual en un bloque "HTML personalizado" de WordPress.\n'
             '%s -->\n')
    if autocontenido:
        nota = ('     Todo va dentro del archivo: tipografías, fotos, estilos y guion.\n'
                '     No hay nada que subir ni nada que sustituir.\n'
                '     El enlace de idioma apunta a %s; si la otra página acaba en\n'
                '     otra dirección, se cambia ese enlace.'
                % ('/es/' if lang == 'ca' else '/'))
    else:
        nota = ('     Antes de pegar: sustituir %s por la URL de la carpeta assets,\n'
                '     por ejemplo https://tudominio.com/wp-content/uploads/laconic/\n'
                '     y %s por la URL de la otra versión de idioma.'
                % (BASE, '__URL_ES__' if lang == 'ca' else '__URL_CA__'))
    aviso = aviso % (lang.upper(), nota)

    partes = [aviso,
              '<style>',
              fuentes_css(autocontenido),
              css,
              '</style>',
              '',
              '<div id="laconic-app">',
              cuerpo,
              '</div>',
              '',
              '<script>',
              js,
              '</script>']
    return '\n'.join(partes) + '\n'


def main():
    DEST.mkdir(exist_ok=True)
    for lang in ('ca', 'es'):
        for auto in (False, True):
            nombre = 'widget-%s%s.html' % (lang, '-autocontenido' if auto else '')
            texto = construir(lang, auto)
            (DEST / nombre).write_text(texto, encoding='utf-8')
            print('%-34s %6.2f MB' % (nombre, len(texto.encode()) / 1024 / 1024))


if __name__ == '__main__':
    main()
