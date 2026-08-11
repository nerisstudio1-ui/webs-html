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


def text(markup, css_class="bl-lead"):
    """Widget Editor de texto: el cliente puede editar el copy sin tocar codigo."""
    return widget("text-editor", {"editor": markup, "_css_classes": css_class})


def button(label, url="#", css_class="bl-btn-el"):
    return widget("button", {
        "text": label,
        "link": {"url": url, "is_external": "", "nofollow": ""},
        "_css_classes": css_class,
    })


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
                '<footer class="bl-portal__footer"><a href="#">CONTACT US</a>'
                '<a href="#">BEHIND BLOMSTRA</a><a href="#">NEWSLETTER</a></footer>'
            ),
        ],
        direction="column",
    )


TICKER = (
    '<div class="bl-ticker"><span>Diseño</span>'
    '<span>Dirección de arte</span><span>Branding</span></div>'
)

COLLAGE = """
<div class="bl-collage">
  <p class="bl-collage__label">Narrativas<br>que conectan</p>
  <div class="bl-collage__img bl-collage__img--b"></div>
  <p class="bl-collage__label">Marcas con<br>identidad clara</p>
  <div class="bl-collage__img bl-collage__img--a"></div>
  <p class="bl-collage__label">Experiencias<br>que se recuerdan</p>
  <div class="bl-collage__img bl-collage__img--c"></div>
</div>
""".strip()

HERO = """
<div class="bl-hero">
  <div class="bl-hero__media" role="img" aria-label="Fotografía de plató"></div>
  <a class="bl-hero__pill" href="#universo">WELCOME TO OUR UNIVERSE</a>
</div>
""".strip()


def section(css_class, children, inner="bl-container"):
    """Seccion a ancho completo con un contenedor interior centrado."""
    return container(css_class, [container(inner, children, direction="column")],
                     direction="column")


def duo_card(sub, eyebrow, body):
    return container(
        "bl-duo__card",
        [
            html(f'<p class="bl-lockup"><span class="bl-lockup__name">BLOMSTRA</span>'
                 f'<span class="bl-lockup__sub">{sub}</span></p>'),
            html('<div class="bl-duo__media"></div>'),
            heading(eyebrow, "bl-duo__eyebrow", tag="p"),
            text(f"<p>{body}</p>", "bl-duo__text"),
            button("descubre nuestros servicios"),
        ],
        direction="column",
    )


