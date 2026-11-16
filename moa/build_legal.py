"""Genera los textos legales de MOA para pegar en WordPress.

    python3 build_legal.py

Escribe en wordpress/legal/ un archivo por página (aviso legal, privacidad y
cookies). Cada uno lleva los tres idiomas con un selector CA · ES · EN arriba,
para crear una sola página por texto. Los datos se rellenan en src/legal/textos.py;
los que estén vacíos salen marcados en amarillo.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src" / "legal"))
from textos import DATOS, PAGINAS  # noqa: E402

LANGS = [("ca", "CA"), ("es", "ES"), ("en", "EN")]
PENDIENTE = {"ca": "pendent", "es": "pendiente", "en": "pending"}

CSS = """<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
<style>
#moa-legal{max-width:760px;margin:0 auto;padding:40px 20px 80px;font-family:Montserrat,system-ui,sans-serif;font-size:16px;line-height:1.7;color:#2B2D2B;text-align:left}
#moa-legal h1{font-family:'Bricolage Grotesque',system-ui,sans-serif;font-size:2.4rem;line-height:1.05;text-transform:uppercase;margin:0 0 1.5rem;color:#2B2D2B}
#moa-legal h2{font-family:'Bricolage Grotesque',system-ui,sans-serif;font-size:1.25rem;margin:2rem 0 .6rem;color:#2B2D2B}
#moa-legal p,#moa-legal li{margin:0 0 .8em}
#moa-legal ul{padding-left:1.2em}
#moa-legal a{color:#9242F3}
#moa-legal .langs{display:flex;gap:6px;margin:0 0 2rem}
#moa-legal .langs a{padding:.35em .7em;border-radius:6px;border:1px solid #E6E6E3;text-decoration:none;font-weight:600;font-size:.8rem;color:#2B2D2B}
#moa-legal .langs a.on{background:#9242F3;border-color:#9242F3;color:#fff}
#moa-legal .falta{background:#FFF3A3;padding:0 .3em;border-radius:3px;font-weight:600}
#moa-legal [data-lang]{display:none}
#moa-legal [data-lang].on{display:block}
</style>"""

JS = """<script>(function(){var r=document.getElementById('moa-legal');if(!r)return;
function set(l){r.querySelectorAll('[data-lang]').forEach(function(s){s.classList.toggle('on',s.dataset.lang===l)});
r.querySelectorAll('.langs a').forEach(function(a){a.classList.toggle('on',a.dataset.set===l)});}
var l='ca';try{l=localStorage.getItem('moa-lang')||l}catch(e){}
var q=(location.search.match(/[?&]lang=(ca|es|en)/)||[])[1];if(q)l=q;set(l);
r.querySelectorAll('.langs a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();set(a.dataset.set);try{localStorage.setItem('moa-lang',a.dataset.set)}catch(x){}})});})();</script>"""


def fill(html, lang):
    def repl(m):
        v = DATOS.get(m.group(1), "")
        return v if v else '<span class="falta">[%s: %s]</span>' % (m.group(1).upper(), PENDIENTE[lang])
    return re.sub(r"\{\{(\w+)\}\}", repl, html)


def build():
    out_dir = ROOT / "wordpress" / "legal"
    out_dir.mkdir(parents=True, exist_ok=True)
    for slug, langs in PAGINAS.items():
        nav = '<nav class="langs">' + "".join(
            '<a href="#" data-set="%s">%s</a>' % (c, n) for c, n in LANGS) + "</nav>"
        secs = "".join(
            '<section data-lang="%s" lang="%s"%s><h1>%s</h1>%s</section>' % (
                c, c, ' class="on"' if c == "ca" else "", langs[c]["titulo"], fill(langs[c]["html"], c))
            for c, _ in LANGS)
        html = ("<!-- MOA · %s. Generado con build_legal.py: los datos se cambian en src/legal/textos.py -->\n"
                % slug + CSS + '\n<div id="moa-legal">' + nav + secs + "</div>\n" + JS + "\n")
        html = "\n".join(l for l in html.split("\n") if l.strip())
        for ext in ("html", "txt"):
            (out_dir / ("%s.%s" % (slug, ext))).write_text(html, encoding="utf-8")
        faltan = sorted(set(re.findall(r"\[(\w+): pendent\]", html)))
        print("wordpress/legal/%s.txt%s" % (slug, ("  · faltan: " + ", ".join(faltan)) if faltan else ""))


if __name__ == "__main__":
    build()
