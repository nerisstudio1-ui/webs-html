#!/usr/bin/env python3
"""
Genera la versión de la web para pegar en un bloque de HTML personalizado de
WordPress (o de cualquier gestor).

    python3 build/build_widget.py

Escribe en `wordpress/`:

    widget-ca.html                 catalán, con los archivos por URL (130 KB)
    widget-es.html                 castellano, ídem
    widget-ca-copiar-pegar.html    catalán, con todo dentro menos los .mp4 (3 MB)
    widget-es-copiar-pegar.html    castellano, ídem

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
6. La marca `has-js` —la que permite que los bloques empiecen escondidos para
   entrar al hacer scroll— se pone en el contenedor y no en el `<html>` del tema,
   con una red de seguridad: si el guion no llega a arrancar porque un plugin lo
   ha roto, la marca se retira y la web se ve entera, sin animaciones.
"""
import base64
import datetime
import io
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEST = ROOT / 'wordpress'
APP = '#laconic-app'

# Marcador que el usuario sustituye por la URL donde suba la carpeta assets
BASE = '__BASE__'

# Sello de generación. Va en el comentario de cabecera de los cuatro archivos
# para poder saber qué versión está publicada de verdad: si la web sirve una
# copia en caché de antes, en el código fuente de la página aparecerá un sello
# viejo. Se busca con Ctrl+U y Ctrl+F, «Generado».
SELLO = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

