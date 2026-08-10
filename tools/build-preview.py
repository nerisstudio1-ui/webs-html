#!/usr/bin/env python3
"""Empaqueta las 5 páginas del sitio en un único HTML autocontenido.

Mantiene el diseño y el contenido tal cual; solo cambia el transporte:
CSS y JS en línea, ilustraciones como data URI y un enrutador por hash que
sustituye la navegación entre archivos.
"""
import base64, os, re

PAGES = [
    ("inicio",       "index.html"),
    ("tratamientos", "servicios.html"),
    ("metodo",       "metodo.html"),
    ("bela",         "estudio.html"),
    ("contacto",     "contacto.html"),
]
FILE_TO_SLUG = {f: s for s, f in PAGES}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "bela-preview.html")
FONT = os.environ.get("PREVIEW_FONT", "")  # woff2 opcional para incrustar como serif


def read(p):
    return open(os.path.join(ROOT, p), encoding="utf-8").read()


def between(s, start, end):
    i = s.index(start)
    j = s.index(end) + len(end)
    return s[i:j]


def ascii_html(text):
    """Entidades numéricas: el documento queda en ASCII puro y no depende
    de que el servidor declare UTF-8."""
    return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in text)


def ascii_css(text):
    r"""Escapes CSS (\XXXX ) para que las cadenas sobrevivan sin charset."""
    return "".join(c if ord(c) < 128 else "\\%04x " % ord(c) for c in text)


def ascii_js(text):
    r"""Escapes uXXXX para las cadenas de JavaScript."""
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in text)


# --- ilustraciones como data URI -----------------------------------------
images = {}
for name in os.listdir(os.path.join(ROOT, "assets/img")):
    if not name.endswith(".svg"):
        continue
    raw = open(os.path.join(ROOT, "assets/img", name), "rb").read()
    images["assets/img/" + name] = (
        "data:image/svg+xml;base64," + base64.b64encode(raw).decode()
    )

font_b64 = base64.b64encode(open(FONT, "rb").read()).decode() if FONT and os.path.exists(FONT) else ""

css = read("assets/css/style.css")
js = read("assets/js/main.js")

index = read("index.html")
announce = between(index, '<div class="announce"', "</div>\n</div>") + "\n"
header = between(index, '<header class="header', "</header>")
mobile = between(index, '<div class="mobile-nav"', '</nav>\n  <div class="mobile-nav__foot">')
mobile = between(index, '<div class="mobile-nav"', "</div>\n</div>") + "\n"
footer = between(index, '<footer class="footer">', "</footer>")
wa = between(index, '<a class="wa-float"', "</a>")


def rewrite_links(html):
    """servicios.html#cejas → #/tratamientos/cejas ; index.html → #/inicio"""
    def sub(m):
        f, anchor = m.group(1), m.group(2) or ""
        slug = FILE_TO_SLUG.get(f)
        if not slug:
            return m.group(0)
        return 'href="#/' + slug + (("/" + anchor[1:]) if anchor else "") + '"'
    return re.sub(r'href="([a-z]+\.html)(#[a-z0-9\-]+)?"', sub, html)


def swap_images(html):
    for path, uri in images.items():
        html = html.replace('src="' + path + '"', 'src="' + uri + '"')
    return html


# --- cuerpo de cada página ------------------------------------------------
sections = []
for slug, filename in PAGES:
    page = read(filename)
    main = between(page, "<main>", "</main>")
    main = main[len("<main>"):-len("</main>")]
    sections.append(
        '<div class="page" data-page="%s" id="page-%s">%s</div>' % (slug, slug, main)
    )

body = announce + header + mobile + \
    '<main id="app">' + "\n".join(sections) + "</main>" + footer + wa + "</a>"
body = swap_images(rewrite_links(body))

# el logotipo del header vuelve al inicio
body = body.replace('href="index.html"', 'href="#/inicio"')

