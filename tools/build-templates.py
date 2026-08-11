#!/usr/bin/env python3
"""
Genera las plantillas de Elementor a partir de una descripcion compacta.

Se genera en vez de escribirse a mano porque el JSON de Elementor es muy
repetitivo (cada elemento necesita su id unico) y a mano se cuelan erratas
que Elementor no avisa: simplemente ignora el ajuste.

Criterio de diseno de las plantillas: Elementor pone SOLO la estructura
(contenedores flex y widgets) y cada elemento lleva su clase CSS. Todo lo
visual vive en el CSS del tema hijo. Asi el proyecto no depende de controles
de estilo de Elementor Pro y el diseno queda versionado en git.

Uso:  python3 tools/build-templates.py
"""

import json
import pathlib

OUT_DIR = pathlib.Path(__file__).resolve().parent.parent / "elementor-kit" / "content" / "page"

_counter = 0


def _next_id() -> str:
    """Elementor espera ids alfanumericos de 7 caracteres, unicos por plantilla."""
    global _counter
    _counter += 1
    return f"bl{_counter:05d}"


def container(css_class, children, direction="row", extra=None):
    settings = {
        "container_type": "flex",
        "content_width": "full",
        "flex_direction": direction,
        "flex_gap": {"unit": "px", "size": 0, "column": "0", "row": "0"},
        "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
        "_css_classes": css_class,
    }
    if extra:
        settings.update(extra)
    return {
        "id": _next_id(),
        "elType": "container",
        "isInner": False,
        "settings": settings,
        "elements": children,
    }


def widget(widget_type, settings):
    return {
        "id": _next_id(),
        "elType": "widget",
        "widgetType": widget_type,
        "settings": settings,
        "elements": [],
    }


def heading(text, css_class, tag="div", url=None):
    settings = {"title": text, "header_size": tag, "_css_classes": css_class}
    if url is not None:
        settings["link"] = {"url": url, "is_external": "", "nofollow": ""}
    return widget("heading", settings)


def html(markup, css_class=""):
    return widget("html", {"html": markup, "_css_classes": css_class})


# --- Trozos reutilizables ---------------------------------------------------

BURGER = (
    '<button class="bl-burger" type="button" aria-label="Abrir menú" aria-expanded="false">'
    "<span></span><span></span><span></span></button>"
)

BRAND = (
    '<a class="bl-brand" href="/">'
    '<span class="bl-brand__kicker">This is</span>'
    '<span class="bl-brand__name">BLOMSTRA</span></a>'
)

LANG = (
    '<a class="bl-lang" href="#">EN'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
    '<path d="M6 9l6 6 6-6"/></svg></a>'
)


def site_header():
    """Header comun. En WordPress vive en Header Footer Builder, no en la pagina,
    pero se deja aqui para que la plantilla se pueda previsualizar suelta."""
    return container(
        "bl-header",
        [
            html(BURGER),
            html(BRAND),
            html(f'<div class="bl-tools">{LANG}<a class="bl-btn-ghost" href="#">WHATS</a></div>'),
        ],
    )


def portal_panel(number, name, sub, links, active=None):
    nav_items = "".join(
        '<a href="#"{}>{}</a>'.format(
            ' aria-current="page"' if item == active else "", item
        )
        for item in links
    )
    return container(
        "bl-panel",
        [
            heading(number, "bl-badge", tag="span"),
            html(
                f'<p class="bl-lockup"><span class="bl-lockup__name">{name}</span>'
                f'<span class="bl-lockup__sub">{sub}</span></p>'
            ),
            html(f'<nav class="bl-panel__nav" aria-label="{name} {sub}">{nav_items}</nav>'),
        ],
        direction="column",
    )


# --- Plantillas -------------------------------------------------------------

def template_portal():
    return container(
        "bl-portal",
        [
            site_header(),
            container(
                "bl-portal__body",
                [
                    portal_panel("01", "BLOMSTRA", "Visual",
                                 ["ABOUT", "SERVICES", "LOOKBOOK", "CONTACT US"],
                                 active="ABOUT"),
                    portal_panel("03", "BLOMSTRA", "Experiences",
                                 ["ABOUT", "SERVICES", "LOOKBOOK"]),
                ],
            ),
            html(
                '<a href="#">CONTACT US</a><a href="#">BEHIND BLOMSTRA</a><a href="#">NEWSLETTER</a>',
                "bl-portal__footer",
            ),
        ],
        direction="column",
    )


TEMPLATES = {
    "01-portal": ("Blomstra — Portal", template_portal),
}


def main():
    global _counter
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, (title, builder) in TEMPLATES.items():
        _counter = 0
        doc = {
            "version": "0.4",
            "title": title,
            "type": "page",
            "content": [builder()],
            "page_settings": {"template": "elementor_canvas"},
        }
        path = OUT_DIR / f"{slug}.json"
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n")
        print(f"Generada {path.relative_to(OUT_DIR.parents[2])}")


if __name__ == "__main__":
    main()
