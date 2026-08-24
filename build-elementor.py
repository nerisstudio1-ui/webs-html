#!/usr/bin/env python3
"""
Genera el código para pegar en un widget HTML de Elementor.

Produce dos archivos:

  calma-elementor.html            fotos enlazadas desde la Biblioteca de
                                  medios de WordPress (ligero, recomendado)
  calma-elementor-con-fotos.html  fotos incrustadas dentro del propio código
                                  (no hay que subir nada, pero pesa mucho)

Todo el CSS queda encerrado bajo #calma-web, así que ni el tema de
WordPress puede descolocar la web ni la web puede descolocar el tema.

    python3 build-elementor.py
"""
import base64, mimetypes, pathlib, re, urllib.parse

RAIZ  = pathlib.Path(__file__).parent
CAJA    = 'calma-web'                   # id que envuelve toda la web
PREFIJO = '.calma-web.calma-web'        # con qué se encierra cada selector
                                        # (clase, no id: así el menú sigue
                                        #  con estilo aunque se cuelgue del
                                        #  final de la página)
BASE  = 'https://TU-DOMINIO.com/wp-content/uploads/calma/'

FUENTES_CDN = ("https://fonts.googleapis.com/css2?"
               "family=Instrument+Serif:ital@0;1"
               "&family=Montserrat:wght@200;300;400;500"
               "&family=Jost:wght@200;300;400&display=swap")

# ── CSS: encerrar cada selector bajo #calma-web ───────────────────
GLOBALES = {'html', 'body', ':root', '*', '*::before', '*::after'}

def encajar(selector: str) -> str:
    s = selector.strip()
    if not s:
        return s
    if s.startswith('@'):
        return s
    if s in GLOBALES:
        return PREFIJO
    if s.startswith('*'):                       # *::before → .caja *::before
        return f'{PREFIJO} {s}'
    if s.startswith('.js '):                    # la clase js pasa a la propia caja
        return f'{PREFIJO}.js {s[4:]}'
    if s.startswith('html') or s.startswith('body'):
        resto = s.split(None, 1)
        return f'{PREFIJO} {resto[1]}' if len(resto) > 1 else PREFIJO
    if s.startswith(':focus-visible') or s.startswith('::selection'):
        return f'{PREFIJO} {s}'
    return f'{PREFIJO} {s}'

def encajar_css(css: str) -> str:
    # Fuera los comentarios: si no, se cuelan dentro de los selectores
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\n{3,}', '\n\n', css)

    fuera = []          # @font-face y @keyframes se quedan tal cual
    def guardar(m):
        fuera.append(m.group(0))
        return f'/*__FUERA{len(fuera)-1}__*/'
    css = re.sub(r'@(?:font-face|keyframes)[^{]*\{(?:[^{}]|\{[^{}]*\})*\}', guardar, css)

    def por_regla(m):
        sel, cuerpo = m.group(1), m.group(2)
        if sel.strip().startswith('@'):
            return m.group(0)
        nuevos = ','.join(encajar(p) for p in sel.split(','))
        return f'{nuevos}{{{cuerpo}}}'
    css = re.sub(r'([^{}@][^{}]*?)\{([^{}]*)\}', por_regla, css)

    for i, txt in enumerate(fuera):
        css = css.replace(f'/*__FUERA{i}__*/', txt)
    return css

estilos = encajar_css((RAIZ / 'assets/css/styles.css').read_text())

marco = f'''
/* ═══ CALMA · código para el widget HTML de Elementor ═══
   Todo cuelga de #{CAJA}: ni el tema toca esta web ni esta web toca el tema.
   Las fotos se cambian buscando y reemplazando la dirección de arriba. */
@import url('{FUENTES_CDN}');

{PREFIJO} *,{PREFIJO} *::before,{PREFIJO} *::after{{box-sizing:border-box}}
/* Blindaje: los temas de WordPress suelen imponer bordes, mayúsculas
   y subrayados a todo. Aquí dentro, no. */
{PREFIJO} img{{max-width:100%;height:auto;display:block;border:0;border-radius:0;box-shadow:none;filter:none}}
{PREFIJO} a{{text-decoration:none;color:inherit;box-shadow:none}}
{PREFIJO} h1,{PREFIJO} h2,{PREFIJO} h3,{PREFIJO} h4{{text-transform:none;font-weight:inherit}}
{PREFIJO} button{{border:0;background:none;font:inherit;color:inherit}}
{PREFIJO} svg{{display:inline-block;vertical-align:middle}}
{PREFIJO} h1,{PREFIJO} h2,{PREFIJO} h3,{PREFIJO} h4,{PREFIJO} p,{PREFIJO} ul,{PREFIJO} ol,{PREFIJO} figure{{margin:0;padding:0}}
{PREFIJO} ul,{PREFIJO} ol{{list-style:none}}
body.calma-menu-abierto{{overflow:hidden}}
'''

