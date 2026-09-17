#!/usr/bin/env python3
"""
Prepara las fotos originales para la web.

Uso:
    pip install pillow
    python3 tools/optimizar-fotos.py

Lee los originales de assets/img/ (los que suben desde GitHub con nombre
imageNNNNN.jpeg) y escribe las versiones recortadas, reescaladas y
comprimidas con el nombre que espera la web.

Para reasignar una foto a otro hueco, edita la lista PLAN de abajo:
    (numero_de_original, nombre_final, proporcion, foco_vertical)

  proporcion    3/4 vertical · 3/2 apaisada · 16/9 panorámica
  foco_vertical 0 = recorta pegado arriba · 0.5 = centrado · 1 = abajo
                (bájalo cuando la cara quede en la parte alta de la foto)
"""

import os
from PIL import Image, ImageOps

IMG = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')

PRINCIPALES = [
    # (original, nombre,             proporción,  foco, calidad, lado máx)
    (7,  'hero.jpg',          16 / 9,     0.50, 82, 2400),
    (9,  'chio-retrato.jpg',   3 / 4,     0.35, 86, 1400),
    (7,  'og.jpg',          1200 / 630,   0.50, 85, 1200),
]

PLAN = [
    (8,  'novia-01.jpg',     3 / 4, 0.30),   # recogido de novia
    (7,  'novia-02.jpg',     3 / 2, 0.50),   # preparativos en el hotel
    (10, 'novia-03.jpg',     3 / 4, 0.30),   # el abrazo
    (6,  'evento-01.jpg',    3 / 2, 0.50),   # prueba junto a la ventana
    (3,  'av-01.jpg',        3 / 4, 0.40),   # rodaje a contraluz
    (4,  'av-02.jpg',        3 / 4, 0.35),   # maquillaje en set
    (2,  'av-03.jpg',        3 / 4, 0.30),   # peinado a contraluz
    (11, 'formacion-01.jpg', 3 / 2, 0.45),   # Escuma Granada
    (1,  'retrato-01.jpg',   3 / 4, 0.30),
    (5,  'retrato-02.jpg',   3 / 4, 0.30),
]

MAX_PORTFOLIO = 1600
CALIDAD = 82


def load(n):
    im = Image.open(os.path.join(IMG, 'image%05d.jpeg' % n))
    return ImageOps.exif_transpose(im).convert('RGB')   # respeta la orientación de la cámara


def crop_to(im, ratio, focal=0.5):
    w, h = im.size
    if w / h > ratio:
        nw = int(h * ratio)
        return im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    nh = int(w / ratio)
    y = int((h - nh) * focal)
    return im.crop((0, y, w, y + nh))


def fit(im, maxside):
    im = im.copy()
    im.thumbnail((maxside, maxside), Image.LANCZOS)
    return im


def save(im, name, q):
    path = os.path.join(IMG, name)
    im.save(path, 'JPEG', quality=q, optimize=True, progressive=True)
    print('  %-22s %-11s %6.0f KB' % (name, '%dx%d' % im.size, os.path.getsize(path) / 1024))


def main():
    print('Principales')
    for n, name, ratio, focal, q, side in PRINCIPALES:
        save(fit(crop_to(load(n), ratio, focal), side), name, q)

    print('Portfolio')
    for n, name, ratio, focal in PLAN:
        save(fit(crop_to(load(n), ratio, focal), MAX_PORTFOLIO), name, CALIDAD)


if __name__ == '__main__':
    main()
