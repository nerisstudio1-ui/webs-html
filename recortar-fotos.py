"""Recorta las fotos reales del estudio a las proporciones que usa la web.

Las fotos originales de Rocío están en assets/img/originales (1600x2000 cada una).
Este script las recorta y las guarda en WebP, que es lo que carga la web.

    pip install pillow
    python3 recortar-fotos.py
"""
from pathlib import Path
from PIL import Image

AQUI = Path(__file__).parent
ORIG = AQUI / 'assets/img/originales'
DEST = AQUI / 'assets/img'


def recorta(origen, destino, ratio, ancho, foco=0.5, calidad=72):
    """ratio = ancho/alto del hueco. foco: 0 arriba del todo, 1 abajo, 0.5 centrado."""
    im = Image.open(ORIG / origen)
    W, H = im.size
    if W / H > ratio:                       # sobra ancho
        nh, nw = H, int(H * ratio)
        x, y = int((W - nw) * 0.5), 0
    else:                                   # sobra alto
        nw, nh = W, int(W / ratio)
        x, y = 0, int((H - nh) * foco)
    im = im.crop((x, y, x + nw, y + nh)).resize((ancho, int(ancho / ratio)), Image.LANCZOS)
    im.convert('RGB').save(DEST / destino, 'WEBP', quality=calidad, method=6)
    print(f'  {destino}  {im.size[0]}x{im.size[1]}')


#        origen     destino         ratio   ancho  foco
recorta('5.jpg', 'hero.webp',       1.50,   1600,  0.40)   # la sala entera (cabecera y franja)
recorta('rocio-10.jpg', 'barre.webp',   1.777,  1600,  0.62)   # Rocío con la barra de peso
recorta('rocio-11.jpg', 'clases.webp',  0.833,  1050,  0.35)   # Rocío en la barra
recorta('rocio-7.jpg',  'fitness.webp', 1.777,  1600,  0.76)   # Rocío en plancha
recorta('2.jpg', 'calma.webp',      0.80,   1100,  0.50)   # los espejos dorados
recorta('1.jpg', 'est-1.webp',      0.80,    800,  0.50)   # barra y cortinas, en vertical
recorta('3.jpg', 'est-2.webp',      1.33,    900,  0.45)   # el material, de cerca
recorta('4.jpg', 'est-3.webp',      1.33,    900,  0.88)   # la esterilla con el logo
recorta('5.jpg', 'est-4.webp',      0.80,    800,  0.60)   # la sala, en vertical

# La foto de Rocío para "Hola, soy Rocío". El original ya viene en 4:5, que es
# justo la proporción del hueco, así que no hay que recortar nada.
recorta('rocio.jpg',    'retrato.webp', 0.80,   1100,  0.50)
recorta('rocio-8.jpg',  'faq.webp',     0.80,   1100,  0.50)   # Rocío en plancha lateral