# ── HTML: solo el contenido, dentro de la caja ────────────────────
html = (RAIZ / 'index.html').read_text()
cuerpo = html.split('<body>', 1)[1].rsplit('</body>', 1)[0]
cuerpo = cuerpo.replace('<script src="assets/js/main.js"></script>', '').strip()

# ── JS: mirar solo dentro de la caja ──────────────────────────────
guion = (RAIZ / 'assets/js/main.js').read_text()
guion = guion.replace(
    "  var $  = function (s, c) { return (c || document).querySelector(s); };\n"
    "  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };",
    f"  var caja = document.getElementById('{CAJA}');\n"
    "  if (!caja) return;\n"
    "  caja.className += ' js';\n"
    "  var $  = function (s, c) { return (c || caja).querySelector(s); };\n"
    "  var $$ = function (s, c) { return Array.prototype.slice.call((c || caja).querySelectorAll(s)); };")
guion = guion.replace("document.body.classList.toggle('nav-open', open);",
                      "document.body.classList.toggle('calma-menu-abierto', open);")
guion = guion.replace("document.documentElement.classList.add('sin-reservas');",
                      "caja.className += ' sin-reservas';")
guion = guion.replace("(function () {\n  'use strict';", "(function () {\n  'use strict';")

# Va al final del CSS: si fuera antes, lo pisaría el margin:0 del body
cierre = f"""
/* La web ocupa todo el ancho de la ventana, aunque el contenedor
   de Elementor sea más estrecho. Si aun así aparece barra horizontal,
   pon el contenedor de Elementor a ancho completo y sin relleno. */
#{CAJA}{{
  margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw);
  overflow-x:clip;text-align:left
}}
/* El menú del móvil se cuelga del final de la página, dentro de este
   envoltorio. Ni ancho completo ni márgenes: solo hereda el estilo. */
.calma-refugio-menu{{margin:0;padding:0;width:auto;overflow:visible;background:none}}
"""

def escribir(nombre, resolver_imagen):
    c = re.sub(r'assets/img/([\w.\- ]+?\.(?:jpg|jpeg|png|svg|webp))', resolver_imagen, cuerpo)
    doc = (f'<div id="{CAJA}" class="{CAJA}">\n\n<style>\n{marco}\n{estilos}\n{cierre}\n</style>\n\n'
           f'{c}\n\n<script>\n{guion}\n</script>\n\n</div>\n')
    (RAIZ / nombre).write_text(doc)
    print(f'{nombre} · {len(doc)/1024:.0f} KB')

# 1 · fotos enlazadas desde WordPress
escribir('calma-elementor.html', lambda m: BASE + m.group(1))

# 2 · fotos incrustadas
def incrustar(m):
    ruta = RAIZ / 'assets/img' / m.group(1)
    if not ruta.exists():
        return m.group(0)
    if ruta.suffix == '.svg':
        return 'data:image/svg+xml;charset=utf-8,' + urllib.parse.quote(ruta.read_text(), safe='')
    tipo = mimetypes.guess_type(ruta.name)[0] or 'application/octet-stream'
    return f'data:{tipo};base64,' + base64.b64encode(ruta.read_bytes()).decode()
escribir('calma-elementor-con-fotos.html', incrustar)

print('\nFotos que hay que subir a la Biblioteca de medios:')
for n in sorted({m for m in re.findall(r'assets/img/([\w.\- ]+?\.(?:jpg|jpeg|png|svg|webp))', cuerpo)}):
    print('  ·', n)
