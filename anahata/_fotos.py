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
    # ---- práctica ----
    ("pilates-fitball.jpg", "hero-inicio.jpg",       1920, 1280, 0.46, 0.50, 1.00),
    ("pilates-fitball.jpg", "servicio-pilates.jpg",  1000, 1333, 0.50, 0.50, 1.00),
    ("pilates-fitball.jpg", "pilar-yoga.jpg",        1200,  900, 0.45, 0.50, 1.00),
    ("pilates-suelo.jpg",   "programa-sueltas.jpg",  1200,  900, 0.45, 0.50, 1.00),
    ("pilates-suelo.jpg",   "hero-servicios.jpg",    1920,  900, 0.48, 0.50, 1.00),
    ("pilates-suelo.jpg",   "detalle-esterillas.jpg",1200,  900, 0.82, 0.45, 1.25),
    # ---- el espacio ----
    ("pilates-fitball.jpg", "espacio-estudio.jpg",   1200,  900, 0.42, 0.88, 1.70),
    ("pilates-fitball.jpg", "hero-contacto.jpg",     1920,  900, 0.44, 0.75, 1.30),
    # ---- comunidad ----
    ("grupo-pequeno.jpg",   "pilar-programas.jpg",   1200,  900, 0.42, 0.50, 1.00),
    ("grupo-grande.jpg",    "retiro-finde.jpg",      1400, 1050, 0.40, 0.50, 1.00),
    ("grupo-grande.jpg",    "hero-clases.jpg",       1920,  900, 0.42, 0.50, 1.00),
    ("grupo-pequeno.jpg",   "comunidad.jpg",         1200,  900, 0.40, 0.50, 1.25),
    # ---- retiro y alimentación ----
    ("retiro-mesa.jpg",     "alimentacion.jpg",      1000, 1333, 0.62, 0.50, 1.00),
    ("retiro-mesa.jpg",     "retiro-paisaje.jpg",    1400, 1050, 0.16, 0.50, 1.00),
    ("retiro-mesa.jpg",     "hero-retiros.jpg",      1920,  900, 0.18, 0.50, 1.00),
    ("retiro-mesa.jpg",     "evento-brunch.jpg",     1200,  900, 0.58, 0.50, 1.30),
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

total = 0
for origen, destino, w, h, fv, fh, zoom in TRABAJOS:
    ruta = os.path.join(ORIG, origen)
    if not os.path.exists(ruta):
        print(f"  falta {origen}"); continue
    img = ImageOps.exif_transpose(Image.open(ruta)).convert("RGB")
    recortar(img, w, h, fv, fh, zoom).save(os.path.join(OUT, destino), "JPEG",
                                   quality=82, optimize=True, progressive=True)
    kb = os.path.getsize(os.path.join(OUT, destino)) // 1024
    print(f"  {destino:24} {w}x{h}  {kb} KB")
    total += kb
print(f"total: {total} KB")