# Vídeos ya subidos a la Biblioteca de medios de WordPress.
#
# Van como ruta desde la raíz del dominio, sin `https://dominio`, a propósito: el
# sitio está de momento en el dominio de pruebas de Hostinger
# (darkviolet-partridge-547677.hostingersite.com) y al conectar el definitivo
# estas rutas seguirán resolviendo solas. Con la URL completa habría que
# reemplazarlas una a una.
#
# WordPress cambia el nombre del archivo al subirlo (mete guiones donde encuentra
# ciertas secuencias), así que estos nombres son los que devolvió el panel, no los
# de los archivos originales.
CARPETA_WP = '/wp-content/uploads/2026/08/'
VIDEOS_WORDPRESS = {
    'quality-1': 'SaveClip.App_AQNGmLNHLGiFU9jlnXVKT2ZTtiSuHIAXimbueKtPY6wd2bGcTUdY'
                 '_qu04_bKFnE2nSWoPuglzN2pdciWazSeGuvtksqPb3KGlhxDjr8.mp4',
    'malhivern-1': 'SaveClip.App_AQMSZ3boGR5agJ7If7Wa-Ydn36pldFkvnxjJGkcYEIMSpLz2R7T'
                   '_qK3WYX6RbpTZMmqp5BT7JlaJcqwII2wp_gCQjfPnRqPElfeSddM.mp4',
    'jordi-coll-1': 'SaveClip.App_AQNS2Ec6oy9vSJAV-da-cldU22A56AM9Li009TWgQvCXM4PHD33eA80Dq'
                    '_GteYQnpFsn8XSnFV1G7ry1Kclem41v.mp4',
    'puig-1': 'SaveClip.App_AQM3VYtfZNzijSNtRXjDuO_lcED8X0m2o9ldGC5tbg2BILJT5jHHIwBgBkSSANH9'
              'P3ZKMH92GnYktmVwknUt1KlHcq2FVBEqgMHYwYI.mp4',
}


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
    #
    # Ojo con lo que cuenta como selector. La regla «acaba en coma o en llave» no
    # basta: un degradado escrito en varias líneas también tiene líneas que acaban
    # en coma, y prefijarlas mete el id dentro del valor y lo invalida —así se
    # quedó el inicio de WordPress sin la sombra que hace legible el logotipo—.
    # Por eso se lleva la cuenta de las llaves: dentro del cuerpo de una regla no
    # se toca nada.
    fuera = ('@', '}', '/*', '*/')
    salida = []
    pila = []            # qué abrió cada llave: 'arroba' o 'regla'
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
            pila.append('arroba')
            salida.append(linea)
            continue

        if strip.startswith('}'):
            if pila:
                pila.pop()
            salida.append(linea)
            continue

        # Solo se prefija en el nivel de los selectores: nunca dentro de una regla
        nivel_selector = 'regla' not in pila

        if (nivel_selector and strip and not strip.startswith(fuera)
                and (strip.endswith(',') or strip.endswith('{'))):
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
            if strip.endswith('{'):
                pila.append('regla')
        else:
            salida.append(linea)
            if strip.endswith('{'):
                pila.append('regla')
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

    # La primera pantalla descuenta la cabecera del tema, para que el logotipo
    # quede centrado en lo que se ve y no detrás de la barra de arriba.
    css = css.replace('''.hero {
  position: relative;
  height: 100svh;''', '''.hero {
  position: relative;
  height: calc(100svh - var(--lac-top, 0px));''')

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
        # Un tema con `video { filter: invert(1) }` o `img { mix-blend-mode }`
        # nos repintaba los reels: no las declaramos en ningún sitio, así que
        # ganaba él. Nuestras reglas llevan clase y pisan esto sin esfuerzo.
        '  filter: none;\n'
        '  mix-blend-mode: normal;\n'
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
  if (!APP) return;

  // Señal de vida para la red de seguridad del principio del bloque: si esto no
  // llega a ejecutarse, retira has-js y la web se ve entera, sin animaciones.
  APP.classList.add("lac-ok");''')
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

    # Dentro de una página, la cabecera no está en la parte alta de la ventana:
    # el widget empieza más abajo. Así que "pegada" se decide por la posición
    # real de la cabecera, no por window.scrollY.
    js = js.replace('''      header.classList.toggle("is-stuck", y > 60);''',
                    '''      var caja = header.getBoundingClientRect();
      header.classList.toggle("is-stuck", caja.top <= 1);''')
    js = js.replace('''        header.classList.toggle("is-hidden", y > lastY && y > 400);''',
                    '''        header.classList.toggle("is-hidden", y > lastY && caja.top <= 1);''')

    # El scroll suave se hace aquí porque ya no tocamos el html del tema (la
    # marca has-js la pone GUARDIA, al principio del contenedor)
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

# En la web normal, `has-js` se pone en el <head>: es la marca de que hay guion y
# de que, por tanto, los bloques pueden empezar escondidos para entrar al hacer
# scroll. Aquí no tocamos el <head> del tema, así que se pone en el contenedor, y
# desde dentro del propio contenedor para que no haya parpadeo: cuando el
# navegador llega a esta línea todavía no ha pintado el resto del bloque.
#
# Y va con red. Si un plugin de caché aplaza, combina o rompe el guion grande, sin
# esta salvaguarda todo lo que entra al hacer scroll se quedaría escondido para
# siempre: la página, medio en blanco. Así que se comprueba si el guion arrancó
# —él pone `lac-ok` en su primera línea— y, si no, se retira la marca y todo se ve,
# sin animaciones pero completo.
#
# Se mira poco después del load, que es cuando ya han corrido hasta los guiones
# que el plugin haya aplazado, con un tope de 6 s por si el load no llega nunca.
GUARDIA = (
    '<script>(function(){var a=document.getElementById("laconic-app");if(!a)return;'
    'a.classList.add("has-js");'
    'var r=function(){if(!a.classList.contains("lac-ok"))a.classList.remove("has-js");};'
    'if(document.readyState==="complete"){setTimeout(r,300);}'
    'else{window.addEventListener("load",function(){setTimeout(r,300);});}'
    'setTimeout(r,6000);})();</script>')


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
    """Mete todas las fotos dentro como data URI y quita el srcset.

    Recorre las rutas que hay en el HTML en lugar de una carpeta concreta: así
    una foto nueva (la del hero, por ejemplo) no se queda fuera y con la ruta
    relativa rota.
    """
    html = re.sub(r'\s*srcset="[^"]*"', '', html)
    html = re.sub(r'\s*sizes="[^"]*"', '', html)
    from PIL import Image
    rutas = set(re.findall(r'(?:src|poster)="((?:__BASE__)?assets/img/[^"]+\.jpg)"', html))
    for ruta in sorted(rutas):
        rel = ruta.replace(BASE, '')
        im = Image.open(ROOT / rel).convert('RGB')
        w = min(900, im.width)
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'JPEG', quality=80, optimize=True, progressive=True)
        uri = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
        html = html.replace('"%s"' % ruta, '"%s"' % uri)
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
             '     Generado: %s\n'
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
    aviso = aviso % (lang.upper(), SELLO, nota)

    partes = [aviso,
              '<style>',
              fuentes_css(autocontenido),
              css,
              '</style>',
              '',
              '<div id="laconic-app">',
              GUARDIA,
              cuerpo,
              '</div>',
              '',
              '<script>',
              js,
              '</script>']
    return '\n'.join(partes) + '\n'


def copiar_pegar(lang):
    """Versión sin nada que subir por FTP.

    Mete dentro del archivo las tipografías, las fotos y también los pósters de
    los vídeos, que son pequeños. Lo único que queda fuera son los cuatro `.mp4`:
    45 MB de base64 dentro de una entrada de WordPress no es viable. En su lugar
    deja un marcador por vídeo, `__VIDEO_quality-1__`, para pegar la URL que da la
    Biblioteca de medios al subirlo. Cuatro sustituciones y sin tocar el FTP.
    """
    from PIL import Image
    html = construir(lang, autocontenido=True)

    # Los pósters sí caben dentro
    for ruta in sorted(set(re.findall(r'__BASE__(assets/video/[^"]+\.jpg)', html))):
        im = Image.open(ROOT / ruta).convert('RGB')
        w = min(720, im.width)
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'JPEG', quality=78, optimize=True, progressive=True)
        html = html.replace(BASE + ruta,
                            'data:image/jpeg;base64,'
                            + base64.b64encode(buf.getvalue()).decode())

    # Y los vídeos apuntan a la Biblioteca de medios si ya están subidos; si no,
    # se queda un marcador con el nombre del proyecto para pegar su URL a mano.
    for ruta in sorted(set(re.findall(r'__BASE__assets/video/([^"]+\.mp4)', html))):
        clave = ruta[:-4]
        destino = (CARPETA_WP + VIDEOS_WORDPRESS[clave] if clave in VIDEOS_WORDPRESS
                   else '__VIDEO_%s__' % clave)
        html = html.replace(BASE + 'assets/video/' + ruta, destino)

    aviso = ('<!-- Laconic Studio — bloque de HTML personalizado (%s), para copiar y pegar.\n'
             '     Generado: %s\n'
             '\n'
             '     Tipografías, fotos y pósters van DENTRO de este archivo, y los cuatro\n'
             '     vídeos apuntan ya a la Biblioteca de medios. No hay nada que subir ni\n'
             '     nada que sustituir: se copia todo y se pega.\n'
             '\n'
             '     Los vídeos van como ruta desde la raíz (/wp-content/uploads/...), sin\n'
             '     el dominio, así que seguirán funcionando cuando el sitio pase del\n'
             '     dominio de pruebas al definitivo.\n'
             '\n'
             '     El enlace de idioma apunta a %s. Si la otra página acaba en otra\n'
             '     dirección, cambia ese enlace (sale tres veces). -->\n'
             % (lang.upper(), SELLO, '/es/' if lang == 'ca' else '/'))
    return re.sub(r'^<!--.*?-->\n', aviso, html, count=1, flags=re.S)


def main():
    DEST.mkdir(exist_ok=True)
    for lang in ('ca', 'es'):
        for nombre, texto in (
                ('widget-%s.html' % lang, construir(lang, autocontenido=False)),
                ('widget-%s-copiar-pegar.html' % lang, copiar_pegar(lang))):
            (DEST / nombre).write_text(texto, encoding='utf-8')
            print('%-34s %6.2f MB' % (nombre, len(texto.encode()) / 1024 / 1024))


if __name__ == '__main__':
    main()
