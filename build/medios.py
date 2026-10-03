#!/usr/bin/env python3
"""Arma dist/medios-wordpress.zip: todo lo que el widget pide a la biblioteca
de medios de WordPress, plano y con el nombre exacto que espera.

    python3 build/medios.py

Hay que haber corrido antes build/empaquetar.py, porque la lista sale de leer
el widget ya generado: así el zip nunca se desalinea del HTML.
"""
import collections
import io
import os
import re
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIDGET = os.path.join(RAIZ, 'dist', 'cristina-falcon-widget.html')
DESTINO = os.path.join(RAIZ, 'dist', 'medios-wordpress.zip')


def main():
    if not os.path.exists(WIDGET):
        sys.exit('Falta %s. Corre antes build/empaquetar.py.' % WIDGET)

    html = io.open(WIDGET, encoding='utf-8').read()
    # La BASE es el prefijo común de los medios enlazados: .../uploads/AAAA/MM/
    # Puede haber más de una carpeta: WordPress reparte las subidas por año
    # y mes, así que lo de septiembre y lo de octubre viven en sitios
    # distintos. Los nombres se recogen de todas.
    bases = sorted(set(re.findall(r'https?://[^"\']+?/wp-content/uploads/\d{4}/\d{2}/', html)))
    if not bases:
        sys.exit('No encuentro ninguna carpeta de medios en el widget.')
    nombres = sorted(set(
        n for b in bases for n in re.findall(re.escape(b) + r'([A-Za-z0-9._-]+)', html)))

    indice = collections.defaultdict(list)
    for carpeta, _, ficheros in os.walk(os.path.join(RAIZ, 'assets')):
        for f in ficheros:
            indice[f].append(os.path.join(carpeta, f))

    faltan = [n for n in nombres if not indice.get(n)]
    dobles = [n for n in nombres if len(indice.get(n, [])) > 1]
    if faltan or dobles:
        for n in faltan:
            print('  no está en assets/:', n)
        for n in dobles:
            print('  nombre repetido:', n, indice[n])
        sys.exit('El zip no se ha tocado.')

    with zipfile.ZipFile(DESTINO, 'w', zipfile.ZIP_DEFLATED) as z:
        for n in nombres:
            z.write(indice[n][0], n)

    print('  %s   %d archivos   %d KB' % (
        os.path.relpath(DESTINO, RAIZ), len(nombres), os.path.getsize(DESTINO) // 1024))
    print('  Carpetas: %s' % ', '.join(b.split('/uploads/')[1] for b in bases))


if __name__ == '__main__':
    main()
