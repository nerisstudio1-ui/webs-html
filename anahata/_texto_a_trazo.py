# -*- coding: utf-8 -*-
"""Convierte un texto en trazos SVG con una tipografía concreta.
   Lo usa _gen_logo.py para que el logotipo se vea igual en cualquier sitio,
   sin depender de que el navegador cargue la fuente."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

def trazar(texto, fuente, tam, x, y, ancho=None, anclaje="middle", color="#000"):
    """Devuelve un <path> con el texto ya convertido a curvas.
       ancho: si se indica, ajusta el interletraje para ocupar exactamente ese ancho."""
    f = TTFont(fuente)
    upm = f["head"].unitsPerEm
    cmap = f.getBestCmap()
    glifos = f.getGlyphSet()
    escala = tam / upm

    nombres, avances = [], []
    for ch in texto:
        g = cmap.get(ord(ch))
        if g is None:
            g = cmap.get(ord(" "))
        nombres.append(g)
        avances.append(glifos[g].width * escala)

    natural = sum(avances)
    extra = 0.0
    if ancho is not None and len(texto) > 1:
        extra = (ancho - natural) / (len(texto) - 1)
    total = natural + extra * (len(texto) - 1)

    if anclaje == "middle":
        cursor = x - total / 2
    elif anclaje == "end":
        cursor = x - total
    else:
        cursor = x

    partes = []
    for nombre, avance in zip(nombres, avances):
        pen = SVGPathPen(glifos)
        glifos[nombre].draw(pen)
        d = pen.getCommands()
        if d:
            partes.append(f'<g transform="translate({cursor:.2f} {y:.2f}) scale({escala:.5f} {-escala:.5f})">'
                          f'<path d="{d}"/></g>')
        cursor += avance + extra
    return f'<g fill="{color}">{"".join(partes)}</g>'
