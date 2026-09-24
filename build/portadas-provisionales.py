#!/usr/bin/env python3
"""Genera las cubiertas provisionales de los libros cuya portada real todavía
no ha llegado.

    python3 build/portadas-provisionales.py

Se ven como un libro encuadernado en tela, con su título y su editorial. Antes
eran rectángulos con «Poesía 2» y «600 × 900» dentro: andamiaje de taller, que
no debería llegar nunca a un visitante. Cuando llegue la portada de verdad se
sustituye el archivo y ya está.
"""
import html
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, 'assets', 'img', 'obra')

AN, AL = 600, 900

# De la paleta de la web. Se alternan para que dos fichas contiguas no salgan
# del mismo color.
VERDE  = '#255647'
AZUL   = '#1B3448'
TIERRA = '#8A5C3E'
CREMA  = '#F7F3EA'

LIBROS = [
    ('poesia-2',   'Borrar el paisaje',           'Candaya · 2014',                      VERDE),
    ('poesia-3',   'Memoria errante',             'Candaya · 2009',                      AZUL),
    ('infantil-3', 'La palabra encantada',        'CEPLI-UCLM · 2017',                   VERDE),
    ('infantil-4', 'Peperoncino',                 'Giunti Editori · 2014',               TIERRA),
    ('infantil-6', '1, 2, 3, de repente en…',     'Edebé · 2011-2012',                   AZUL),
    ('infantil-7', 'Guías infantiles de España',  'Susaeta · 2012-2018',                 TIERRA),
    ('infantil-8', 'Caja de cuentos y aventuras', 'F. Turismo de Cuenca · 2006',         VERDE),
]


def parte(texto, ancho_max):
    """Reparte el título en renglones que quepan. Mide a ojo de ancho medio de
    letra, que para una serif a este cuerpo se queda en torno a 0,5 em."""
    palabras, lineas, actual = texto.split(), [], ''
    for p in palabras:
        prueba = (actual + ' ' + p).strip()
        if len(prueba) <= ancho_max:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


def cubierta(titulo, editorial, fondo):
    cuerpo = 54 if len(titulo) <= 18 else 44
    lineas = parte(titulo, 16 if cuerpo == 54 else 20)
    alto = cuerpo * 1.25
    y0 = AL / 2 - (len(lineas) - 1) * alto / 2 - 20

    filas = '\n'.join(
        '    <tspan x="50%%" y="%.1f">%s</tspan>' % (y0 + i * alto, html.escape(l))
        for i, l in enumerate(lineas))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {AN} {AL}" width="{AN}" height="{AL}">
  <rect width="{AN}" height="{AL}" fill="{fondo}"/>
  <rect x="26" y="26" width="{AN - 52}" height="{AL - 52}"
        fill="none" stroke="{CREMA}" stroke-width="1" opacity=".35"/>
  <text fill="{CREMA}" font-family="Georgia, 'Times New Roman', serif"
        font-size="{cuerpo}" text-anchor="middle">
{filas}
  </text>
  <text x="50%" y="{AL - 96}" fill="{CREMA}" opacity=".62"
        font-family="Helvetica, Arial, sans-serif" font-size="21"
        letter-spacing="2.4" text-anchor="middle">{html.escape(editorial.upper())}</text>
</svg>
"""


def main():
    for nombre, titulo, editorial, fondo in LIBROS:
        f = os.path.join(DESTINO, nombre + '.svg')
        with open(f, 'w', encoding='utf-8') as h:
            h.write(cubierta(titulo, editorial, fondo))
        print('  %-14s %s' % (nombre + '.svg', titulo))


if __name__ == '__main__':
    main()
