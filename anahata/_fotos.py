# -*- coding: utf-8 -*-
"""Recorta y optimiza las fotos originales a los huecos de la web.
   Uso: python3 _fotos.py   ·  Los originales viven en assets/img/originales/"""
from PIL import Image, ImageOps
import os

ORIG = "assets/img/originales"
OUT  = "assets/img"

# (origen, destino, ancho, alto, foco vertical, [foco horizontal])
# foco 0 = arriba/izquierda · 0.5 = centro · 1 = abajo/derecha
TRABAJOS = [
    # Cinco fotos originales → cinco imágenes. Ni una escena repetida.
    ("pilates-fitball.jpg", "portada.jpg",   1920, 1280, 0.46, 0.50, 1.00),  # portada
    ("sara-desierto.jpg",   "sara.jpg",       900, 1200, 0.42, 0.50, 1.00),  # Sara, en «Sobre mí»
    ("grupo-pequeno.jpg",   "comunidad.jpg", 1400,  800, 0.42, 0.50, 1.00),  # banda de opiniones
    ("pilates-suelo.jpg",   "pilates.jpg",   1200,  900, 0.45, 0.50, 1.00),  # Pilates con implementos
    ("grupo-grande.jpg",    "tribu.jpg",     1400,  800, 0.40, 0.50, 1.00),  # banda de retiros
    ("retiro-mesa.jpg",     "retiro.jpg",    1920,  900, 0.18, 0.50, 1.00),  # banda de llamada a la acción
]

def recortar(img, w, h, foco_v=0.5, foco_h=0.5, zoom=1.0):
    """Recorta al aspecto pedido respetando el foco, con acercamiento opcional."""
    ow, oh = img.size
    objetivo = w / h
    # ventana de recorte del mayor tamaño posible, reducida por el zoom
    if ow / oh > objetivo:
        nh = oh / zoom
        nw = nh * objetivo
    else:
        nw = ow / zoom
        nh = nw / objetivo
    nw, nh = min(int(nw), ow), min(int(nh), oh)
    izq    = int((ow - nw) * foco_h)
    arriba = int((oh - nh) * foco_v)
    caja = (izq, arriba, izq + nw, arriba + nh)
    return img.crop(caja).resize((w, h), Image.LANCZOS)

def generar():
    total = 0
    for origen, destino, w, h, fv, fh, zoom in TRABAJOS:
        ruta = os.path.join(ORIG, origen)
        if not os.path.exists(ruta):
            print(f"  falta {origen}"); continue
        img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
        recortar(img, w, h, fv, fh, zoom).save(os.path.join(OUT, destino), "JPEG",
                                               quality=84, optimize=True, progressive=True)
        kb = os.path.getsize(os.path.join(OUT, destino)) // 1024
        print(f"  {destino:24} {w}x{h}  {kb} KB")
        total += kb
    print(f"total: {total} KB")

if __name__ == "__main__":
    generar()
