# -*- coding: utf-8 -*-
"""Vectorización del logo ANAHATA (símbolo + lockup + favicon)."""
import os, math, random
from _texto_a_trazo import trazar

SERIF = 'assets/fonts/marcellus-400-normal-latin.woff2'
SANS  = 'assets/fonts/inter-400-normal-latin.woff2'

OUT = "assets/img"
os.makedirs(OUT, exist_ok=True)

GREEN = "#3C4A31"
GOLD  = "#AE8229"

# --- Lotus ------------------------------------------------------------------
def lotus(cx, cy, w, stroke, sw):
    """Flor de loto de línea: 3 capas de pétalos + base."""
    p = []
    h = w * 0.62
    # pétalo central
    p.append(f'<path d="M {cx} {cy-h} C {cx+w*0.17} {cy-h*0.45} {cx+w*0.13} {cy-h*0.08} {cx} {cy} '
             f'C {cx-w*0.13} {cy-h*0.08} {cx-w*0.17} {cy-h*0.45} {cx} {cy-h} Z"/>')
    # pétalos intermedios y exteriores
    for side in (-1, 1):
        for k, (dx, dy, sx, sy, rot) in enumerate((
            (0.20, 0.06, 0.78, 0.80, 26),
            (0.37, 0.14, 0.62, 0.58, 50),
        )):
            px, py = cx + side * w * dx, cy - h * dy
            ph = h * sy
            pw = w * sx
            p.append(
                f'<path d="M {px} {py-ph} C {px+pw*0.17} {py-ph*0.45} {px+pw*0.13} {py-ph*0.08} {px} {py} '
                f'C {px-pw*0.13} {py-ph*0.08} {px-pw*0.17} {py-ph*0.45} {px} {py-ph} Z" '
                f'transform="rotate({side*rot} {px} {py})"/>')
    # capa exterior abierta (abanico)
    for side in (-1, 1):
        px = cx + side * w * 0.50
        p.append(f'<path d="M {cx} {cy} Q {cx+side*w*0.42} {cy-h*0.52} {px} {cy-h*0.16}" fill="none"/>')
    # base
    p.append(f'<path d="M {cx-w*0.54} {cy} Q {cx} {cy+h*0.20} {cx+w*0.54} {cy}" fill="none"/>')
    return (f'<g fill="none" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{"".join(p)}</g>')

# --- Heart ------------------------------------------------------------------
def heart(cx, cy, w, stroke, sw):
    s = w / 100.0
    d = ("M50,90 C20,67 3,48 3,31 C3,14 16,4 29,4 C38,4 46,9 50,17 "
         "C54,9 62,4 71,4 C84,4 97,14 97,31 C97,48 80,67 50,90 Z")
    tx, ty = cx - 50 * s, cy - 47 * s
    return (f'<path d="{d}" transform="translate({tx:.2f} {ty:.2f}) scale({s:.4f})" '
            f'fill="none" stroke="{stroke}" stroke-width="{sw/s:.2f}" stroke-linejoin="round"/>')

# --- Roots ------------------------------------------------------------------
def roots(x, y, length, stroke, sw):
    rnd = random.Random(7)
    seg = [f'<path d="M {x} {y} C {x-2} {y+length*0.35} {x+2} {y+length*0.65} {x} {y+length}"/>']
    for i in range(7):
        t = 0.10 + i * 0.115
        sy = y + length * t
        side = -1 if i % 2 == 0 else 1
        spread = (1 - t) * length * rnd.uniform(0.85, 1.20)
        ex = x + side * spread
        ey = sy + length * rnd.uniform(0.22, 0.40)
        seg.append(f'<path d="M {x} {sy:.1f} Q {x+side*spread*0.45:.1f} {sy+2:.1f} {ex:.1f} {ey:.1f}"/>')
        # sub-raicillas
        for j in range(2):
            u = 0.45 + j * 0.35
            mx = x + (ex - x) * u
            my = sy + (ey - sy) * u
            seg.append(f'<path d="M {mx:.1f} {my:.1f} Q {mx+side*spread*0.14:.1f} {my+length*0.06:.1f} '
                       f'{mx+side*spread*0.20:.1f} {my+length*0.16:.1f}"/>')
    return (f'<g fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round">'
            f'{"".join(seg)}</g>')

def dots(x, ys, r, fill):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>' for y in ys)

def leaf(cx, cy, w, h, fill):
    return (f'<path d="M {cx} {cy-h/2} C {cx+w/2} {cy-h*0.12} {cx+w*0.30} {cy+h*0.38} {cx} {cy+h/2} '
            f'C {cx-w*0.30} {cy+h*0.38} {cx-w/2} {cy-h*0.12} {cx} {cy-h/2} Z" fill="{fill}"/>')

def laurel(cx, cy, w, side, stroke, sw):
    """Ramita de laurel: tallo curvo con hojas ovaladas alternas."""
    x2 = cx + side * w
    stem = f'<path d="M {cx} {cy} Q {cx+side*w*0.55:.1f} {cy-w*0.13:.1f} {x2} {cy-w*0.02:.1f}" fill="none"/>'
    leaves = []
    for i in range(7):
        t = 0.10 + i * 0.132
        bx = cx + side * w * t
        by = cy - w * 0.13 * 2 * t * (1 - t) * 2 - w * 0.01
        ln = w * (0.20 - 0.012 * i)
        for up in (-1, 1):
            ang = side * (52 + i * 2) * (1 if up < 0 else -1)
            leaves.append(
                f'<ellipse cx="{bx + side*ln*0.42:.1f}" cy="{by + up*ln*0.34:.1f}" '
                f'rx="{ln*0.46:.1f}" ry="{ln*0.20:.1f}" fill="{stroke}" fill-opacity="0.9" '
                f'transform="rotate({ang:.0f} {bx + side*ln*0.42:.1f} {by + up*ln*0.34:.1f})"/>')
    return (f'<g stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round">{stem}</g>'
            f'<g>{"".join(leaves)}</g>')

