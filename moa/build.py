"""Genera las tres versiones de la web de MOA a partir de la plantilla y los textos.

    python3 build.py

Salida: index.html (català), es.html (castellano) y en.html (English), y además
moa-3-idiomas.html: una sola página con los tres idiomas y un selector que
cambia el texto al momento, sin recargar.
"""
import html as htmlmod
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


MULTI = "moa-3-idiomas.html"
LANGS = list(PAGES)

# Se añade al final del guion principal en la versión con los tres idiomas
MULTI_JS = r"""
  // ---- Cambio de idioma dentro de la misma página ----
  var LANG_KEY = 'moa-lang';
  function pickLang(){
    var q = (location.search.match(/[?&]lang=(ca|es|en)/) || [])[1];
    if (q) return q;
    try { var s = localStorage.getItem(LANG_KEY); if (I18N[s]) return s; } catch (e) {}
    var n = (navigator.language || 'ca').slice(0, 2).toLowerCase();
    return I18N[n] ? n : 'ca';
  }
  function splitWords(el){
    var i = 0;
    (function walk(node){
      Array.prototype.slice.call(node.childNodes).forEach(function(child){
        if (child.nodeType === 3) {
          var frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach(function(part){
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
            var w = document.createElement('span'); w.className = 'w';
            var s = document.createElement('span'); s.textContent = part; s.style.setProperty('--i', i++);
            w.appendChild(s); frag.appendChild(w);
          });
          node.replaceChild(frag, child);
        } else if (child.nodeType === 1 && child.tagName !== 'BR') { walk(child); }
      });
    })(el);
  }
  function setLang(lang){
    if (!I18N[lang]) return;
    var D = I18N[lang].t;
    T = I18N[lang].js;
    var splits = document.querySelectorAll('[data-split]');
    splits.forEach(function(el){
      el.querySelectorAll('.w').forEach(function(w){ w.replaceWith(document.createTextNode(w.textContent)); });
      el.normalize();
    });
    document.querySelectorAll('[data-t]').forEach(function(el){
      var v = D[el.getAttribute('data-t')];
      if (v == null) return;
      if (/[<&]/.test(v)) el.innerHTML = v; else el.textContent = v;
    });
    document.querySelectorAll('[data-ta]').forEach(function(el){
      var map = JSON.parse(el.getAttribute('data-ta'));
      Object.keys(map).forEach(function(a){ el.setAttribute(a, map[a][lang]); });
    });
    splits.forEach(splitWords);
    document.querySelectorAll('[data-setlang]').forEach(function(a){
      if (a.getAttribute('data-setlang') === lang) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
    (document.getElementById('moa-app') || document.documentElement).lang = lang;
    if (!document.getElementById('moa-app')) document.title = D.meta_title;
    document.getElementById('waFloat').href = waLink(T.waDefault);
    menuBtn.setAttribute('aria-label', document.body.classList.contains('menu-open') ? T.menuClose : T.menuOpen);
    if (result.classList.contains('active')) document.getElementById('qRestart').click(); else show(current);
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
  }
  document.querySelectorAll('[data-setlang]').forEach(function(a){
    a.addEventListener('click', function(e){
      e.preventDefault();
      setLang(a.getAttribute('data-setlang'));
      if (document.body.classList.contains('menu-open')) setMenu(false);
    });
  });
  var firstLang = pickLang();
  if (firstLang !== 'ca') setLang(firstLang);
"""


def multi_switch():
    links = []
    for code in LANGS:
        short, name = LANG_LABELS[code]
        cur = ' aria-current="true"' if code == "ca" else ""
        links.append(f'<a href="#" data-setlang="{code}" hreflang="{code}" lang="{code}" title="{name}"{cur}>{short}</a>')
    return '<nav class="langs" aria-label="Idioma / Language">' + "".join(links) + "</nav>"


def build_multi(template):
    vals = {}
    for lang in LANGS:
        v = {k: x for k, x in TEXT[lang].items() if k != "js"}
        v["lang"] = lang
        vals[lang] = v
    ca = vals["ca"]

    head, body = template.split("<body>", 1)
    head = re.sub(r'<link rel="alternate" hreflang[^>]*>\n', "", head)
    head = re.sub(r"\{\{(\w+)\}\}", lambda m: ca[m.group(1)], head)

    body = body.replace("{{lang_switch}}", multi_switch())
    data = {l: {"t": vals[l], "js": TEXT[l]["js"]} for l in LANGS}
    body = body.replace("var T = {{js_i18n}};",
                        "var I18N = " + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") +
                        ";\n  var T = I18N.ca.js;")

    # 1. Atributos: cada etiqueta con {{...}} en sus atributos guarda el valor de
    #    cada idioma en data-ta y se rellena en catalán
    def tag_repl(m):
        tag = m.group(0)
        if "{{" not in tag:
            return tag
        per = {}

        def attr_repl(am):
            name, raw = am.group(1), am.group(2)
            if "{{" not in raw:
                return am.group(0)
            res = {l: re.sub(r"\{\{(\w+)\}\}", lambda k: vals[l][k.group(1)], raw) for l in LANGS}
            per[name] = res
            return '%s="%s"' % (name, htmlmod.escape(res["ca"], quote=True) if "<" in res["ca"] else res["ca"])
        tag = re.sub(r'([\w:-]+)="([^"]*)"', attr_repl, tag)
        ta = htmlmod.escape(json.dumps(per, ensure_ascii=False), quote=True)
        close = "/>" if tag.endswith("/>") else ">"
        return tag[:-len(close)] + ' data-ta="%s"%s' % (ta, close)
    body = re.sub(r"<[a-zA-Z][^<>]*>", tag_repl, body)

    # 2. Texto: si el elemento solo contiene el marcador, data-t va en él;
    #    si no, el texto se envuelve en un <span data-t>
    def own(m):
        return '%s data-t="%s">%s</' % (m.group(1), m.group(2), ca[m.group(2)])
    body = re.sub(r"(<[a-zA-Z][^<>]*?)>\{\{(\w+)\}\}</", own, body)
    body = re.sub(r"\{\{(\w+)\}\}", lambda m: '<span data-t="%s">%s</span>' % (m.group(1), ca[m.group(1)]), body)
    assert "{{" not in body, "quedan marcadores sin resolver"

    old = "\n  window.MOA_OK = true;\n"
    assert body.count(old) == 1, "no encuentro el final del guion"
    body = body.replace(old, MULTI_JS + old)
    html = head.replace('<html lang="ca">', '<html lang="ca">') + "<body>" + body
    (ROOT / MULTI).write_text(html, encoding="utf-8")
    print(f"{MULTI} generado (ca · es · en)")


if __name__ == "__main__":
    build()
    build_multi((ROOT / "src" / "template.html").read_text(encoding="utf-8"))
