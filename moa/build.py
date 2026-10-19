"""Genera las tres versiones de la web de MOA a partir de la plantilla y los textos.

    python3 build.py

Salida: index.html (català), es.html (castellano) y en.html (English).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
from i18n import PAGES, TEXT  # noqa: E402

LANG_LABELS = {"ca": ("CA", "Català"), "es": ("ES", "Castellano"), "en": ("EN", "English")}


def lang_switch(current):
    links = []
    for code, page in PAGES.items():
        short, name = LANG_LABELS[code]
        cur = ' aria-current="true"' if code == current else ""
        links.append(f'<a href="{page}" hreflang="{code}" lang="{code}" title="{name}"{cur}>{short}</a>')
    return '<nav class="langs" aria-label="Idioma / Language">' + "".join(links) + "</nav>"


def build():
    template = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    keys = set(re.findall(r"\{\{(\w+)\}\}", template))
    for lang, page in PAGES.items():
        values = dict(TEXT[lang])
        values["lang"] = lang
        values["lang_switch"] = lang_switch(lang)
        # </ escapado para que ningún texto pueda cerrar el <script>
        values["js_i18n"] = json.dumps(values.pop("js"), ensure_ascii=False).replace("</", "<\\/")
        missing = keys - values.keys()
        if missing:
            sys.exit(f"[{lang}] faltan textos: {', '.join(sorted(missing))}")
        unused = values.keys() - keys
        if unused:
            print(f"[{lang}] aviso, textos sin usar: {', '.join(sorted(unused))}")
        html = re.sub(r"\{\{(\w+)\}\}", lambda m: values[m.group(1)], template)
        (ROOT / page).write_text(html, encoding="utf-8")
        print(f"{page} generado ({lang})")


if __name__ == "__main__":
    build()
