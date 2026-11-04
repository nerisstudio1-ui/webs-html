"""Mejora las fotos para la web de MOA con un mismo tratamiento para todas.

    python3 tools/mejorar_fotos.py ORIGINAL.jpg [ORIGINAL2.jpg ...] --out fotos/

Las fotos de la sala salen con una dominante rosa (paredes lila y tatami rojo),
algo oscuras y planas. Para cada una:

1. Balance de blancos tomando como referencia las zonas claras y poco saturadas
   (las paredes), que deberían ser blancas.
2. Niveles automáticos: estira el rango sin quemar las luces.
3. Levanta un poco las sombras y añade contraste suave en curva S.
4. Baja la saturación de los rojos y magentas (el tatami) para que no se coma
   la paleta violeta y verde de MOA, sin tocar pieles ni el resto de colores.
5. Un toque cálido hacia el crema de la marca.
6. Reducción de ruido ligera y enfoque.

Se guarda a 1600 px de ancho como máximo, sin metadatos (ni GPS).
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageOps


def white_balance(a):
    # Las paredes son lo más claro de la sala y deberían ser blancas
    lum = a.mean(axis=2)
    mask = lum > np.percentile(lum, 80)
    ref = np.median(a[mask], axis=0)
    gain = ref.mean() / np.maximum(ref, 1)
    gain = np.clip(gain, 0.82, 1.22)
    return a * gain


def levels(a):
    lum = a.mean(axis=2)
    lo, hi = np.percentile(lum, 0.6), np.percentile(lum, 99.6)
    return (a - lo) * (255.0 / max(hi - lo, 1))


def tone(a):
    x = np.clip(a / 255.0, 0, 1)
    x = x ** 0.9                                           # sombras arriba
    x = x + 0.12 * np.sin(np.pi * x) * (x - 0.5) * 2        # curva S suave
    return np.clip(x, 0, 1) * 255.0


def tame_reds(a):
    # Tatami rojo-magenta: se baja su saturación por tono, sin tocar pieles
    # (las pieles están en tonos anaranjados, entre 12 y 40 grados)
    hsv = np.asarray(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("HSV")).astype(np.float32)
    h = hsv[..., 0] * 360 / 255
    s = hsv[..., 1] / 255
    in_red = (h >= 300) | (h <= 10)
    edge = np.clip((h - 285) / 15, 0, 1) * (h >= 285) + np.clip((14 - h) / 4, 0, 1) * (h < 14)
    w = np.where(in_red, 1.0, edge) * np.clip((s - 0.25) / 0.3, 0, 1) * 0.6
    gray = a.mean(axis=2, keepdims=True)
    out = a * (1 - w[..., None]) + gray * w[..., None]
    return out * (1 - 0.08 * w[..., None])


def warm(a):
    return a * np.array([1.02, 1.005, 0.975])


def process(src, dst, max_w=1600):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    im = im.filter(ImageFilter.SMOOTH_MORE) if im.width < 1200 else im
    a = np.asarray(im).astype(np.float32)
    a = warm(tone(tame_reds(levels(white_balance(a)))))
    out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    out = out.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=3))
    out.save(dst, "JPEG", quality=84, optimize=True, progressive=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="origen:destino.jpg")
    args = ap.parse_args()
    for p in args.pairs:
        src, dst = p.split(":")
        process(src, dst)
        print(dst)
