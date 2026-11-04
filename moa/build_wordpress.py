"""Genera la web de MOA para pegar en un bloque de HTML personalizado de WordPress.

    python3 build_wordpress.py

Lee las páginas ya generadas por build.py (index.html, es.html, en.html), así que
primero hay que ejecutar ese. Escribe en wordpress/:

    moa-wordpress-ca.html    català
    moa-wordpress-es.html    castellano
    moa-wordpress-en.html    English

Cada archivo lleva todo dentro (estilos, guion, logos y fotos) para copiar y
pegar sin subir nada por FTP. Lo que se hace para que conviva con un tema:

1. Todo va dentro de <div id="moa-app"> y cada selector del CSS se prefija con
   ese id: #moa-app .btn gana a cualquier .btn del tema y nuestras reglas no
   salen del contenedor. :root, html y body pasan a ser el propio contenedor.
2. El contenedor arranca con un reinicio propio para que no se cuelen fondos,
   bordes, subrayados ni tipografías del tema.
3. Los identificadores se prefijan con moa- para no chocar con los del tema.
4. La cabecera pasa de fixed a sticky (por debajo de la del tema si es fija) y
   el contenedor sale a todo el ancho de la ventana.
5. El JavaScript solo busca dentro del contenedor.
6. Red de seguridad: si un plugin de caché rompe o aplaza el guion, se retira la
   marca has-js y la web se ve entera, sin animaciones.
"""
import base64
import datetime
import io
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
DEST = ROOT / "wordpress"
APP = "#moa-app"

# Direcciones de las tres páginas en WordPress (para el selector de idioma).
URLS = {"ca": "/", "es": "/es/", "en": "/en/"}

# Vídeo de portada ya subido a la Biblioteca de medios. Vacío: no hay vídeo y se
# ve el hueco de foto. Ejemplo: "/wp-content/uploads/2026/11/portada.mp4"
VIDEO_PORTADA = ""

PAGES = {"ca": "index.html", "es": "es.html", "en": "en.html", "3-idiomas": "moa-3-idiomas.html"}

# Clases que en la web normal van en <html> o <body> y aquí en el contenedor
CLASES_RAIZ = {".js": ".has-js", ".loaded": ".loaded", ".menu-open": ".menu-open"}

KEYFRAMES = ["introArrow", "introOut", "spin", "hint", "qIn", "rv"]

SELLO = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


# --------------------------------------------------------------------------- #
# CSS
# --------------------------------------------------------------------------- #

def split_top(text, sep):
    """Parte por `sep` solo fuera de paréntesis y comillas."""
    out, depth, quote, cur = [], 0, None, ""
    for ch in text:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def prefix_selector(sel):
    sel = sel.strip()
    if not sel:
        return None
    if sel in (":root", "html", "body"):
        return APP
    if sel.startswith(("html ", "body ")):
        sel = sel.split(" ", 1)[1]
    for raiz, clase in CLASES_RAIZ.items():
        if sel.startswith(raiz + " "):
            return APP + clase + " " + sel[len(raiz) + 1:]
    return APP + " " + sel


def scope_rules(css):
    """Recorre el CSS por bloques respetando llaves y prefija los selectores."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j == -1:
            out.append(css[i:])
            break
        head = css[i:j].strip()
        # buscar el cierre de este bloque
        depth, k = 1, j + 1
        while depth and k < n:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        body = css[j + 1:k - 1]
        if head.startswith("@media") or head.startswith("@supports"):
            out.append(head + "{" + scope_rules(body) + "}")
        elif head.startswith("@keyframes") or head.startswith("@font-face"):
            out.append(head + "{" + body + "}")
        else:
            sels = [prefix_selector(s) for s in split_top(head, ",")]
            sels = [s for s in sels if s]
            if head.strip() == "html":      # scroll suave y margen: los hace el guion
                i = k
                continue
            out.append(",".join(sels) + "{" + body + "}")
        i = k
    return "\n".join(out)


RESET = APP + "," + APP + " *," + APP + " *::before," + APP + """ *::after{
  margin:0;padding:0;background:none;border:0;border-radius:0;box-shadow:none;outline:0;text-decoration:none;
  filter:none;mix-blend-mode:normal;float:none;clear:none;min-width:0;max-height:none;
  transition:none;animation:none;list-style:none;
  color:inherit;font-family:inherit;font-size:inherit;font-style:inherit;font-weight:inherit;font-variant:inherit;
  line-height:inherit;letter-spacing:inherit;text-transform:inherit;text-shadow:inherit;text-align:inherit}
