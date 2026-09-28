#!/usr/bin/env python3
"""Vuelve a escribir la galería de index.html a partir de la tabla de abajo.

    python3 build/galeria.py

La galería era una cascada de columnas con las fotos en el orden en que
fueron llegando. Con alturas dispares y sin criterio, Cristina lo describió
como «un pot-pourri». Ahora va en bloques con título, y dentro de cada bloque
una retícula de celdas iguales: el ojo descansa y se entiende qué está
mirando.

La tabla manda. Para mover una foto de bloque, cambiarla de sitio aquí y
volver a ejecutar.
"""
import io
import os
import re
import struct

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GALERIA = os.path.join(RAIZ, 'assets', 'img', 'galeria')

# (clave, archivo) por bloque. El orden es el que se ve.
BLOQUES = [
    ('raices', [
        ('11', '11-infancia-sola.jpg'),
        ('12', '12-con-su-hermano.jpg'),
        ('07', '07-paramo.jpg'),
        ('05', '05-festival-trujillo.jpg'),
        ('20', '20-con-ramon-palomares.jpg'),
    ]),
    ('poesia', [
        ('08', '08-itaca-libreria.jpg'),
        ('14', '14-editora-cuadro.jpg'),
        ('01', '01-firmando.jpg'),
        ('02', '02-casa-america.jpg'),
        ('03', '03-recital.jpg'),
        ('23', '23-aires-poetics.jpg'),
        ('24', '24-lectura-barcelona.jpg'),
        ('21', '21-libreria-amigos.jpg'),
    ]),
    ('escena', [
        ('25', '25-auditori-montcada.jpg'),
        ('26', '26-programa-deria.jpg'),
    ]),
    ('infantil', [
        # La presentación de «De aventuras por Cuenca» con los niños estaba
        # en poesía, y es un libro infantil.
        ('22', '22-presentacion-cuenca.jpg'),
        ('15', '15-con-siwar.jpg'),
        ('19', '19-firma-akiara.jpg'),
        ('17', '17-firma-letras.jpg'),
        ('18', '18-bolonia-kalandraka.jpg'),
        ('04', '04-bolonia.jpg'),
        ('16', '16-feria-bolonia.jpg'),
    ]),
    ('cuenca', [
        ('10', '10-cuenca.jpg'),
        ('06', '06-haciendo-papel.jpg'),
        ('09', '09-luna.jpg'),
    ]),
]


def dimensiones(ruta):
    d = open(ruta, 'rb').read()
    i = 2
    while i < len(d):
        if d[i] != 0xFF:
            i += 1
            continue
        m = d[i + 1]
        if m in (0xC0, 0xC1, 0xC2):
            al, an = struct.unpack('>HH', d[i + 5:i + 9])
            return an, al
        if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
            i += 2
            continue
        i += 2 + struct.unpack('>H', d[i + 2:i + 4])[0]
    raise ValueError(ruta)


def html():
    partes = []
    for bloque, fotos in BLOQUES:
        partes.append(
            '      <section class="galeria__bloque reveal">\n'
            '        <h3 class="galeria__bloque-titulo" data-i18n="galeria.%s">—</h3>\n'
            '        <div class="galeria__grid">' % bloque)
        for clave, archivo in fotos:
            an, al = dimensiones(os.path.join(GALERIA, archivo))
            partes.append(
                '          <button class="galeria__item" data-i18n-attr="aria-label:galeria.ampliar"\n'
                '                  aria-label="Ampliar imagen">\n'
                '            <img width="%d" height="%d" loading="lazy" alt=""\n'
                '                 src="assets/img/galeria/%s" data-i18n-attr="alt:galeria.%s">\n'
                '          </button>' % (an, al, archivo, clave))
        partes.append('        </div>\n      </section>')
    return '\n'.join(partes)


def main():
    p = os.path.join(RAIZ, 'index.html')
    s = io.open(p, encoding='utf-8').read()
    nuevo = ('<!-- galeria:inicio -->\n' + html() + '\n      <!-- galeria:fin -->')
    marcado = re.compile(r'<!-- galeria:inicio -->.*?<!-- galeria:fin -->', re.S)
    if marcado.search(s):
        s = marcado.sub(nuevo, s)
    else:
        viejo = re.compile(r'<div class="galeria__grid reveal" id="galeria-grid">.*?</div>\n\n', re.S)
        if not viejo.search(s):
            raise SystemExit('No encuentro la galería en index.html.')
        s = viejo.sub(nuevo + '\n\n', s)
        s = s.replace('    <!-- TODO: sustituir por las fotos reales. '
                      'Clases --tall / --wide para variar el ritmo. -->\n', '')
    io.open(p, 'w', encoding='utf-8').write(s)
    print('  %d fotos en %d bloques' % (sum(len(f) for _, f in BLOQUES), len(BLOQUES)))


if __name__ == '__main__':
    main()
