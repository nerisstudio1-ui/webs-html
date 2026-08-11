#!/usr/bin/env python3
"""
Genera las plantillas de Elementor de Blomstra.

Criterio: **todo con widgets nativos de Elementor y estilos en los controles de
Elementor**, para que el cliente pueda cambiar textos, colores y espaciados
desde el editor sin tocar codigo. No se usan widgets HTML salvo donde no hay
alternativa.

Solo queda en el CSS del tema hijo lo que Elementor no sabe hacer:
  - el fondo de rayas del manifiesto (degradado repetido)
  - las proporciones fijas de los huecos de imagen
  - la inversion de tema del portal en movil
Todo lo demas es editable desde la interfaz.

Se genera con un script en vez de a mano porque el JSON de Elementor es muy
repetitivo y cada elemento necesita su id unico; a mano se cuelan erratas que
Elementor no avisa, simplemente ignora el ajuste.

Uso:  python3 tools/build-templates.py
"""

import json
import pathlib

OUT_DIR = pathlib.Path(__file__).resolve().parent.parent / "elementor-kit" / "content" / "page"

# --- Paleta (los mismos hex que el kit) -------------------------------------
INK = "#221C18"
WHITE = "#FFFFFF"
COTTON = "#D7CBB5"
ANTIQUE = "#FAF3ED"
BONE = "#EFE9D8"
ESPRESSO = "#33261C"
PLACEHOLDER = "#D9D9D9"

DISPLAY = "Playfair Display"
SCRIPT = "Pinyon Script"
SANS = "Montserrat"

_counter = 0


def _next_id():
    global _counter
    _counter += 1
    return f"bl{_counter:05d}"


# --- Helpers de ajustes -----------------------------------------------------

def dim(top=0, right=0, bottom=0, left=0, unit="px"):
    return {"unit": unit, "top": str(top), "right": str(right),
            "bottom": str(bottom), "left": str(left), "isLinked": False}


def size(value, unit="px"):
    return {"unit": unit, "size": value, "sizes": []}


def gap(value):
    return {"unit": "px", "size": value, "column": str(value), "row": str(value),
            "isLinked": True}


def typo(prefix="typography_", family=None, fsize=None, weight=None, ls=None,
         lh=None, transform=None, style=None, fsize_tablet=None, fsize_mobile=None,
         fsize_unit="px"):
    """Tipografia personalizada de un widget, en los controles de Elementor."""
    s = {f"{prefix}typography": "custom"}
    if family:        s[f"{prefix}font_family"] = family
    if fsize:         s[f"{prefix}font_size"] = size(fsize, fsize_unit)
    if fsize_tablet:  s[f"{prefix}font_size_tablet"] = size(fsize_tablet)
    if fsize_mobile:  s[f"{prefix}font_size_mobile"] = size(fsize_mobile)
    if weight:        s[f"{prefix}font_weight"] = weight
    if ls is not None: s[f"{prefix}letter_spacing"] = size(ls)
    if lh:            s[f"{prefix}line_height"] = {"unit": "em", "size": lh, "sizes": []}
    if transform:     s[f"{prefix}text_transform"] = transform
    if style:         s[f"{prefix}font_style"] = style
    return s


# --- Constructores de elementos ---------------------------------------------

