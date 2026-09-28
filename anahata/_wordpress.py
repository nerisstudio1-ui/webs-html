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
from _css_ambito import encapsular

MARCADOR = "URL_DE_TUS_IMAGENES"
AMBITO = "anahata-landing"   # clase que envuelve todo, para no chocar con el tema

# Rompe el contenedor del tema y ocupa el ancho de la ventana.
ANCHO_COMPLETO = """
/* --- Ancho completo dentro de WordPress ---------------------------------
   El tema mete el contenido en una columna estrecha. Estas reglas sacan la
   landing de esa columna y la llevan de lado a lado de la ventana.
   Si tu tema ya da ancho completo, puedes borrar este bloque.            */
.%(a)s{
  width:100vw; max-width:100vw;
  margin-left:calc(50%% - 50vw); margin-right:calc(50%% - 50vw);
  overflow-x:hidden;
}
/* El tema suele poner bordes a las imágenes, subrayar los enlaces o dar
   estilo a los botones. Aquí lo neutralizamos dentro de la landing.      */
.%(a)s img, .%(a)s svg{ border:0 !important; box-shadow:none !important; border-radius:inherit; }
.%(a)s a{ text-decoration:none; box-shadow:none; }
.%(a)s a:hover{ text-decoration:none; }
.%(a)s button, .%(a)s input, .%(a)s select, .%(a)s textarea{ -webkit-appearance:none; appearance:none; }
.%(a)s ul, .%(a)s li{ list-style:none; margin:0; padding:0; }
.%(a)s figure{ margin:0; }
/* El acordeón no debe teñirse al pulsarlo */
.%(a)s .acordeon__boton,
.%(a)s .acordeon__boton:hover,
.%(a)s .acordeon__boton:focus,
.%(a)s .acordeon__boton:active{ background:transparent !important; box-shadow:none !important; }
.%(a)s{ -webkit-tap-highlight-color:transparent; }
.%(a)s *{ box-sizing:border-box; }
.%(a)s .tarjeta__media img, .%(a)s .galeria__item img, .%(a)s .duo__media img,
.%(a)s .hero__media img, .%(a)s .franja__media img{ border-radius:0; }

/* El tema no debe recortar lo que sobresale */
.%(a)s-envoltorio{ max-width:none !important; padding-left:0 !important; padding-right:0 !important; }
""" 
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
    css = css.replace('@import url("../fonts/fuentes.css");', "")
    # Las tipografías van fuera del ámbito: @font-face es global
    css = fcss + "\n" + encapsular(css, "." + AMBITO) + (ANCHO_COMPLETO % {"a": AMBITO})

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
     Va a ancho completo por sí solo: rompe la columna del tema.
     Los estilos están encapsulados, así que no tocan al resto de la web.
  4. Crea dos páginas de WordPress con los slugs aviso-legal y privacidad.
     Sus textos están en aviso-legal.html y privacidad.html.

  Las tipografías van incrustadas: no hay que subir nada más.
-->
"""
    salida = (cabecera + "<style>\n" + css + "\n</style>\n"
              + f'<div class="{AMBITO}">\n' + cuerpo.strip() + "\n</div>\n"
              + "\n<script>\n" + js + "\n</script>\n")
    open("anahata-wordpress.html", "w", encoding="utf-8").write(salida)
    n = len(set(re.findall(MARCADOR + r"/([\w.-]+)", salida)))
    print(f"anahata-wordpress.html: {os.path.getsize('anahata-wordpress.html')//1024} KB · {n} imágenes a sustituir")

def todo_incluido():
    """Variante sin dependencias: también las imágenes van en base64."""
    from PIL import Image
    import io
    LIMITES = {"portada.jpg": 1500, "sara.jpg": 800, "retiro.jpg": 1500}
    html = open("anahata-wordpress.html", encoding="utf-8").read()

    def incrustar_img(m):
        nombre = m.group(1)
        origen = f"assets/img/png/{nombre}" if nombre.endswith(".png") else f"assets/img/{nombre}"
        if not os.path.exists(origen):
            print("  falta", origen); return m.group(0)
        if nombre.endswith(".png"):
            datos, tipo = open(origen, "rb").read(), "image/png"
        else:
            im = Image.open(origen)
            ancho = LIMITES.get(nombre, 1100)
            if im.width > ancho:
                im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
            buf = io.BytesIO()
            im.save(buf, "JPEG", quality=74, optimize=True, progressive=True)
            datos, tipo = buf.getvalue(), "image/jpeg"
        return f"data:{tipo};base64," + base64.b64encode(datos).decode("ascii")

    html = re.sub(MARCADOR + r"/([\w.-]+)", incrustar_img, html)
    open("anahata-wordpress-todo-incluido.html", "w", encoding="utf-8").write(html)
    print(f"anahata-wordpress-todo-incluido.html: "
          f"{os.path.getsize('anahata-wordpress-todo-incluido.html')//1024} KB")

if __name__ == "__main__":
    construir()
    todo_incluido()
