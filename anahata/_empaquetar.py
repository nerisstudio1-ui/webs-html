# -*- coding: utf-8 -*-
"""Genera una versión de una sola página con todo incrustado (CSS, JS e imágenes).
   Uso: python3 _empaquetar.py [pagina.html] [salida.html]"""
import base64, re, sys, os

origen  = sys.argv[1] if len(sys.argv) > 1 else "landing.html"
destino = sys.argv[2] if len(sys.argv) > 2 else "anahata-landing-autonoma.html"

html = open(origen, encoding="utf-8").read()
css  = open("assets/css/style.css", encoding="utf-8").read()
js   = open("assets/js/main.js", encoding="utf-8").read()

def datauri(ruta):
    with open(ruta, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    tipo = "image/svg+xml" if ruta.endswith(".svg") else "image/jpeg"
    return f"data:{tipo};base64,{b64}"

# 1) Imágenes → data URI
usadas = set(re.findall(r'assets/img/([\w.-]+)', html))
for nombre in usadas:
    ruta = f"assets/img/{nombre}"
    if os.path.exists(ruta):
        html = html.replace(f"assets/img/{nombre}", datauri(ruta))

# 2) CSS y JS incrustados
html = html.replace('<link rel="stylesheet" href="assets/css/style.css">',
                    "<style>\n" + css + "\n</style>")
html = html.replace('<script src="assets/js/main.js" defer></script>',
                    "<script>\n" + js + "\n</script>")

# 3) Aviso sobre los enlaces a las páginas legales, que aquí no existen
html = html.replace('<a href="privacidad.html">política de privacidad</a>',
                    '<a href="privacidad.html" title="Disponible en el proyecto completo">política de privacidad</a>')

open(destino, "w", encoding="utf-8").write(html)
print(f"{destino}: {os.path.getsize(destino)//1024} KB · {len(usadas)} imágenes incrustadas")
