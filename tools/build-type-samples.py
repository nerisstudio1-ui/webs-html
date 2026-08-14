#!/usr/bin/env python3
"""Segunda ronda tipográfica: grotescas condensadas de display, en la línea de
la referencia que envió la clienta. Cada opción se ve en dos tratamientos:
el bloque de bienvenida centrado y el hero de la web."""
import base64, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREV = os.environ.get("PREVIEW_IMG", os.path.join(ROOT, "assets", "img"))
OUT = os.path.join(ROOT, "bela-tipografias.html")

FONTS = [
    # (familia, archivo, peso, estilo, ancho)
    ("Bricolage Grotesque", "bricolage-grotesque-latin-200-800-normal.woff2", "200 800", "normal", "75% 100%"),
    ("Familjen Grotesk", "familjen-grotesk-latin-400-normal.woff2", "400", "normal", ""),
    ("Familjen Grotesk", "familjen-grotesk-latin-500-normal.woff2", "500", "normal", ""),
    ("Archivo", "archivo-latin-300-600-normal.woff2", "300 600", "normal", "62% 125%"),
    ("Darker Grotesque", "darker-grotesque-latin-400-normal.woff2", "400", "normal", ""),
    ("Darker Grotesque", "darker-grotesque-latin-500-normal.woff2", "500", "normal", ""),
    ("Instrument Serif", "instrument-serif-latin-400-italic.woff2", "400", "italic", ""),
    ("Instrument Serif", "instrument-serif-latin-400-normal.woff2", "400", "normal", ""),
    ("Bodoni Moda", "bodoni-moda-latin-400-italic.woff2", "400", "italic", ""),
    ("Fraunces", "fraunces-latin-300-500-italic.woff2", "300 500", "italic", ""),
    ("Jost", "jost-latin-300-normal.woff2", "300", "normal", ""),
    ("Jost", "jost-latin-400-normal.woff2", "400", "normal", ""),
    ("Playfair Display", "playfair-display-latin-400-italic.woff2", "400", "italic", ""),
]

# (nº, nombre, nota, sans, serif, peso titular, ancho titular, ajuste de tamaño)
OPTIONS = [
    ("A", "Bricolage Grotesque + Instrument Serif",
     "condensada y con carácter, la más cercana a tu referencia",
     "Bricolage Grotesque", "Instrument Serif", 500, "76%", 1.05),
    ("B", "Familjen Grotesk + Bodoni Moda",
     "grotesca con personalidad, algo más ancha",
     "Familjen Grotesk", "Bodoni Moda", 500, "100%", 0.95),
    ("C", "Archivo + Fraunces",
     "robusta y editorial, se puede estrechar a voluntad",
     "Archivo", "Fraunces", 500, "70%", 1.05),
    ("D", "Darker Grotesque + Instrument Serif",
     "la más extrema: muy estrecha y muy alta",
     "Darker Grotesque", "Instrument Serif", 500, "100%", 1.3),
]


def data_uri(path, mime):
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())


faces = []
for family, name, weight, style, stretch in FONTS:
    faces.append(
        '@font-face{font-family:"%s";font-weight:%s;font-style:%s;%sfont-display:swap;'
        'src:url(%s) format("woff2")}'
        % (family, weight, style,
           ('font-stretch:%s;' % stretch) if stretch else "",
           data_uri(os.path.join(ROOT, "assets/fonts", name), "font/woff2")))

img_hero = data_uri(os.path.join(PREV, "hero-left.jpg"), "image/jpeg")
logo = data_uri(os.path.join(ROOT, "assets/brand/logo-burgundy.png"), "image/png")

blocks = []
for num, title, note, sans, serif, weight, stretch, scale in OPTIONS:
    blocks.append(f'''
<section class="opt" style="--sans:'{sans}';--serif:'{serif}';--hw:{weight};--hs:{stretch};--k:{scale}">
  <header class="opt__head">
    <span class="num">Opción {num}</span>
    <h2>{title}</h2>
    <span class="note">{note}</span>
  </header>

  <div class="welcome">
    <p class="eyebrow">bienvenida a bela</p>
    <p class="big">Más que un estudio de micropigmentación, Bela es un espacio donde
       cuidar tu mirada con calma. Trabajamos con una clienta cada vez para ofrecer
       una atención personalizada y un resultado <em>natural</em>.</p>
  </div>

  <div class="hero">
    <img src="{img_hero}" alt="">
    <div class="hero__over">
      <h3 class="display">belleza<br><em>natural</em>,<br>cuidada.</h3>
      <p>Micropigmentación de cejas con técnica Hair Stroke.</p>
      <span class="btn">ver tratamientos</span>
    </div>
  </div>

  <div class="strip">
    <span class="ttl">Cejas realistas · Hair Stroke</span>
    <span class="menu">tratamientos · el método · sobre bela · contacto</span>
  </div>
</section>''')

