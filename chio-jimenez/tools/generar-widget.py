# -*- coding: utf-8 -*-
"""Genera una versión de la web en un solo archivo, para pegar en un widget."""
import re, os

RAIZ = '/home/user/webs-html/chio-jimenez'
SALIDA = '/tmp/claude-0/-home-user-webs-html/4222ec57-bb53-5365-b8aa-568195089d83/scratchpad/entrega/chio-jimenez-widget.html'
AMBITO = '.cj'          # todo queda encerrado aquí dentro

html = open(os.path.join(RAIZ,'index.html'), encoding='utf-8').read()
css  = open(os.path.join(RAIZ,'assets/styles.css'), encoding='utf-8').read()
js   = open(os.path.join(RAIZ,'assets/script.js'), encoding='utf-8').read()

# ---------- 1. Acotar el CSS al contenedor ----------
def acotar_selector(sel):
    sel = sel.strip()
    if not sel or sel.startswith('@') or sel.startswith('%') or re.match(r'^\d', sel):
        return sel
    partes = []
    for s in sel.split(','):
        s = s.strip()
        if not s:
            continue
        if s in (':root', 'html', 'body'):
            partes.append(AMBITO)
        elif s.startswith('html ') or s.startswith('body '):
            partes.append(AMBITO + ' ' + s.split(' ', 1)[1])
        elif s.startswith('::selection'):
            partes.append(AMBITO + ' ' + s)
        elif s.startswith(AMBITO):
            partes.append(s)
        else:
            partes.append(AMBITO + ' ' + s)
    return ', '.join(partes)

def acotar_bloque(texto):
    fuera, i, n = [], 0, len(texto)
    while i < n:
        # comentarios
        if texto.startswith('/*', i):
            j = texto.find('*/', i) + 2
            fuera.append(texto[i:j]); i = j; continue
        # at-rules
        m = re.match(r'@[\w-]+[^{;]*', texto[i:])
        if m:
            cabecera = m.group(0)
            j = i + len(cabecera)
            if j < n and texto[j] == '{':
                cuerpo, fin = extraer_bloque(texto, j)
                if cabecera.lstrip().startswith(('@media', '@supports')):
                    fuera.append(cabecera + '{' + acotar_bloque(cuerpo) + '}')
                else:                       # @keyframes y demás: intactos
                    fuera.append(cabecera + '{' + cuerpo + '}')
                i = fin; continue
            k = texto.find(';', i) + 1
            fuera.append(texto[i:k]); i = k; continue
        # regla normal
        llave = texto.find('{', i)
        if llave == -1:
            fuera.append(texto[i:]); break
        sel = texto[i:llave]
        cuerpo, fin = extraer_bloque(texto, llave)
        fuera.append(acotar_selector(sel) + '{' + cuerpo + '}')
        i = fin
    return ''.join(fuera)

def extraer_bloque(texto, pos_llave):
    """Devuelve (contenido, índice tras la llave de cierre)."""
    prof, i = 0, pos_llave
    while i < len(texto):
        if texto[i] == '{': prof += 1
        elif texto[i] == '}':
            prof -= 1
            if prof == 0:
                return texto[pos_llave+1:i], i+1
        i += 1
    return texto[pos_llave+1:], len(texto)

escudo = """
/* Escudo: impide que los estilos del tema de WordPress se cuelen dentro.
   Va el primero, así cualquier regla propia de abajo lo sobrescribe. */
.cj, .cj *, .cj *::before, .cj *::after{
  margin:0; padding:0;
  border:0; border-radius:0;
  box-shadow:none; text-shadow:none;
  outline:none; float:none;
  list-style:none; text-decoration:none;
  text-transform:none; letter-spacing:normal;
  font-style:normal; text-align:left;
  max-width:none; min-width:0;
}
.cj{ isolation:isolate; }
"""
remate = """
/* El selector de idioma ya no vive en la cabecera, sino en la portada. */
.cj .hero__inner .lang{ margin-bottom:20px; }
"""
css_acotado = escudo + acotar_bloque(css) + remate

