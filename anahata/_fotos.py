# -*- coding: utf-8 -*-
"""Recorta y optimiza las fotos originales a los huecos de la web.
   Uso: python3 _fotos.py   ·  Los originales viven en assets/img/originales/"""
from PIL import Image, ImageOps
import os

ORIG = "assets/img/originales"
OUT  = "assets/img"

# (origen, destino, ancho, alto, foco vertical 0=arriba 0.5=centro 1=abajo)
TRABAJOS = [
    # práctica
    ("pilates-fitball.jpg", "servicio-pilates.jpg", 1000, 1333, 0.50),
    ("pilates-fitball.jpg", "pilar-yoga.jpg",       1200,  900, 0.45),
    ("pilates-suelo.jpg",   "programa-sueltas.jpg", 1200,  900, 0.45),
    # comunidad
    ("grupo-pequeno.jpg",   "pilar-programas.jpg",  1200,  900, 0.42),
    ("grupo-grande.jpg",    "retiro-finde.jpg",     1400, 1050, 0.40),
    # retiro y alimentación
    ("retiro-mesa.jpg",     "alimentacion.jpg",     1000, 1333, 0.55),
]

def recortar(img, w, h, foco):
    """Recorta al aspecto pedido respetando el foco vertical, y escala."""
    ow, oh = img.size
    objetivo = w / h
    actual = ow / oh
    if actual > objetivo:                      # sobra ancho
        nw = int(oh * objetivo)
        izq = (ow - nw) // 2
        caja = (izq, 0, izq + nw, oh)
    else:                                      # sobra alto
        nh = int(ow / objetivo)
        arriba = int((oh - nh) * foco)
        arriba = max(0, min(arriba, oh - nh))
        caja = (0, arriba, ow, arriba + nh)
    return img.crop(caja).resize((w, h), Image.LANCZOS)

total = 0
for origen, destino, w, h, foco in TRABAJOS:
    ruta = os.path.join(ORIG, origen)
    if not os.path.exists(ruta):
        print(f"  falta {origen}"); continue
    img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
    recortar(img, w, h, foco).save(os.path.join(OUT, destino), "JPEG",
                                   quality=82, optimize=True, progressive=True)
    kb = os.path.getsize(os.path.join(OUT, destino)) // 1024
    print(f"  {destino:24} {w}x{h}  {kb} KB")
    total += kb
print(f"total: {total} KB")