html = f'''<meta charset="utf-8">
<title>Tipografías — Bela</title>
<style>
{''.join(faces)}
:root {{
  --burgundy:#741c2d; --deep:#4e0f1e; --cream:#f6f1ec; --blush:#f7dfe1;
  --ink:#1c1210; --muted:#8a7a72; --line:rgba(28,18,16,.14);
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--cream);color:var(--ink);
  font-family:"Jost",system-ui,sans-serif;font-weight:300;line-height:1.6}}

.intro{{max-width:720px;margin:0 auto;padding:clamp(2rem,6vw,4rem) 1.5rem 0;text-align:center}}
.intro img{{height:48px;margin:0 auto 1.5rem}}
.intro h1{{font-family:"Playfair Display",serif;font-weight:400;font-size:clamp(1.5rem,3.6vw,2.2rem);
  margin:0 0 .6rem;line-height:1.2}}
.intro p{{margin:0;color:#4a3934;font-size:.95rem}}

.opt{{max-width:1080px;margin:0 auto clamp(2.5rem,6vw,5rem);padding:0 1.5rem}}
.opt__head{{display:flex;align-items:baseline;gap:.9rem;flex-wrap:wrap;
  padding:clamp(1.5rem,4vw,2.5rem) 0 .9rem;border-bottom:1px solid var(--line);margin-bottom:1.25rem}}
.num{{background:var(--burgundy);color:var(--cream);font-size:.64rem;letter-spacing:.16em;
  text-transform:uppercase;padding:.35em .9em;border-radius:100px}}
.opt__head h2{{font-family:"Jost",sans-serif;font-weight:400;font-size:1.1rem;margin:0}}
.note{{color:var(--muted);font-size:.82rem;margin-left:auto}}

/* bloque de bienvenida, al estilo de la referencia */
.welcome{{background:var(--blush);padding:clamp(2rem,5vw,3.5rem) clamp(1.5rem,4vw,3rem);text-align:center}}
.welcome .eyebrow{{font-family:var(--sans),sans-serif;font-size:.72rem;letter-spacing:.42em;
  text-transform:uppercase;color:var(--burgundy);margin:0 0 1.25rem}}
.welcome .big{{font-family:var(--sans),sans-serif;font-weight:var(--hw);font-stretch:var(--hs);
  font-size:calc(clamp(1.7rem,4.2vw,3rem) * var(--k));line-height:1.06;letter-spacing:-.02em;
  color:var(--burgundy);margin:0 auto;max-width:24ch}}
.welcome .big em{{font-family:var(--serif),serif;font-style:italic;font-weight:400;font-stretch:normal}}

.hero{{position:relative;min-height:420px;overflow:hidden;margin-top:1px}}
.hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.hero::after{{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(46,15,19,.3),rgba(46,15,19,.05) 35%,rgba(46,15,19,.62))}}
.hero__over{{position:absolute;left:clamp(1.25rem,3vw,2.5rem);bottom:clamp(1.25rem,3vw,2.5rem);z-index:2;color:#fff}}
.hero__over p{{font-family:var(--sans),sans-serif;font-stretch:normal;font-size:.86rem;margin:.7rem 0 1.1rem;opacity:.94}}
.display{{font-family:var(--sans),sans-serif;font-weight:var(--hw);font-stretch:var(--hs);
  font-size:calc(clamp(2.1rem,5vw,3.6rem) * var(--k));line-height:.98;letter-spacing:-.02em;
  text-transform:lowercase;margin:0}}
.display em{{font-family:var(--serif),serif;font-style:italic;font-weight:400;font-stretch:normal}}
.btn{{display:inline-block;background:#fff;color:var(--ink);border-radius:100px;padding:.75em 1.7em;
  font-family:var(--sans),sans-serif;font-stretch:normal;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase}}

.strip{{display:flex;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;
  background:var(--burgundy);color:var(--cream);padding:1rem clamp(1.25rem,3vw,2.5rem);
  font-family:var(--sans),sans-serif;font-stretch:normal}}
.strip .ttl{{font-size:1rem}}
.strip .menu{{font-size:.85rem;opacity:.75;text-transform:lowercase}}

@media (max-width:700px){{ .note{{margin-left:0;width:100%}} .hero{{min-height:320px}} }}
</style>

<div class="intro">
  <img src="{logo}" alt="Bela Brow Studio and Beauty">
  <h1>Segunda ronda: grotescas de display</h1>
  <p>Cuatro tipografías con más carácter, en la línea de la referencia que enviaste.
     Cada una se ve en el bloque de bienvenida (fondo rosa, texto grande centrado) y
     en el hero de la web. Dime la letra que prefieres.</p>
</div>

{''.join(blocks)}

<div class="intro" style="padding:0 1.5rem 4rem">
  <p style="color:var(--muted);font-size:.83rem">El rosa palo del bloque de bienvenida
     también es nuevo: sale del propio granate del logotipo y da aire a la web sin
     salirse de la marca. Si no encaja, se quita.</p>
</div>
'''

open(OUT, "w", encoding="utf-8").write(html)
print(OUT, "·", round(len(html.encode()) / 1e6, 1), "MB")