# la tipografía, como @import al principio de la hoja
fuente = '@import url("https://fonts.googleapis.com/css2?family=Archivo:wght@300;400;500;600&display=swap");\n'

# ---------- 2. Quedarnos con el cuerpo del HTML ----------
cuerpo = html[html.index('<body>')+len('<body>') : html.index('</body>')]
cuerpo = re.sub(r'<script src="assets/script\.js"[^>]*></script>', '', cuerpo)

# ---------- 2b. Fuera la cabecera fija ----------
# WordPress ya pone su propio menú arriba, y además la cabecera va en
# position:fixed: dentro de una página se quedaría flotando por encima del
# tema. Se retira y el selector de idioma se traslada a la portada.
m = re.search(r'<div class="lang".*?</div>', cuerpo, re.S)
selector_idioma = m.group(0) if m else ''
cuerpo = re.sub(r'<header class="nav".*?</header>', '', cuerpo, flags=re.S)
if selector_idioma:
    cuerpo = cuerpo.replace(
        '      <p class="eyebrow reveal" data-i18n="hero.eyebrow">',
        '      ' + selector_idioma + '\n      <p class="eyebrow reveal" data-i18n="hero.eyebrow">',
        1)

# el JS espera encontrar la cabecera: si no está, sigue adelante sin ella
js = js.replace(
    "    var nav = $('#nav');\n    var toggle = $('#navToggle');",
    "    var nav = $('#nav');\n    if (!nav) {                       // versión para widget: no hay cabecera\n"
    "      var waSuelto = $('.wa');\n      if (waSuelto) waSuelto.classList.add('is-visible');\n      return;\n    }\n"
    "    var toggle = $('#navToggle');")

# ---------- 3. Las imágenes salen de Medios de WordPress ----------
#     src="assets/img/x.jpg"  ->  data-cj="x.jpg"   (una sola línea que editar)
cuerpo = re.sub(r'src="assets/img/([\w.-]+)"', r'data-cj="\1"', cuerpo)
# el JS arma rutas de dos maneras distintas; hay que cubrir las dos
antes = js
js = js.replace(
    '\'<img src="assets/img/\' + p.src +',
    '\'<img src="\' + (window.CJ_IMAGENES || \'\') + p.src +')          # plantilla del portfolio
js = js.replace("'assets/img/' + p.src", "(window.CJ_IMAGENES || '') + p.src")  # visor
assert js != antes, 'no se sustituyó ninguna ruta de imagen'
restantes = re.findall(r'assets/img/', js.split('/*', 1)[0] + js)
sospechosas = [l for l in js.splitlines() if 'assets/img/' in l and not l.strip().startswith(('*', '//', 'Para'))]
if sospechosas:
    raise SystemExit('quedan rutas sin sustituir:\n  ' + '\n  '.join(sospechosas))

# ---------- 4. Montar el archivo ----------
salida = '''<!-- ===================================================================
     Chío Jiménez · Maquillaje profesional
     Pega TODO este bloque en un widget de HTML personalizado.

     ANTES DE PEGARLO, cambia la línea de abajo por la carpeta donde
     hayan quedado las imágenes en Medios de WordPress. Es lo único
     que hay que tocar. La ves abriendo cualquier imagen en Medios y
     copiando su URL hasta la última barra.
     =================================================================== -->
<script>
  window.CJ_IMAGENES = "https://chiojimenez.makeup/wp-content/uploads/2026/09/";
</script>

<style>
%s%s
</style>

<div class="cj">
%s
</div>

<script>
// coloca las imágenes desde la carpeta indicada arriba
(function () {
  var base = window.CJ_IMAGENES || '';
  var nodos = document.querySelectorAll('.cj [data-cj]');
  for (var i = 0; i < nodos.length; i++) nodos[i].src = base + nodos[i].getAttribute('data-cj');
})();
%s
</script>
''' % (fuente, css_acotado, cuerpo, js)

open(SALIDA, 'w', encoding='utf-8').write(salida)
print('generado: %s  (%.0f KB)' % (os.path.basename(SALIDA), os.path.getsize(SALIDA)/1024))
print('reglas acotadas a "%s"' % AMBITO)