def container(children, direction="column", justify=None, align=None, gap_px=0,
              padding=None, bg=None, min_h=None, width=None, boxed=False,
              border=None, radius=None, css_class="", grow=None, extra=None,
              stack_mobile=True):
    s = {
        "container_type": "flex",
        "content_width": "boxed" if boxed else "full",
        "flex_direction": direction,
        "flex_gap": gap(gap_px),
        "padding": padding or dim(),
    }
    # Las filas se apilan en movil. Es un control responsive nativo de
    # Elementor, asi que se puede cambiar desde el editor.
    if direction == "row" and stack_mobile:
        s["flex_direction_mobile"] = "column"
        s["flex_gap_mobile"] = gap(max(gap_px // 2, 24))
    if justify:  s["flex_justify_content"] = justify
    if align:    s["flex_align_items"] = align
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    if min_h:    s["min_height"] = min_h
    if width:    s["width"] = width
    if grow is not None:
        # En Elementor las propiedades del elemento COMO HIJO llevan guion bajo.
        # Se acompanan de una clase CSS que garantiza el reparto a partes
        # iguales aunque cambie el nombre del control entre versiones.
        s["_flex_size"] = "custom"
        s["_flex_grow"] = grow
        s["_flex_shrink"] = 1
    if border:
        s["border_border"] = "solid"
        s["border_width"] = border["width"]
        s["border_color"] = border["color"]
    if radius:   s["border_radius"] = radius
    if css_class: s["_css_classes"] = css_class
    if extra:    s.update(extra)
    return {"id": _next_id(), "elType": "container", "isInner": False,
            "settings": s, "elements": children}


def widget(kind, settings):
    return {"id": _next_id(), "elType": "widget", "widgetType": kind,
            "settings": settings, "elements": []}


def heading(title, tag="h2", align=None, color=INK, url=None, css_class="", **t):
    s = {"title": title, "header_size": tag}
    if align: s["align"] = align
    if color: s["title_color"] = color
    if url is not None:
        s["link"] = {"url": url, "is_external": "", "nofollow": ""}
    if css_class: s["_css_classes"] = css_class
    s.update(typo(**t))
    return widget("heading", s)


def text(html_body, align=None, color=INK, css_class="", **t):
    s = {"editor": html_body}
    if align: s["align"] = align
    if color: s["text_color"] = color
    if css_class: s["_css_classes"] = css_class
    s.update(typo(**t))
    return widget("text-editor", s)


def button(label, url="#", color=INK, border_color=None, hover_bg=INK,
           hover_color=ANTIQUE, align="center", radius_px=0, pad=None, **t):
    s = {
        "text": label,
        "link": {"url": url, "is_external": "", "nofollow": ""},
        "align": align,
        "button_text_color": color,
        "background_color": "#00000000",
        "hover_color": hover_color,
        "button_background_hover_color": hover_bg,
        "border_border": "solid",
        "border_width": dim(1, 1, 1, 1),
        "border_color": border_color or color,
        "border_radius": dim(radius_px, radius_px, radius_px, radius_px),
        "text_padding": pad or dim(16, 30, 16, 30),
    }
    s.update(typo(**t))
    return widget("button", s)


def icon(name, library, color=INK, px=22, url=None):
    s = {
        "selected_icon": {"value": name, "library": library},
        "primary_color": color,
        "size": size(px),
        "view": "default",
    }
    if url is not None:
        s["link"] = {"url": url, "is_external": "", "nofollow": ""}
    return widget("icon", s)


def media(ratio_class, min_h=None):
    """Hueco de imagen. Se sustituye soltando un widget Imagen dentro, o
    poniendole una imagen de fondo al contenedor desde Elementor."""
    return container([], bg=PLACEHOLDER, css_class=ratio_class,
                     min_h=min_h or size(240), width=size(100, "%"))


def spacer(px):
    return widget("spacer", {"space": size(px)})


# --- Piezas comunes ---------------------------------------------------------

def lockup(sub, name_px=46, sub_px=34, color=INK, align="center"):
    """Logotipo de submarca. Provisional hasta que llegue el SVG: cuando llegue,
    se sustituyen estos dos encabezados por un widget Imagen."""
    return container([
        heading("BLOMSTRA", tag="div", align=align, color=color,
                family=DISPLAY, fsize=name_px, weight="500", ls=0.5, lh=1),
        heading(sub, tag="div", align=align, color=color,
                family=SCRIPT, fsize=sub_px, weight="400", lh=1),
    ], gap_px=0, align="center" if align == "center" else "flex-start")


def site_header():
    """Header. En WordPress va en Header Footer Builder, no dentro de la pagina;
    se incluye para poder previsualizar la plantilla suelta."""
    return container([
        icon("fas fa-bars", "fa-solid", color=WHITE, px=26, url="#"),
        container([
            heading("This is", tag="div", align="center", color=WHITE,
                    family=SCRIPT, fsize=18, lh=1),
            heading("BLOMSTRA", tag="div", align="center", color=WHITE,
                    family=DISPLAY, fsize=34, ls=0.7, lh=1),
        ], gap_px=0, align="center", width=size(30, "%")),
        container([
            heading("EN", tag="div", color=WHITE, url="#",
                    family=SANS, fsize=14, ls=1.1),
            icon("fas fa-chevron-down", "fa-solid", color=WHITE, px=12),
            button("WHATS", color=WHITE, hover_bg=WHITE, hover_color=INK,
                   radius_px=999, pad=dim(17, 26, 17, 26),
                   family=SANS, fsize=14, weight="500", ls=1.4),
        ], direction="row", align="center", justify="flex-end", gap_px=14,
            stack_mobile=False),
    ], direction="row", justify="space-between", align="center",
        stack_mobile=False, padding=dim(0, 44, 0, 44), min_h=size(124),
        border={"width": dim(0, 0, 1, 0), "color": WHITE})


def nav_column(items, active=None, color=INK):
    return container([
        heading(i, tag="div", align="center", color=color, url="#",
                css_class="bl-nav-active" if i == active else "",
                family=SANS, fsize=16, ls=1.3, lh=1.1)
        for i in items
    ], gap_px=11, align="center")


# --- Plantilla: portal ------------------------------------------------------

def portal_panel(number, sub, items, active=None, first=True):
    return container([
        # Capsula ovalada del numero: contenedor con borde y radio del 50 %
        container([
            heading(number, tag="div", align="center", color=INK,
                    family=SANS, fsize=14, weight="600", ls=1.7, lh=1),
        ], justify="center", align="center", width=size(124),
            min_h=size(68), border={"width": dim(1, 1, 1, 1), "color": INK},
            radius=dim(50, 50, 50, 50, unit="%")),
        spacer(62),
        lockup(sub),
        spacer(76),
        nav_column(items, active),
    ], align="center", grow=1, css_class="bl-panel",
        padding=dim(120, 24, 40, 24),
        border=None if first else {"width": dim(0, 0, 0, 1), "color": WHITE})


def template_portal():
    return container([
        site_header(),
        container([
            portal_panel("01", "Visual",
                         ["ABOUT", "SERVICES", "LOOKBOOK", "CONTACT US"],
                         active="ABOUT", first=True),
            portal_panel("03", "Experiences",
                         ["ABOUT", "SERVICES", "LOOKBOOK"], first=False),
        ], direction="row", grow=1, css_class="bl-portal__body"),
        container([
            heading(t, tag="div", align="center", color=INK, url="#",
                    family=SANS, fsize=14, ls=1.3)
            for t in ("CONTACT US", "BEHIND BLOMSTRA", "NEWSLETTER")
        ], direction="row", justify="space-around", align="center",
            min_h=size(188), padding=dim(40, 44, 40, 44),
            border={"width": dim(1, 0, 0, 0), "color": WHITE}),
    ], bg=COTTON, min_h=size(100, "vh"), css_class="bl-portal")


# --- Plantilla: home --------------------------------------------------------

def section(children, bg=None, pad_y=120, css_class="", gap_px=26):
    """Seccion a ancho completo con el contenido en un contenedor centrado."""
    return container([
        container(children, gap_px=gap_px, boxed=True, align="center"),
    ], bg=bg, padding=dim(pad_y, 24, pad_y, 24), css_class=css_class)


def ticker():
    return container([
        heading(t, tag="div", color=INK, family=SANS, fsize=11, ls=1.8,
                transform="uppercase")
        for t in ("Diseño", "Dirección de arte", "Branding")
    ], direction="row", justify="center", align="center", gap_px=46,
        stack_mobile=False, padding=dim(14, 16, 14, 16),
        border={"width": dim(1, 0, 1, 0), "color": INK})


def collage_column(label, ratio, offset_top=0):
    return container([
        media(ratio),
        heading(label, tag="div", align="center", color=INK,
                family=DISPLAY, fsize=22, ls=1.1, lh=1.3, transform="uppercase"),
    ], gap_px=24, grow=1, padding=dim(offset_top, 0, 0, 0))


def duo_card(sub, eyebrow, body):
    return container([
        lockup(sub, name_px=38, sub_px=30, color=ANTIQUE),
        media("bl-ratio-43"),
        heading(eyebrow, tag="div", align="center", color=ANTIQUE,
                family=SANS, fsize=12, ls=1.9, transform="uppercase"),
        text(f"<p>{body}</p>", align="center", color=ANTIQUE,
             family=SANS, fsize=16, lh=1.7),
        button("descubre nuestros servicios", color=ANTIQUE,
               hover_bg=ANTIQUE, hover_color=ESPRESSO,
               family=SANS, fsize=13, ls=1.6),
    ], gap_px=26, align="center", grow=1)


def template_home():
    return container([
        heading("Texto de la barra de aviso pendiente", tag="div", align="center",
                color=INK, family=SANS, fsize=11, ls=1.6, transform="uppercase"),
        site_header(),

        # Hero: imagen de fondo del contenedor + boton dentro
        container([
            button("WELCOME TO OUR UNIVERSE", color=WHITE, hover_bg=WHITE,
                   hover_color=INK, pad=dim(15, 34, 15, 34),
                   family=SANS, fsize=12, ls=1.9),
        ], justify="flex-end", align="center", min_h=size(620),
            bg=ESPRESSO, padding=dim(0, 24, 52, 24), css_class="bl-hero"),

        # Presentacion
        section([
            heading("Romantiza tu vida.", tag="h1", align="center", color=INK,
                    family=SCRIPT, fsize=54, fsize_mobile=32, lh=1.05),
            heading("Diseña un universo que se pueda ver, contar y vivir.",
                    tag="h2", align="center", color=INK,
                    family=DISPLAY, fsize=46, fsize_mobile=26, lh=1.2),
            text("<p>Blomstra es un <strong>estudio creativo</strong> donde transformamos "
                 "ideas, proyectos y momentos importantes en <strong>universos estéticos "
                 "con narrativa propia</strong>.</p>"
                 "<p>Algunos toman forma de marca. Otros se convierten en experiencias. "
                 "Creemos que cuando algo se diseña con intención, la vida también puede "
                 "romantizarse.</p>",
                 align="center", family=SANS, fsize=19, lh=1.7),
            button("entrar en el universo", family=SANS, fsize=13, ls=1.6),
        ], bg=ANTIQUE),

        # Collage
        section([
            container([
                collage_column("Narrativas que conectan", "bl-ratio-34", 0),
                collage_column("Marcas con identidad clara", "bl-ratio-11", 60),
                collage_column("Experiencias que se recuerdan", "bl-ratio-34", 20),
            ], direction="row", gap_px=20, css_class="bl-collage"),
            spacer(50),
            text("<p>Aquí no creemos en marcas vacías ni en eventos sin alma. Creemos en "
                 "universos con intención.</p>"
                 "<p>Por eso trabajamos con proyectos que quieren ir más allá de lo "
                 "funcional, proyectos que buscan construir algo con <strong>presencia, "
                 "belleza y significado</strong>.</p>",
                 align="center", family=SANS, fsize=19, lh=1.7),
        ], bg=ANTIQUE, pad_y=80),

        ticker(),

        # Dos formas de habitar Blomstra
        section([
            heading("Dos formas de habitar Blomstra", tag="h2", align="center",
                    color=ANTIQUE, family=DISPLAY, fsize=52, fsize_mobile=27,
                    ls=3, lh=1.15, transform="uppercase"),
            spacer(44),
            container([
                duo_card("Brands", "Universos de marca",
                         "Para emprendedoras y proyectos que quieren transformar una idea "
                         "en una marca clara, coherente y magnética."),
                duo_card("Experiences", "Experiencias",
                         "Para momentos que merecen convertirse en algo extraordinario. "
                         "Diseñamos bodas y eventos como universos estéticos que se viven "
                         "y se recuerdan."),
            ], direction="row", gap_px=70, css_class="bl-duo"),
        ], bg=ESPRESSO),

        ticker(),

        # Esta podria ser tu marca
        section([
            heading("Esta podría ser tu marca", tag="h2", align="center", color=INK,
                    family=DISPLAY, fsize=52, fsize_mobile=27, ls=3, lh=1.15,
                    transform="uppercase"),
            spacer(30),
            container([media("bl-ratio-34") for _ in range(5)],
                      direction="row", gap_px=18, css_class="bl-strip"),
        ], bg=ANTIQUE),

        # Como trabajamos
        section([
            container([
                container([
                    heading("Cómo trabajamos", tag="h2", color=ANTIQUE,
                            family=DISPLAY, fsize=52, fsize_mobile=27, ls=3, lh=1.15,
                            transform="uppercase"),
                    text("<p>Cada proyecto en Blomstra comienza igual: escuchando.</p>"
                         "<p>Escuchamos la historia detrás del proyecto. La visión que la "
                         "impulsa. La sensibilidad que la hace única.</p>"
                         "<p>A partir de ahí construimos un universo que puede expresarse "
                         "de forma clara y coherente a través de la narrativa, el diseño "
                         "gráfico y la dirección de arte.</p>",
                         color=ANTIQUE, family=SANS, fsize=19, lh=1.7),
                    button("descubre nuestros servicios", color=ANTIQUE,
                           hover_bg=ANTIQUE, hover_color=ESPRESSO, align="left",
                           family=SANS, fsize=13, ls=1.6),
                ], gap_px=24, grow=1),
                media("bl-ratio-45"),
            ], direction="row", gap_px=70, align="center", css_class="bl-duo"),
        ], bg=ESPRESSO),

        # Manifiesto. El fondo de rayas es lo unico que Elementor no sabe hacer.
        container([
            container([
                heading("Manifiesto", tag="h2", align="center", color=INK,
                        family=DISPLAY, fsize=52, fsize_mobile=27, ls=3, lh=1.15,
                        transform="uppercase"),
                text("<p>Romantizar la vida no significa idealizarla.</p>"
                     "<p>Significa prestar atención.</p>"
                     "<p>A los detalles que crean atmósfera.<br>"
                     "A las historias que merecen ser contadas.<br>"
                     "A los momentos que transforman lo cotidiano en algo especial.</p>"
                     "<p>En Blomstra creemos que una marca, una boda o un evento pueden "
                     "convertirse en un universo propio cuando se diseñan con intención.</p>"
                     "<p>Nuestro trabajo consiste en dar forma a esos mundos para que "
                     "puedan verse, contarse y vivirse.</p>",
                     align="center", family=SANS, fsize=16, lh=1.8),
            ], gap_px=26, bg=ANTIQUE, boxed=True,
                padding=dim(70, 60, 70, 60)),
        ], padding=dim(90, 24, 90, 24), css_class="bl-stripes"),

        # Fundadora
        section([
            container([
                media("bl-ratio-45"),
                container([
                    heading("Meet the founder", tag="div", color=INK,
                            family=SCRIPT, fsize=34, lh=1),
                    heading("Anna Areas · The founder.", tag="div", color=INK,
                            family=SANS, fsize=17, weight="600"),
                    heading("Designer, Creative Director & Visual Storyteller", tag="div",
                            color=INK, family=SANS, fsize=14, style="italic"),
                    text("<p>Cada proyecto en Blomstra comienza igual: escuchando. "
                         "Escuchamos la historia detrás del proyecto. La visión que la "
                         "impulsa. La sensibilidad que la hace única.</p>"
                         "<p>A partir de ahí construimos un universo que puede expresarse "
                         "de forma clara y coherente. Trabajamos con pocos proyectos a la "
                         "vez para que cada proceso tenga el espacio que necesita.</p>",
                         family=SANS, fsize=19, lh=1.7),
                    button("Café con la fundadora", align="left",
                           family=SANS, fsize=13, ls=1.6),
                ], gap_px=14, grow=1),
            ], direction="row", gap_px=70, align="center", css_class="bl-duo"),
        ], bg=ANTIQUE),

        # Cierre
        section([
            text("<p>Si sientes que tu proyecto o tu historia <em>tiene un universo "
                 "propio</em>, pero todavía no sabes cómo darle forma, podemos trabajar "
                 "juntas.</p>",
                 align="center", family=DISPLAY, fsize=46, fsize_mobile=26, lh=1.3),
            button("Trabajar con Blomstra", family=SANS, fsize=13, ls=1.6),
        ], bg=COTTON),

        # Newsletter
        section([
            container([
                container([
                    heading("The Club", tag="div", color=INK,
                            family=SCRIPT, fsize=34, lh=1),
                    heading("Sign up to our newsletter", tag="div", color=INK,
                            family=SANS, fsize=12, ls=1.9, transform="uppercase"),
                    text("<p>Sign up to be told about new services &amp; updates launches "
                         "before anyone else. We promise not to flood your inbox.</p>",
                         family=SANS, fsize=19, lh=1.7),
                    # Sustituir por el shortcode de Fluent Forms cuando exista.
                    text("<p><em>[Aquí va el shortcode del formulario de Fluent Forms]</em></p>",
                         family=SANS, fsize=15),
                ], gap_px=14, grow=1),
                container([media("bl-ratio-34") for _ in range(3)],
                          direction="row", gap_px=18, grow=1, css_class="bl-strip"),
            ], direction="row", gap_px=60, align="center", css_class="bl-duo"),
        ], bg=ANTIQUE, pad_y=80),

        # Wordmark del pie. vw es una unidad valida en Elementor.
        container([
            heading("BLOMSTRA", tag="div", align="center", color=INK,
                    family=DISPLAY, fsize=15, fsize_unit="vw",
                    fsize_mobile=22, lh=0.78),
        ], bg=ANTIQUE, padding=dim(40, 0, 0, 0), css_class="bl-wordmark"),
    ], bg=ANTIQUE)


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
        (OUT_DIR / f"{slug}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=2) + "\n")
        print(f"Generada {slug}.json")


if __name__ == "__main__":
    main()
