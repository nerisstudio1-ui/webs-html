#!/usr/bin/env python3
"""
Empaqueta la web en un solo archivo HTML.

Genera dos versiones:

  dist/cristina-falcon-completa.html
      Todo dentro: estilos, guiones, tipografías e imágenes en base64.
      Se abre con doble clic, sin servidor. Los vídeos NO se empotran
      (pesan 12 MB) y se quedan enlazados a BASE.

  dist/cristina-falcon-widget.html
      Para pegar en un bloque HTML de WordPress. Estilos y guiones dentro,
      pero todo el CSS va encerrado bajo #cfm-web para que no toque nada
      del tema. Imágenes y vídeos se sirven desde BASE.
"""
import base64, mimetypes, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ENVOLTORIO = "cfm-web"

# Dónde estarán las imágenes y los vídeos una vez subidos a WordPress.
BASE = sys.argv[1] if len(sys.argv) > 1 else "https://TU-DOMINIO.com/wp-content/uploads/cristina/"


def leer(rel):
    return (RAIZ / rel).read_text(encoding="utf-8")


def a_datos(rel):
    ruta = RAIZ / rel
    tipo = mimetypes.guess_type(str(ruta))[0] or "application/octet-stream"
    return f"data:{tipo};base64," + base64.b64encode(ruta.read_bytes()).decode()


# ---------------------------------------------------------------- tipografías
def sin_comentarios(css):
    """Fuera los comentarios. Importa porque dentro hay un bloque comentado
    (Hatton y Agrandir) que apunta a archivos que no están."""
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def fuentes_en_linea(css):
    """Mete cada .woff2 dentro del propio CSS, en base64."""
    def cambio(m):
        rel = "assets/fonts/" + m.group(1)
        return 'url("%s")' % a_datos(rel) if (RAIZ / rel).exists() else m.group(0)
    return re.sub(r'url\("\.\./fonts/([^"]+)"\)', cambio, css)


# ------------------------------------------------------------------- alcance
NO_TOCAR = ("@font-face", "@keyframes", "@-webkit-keyframes", "@import", "@charset")
RECURSIVAS = ("@media", "@supports", "@container", "@layer")


def acotar_selector(sel):
    sel = sel.strip()
    if not sel or sel.startswith("%"):
        return sel
    if sel in (":root", "html", "body"):
        return "#" + ENVOLTORIO
    if sel.startswith(("html ", "body ")):
        return "#%s %s" % (ENVOLTORIO, sel.split(" ", 1)[1])
    if sel.startswith("html.") or sel.startswith("body."):
        # p. ej. body.nav-open .nav
        resto = sel.split(" ", 1)
        clase = resto[0].split(".", 1)[1]
        cola = " " + resto[1] if len(resto) > 1 else ""
        return "#%s.%s%s" % (ENVOLTORIO, clase, cola)
    if sel == "*":
        return "#%s, #%s *" % (ENVOLTORIO, ENVOLTORIO)
    if sel.startswith("*::"):
        return "#%s *%s" % (ENVOLTORIO, sel[1:])
    if sel.startswith("::selection") or sel.startswith(":focus-visible"):
        return "#%s %s" % (ENVOLTORIO, sel)
    return "#%s %s" % (ENVOLTORIO, sel)


def acotar(css):
    """Encierra todas las reglas bajo #cfm-web, respetando las @-reglas."""
    salida, i, n = [], 0, len(css)
    while i < n:
        llave = css.find("{", i)
        if llave == -1:
            salida.append(css[i:])
            break
        cabeza = css[i:llave]
        # comentarios sueltos antes del selector
        pre, sel = "", cabeza
        ult = cabeza.rfind("*/")
        if ult != -1:
            pre, sel = cabeza[:ult + 2], cabeza[ult + 2:]

        # buscar el cierre equilibrado
        prof, j = 1, llave + 1
        while j < n and prof:
            if css[j] == "{":
                prof += 1
            elif css[j] == "}":
                prof -= 1
            j += 1
        cuerpo = css[llave + 1:j - 1]

        limpio = sel.strip()
        if limpio.startswith(NO_TOCAR):
            salida.append(pre + sel + "{" + cuerpo + "}")
        elif limpio.startswith(RECURSIVAS):
            salida.append(pre + sel + "{" + acotar(cuerpo) + "}")
        else:
            nuevos = ", ".join(acotar_selector(s) for s in limpio.split(",") if s.strip())
            salida.append(pre + "\n" + nuevos + " {" + cuerpo + "}")
        i = j
    return "".join(salida)


# --------------------------------------------------------------------- medios
def medios(texto, empotrar_imagenes):
    """Cambia las rutas de assets/img y assets/video.

    Los SVG van siempre dentro del archivo: WordPress los rechaza al subir,
    por seguridad, y el logotipo es un SVG. Además pesan poco.
    """
    def cambio(m):
        rel = m.group(1)
        if rel.endswith(".svg"):
            return m.group(0).replace(rel, a_datos(rel))
        if rel.startswith(("assets/video/", "assets/docs/")):
            return m.group(0).replace(rel, BASE + rel.split("/")[-1])
        if empotrar_imagenes:
            return m.group(0).replace(rel, a_datos(rel))
        return m.group(0).replace(rel, BASE + rel.split("/")[-1])
    return re.sub(r'(?:src|href|poster)="(assets/(?:img|video|docs)/[^"]+)"', cambio, texto)


