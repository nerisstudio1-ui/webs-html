#!/usr/bin/env python3
"""Deja una foto lista para la galería: gira según el EXIF, la reduce y la
guarda en JPEG.

    python3 build/preparar-foto.py entrada.HEIC salida.jpg [lado_mayor]

Acepta HEIC, que es lo que sale de un iPhone sin tocar ajustes, además de los
formatos de siempre. El lado mayor por defecto son 1400 píxeles, que es lo que
usan el resto de fotos de la galería.
"""
import os
import sys

import pillow_heif
from PIL import Image, ImageOps

pillow_heif.register_heif_opener()

LADO = 1400
CALIDAD = 86


def preparar(origen, destino, lado=LADO):
    im = Image.open(origen)
    # El giro va en una etiqueta EXIF, no en los píxeles: sin esto, las fotos
    # verticales de móvil salen tumbadas.
    im = ImageOps.exif_transpose(im)
    if max(im.size) > lado:
        escala = lado / max(im.size)
        im = im.resize((round(im.width * escala), round(im.height * escala)),
                       Image.LANCZOS)
    im.convert('RGB').save(destino, 'JPEG', quality=CALIDAD, optimize=True)
    return im.size


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    lado = int(sys.argv[3]) if len(sys.argv) > 3 else LADO
    an, al = preparar(sys.argv[1], sys.argv[2], lado)
    print('  %-30s %4d x %4d   %4d KB' % (
        os.path.basename(sys.argv[2]), an, al, os.path.getsize(sys.argv[2]) // 1024))
