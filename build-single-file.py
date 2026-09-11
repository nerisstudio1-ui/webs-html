#!/usr/bin/env python3
"""
Genera calma-web.html: la web entera en UN solo archivo.

Mete dentro los estilos, el JavaScript, las tipografías y las imágenes,
para poder subirla a cualquier hosting (o a WordPress) sin arrastrar
carpetas ni preocuparse por las rutas.

    python3 build-single-file.py
"""
import base64, mimetypes, pathlib, re, urllib.parse

RAIZ   = pathlib.Path(__file__).parent
SALIDA = RAIZ / 'calma-web.html'

def como_datos(ruta: pathlib.Path) -> str:
    """Convierte un archivo en una URL de datos."""
    tipo = {'.webp': 'image/webp'}.get(ruta.suffix) \
           or mimetypes.guess_type(ruta.name)[0] or 'application/octet-stream'
    if ruta.suffix == '.svg':
        return 'data:image/svg+xml;charset=utf-8,' + urllib.parse.quote(ruta.read_text(), safe='')
    return f'data:{tipo};base64,' + base64.b64encode(ruta.read_bytes()).decode()

html   = (RAIZ / 'index.html').read_text()
estilos = (RAIZ / 'assets/css/styles.css').read_text()
fuentes = (RAIZ / 'assets/css/fonts.css').read_text()
guion   = (RAIZ / 'assets/js/main.js').read_text()

# Tipografías dentro del CSS
fuentes = re.sub(r"url\('\.\./fonts/([\w.-]+)'\)",
                 lambda m: f"url({como_datos(RAIZ / 'assets/fonts' / m.group(1))})", fuentes)

# Imágenes dentro del HTML
def imagen(m):
    ruta = RAIZ / m.group(0)
    return como_datos(ruta) if ruta.exists() else m.group(0)
html = re.sub(r'assets/img/[\w.\- ]+?\.(?:jpg|jpeg|png|svg|webp)', imagen, html)

# Estilos y guion dentro del documento
html = html.replace('<link rel="stylesheet" href="assets/css/fonts.css">',
                    '<style>\n' + fuentes + '\n</style>')
html = html.replace('<link rel="stylesheet" href="assets/css/styles.css">',
                    '<style>\n' + estilos + '\n</style>')
html = html.replace('<script src="assets/js/main.js"></script>',
                    '<script>\n' + guion + '\n</script>')

SALIDA.write_text(html)
print(f'{SALIDA.name} · {len(html) / 1048576:.2f} MB')