# ---------------------------------------------------------------------- build
def comprobar_etiquetas(cuerpo):
    """Aborta si las <div> no cuadran.

    En el widget todo el contenido cuelga de un <div id="cfm-web">, y de ahí
    cuelga también el alcance del CSS. Un </div> de más lo cierra antes de
    tiempo: el navegador saca de dentro todo lo que venga después, esas
    secciones se quedan sin ninguna regla aplicada, las imágenes salen a su
    tamaño natural y la página se va de ancho. Se ve raro, pero no da ningún
    error, así que conviene que el empaquetado no lo deje pasar.
    """
    prof, minimo = 0, 0
    for m in re.finditer(r"<(/?)div\b[^>]*?(/?)>", cuerpo):
        if m.group(2) == "/":        # <div/>, que no abre nada
            continue
        prof += -1 if m.group(1) else 1
        minimo = min(minimo, prof)
    if prof or minimo:
        sys.exit("index.html tiene las <div> descuadradas: saldo %d, mínimo %d.\n"
                 "Sobra un </div> o falta un <div>. No se ha generado nada."
                 % (prof, minimo))


def construir(widget, destino):
    html = leer("index.html")

    cuerpo = re.search(r"<body>(.*)</body>", html, re.S).group(1)
    comprobar_etiquetas(cuerpo)
    cuerpo = re.sub(r'\s*<script src="[^"]+"></script>', "", cuerpo)

    css = (fuentes_en_linea(sin_comentarios(leer("assets/css/fonts.css")))
           + "\n" + leer("assets/css/styles.css"))
    if widget:
        css = acotar(css)
    js = "\n".join(leer("assets/js/" + f) for f in ("config.js", "i18n.js", "main.js"))

    cuerpo = medios(cuerpo, empotrar_imagenes=not widget)
    css = medios(css, empotrar_imagenes=not widget)

    if widget:
        # Dentro de una página de WordPress hay que renunciar a un par de
        # cosas que sí valen cuando la web ocupa la pantalla entera.
        css += """

/* ----------------------------------------------------------------------
   Ajustes para vivir dentro de una página de WordPress
   ---------------------------------------------------------------------- */

/* La cabecera fija se sale del bloque y se planta encima de la del tema.
   Dentro de una página tiene que quedarse quieta donde está. */
#%(w)s .header { position: static; background: var(--crema); box-shadow: 0 1px 0 var(--line); }
#%(w)s .header.is-stuck { backdrop-filter: none; }

/* La portada a pantalla completa deja de tener sentido cuando encima hay
   una cabecera del tema y debajo un pie. */
#%(w)s .hero { min-height: 82vh; padding-top: clamp(2rem, 5vw, 4rem); }

/* El menú de móvil se abría a pantalla completa contando con que la web
   era la página entera. */
@media (max-width: 62rem) {
  #%(w)s .nav { position: absolute; }
}

/* A todo lo ancho, aunque el tema meta el contenido en un contenedor
   estrecho. Los márgenes negativos compensan lo que el contenedor aparta
   por cada lado.

   El ancho sale de --ancho-real, que pone el guion con la anchura del
   documento SIN la barra de desplazamiento. Con 100vw a secas la página
   se queda unos píxeles más ancha que la ventana y aparece una barra
   horizontal. 100vw queda de reserva por si el guion no llega a correr. */
#%(w)s {
  width: var(--ancho-real, 100vw);
  max-width: var(--ancho-real, 100vw);
  margin-left: calc(50%% - var(--ancho-real, 100vw) / 2);
  margin-right: calc(50%% - var(--ancho-real, 100vw) / 2);
}
""" % {"w": ENVOLTORIO}

        doc = (
            "<!-- ==========================================================\n"
            "     Cristina Falcón Maldonado — para un bloque HTML personalizado\n"
            "     Los estilos van encerrados bajo #cfm-web: no tocan el tema.\n"
            f"     Imágenes y vídeos se sirven desde: {BASE}\n"
            "     ========================================================== -->\n"
            f'<div id="{ENVOLTORIO}">\n<style>\n{css}\n</style>\n{cuerpo}\n'
            f"<script>\n{js}\n</script>\n</div>\n"
        )
    else:
        cabecera = re.search(r"<head>(.*)</head>", html, re.S).group(1)
        cabecera = re.sub(r'\s*<link rel="(?:preload|stylesheet)"[^>]*>', "", cabecera)
        doc = ("<!DOCTYPE html>\n<html lang=\"es\">\n<head>" + cabecera +
               f"\n<style>\n{css}\n</style>\n</head>\n<body>{cuerpo}\n"
               f"<script>\n{js}\n</script>\n</body>\n</html>\n")

    (RAIZ / destino).write_text(doc, encoding="utf-8")
    kb = (RAIZ / destino).stat().st_size // 1024
    print("  %-42s %6d KB" % (destino, kb))


construir(widget=False, destino="dist/cristina-falcon-completa.html")
construir(widget=True,  destino="dist/cristina-falcon-widget.html")
print("\n  Medios enlazados a:", BASE)