""" + APP + "{font-style:normal;font-variant:normal;font-weight:400;text-align:left;text-transform:none;text-shadow:none}\n" + \
    ",".join(APP + " " + e for e in ("h1", "h2", "h3", "p", "ul", "ol", "li", "figure", "blockquote", "form", "fieldset", "legend")) + \
    "{margin:0;padding:0}\n" + APP + " strong{font-weight:600}\n" + APP + " em{font-style:italic}\n"

AJUSTES = """
/* ---------- Ajustes para vivir dentro de un tema ---------- */
#moa-app{
  /* Si el tema tiene una cabecera fija, poner aquí su altura para que la de MOA
     quede justo debajo al bajar. Con 0px se comporta como la web suelta. */
  --moa-top:0px;
  position:relative;isolation:isolate;margin:0;padding:0;
  /* A todo el ancho aunque el tema meta el contenido en una columna. Se descuenta
     la barra de desplazamiento (la mide el guion de arriba) para no desbordar.
     overflow-x visible: hidden o clip romperían el sticky de servicios. */
  width:calc(100vw - var(--moa-barra,0px));max-width:calc(100vw - var(--moa-barra,0px));
  margin-inline:calc(50% - (100vw - var(--moa-barra,0px)) / 2);
  overflow-x:visible;
}
#moa-app .header{position:sticky;top:var(--moa-top,0px)}
#moa-app .hero{padding-top:0;min-height:calc(100vh - 74px - var(--moa-top,0px))}
#moa-app .hero,#moa-app .intro-sec,#moa-app .who,#moa-app .community,#moa-app .how,#moa-app .stats,#moa-app .behind,#moa-app .contact{overflow-x:clip}
#moa-app .wrap{box-sizing:border-box}
/* Botones: algunos temas pintan .btn o button con !important */
#moa-app .btn,#moa-app button{background:transparent!important}
#moa-app .btn-fill{background:var(--violeta)!important}
#moa-app .btn-wa{background:#1E8E50!important}
#moa-app .btn::before{background:var(--carbon)!important}
#moa-app .btn-light::before{background:var(--crema)!important}
"""


def rem_to_px(css):
    """El tema puede cambiar el tamaño de letra de <html> y con él todos los rem.
    Se pasan a píxeles (1rem = 16px, el tamaño base de la web suelta)."""
    def px(m):
        v = float(m.group(1)) * 16
        return ("%.2f" % v).rstrip("0").rstrip(".") + "px"
    return re.sub(r"(?<![\w.-])(\d*\.?\d+)rem\b", px, css)


def scope_css(css):
    # Fuera comentarios: uno pegado delante de un @media hacía que no se reconociera
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = rem_to_px(css)
    # Renombrar las animaciones solo donde se definen y donde se usan: un \b a
    # secas también pillaría clases como .rv-row o .hs-hint
    names = "|".join(KEYFRAMES)
    css = re.sub(r"@keyframes (%s)\b" % names, r"@keyframes moa-\1", css)
    css = re.sub(r"(animation(?:-name)?:)([^;}]*)",
                 lambda m: m.group(1) + re.sub(r"(?<![\w-])(%s)(?![\w-])" % names, r"moa-\1", m.group(2)), css)
    scoped = scope_rules(css)
    sueltos = [h for h in re.findall(r"(?:^|[{}])\s*([^{}@]+)\{", scoped)
               if not all(p.strip().startswith(APP) or re.fullmatch(r"\s*(from|to|[\d.]+%)\s*", p) for p in split_top(h, ","))]
    assert not sueltos, "selectores sin prefijar: %s" % sueltos[:5]
    return RESET + scoped + AJUSTES


# --------------------------------------------------------------------------- #
# HTML y JS
# --------------------------------------------------------------------------- #

def inline_assets(html):
    cache = {}

    def data(rel):
        if rel not in cache:
            p = ROOT / rel
            if p.suffix == ".svg":
                cache[rel] = "data:image/svg+xml;base64," + base64.b64encode(p.read_bytes()).decode()
            else:
                im = Image.open(p).convert("RGB")
                w = min(900, im.width)
                im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
                buf = io.BytesIO()
                im.save(buf, "JPEG", quality=80, optimize=True, progressive=True)
                cache[rel] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
        return cache[rel]

    def repl(m):
        rel = m.group(2)
        if not (ROOT / rel).exists():
            return m.group(0)
        return '%s="%s"' % (m.group(1), data(rel))

    html = re.sub(r'(src|href)="((?:assets|fotos)/[^"]+\.(?:svg|jpg|jpeg|png))"', repl, html)
    # Rutas dentro de data-ta (los logos de cada idioma en la versión de tres idiomas)
    return re.sub(r'(?<![\w/])((?:assets|fotos)/[\w./-]+\.(?:svg|jpg|jpeg|png))',
                  lambda m: data(m.group(1)) if (ROOT / m.group(1)).exists() else m.group(0), html)


def scope_js(js, ids):
    js = js.replace("(function(){\n", """(function(){
  // Todo se busca dentro del contenedor, nunca en el resto del tema
  var APP = document.getElementById('moa-app');
  if (!APP) return;
  APP.classList.add('moa-ok');
""", 1)
    js = js.replace("document.body.classList", "APP.classList")
    js = js.replace("document.querySelectorAll(", "APP.querySelectorAll(")
    js = js.replace("document.querySelector(", "APP.querySelector(")
    for i in ids:
        js = js.replace("getElementById('%s')" % i, "getElementById('moa-%s')" % i)
    # La cabecera ya no está arriba de la ventana: «pegada» según su posición real
    old = "    header.classList.toggle('scrolled', y > 30);\n"
    assert old in js, "no encuentro el cambio de cabecera"
    js = js.replace(old, "    var caja = header.getBoundingClientRect(), pegada = caja.top <= parseFloat(getComputedStyle(APP).getPropertyValue('--moa-top') || 0) + 1;\n"
                         "    header.classList.toggle('scrolled', pegada && y > 30);\n")
    old = "header.classList.toggle('hide', dy > 4 && y > 300 ? true"
    assert old in js, "no encuentro la ocultación de cabecera"
    js = js.replace(old, "header.classList.toggle('hide', dy > 4 && y > 300 && pegada ? true")
    # Scroll suave de los enlaces internos, descontando la cabecera
    js = js.rstrip()
    assert js.endswith("})();")
    js = js[:-5] + """
  APP.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var destino = document.getElementById(a.getAttribute('href').slice(1));
      if (!destino) return;
      e.preventDefault();
      var top = destino.getBoundingClientRect().top + window.scrollY - 74 - (parseFloat(getComputedStyle(APP).getPropertyValue('--moa-top')) || 0);
      window.scrollTo({top: top, behavior: reduce ? 'auto' : 'smooth'});
    });
  });
})();"""
    return js


GUARDIA = (
    '<script>(function(){var a=document.getElementById("moa-app");if(!a)return;'
    'a.classList.add("has-js");'
    # ancho de la barra de desplazamiento, acotado (en móvil puede salir negativo)
    'var m=function(){var b=window.innerWidth-document.documentElement.clientWidth;'
    'if(!(b>0&&b<40))b=0;a.style.setProperty("--moa-barra",b+"px");};'
    'm();window.addEventListener("resize",m);'
    'var r=function(){if(!a.classList.contains("moa-ok"))a.classList.remove("has-js");};'
    'if(document.readyState==="complete"){setTimeout(r,300);}'
    'else{window.addEventListener("load",function(){setTimeout(r,300);});}'
    'setTimeout(r,6000);})();</script>')


def build(lang):
    html = (ROOT / PAGES[lang]).read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    fonts = "\n".join(re.findall(r'<link rel="preconnect"[^>]*>|<link href="https://fonts[^>]*>', html))
    body = html[html.index("<body>") + 6:html.index("</body>")]
    js = re.search(r"<script>\n(\(function\(\)\{.*\}\)\(\);)\n</script>", body, re.S)
    assert js, "no encuentro el guion principal"
    body = body.replace(js.group(0), "")
    js = js.group(1)

    # identificadores propios
    ids = sorted(set(re.findall(r'\sid="([^"]+)"', body)), key=len, reverse=True)
    for i in ids:
        for attr in ("id", "for", "aria-controls", "aria-labelledby"):
            body = body.replace('%s="%s"' % (attr, i), '%s="moa-%s"' % (attr, i))
        body = body.replace('href="#%s"' % i, 'href="#moa-%s"' % i)

    # selector de idioma -> páginas de WordPress
    for code, page in PAGES.items():
        if code not in URLS:
            continue
        body = body.replace('href="%s" hreflang="%s"' % (page, code), 'href="%s" hreflang="%s"' % (URLS[code], code))

    # vídeo de portada: solo si ya está subido
    if VIDEO_PORTADA:
        body = body.replace('src="fotos/portada.mp4"', 'src="%s"' % VIDEO_PORTADA)
    else:
        body = re.sub(r'\s*<!-- Vídeo de portada:.*?</video>', "", body, flags=re.S)

    body = inline_assets(body)
    leftover = re.findall(r'(?:src|href)="(?:assets|fotos)/[^"]+"', body)
    assert not leftover, "rutas sin incrustar: %s" % leftover[:3]

    css = scope_css(css)
    js = scope_js(js, ids)

    # sin líneas en blanco: algunos editores las convierten en párrafos
    def compact(t):
        return "\n".join(l for l in t.split("\n") if l.strip())

    out = (
        "<!-- MOA · Moviment i Salut — bloque de HTML personalizado (%s). Generado %s.\n"
        "     No editar aquí: los cambios se hacen en src/ y se regenera con build.py y build_wordpress.py. -->\n"
        % (lang, SELLO)
        + fonts + "\n"
        + "<style>\n" + compact(css) + "\n</style>\n"
        + '<div id="moa-app" lang="%s">\n' % (lang if lang in URLS else "ca")
        + GUARDIA + "\n"
        + compact(body.strip()) + "\n"
        + "<script>\n" + compact(js) + "\n</script>\n"
        + "</div>\n"
    )
    DEST.mkdir(exist_ok=True)
    dst = DEST / ("moa-wordpress-%s.html" % lang)
    dst.write_text(out, encoding="utf-8")
    print("%s  %d KB" % (dst.relative_to(ROOT), len(out.encode()) // 1024))


if __name__ == "__main__":
    for code in (sys.argv[1:] or PAGES):
        build(code)