# --- Símbolo (mandala + corazón + loto + raíces) -----------------------------
def symbol(green=GREEN, gold=GOLD):
    CX, SW = 300, 2.0
    geo = (f'<circle cx="{CX}" cy="300" r="178"/>'
           f'<circle cx="{CX}" cy="322" r="112"/>'
           f'<path d="M {CX} 132 L 470 420 L 130 420 Z" stroke-linejoin="round"/>')
    return (
        dots(CX, (60, 78, 96), 4.2, gold)
        + f'<g fill="none" stroke="{gold}" stroke-width="{SW}">{geo}</g>'
        + leaf(CX, 214, 22, 52, gold)
        + dots(CX, (256, 274), 4.2, gold)
        + heart(CX, 352, 210, green, 6.5)
        + lotus(CX, 392, 118, gold, 2.0)
        + roots(CX, 430, 150, gold, 1.9)
        + dots(CX, (606, 626), 4.2, gold)
    )

# --- Ficheros ---------------------------------------------------------------
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" role="img" aria-label="{al}">'

# 1) Símbolo suelto
with open(f"{OUT}/logo-simbolo.svg", "w", encoding="utf-8") as f:
    f.write(HEAD.format(vb="100 35 400 620", w=400, h=620, al="Símbolo ANAHATA") + symbol() + "</svg>")

# 2) Lockup completo (símbolo + ANAHATA + claim)
word = trazar("ANAHATA", SERIF, 104, 300, 772, ancho=470, color=GREEN)
rule = (f'<g stroke="{GOLD}" stroke-width="1.8"><path d="M 72 806 H 282"/><path d="M 318 806 H 528"/></g>'
        + heart(300, 806, 26, GOLD, 0).replace('fill="none"', f'fill="{GOLD}"'))
claim = trazar("YOGA \u2022 PILATES \u2022 CONEXI\u00d3N \u2022 TRANSFORMACI\u00d3N \u2022 AMOR",
                   SANS, 22, 300, 848, ancho=470, color=GOLD)
lau = laurel(286, 898, 104, -1, GOLD, 1.5) + laurel(314, 898, 104, 1, GOLD, 1.5) + \
      f'<circle cx="300" cy="898" r="4.6" fill="{GOLD}"/>'
with open(f"{OUT}/logo-anahata.svg", "w", encoding="utf-8") as f:
    f.write(HEAD.format(vb="45 35 510 900", w=510, h=900, al="ANAHATA · Yoga, Pilates, Conexión, Transformación, Amor")
            + symbol() + word + rule + claim + lau + "</svg>")

# 3) Favicon (corazón + loto)
fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">'
       f'<rect width="64" height="64" rx="14" fill="#F9F1E7"/>'
       + heart(32, 30, 44, GREEN, 2.6).replace('stroke-width="5.91"', 'stroke-width="6"')
       + lotus(32, 38, 25, GOLD, 1.3) + '</svg>')
with open(f"{OUT}/favicon.svg", "w", encoding="utf-8") as f:
    f.write(fav)


# 4) Símbolo en crema (cabecera sobre imagen)
CREAM = "#F7EFE3"
with open(f"{OUT}/logo-simbolo-crema.svg", "w", encoding="utf-8") as f:
    f.write(HEAD.format(vb="100 35 400 620", w=400, h=620, al="Símbolo ANAHATA")
            + symbol(green=CREAM, gold=CREAM) + "</svg>")

# 5) Marca compacta para la cabecera (corazón + loto en lienzo cuadrado)
def marca(green, gold):
    return (heart(50, 47, 74, green, 3.2) + lotus(50, 60, 40, gold, 1.5)
            + f'<circle cx="50" cy="15" r="2.2" fill="{gold}"/>'
            + f'<circle cx="50" cy="22" r="2.2" fill="{gold}"/>')
for nombre, g, o in (("logo-marca.svg", GREEN, GOLD), ("logo-marca-crema.svg", "#F7EFE3", "#F7EFE3")):
    with open(f"{OUT}/{nombre}", "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" '
                'role="img" aria-label="ANAHATA">' + marca(g, o) + '</svg>')

# 6) Lockup completo en crema (para fondos oscuros: pie, hero de la landing)
def lockup(green, gold):
    w = trazar("ANAHATA", SERIF, 104, 300, 772, ancho=470, color=green)
    r = (f'<g stroke="{gold}" stroke-width="1.8"><path d="M 72 806 H 282"/><path d="M 318 806 H 528"/></g>'
         + heart(300, 806, 26, gold, 0).replace('fill="none"', f'fill="{gold}"'))
    c = trazar("YOGA \u2022 PILATES \u2022 CONEXI\u00d3N \u2022 TRANSFORMACI\u00d3N \u2022 AMOR",
               SANS, 22, 300, 848, ancho=470, color=gold)
    l = (laurel(286, 898, 104, -1, gold, 1.5) + laurel(314, 898, 104, 1, gold, 1.5)
         + f'<circle cx="300" cy="898" r="4.6" fill="{gold}"/>')
    return symbol(green=green, gold=gold) + w + r + c + l

with open(f"{OUT}/logo-anahata-crema.svg", "w", encoding="utf-8") as f:
    f.write(HEAD.format(vb="45 35 510 900", w=510, h=900,
            al="ANAHATA · Yoga, Pilates, Conexi\u00f3n, Transformaci\u00f3n, Amor")
            + lockup("#F7EFE3", "#E0C283") + "</svg>")
print("logo-simbolo.svg / logo-anahata.svg / favicon.svg generados")
