#!/usr/bin/env python3
"""Descarga de Google Fonts los archivos woff2 y los deja en assets/fonts/.

Alojar las fuentes en el propio proyecto evita depender de un servicio
externo (mejor para velocidad y para la protección de datos) y permite
incrustarlas en la vista previa de una sola página.

Uso:
    python3 tools/fetch-fonts.py "Bodoni Moda:ital,wght@0,400;0,500;1,400"
"""
import os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fonts")
# Sin un user-agent de navegador moderno, Google devuelve formatos antiguos
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
# Solo los alfabetos que usa la web
SUBSETS = ("latin", "latin-ext")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def fetch(spec):
    """spec: 'Familia:ital,wght@0,400;1,400' — el formato de Google Fonts."""
    family = spec.split(":")[0]
    url = "https://fonts.googleapis.com/css2?family=%s&display=swap" % (
        spec.replace(" ", "+"))
    css = get(url).decode("utf-8")

    faces, subset = [], None
    for block in css.split("@font-face")[0:]:
        for m in re.finditer(r"/\*\s*([\w-]+)\s*\*/", block):
            subset = m.group(1)
        if "src:" not in block:
            continue
        if subset not in SUBSETS:
            continue
        style = re.search(r"font-style:\s*([\w ]+);", block).group(1).strip()
        # en las fuentes variables el peso y el ancho son rangos ("200 800")
        weight = re.search(r"font-weight:\s*([\d ]+);", block).group(1).strip()
        stretch = re.search(r"font-stretch:\s*([\d%. ]+);", block)
        stretch = stretch.group(1).strip() if stretch else ""
        src = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
        name = "%s-%s-%s-%s.woff2" % (slug(family), subset, slug(weight), slug(style))
        path = os.path.join(OUT, name)
        if not os.path.exists(path):
            open(path, "wb").write(get(src))
        faces.append((family, style, weight, name, stretch))
    return faces


def css_for(faces):
    out = []
    for family, style, weight, name, stretch in faces:
        out.append(
            '@font-face {\n'
            '  font-family: "%s";\n'
            '  font-style: %s;\n'
            '  font-weight: %s;\n'
            '%s'
            '  font-display: swap;\n'
            '  src: url("../fonts/%s") format("woff2");\n'
            '}' % (family, style, weight,
                   ('  font-stretch: %s;\n' % stretch) if stretch else '', name))
    return "\n".join(out)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    all_faces = []
    for spec in sys.argv[1:]:
        all_faces += fetch(spec)
        print("descargada:", spec.split(":")[0])
    print()
    print(css_for(all_faces))
