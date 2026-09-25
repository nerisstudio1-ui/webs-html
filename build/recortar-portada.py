#!/usr/bin/env python3
"""Recorta la portada de un libro fotografiado sobre una mesa.

    python3 build/recortar-portada.py entrada.JPG salida.jpg [ancho]

Busca el recuadro de lo que se aparta del color de las esquinas —la mesa o la
pared— y recorta ahí. Respeta la orientación del EXIF: los móviles guardan la
foto en horizontal y anotan aparte el giro, y si se ignora, el recorte sale
calculado sobre una imagen y aplicado sobre otra.
"""
import os
import struct
import sys

import pymupdf

MARGEN_ESQUINA = 14      # píxeles de esquina que se promedian para el fondo
TOLERANCIA = 46          # cuánto hay que apartarse del fondo para contar
PASO = 4                 # se muestrea de cuatro en cuatro: sobra de sobra
AIRE = 0.012             # margen que se deja alrededor del libro


def orientacion(ruta):
    """El campo Orientation del EXIF. 1 = derecha, 6 = 90° horario, 8 = antihorario."""
    d = open(ruta, 'rb').read()
    i = d.find(b'Exif\x00\x00')
    if i < 0:
        return 1
    t = i + 6
    be = d[t:t + 2] == b'MM'
    u16 = lambda p: struct.unpack('>H' if be else '<H', d[p:p + 2])[0]
    u32 = lambda p: struct.unpack('>I' if be else '<I', d[p:p + 4])[0]
    ifd = t + u32(t + 4)
    for k in range(u16(ifd)):
        e = ifd + 2 + k * 12
        if u16(e) == 0x0112:
            return u16(e + 8)
    return 1


def color_de_fondo(pix):
    muestras, n, d, s = [], pix.n, pix.samples, pix.stride
    filas = list(range(MARGEN_ESQUINA)) + list(range(pix.height - MARGEN_ESQUINA, pix.height))
    cols = list(range(MARGEN_ESQUINA)) + list(range(pix.width - MARGEN_ESQUINA, pix.width))
    for y in filas:
        for x in cols:
            i = y * s + x * n
            muestras.append(d[i:i + 3])
    return [sum(c[k] for c in muestras) // len(muestras) for k in range(3)]


def recuadro_del_libro(pix):
    f = color_de_fondo(pix)
    x0, y0, x1, y1 = pix.width, pix.height, 0, 0
    n, d, s = pix.n, pix.samples, pix.stride
    for y in range(0, pix.height, PASO):
        fila = y * s
        for x in range(0, pix.width, PASO):
            i = fila + x * n
            if abs(d[i] - f[0]) + abs(d[i + 1] - f[1]) + abs(d[i + 2] - f[2]) > TOLERANCIA * 3:
                x0, x1 = min(x0, x), max(x1, x)
                y0, y1 = min(y0, y), max(y1, y)
    m = int(max(pix.width, pix.height) * AIRE)
    return (max(0, x0 - m), max(0, y0 - m),
            min(pix.width, x1 + m), min(pix.height, y1 + m))


def _a_pixmap(ancho, alto, pix, rotate=0, rect=None):
    doc = pymupdf.open()
    pag = doc.new_page(width=ancho, height=alto)
    pag.insert_image(rect if rect is not None else pag.rect, pixmap=pix, rotate=rotate)
    return pag.get_pixmap(dpi=72)


def recortar(origen, destino, ancho=1400):
    # Pixmap lee los píxeles en crudo, sin aplicar el EXIF: el recuadro se
    # calcula en ese sistema y el giro se aplica después, a todo junto.
    pix = pymupdf.Pixmap(origen)
    x0, y0, x1, y1 = recuadro_del_libro(pix)
    an, al = x1 - x0, y1 - y0
    corte = _a_pixmap(an, al, pix,
                      rect=pymupdf.Rect(-x0, -y0, pix.width - x0, pix.height - y0))

    giro = {6: 270, 8: 90, 3: 180}.get(orientacion(origen), 0)
    if giro:
        vertical = giro in (90, 270)
        corte = _a_pixmap(al if vertical else an, an if vertical else al, corte, rotate=giro)

    if corte.width > ancho:
        corte = _a_pixmap(ancho, round(corte.height * ancho / corte.width), corte)

    corte.save(destino, jpg_quality=86)
    return pix.width, pix.height, corte.width, corte.height


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    salida = sys.argv[2]
    aw, ah, nw, nh = recortar(sys.argv[1], salida,
                              int(sys.argv[3]) if len(sys.argv) > 3 else 1400)
    print('  %dx%d  →  %dx%d   %d KB' % (aw, ah, nw, nh, os.path.getsize(salida) // 1024))