EXTRA_CSS = """
/* --- Empaquetado para vista previa ------------------------------------ */
%s:root {
  --serif: "Playfair Display", "Fraunces", "Didot", "Bodoni MT", Georgia, serif;
  --sans: "Jost", "Futura", "Avenir Next", "Century Gothic", "Trebuchet MS", system-ui, sans-serif;
}
.page { display: none; }
.page.is-active { display: block; }

/* En la vista previa el contenido de cada página aparece al entrar en ella:
   las páginas ocultas nunca intersecan, así que el efecto va por CSS. */
.js .page.is-active .reveal { animation: revealin .9s var(--ease) both; }
.js .page.is-active .reveal[data-delay="1"] { animation-delay: .09s; }
.js .page.is-active .reveal[data-delay="2"] { animation-delay: .18s; }
.js .page.is-active .reveal[data-delay="3"] { animation-delay: .27s; }
@keyframes revealin { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) {
  .js .page.is-active .reveal { animation: none; opacity: 1; transform: none; }
}
.preview-note {
  position: fixed; left: 50%%; bottom: clamp(1rem, 2.5vw, 2rem);
  transform: translateX(-50%%);
  z-index: 54;
  background: rgba(46,15,19,.92); color: var(--cream);
  padding: .55rem 1.1rem; border-radius: 100px;
  font-size: .68rem; letter-spacing: .1em; text-transform: uppercase;
  display: flex; align-items: center; gap: .8rem;
  box-shadow: 0 8px 24px rgba(46,15,19,.25);
}
.preview-note button { color: inherit; opacity: .6; font-size: 1rem; line-height: 1; }
.preview-note button:hover { opacity: 1; }
@media (max-width: 720px) { .preview-note { display: none; } }
""" % (
    '@font-face{font-family:"Fraunces";src:url(data:font/woff2;base64,'
    + font_b64 + ');font-weight:600;font-style:normal;font-display:swap}'
    if font_b64 else ""
)

ROUTER_JS = """
/* --- Enrutador de la vista previa -------------------------------------- */
(function () {
  var pages = document.querySelectorAll('.page');
  var links = document.querySelectorAll('a[href^="#/"]');

  function paint() {
    var raw = (location.hash || '#/inicio').slice(2);
    var parts = raw.split('/');
    var slug = parts[0] || 'inicio';
    var anchor = parts[1];
    var found = false;

    pages.forEach(function (p) {
      var on = p.dataset.page === slug;
      p.classList.toggle('is-active', on);
      if (on) found = true;
    });
    if (!found) {
      pages[0].classList.add('is-active');
      slug = pages[0].dataset.page;
    }

    links.forEach(function (a) {
      var target = a.getAttribute('href').slice(2).split('/')[0];
      if (a.closest('.nav') || a.closest('.mobile-nav__links')) {
        if (target === slug) a.setAttribute('aria-current', 'page');
        else a.removeAttribute('aria-current');
      }
    });

    if (anchor) {
      var el = document.getElementById(anchor);
      if (el) { el.scrollIntoView({ behavior: 'auto', block: 'start' }); return; }
    }
    window.scrollTo(0, 0);
  }

  window.addEventListener('hashchange', paint);
  paint();

  var note = document.querySelector('.preview-note');
  if (note) {
    note.querySelector('button').addEventListener('click', function () { note.remove(); });
  }
})();
"""

NOTE = ('<div class="preview-note"><span>Vista previa · imágenes de muestra</span>'
        '<button type="button" aria-label="Ocultar aviso">&#10005;</button></div>')

html = (
    '<meta charset="utf-8">\n'
    '<title>Bela Brow Studio &amp; Beauty</title>\n'
    '<style>\n' + ascii_css(css + "\n" + EXTRA_CSS) + '\n</style>\n'
    + '<script>document.documentElement.classList.add("js");</script>\n'
    + ascii_html(body + "\n" + NOTE) + "\n"
    + "<script>\n" + ascii_js(js + "\n" + ROUTER_JS) + "\n</script>\n"
)

open(OUT, "w", encoding="utf-8").write(html)
print("%s escrito · %.1f MB" % (OUT, len(html.encode()) / 1e6))
