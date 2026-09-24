# -*- coding: utf-8 -*-
"""Marcadores de imagen provisionales, en la gama cálida de la web."""
import os, random

OUT = "assets/img"
os.makedirs(OUT, exist_ok=True)

PARES = {
    "topo":   ("#B49B86", "#93795F"),
    "arena":  ("#D8C8B6", "#B49B86"),
    "crema":  ("#EDE5D9", "#CDBCA7"),
    "moka":   ("#A88E76", "#7A6350"),
    "lino":   ("#E5DCCE", "#C6B49E"),
    "canela": ("#C9AE93", "#A08670"),
}

SLOTS = [
    ("hero-inicio",        1920, 1280, "topo",   "Portada · práctica de yoga"),
    ("hero-sobre-mi",      1920,  900, "crema",  "Sara · retrato"),
    ("hero-servicios",     1920,  900, "arena",  "Clase grupal"),
    ("hero-clases",        1920,  900, "lino",   "Sala de práctica"),
    ("hero-retiros",       1920,  900, "canela", "Retiro en la naturaleza"),
    ("hero-contacto",      1920,  900, "moka",   "Detalle · espacio"),
    ("pilar-meditacion",   1200,  900, "crema",  "Meditación"),
    ("sobre-retrato",       900, 1200, "arena",  "Sara Viñas"),
    ("sobre-detalle",      1200,  900, "lino",   "Detalle · práctica"),
    ("servicio-meditacion",1000, 1000, "crema",  "Meditación"),
    ("programa-membresia", 1200,  900, "arena",  "Membresía mensual"),
    ("programa-reto21",    1200,  900, "canela", "Reto 21 días"),
    ("programa-privadas",  1200,  900, "lino",   "Sesiones privadas"),
    ("evento-brunch",      1200,  900, "crema",  "Yoga & brunch"),
    ("evento-aromaterapia",1200,  900, "arena",  "Taller de aromaterapia"),
    ("evento-menopausia",  1200,  900, "lino",   "Yoga y menopausia"),
    ("evento-familia",     1200,  900, "canela", "Yoga en familia"),
    ("cta-banner",         1920,  900, "moka",   "Respira"),
]

def svg(nombre, w, h, tono, etiqueta):
    c1, c2 = PARES[tono]
    rnd = random.Random(nombre)
    cx, cy = w * rnd.uniform(0.44, 0.60), h * rnd.uniform(0.42, 0.56)
    base = min(w, h)
    # Formas muy suaves: sin mandalas, solo luz difusa
    velos = "".join(
        f'<ellipse cx="{cx + base*dx:.0f}" cy="{cy + base*dy:.0f}" rx="{base*rx:.0f}" ry="{base*ry:.0f}" '
        f'fill="#FFFFFF" fill-opacity="{op}"/>'
        for dx, dy, rx, ry, op in (
            (-0.10, -0.12, 0.52, 0.46, 0.10),
            ( 0.18,  0.10, 0.40, 0.34, 0.07),
            (-0.22,  0.20, 0.30, 0.26, 0.05),
        ))
    fs = base * 0.030
    # Las portadas se recortan a pantalla completa: sin etiqueta, que quedaría cortada
    texto = "" if nombre.startswith("hero-") or nombre == "cta-banner" else (
        f'<text x="{w/2:.0f}" y="{h - base*0.052:.0f}" text-anchor="middle" '
        f'font-family="Playfair Display, Georgia, serif" font-size="{fs:.0f}" '
        f'fill="#FFFFFF" fill-opacity="0.60" letter-spacing="{fs*0.16:.1f}">{etiqueta.upper()}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{etiqueta}">
  <defs>
    <linearGradient id="g" x1="0.1" y1="0" x2="0.9" y2="1">
      <stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/>
    </linearGradient>
    <radialGradient id="v" cx="0.5" cy="0.44" r="0.80">
      <stop offset="0.58" stop-color="#000000" stop-opacity="0"/>
      <stop offset="1" stop-color="#4A3A2C" stop-opacity="0.20"/>
    </radialGradient>
    <filter id="b"><feGaussianBlur stdDeviation="{base*0.10:.0f}"/></filter>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <g filter="url(#b)">{velos}</g>
  <rect width="{w}" height="{h}" fill="url(#v)"/>
  {texto}
</svg>'''

for nombre, w, h, tono, etiqueta in SLOTS:
    with open(f"{OUT}/{nombre}.svg", "w", encoding="utf-8") as f:
        f.write(svg(nombre, w, h, tono, etiqueta))
print(f"{len(SLOTS)} marcadores regenerados en tonos cálidos")