def template_home():
    return container(
        "bl-home",
        [
            html('<div class="bl-announce">Texto de la barra de aviso pendiente</div>'),
            site_header(),
            html(HERO),

            section("bl-section bl-section--cream", [
                heading("Romantiza tu vida.", "bl-script bl-center", tag="h1"),
                heading("Diseña un universo que se pueda ver, contar y vivir.",
                        "bl-display bl-center", tag="h2"),
                text("<p>Blomstra es un <strong>estudio creativo</strong> donde transformamos "
                     "ideas, proyectos y momentos importantes en <strong>universos estéticos "
                     "con narrativa propia</strong>.</p>"
                     "<p>Algunos toman forma de marca. Otros se convierten en experiencias. "
                     "Creemos que cuando algo se diseña con intención, la vida también puede "
                     "romantizarse.</p>", "bl-lead bl-center"),
                button("entrar en el universo"),
            ], inner="bl-container bl-container--narrow bl-center"),

            section("bl-section bl-section--cream bl-section--tight", [
                html(COLLAGE),
                text("<p>Aquí no creemos en marcas vacías ni en eventos sin alma. Creemos en "
                     "universos con intención.</p>"
                     "<p>Por eso trabajamos con proyectos que quieren ir más allá de lo "
                     "funcional, proyectos que buscan construir algo con <strong>presencia, "
                     "belleza y significado</strong>.</p>", "bl-lead bl-center"),
            ]),

            html(TICKER),

            section("bl-section bl-section--dark", [
                heading("Dos formas de habitar Blomstra", "bl-heading-lg bl-center", tag="h2"),
                container("bl-duo", [
                    duo_card("Brands", "Universos de marca",
                             "Para emprendedoras y proyectos que quieren transformar una idea "
                             "en una marca clara, coherente y magnética."),
                    duo_card("Experiences", "Experiencias",
                             "Para momentos que merecen convertirse en algo extraordinario. "
                             "Diseñamos bodas y eventos como universos estéticos que se viven "
                             "y se recuerdan."),
                ]),
            ]),

            html(TICKER),

            section("bl-section bl-section--cream", [
                heading("Esta podría ser tu marca", "bl-heading-lg bl-center", tag="h2"),
                html('<div class="bl-strip"><div></div><div></div><div></div>'
                     '<div></div><div></div></div>'),
            ]),

            section("bl-section bl-section--dark", [
                container("bl-split-text", [
                    container("bl-split-text__col", [
                        heading("Cómo trabajamos", "bl-heading-lg", tag="h2"),
                        text("<p>Cada proyecto en Blomstra comienza igual: escuchando.</p>"
                             "<p>Escuchamos la historia detrás del proyecto. La visión que la "
                             "impulsa. La sensibilidad que la hace única.</p>"
                             "<p>A partir de ahí construimos un universo que puede expresarse de "
                             "forma clara y coherente a través de la narrativa, el diseño "
                             "gráfico y la dirección de arte.</p>", "bl-lead"),
                        button("descubre nuestros servicios"),
                    ], direction="column"),
                    html('<div class="bl-split-text__media"></div>'),
                ]),
            ]),

            container("bl-stripes", [
                container("bl-manifesto", [
                    heading("Manifiesto", "bl-heading-lg", tag="h2"),
                    text("<p>Romantizar la vida no significa idealizarla.</p>"
                         "<p>Significa prestar atención.</p>"
                         "<p>A los detalles que crean atmósfera.<br>"
                         "A las historias que merecen ser contadas.<br>"
                         "A los momentos que transforman lo cotidiano en algo especial.</p>"
                         "<p>En Blomstra creemos que una marca, una boda o un evento pueden "
                         "convertirse en un universo propio cuando se diseñan con intención.</p>"
                         "<p>Nuestro trabajo consiste en dar forma a esos mundos para que puedan "
                         "verse, contarse y vivirse.</p>", ""),
                ], direction="column"),
            ], direction="column"),

            section("bl-section bl-section--cream", [
                container("bl-founder", [
                    html('<div class="bl-founder__media"></div>'),
                    container("bl-founder__col", [
                        heading("Meet the founder", "bl-script", tag="p"),
                        heading("Anna Areas · The founder.", "bl-founder__name", tag="p"),
                        heading("Designer, Creative Director & Visual Storyteller",
                                "bl-founder__role", tag="p"),
                        # OJO: este copy repite casi literal el de "Cómo trabajamos".
                        text("<p>Cada proyecto en Blomstra comienza igual: escuchando. "
                             "Escuchamos la historia detrás del proyecto. La visión que la "
                             "impulsa. La sensibilidad que la hace única.</p>"
                             "<p>A partir de ahí construimos un universo que puede expresarse "
                             "de forma clara y coherente. Trabajamos con pocos proyectos a la "
                             "vez para que cada proceso tenga el espacio que necesita.</p>",
                             "bl-lead"),
                        button("Café con la fundadora"),
                    ], direction="column"),
                ]),
            ]),

            section("bl-section bl-section--cotton", [
                text("<p>Si sientes que tu proyecto o tu historia <em>tiene un universo "
                     "propio</em>, pero todavía no sabes cómo darle forma, podemos trabajar "
                     "juntas.</p>", "bl-display bl-center"),
                button("Trabajar con Blomstra"),
            ], inner="bl-container bl-container--narrow bl-center"),

            section("bl-section bl-section--cream bl-section--tight", [
                container("bl-newsletter", [
                    container("bl-newsletter__col", [
                        heading("The Club", "bl-script", tag="p"),
                        heading("Sign up to our newsletter", "bl-duo__eyebrow", tag="p"),
                        text("<p>Sign up to be told about new services &amp; updates launches "
                             "before anyone else. We promise not to flood your inbox.</p>",
                             "bl-lead"),
                        # En WordPress esto se sustituye por el shortcode de Fluent Forms.
                        html('<p><em>[Aquí va el shortcode del formulario de Fluent Forms]</em></p>'),
                    ], direction="column"),
                    html('<div class="bl-strip bl-strip--3"><div></div><div></div><div></div></div>'),
                ]),
            ]),

            html('<p class="bl-wordmark">BLOMSTRA</p>', "bl-section--cream"),
        ],
        direction="column",
    )


TEMPLATES = {
    "01-portal": ("Blomstra — Portal", template_portal),
    "03-home": ("Blomstra — Home", template_home),
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
