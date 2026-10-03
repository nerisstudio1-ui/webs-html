#!/usr/bin/env python3
"""Saca el texto de los prólogos de los PDF de los poemarios.

    python3 build/extraer-prologos.py <carpeta-con-los-pdf>

Deja un .txt por libro en build/prologos/, con un párrafo por línea en
blanco. De ahí los lee build/prologos.py para montar los desplegables.

Lo delicado es rehacer los párrafos. Un PDF de libro no guarda dónde
empieza y acaba uno: solo renglones. En texto justificado, el renglón que
viene lleno continúa la frase y el que viene corto cierra párrafo. Pero
«lleno» depende de la caja de cada libro, así que el umbral se calcula de
cada PDF: la mediana de sus renglones, menos un margen. Con un número fijo,
Memoria errante se quedaba en dos párrafos de cuarenta líneas e Ítaca se
troceaba en cuarenta y tres.
"""
import os
import re
import statistics
import sys

import pymupdf

DESTINO = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prologos')

# (archivo, salida, primeras palabras, hasta dónde)
LIBROS = [
    ('Páginas desdememoriaerrante7.pdf', 'p3.txt',
     'La angustia, el dolor', 'RAMÓN PALOMARES'),
    ('Borrar el paisaje.pdf', 'p2.txt',
     'La experiencia del dolor', 'Margot Carrillo Pimentel'),
    ('itacaesnunca16-3-12.pdf', 'p1.txt',
     'Volver a un espacio físico', 'Barcelona, 17 de febrero'),
]


def limpiar(bruto):
    t = re.sub(r'^\s*\w+\d*\.qxp.*$', '', bruto, flags=re.M)   # pie de maquetación
    t = re.sub(r'^\s*\d{1,3}\s*$', '', t, flags=re.M)          # números de página
    t = re.sub(r'[­‐-—-]\s*\n\s*', '', t)       # palabra partida
    return re.sub(r'[ \t ]+', ' ', t)


def umbral(lineas):
    largos = [len(l) for l in lineas if len(l) > 20]
    return statistics.median(largos) * 0.86 if largos else 46


def parrafos(bruto):
    lineas = [l.strip() for l in limpiar(bruto).split('\n')]
    lleno = umbral(lineas)
    salida, actual = [], ''
    for l in lineas:
        if not l:
            if actual:
                salida.append(actual)
                actual = ''
        elif actual and len(actual) >= lleno:
            actual += ' ' + l
        elif actual:
            salida.append(actual)
            actual = l
        else:
            actual = l
    if actual:
        salida.append(actual)
    return [p for p in salida if p]


def main(origen):
    os.makedirs(DESTINO, exist_ok=True)
    for archivo, salida, desde, hasta in LIBROS:
        ruta = os.path.join(origen, archivo)
        if not os.path.exists(ruta):
            sys.exit('No encuentro %s' % ruta)
        texto = '\n\n'.join(parrafos(
            '\n'.join(p.get_text() for p in pymupdf.open(ruta))))
        i = texto.index(desde)
        j = texto.index(hasta, i)
        cuerpo = [p.strip() for p in texto[i:j].split('\n\n') if p.strip()]
        with open(os.path.join(DESTINO, salida), 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(cuerpo) + '\n')
        print('  %-8s %4d palabras · %2d párrafos' % (
            salida, sum(len(p.split()) for p in cuerpo), len(cuerpo)))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
