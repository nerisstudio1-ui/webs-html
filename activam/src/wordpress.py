#!/usr/bin/env python3
"""Genera la versión para WordPress (bloque «HTML personalizado») de la landing.

Salida en activam/wordpress/:
  es.html, ca.html, en.html  -> código para pegar en cada página
  imagenes-activam.zip       -> imágenes para subir a la biblioteca de medios
  LEEME.txt                  -> instrucciones y textos SEO

Uso:  python3 activam/src/wordpress.py
"""
import re
import zipfile
from pathlib import Path

import build

# Carpeta donde quedan las imágenes al subirlas a WordPress (Medios > Añadir nuevo).
# WordPress las guarda por año/mes; si se suben otro mes, cambiar aquí y volver a generar.
IMG_BASE = "https://activam.es/wp-content/uploads/2026/11/"
SITE = "https://activam.es/"
SCOPE = ".activam-lp"
OUT = build.ROOT / "wordpress"


def scope_selector(sel):
    sel = sel.strip()
    if sel in (":root", "html", "body"):
        return SCOPE
    if sel.startswith(("html ", "body ")):
        sel = sel.split(" ", 1)[1]
    return f"{SCOPE} {sel}"


def scope_css(css):
    """Prefija cada selector con SCOPE para que el tema de WordPress no interfiera."""
    out, i = [], 0
    while i < len(css):
        j = css.find("{", i)
        if j == -1:
            out.append(css[i:])
            break
        head = css[i:j]
        # bloque completo con llaves anidadas
        depth, k = 0, j
        while True:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        body = css[j + 1:k]
        comments = "".join(re.findall(r"\s*/\*.*?\*/", head, re.S))
        prelude = re.sub(r"/\*.*?\*/", "", head, flags=re.S).strip()
        if prelude.startswith("@media") or prelude.startswith("@supports"):
            out.append(f"{comments}\n  {prelude} {{{scope_css(body)}}}")
        elif prelude.startswith("@"):
            out.append(f"{comments}\n  {prelude} {{{body}}}")
        else:
            sels = ", ".join(scope_selector(s) for s in prelude.split(","))
            if prelude == "html":
                body = body.replace("scroll-behavior: smooth;", "")
            out.append(f"{comments}\n  {sels} {{{body}}}")
        i = k + 1
    return "".join(out)


def to_wordpress(lang, t, template):
    page = build.render(lang, dict(t, path=""), template)

    css = re.search(r"<style>(.*?)</style>", page, re.S).group(1)
    jsonld = re.search(r'<script type="application/ld\+json">.*?</script>', page, re.S).group(0)
    fonts = re.findall(r'<link (?:rel="preconnect"[^>]*|href="https://fonts[^>]*)>', page)
    body = re.search(r"<body>(.*)</body>", page, re.S).group(1).strip()

    # rutas absolutas a las imágenes subidas a WordPress
    body = re.sub(r'(src|poster)="(?:img|video)/', rf'\1="{IMG_BASE}', body)
    body = body.replace("url(img/", f"url({IMG_BASE}")
    jsonld = jsonld.replace("https://activam.es/img/", IMG_BASE)
    # selector de idioma con enlaces absolutos a las páginas de WordPress
    for code, o in build.LANGS.items():
        body = body.replace(f'href="{o["path"]}" hreflang="{code}"', f'href="{SITE}{o["path"]}" hreflang="{code}"')

    extra = f"""
  {SCOPE} {{ width: 100vw; max-width: 100vw; margin-left: calc(50% - 50vw); }}
  {SCOPE} img {{ height: auto; border: 0; border-radius: 0; box-shadow: none; padding: 0; margin: 0; }}
  {SCOPE} .stack img {{ box-shadow: 0 20px 40px -24px rgba(43,22,28,.45); border-radius: 26px; }}
  {SCOPE} .stack img:last-child {{ border: 6px solid var(--bg); }}
  {SCOPE} .svc-img {{ border-radius: 14px; margin-bottom: 22px; }}
  {SCOPE} .insta-grid img {{ border-radius: 16px; }}
  {SCOPE} ul {{ margin-top: 0; }}
  {SCOPE} a:focus {{ outline-offset: 2px; }}
"""
    return (f"<!-- Activa'M · landing {lang.upper()} · pegar entera en un bloque «HTML personalizado» -->\n"
            + "\n".join(fonts) + "\n"
            + f"<style>{scope_css(css)}{extra}</style>\n"
            + jsonld + "\n"
            + f'<div class="{SCOPE[1:]}">\n{body}\n</div>\n')


def embed_images(code):
    """Versión con las imágenes incrustadas (base64): funciona sin subir nada a Medios."""
    import base64
    mime = {".jpg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml"}

    def data_uri(m):
        f = build.ROOT / "img" / m.group(1)
        if not f.exists():
            return m.group(0)
        return f"data:{mime[f.suffix]};base64," + base64.b64encode(f.read_bytes()).decode()

    # los datos estructurados (JSON-LD) mantienen URLs normales; solo se incrusta el contenido visible
    head, sep, body = code.partition('</script>\n<div class="activam-lp">')
    code = head + sep + re.sub(re.escape(IMG_BASE) + r"([\w.-]+\.(?:jpg|png|svg))", data_uri, body)
    # sin vídeo todavía: dejar solo el póster
    return re.sub(r'<video src="' + re.escape(IMG_BASE) + r'activam\.mp4"', "<video", code)


def main():
    template = (build.SRC / "template.html").read_text()
    OUT.mkdir(exist_ok=True)
    for lang, t in build.LANGS.items():
        code = to_wordpress(lang, t, template)
        (OUT / f"{lang}.html").write_text(code)
        (OUT / f"codigo-{lang}.txt").write_text(code)
        (OUT / f"codigo-{lang}-con-imagenes.txt").write_text(embed_images(code))
        print("ok", f"wordpress/{lang}.html", f"wordpress/codigo-{lang}.txt")

    used = set()
    for f in OUT.glob("*.html"):
        used |= set(re.findall(re.escape(IMG_BASE) + r"([\w.-]+)", f.read_text()))
    with zipfile.ZipFile(OUT / "imagenes-activam.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(used):
            src = build.ROOT / "img" / name
            if src.exists():
                z.write(src, name)
            else:
                print("falta (subir aparte cuando exista):", name)
    print("ok", "wordpress/imagenes-activam.zip", len(used), "archivos")

    seo = "\n\n".join(
        f"{lang.upper()}  ({SITE}{t['path']})\n  Título SEO: {t['meta_title']}\n  Meta descripción: {t['meta_desc']}"
        for lang, t in build.LANGS.items())
    (OUT / "LEEME.txt").write_text(f"""ACTIVA'M · VERSIÓN PARA WORDPRESS

1. IMÁGENES
   Medios > Añadir nuevo > subir TODAS las imágenes de imagenes-activam.zip (descomprimido) de una vez.
   Deben quedar en {IMG_BASE}
   Si se suben otro mes, cambiar IMG_BASE en src/wordpress.py y volver a generar.

2. PÁGINAS (una por idioma)
   ES -> página de inicio  ({SITE})
   CA -> página con enlace permanente /ca/
   EN -> página con enlace permanente /en/
   Plantilla de página: ancho completo / sin título / «Canvas» o «Blank» (sin cabecera ni pie del tema).

3. CÓDIGO
   Añadir un bloque «HTML personalizado» y pegar el contenido entero de es.html, ca.html o en.html.

4. SEO (Yoast o Rank Math, en cada página)

{seo}
""")
    print("ok", "wordpress/LEEME.txt")


if __name__ == "__main__":
    main()
