# -*- coding: utf-8 -*-
"""Genera anahata-wordpress.html: la landing lista para pegar en un bloque
   «HTML personalizado» de WordPress.

   - CSS, JavaScript y tipografías incrustados (no hay que subir nada de eso).
   - Sin <head>: un bloque de WordPress solo admite contenido.
   - Las imágenes apuntan a URL_DE_TUS_IMAGENES, que se sustituye por la ruta
     de la biblioteca de medios una vez subidas.
   - Los logotipos pasan de SVG a PNG: WordPress bloquea los SVG por defecto.

   Uso: python3 _wordpress.py
"""
import base64, re, os

MARCADOR = "URL_DE_TUS_IMAGENES"
LOGOS = ("logo-anahata-crema", "logo-anahata", "logo-marca-crema", "logo-marca", "favicon")

def construir():
    html = open("index.html", encoding="utf-8").read()
    css  = open("assets/css/style.css", encoding="utf-8").read()
    js   = open("assets/js/main.js", encoding="utf-8").read()
    fcss = open("assets/fonts/fuentes.css", encoding="utf-8").read()

    def incrustar(m):
        with open("assets/fonts/" + m.group(1), "rb") as f:
            return "url(data:font/woff2;base64," + base64.b64encode(f.read()).decode("ascii") + ")"
    fcss = re.sub(r"url\(\.\./fonts/([\w.-]+)\)", incrustar, fcss)
    css = css.replace('@import url("../fonts/fuentes.css");', fcss)

    cuerpo = html[html.index("<body>") + 6 : html.rindex("</body>")]
    cuerpo = cuerpo.replace('<a class="saltar-al-contenido" href="#contenido">Saltar al contenido</a>', "")
    cuerpo = re.sub(r'<script src="assets/js/main\.js" defer></script>', "", cuerpo)
    cuerpo = re.sub(r'<script type="application/ld\+json">.*?</script>', "", cuerpo, flags=re.S)
    cuerpo = cuerpo.replace('href="aviso-legal.html"', 'href="/aviso-legal/"')
    cuerpo = cuerpo.replace('href="privacidad.html#cookies"', 'href="/privacidad/#cookies"')
    cuerpo = cuerpo.replace('href="privacidad.html"', 'href="/privacidad/"')
    cuerpo = cuerpo.replace("assets/img/", MARCADOR + "/")
    for n in LOGOS:
        cuerpo = cuerpo.replace(f"{n}.svg", f"{n}.png")

    cabecera = f"""<!--
  ANAHATA · Landing para WordPress
  ---------------------------------
  1. Sube las imágenes del ZIP a Medios.
  2. Sustituye en TODO este archivo {MARCADOR} por la ruta de tus
     imágenes, sin barra final. Ejemplo:
     https://tudominio.com/wp-content/uploads/2026/09
  3. Pega todo el contenido en un bloque «HTML personalizado».
  4. Crea dos páginas de WordPress con los slugs aviso-legal y privacidad.
     Sus textos están en aviso-legal.html y privacidad.html.

  Las tipografías van incrustadas: no hay que subir nada más.
-->
"""
    salida = cabecera + "<style>\n" + css + "\n</style>\n" + cuerpo.strip() + "\n\n<script>\n" + js + "\n</script>\n"
    open("anahata-wordpress.html", "w", encoding="utf-8").write(salida)
    n = len(set(re.findall(MARCADOR + r"/([\w.-]+)", salida)))
    print(f"anahata-wordpress.html: {os.path.getsize('anahata-wordpress.html')//1024} KB · {n} imágenes a sustituir")

if __name__ == "__main__":
    construir()
