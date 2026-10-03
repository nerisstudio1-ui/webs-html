#!/usr/bin/env python3
"""Escribe los paneles de prólogo y poemas de los tres poemarios.

    python3 build/prologos.py

Se despliegan al pinchar la ilustración o el título, en el apartado
«Migración, memoria y viaje». Van en <details>, que abre y cierra sin
JavaScript: dentro de WordPress cuanto menos dependa de un script, mejor.

Los prólogos son de terceros —Miriam Reyes, Ramón Palomares y Margot
Carrillo Pimentel— y están publicados por Candaya. Van completos: su editora
lo autorizó en octubre de 2026. El texto se lee de build/prologos/*.txt, que
saca build/extraer-prologos.py de los PDF de los libros.

Los poemas y los prólogos no se traducen: se dejan en español también en la
versión inglesa, con el rótulo advirtiéndolo. Traducir a máquina la poesía
de la autora, o el prólogo firmado por otra persona, no es cosa nuestra.
"""
import html
import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIBROS = [
    ('p3', 'memoria-errante'),
    ('p2', 'borrar-el-paisaje'),
    ('p1', 'itaca-es-nunca'),
]

TEXTOS = {
    'p3': {
        'prologo_titulo': 'Palabras iniciales',
        'prologo_autor': 'Ramón Palomares',
        'poemas': [
            ('VII', 'No menciones\nla memoria\nporque en ella pueden encontrar\nese reflejo\n'
                    'al que han decidido tirarle una piedra.'),
            ('XVI', 'Uno aprende a estar solo\ncomo el perro que aprende\na no pasar\n'
                    'a quedarse afuera.\n\nBueno, uno aprende\nporque no le queda remedio.\n\n'
                    'Uno sin embargo\naprende a estar solo\ncomo el perro que mira\n'
                    'desde la intemperie\ny araña la puerta\ny no le abre y no le oyen.\n\n'
                    'Uno aprende\na estar solo\no lo que es peor aún\na creer que ha aprendido.'),
        ],
    },
    'p2': {
        'prologo_titulo': 'Si después la vida',
        'prologo_autor': 'Margot Carrillo Pimentel',
        'poemas': [
            ('I', 'Echabas atrás la cabeza\ncerrando los ojos\n\nlas manos recogían\n'
                  'como si fueran de agua\ntus cabellos.\n\nEse gesto tuyo\n'
                  'de amarrar con una cinta\nlo inasible.'),
            ('LXX', 'Tengo que combatir\nesta tristeza que\nno ayuda a vivir que\n'
                    'no va a hacer que vuelvas.\n\nPero cómo decirle a la memoria\n'
                    'decirle a ese músculo que late\narrítmico\na destiempo.\n\n'
                    'Cómo silenciar la música\nborrar el paisaje\ndesvestirse de abrazos.'),
        ],
    },
    'p1': {
        'prologo_titulo': 'De lo que no se puede escribir ni callar',
        'prologo_autor': 'Miriam Reyes',
        'poemas': [
            ('III', 'País del revés\níngrima dignidad\nresistiendo.\n\nPaís a expensas\n\n'
                    'penúltimo aliento\nque nadie cree\ninvisible\npaís\nfamélico\n'
                    'aguantas de pie\ncon huecos en la faltriquera.'),
            ('LXIV', 'Ella emprende cada día\nsu viaje para siempre.\n\nAbre los ojos\n'
                     'esboza una sonrisa en lo oscuro.\n\nNo conoce obediencia mayor\n'
                     'que su propia desobediencia.'),
        ],
    },
}

ROTULOS = {
    'es': {'abrir': 'Prólogo y poemas', 'prologo': 'Prólogo'},
    'en': {'abrir': 'Preface and poems', 'prologo': 'Preface'},
}



def leer_prologo(clave):
    f = os.path.join(RAIZ, 'build', 'prologos', clave + '.txt')
    with io.open(f, encoding='utf-8') as h:
        return [p.strip() for p in h.read().split('\n\n') if p.strip()]


def html_panel(clave, archivo):
    t = TEXTOS[clave]
    parrafos = '\n'.join(
        '            <p>%s</p>' % html.escape(p) for p in leer_prologo(clave))
    poemas = '\n'.join(
        '            <figure class="poema">\n'
        '              <figcaption>%s</figcaption>\n'
        '              <blockquote>%s</blockquote>\n'
        '            </figure>' % (num, texto.replace('\n', '<br>'))
        for num, texto in t['poemas'])
    return f"""        <details class="lectura" id="lectura-{archivo}">
          <summary>
            <span class="lectura__libro" data-i18n="libro.{clave}.titulo">—</span>
            <span class="lectura__abrir" data-i18n="lectura.abrir">—</span>
          </summary>
          <div class="lectura__cuerpo">
            <h4 class="lectura__rotulo" data-i18n="lectura.prologo">—</h4>
            <p class="lectura__titulo">{t['prologo_titulo']}</p>
            <p class="lectura__autor">{t['prologo_autor']}</p>
{parrafos}
{poemas}
          </div>
        </details>"""


def main():
    p = os.path.join(RAIZ, 'index.html')
    s = io.open(p, encoding='utf-8').read()

    paneles = '\n'.join(html_panel(c, a) for c, a in LIBROS)
    nuevo = ('<!-- lecturas:inicio -->\n'
             '        <div class="lecturas">\n' + paneles + '\n        </div>\n'
             '        <!-- lecturas:fin -->')
    marca = re.compile(r'<!-- lecturas:inicio -->.*?<!-- lecturas:fin -->', re.S)
    if marca.search(s):
        s = marca.sub(nuevo, s)
    else:
        ancla = '        </div>\n      </section>\n\n    </div>'
        if ancla not in s:
            raise SystemExit('No encuentro dónde colgar las lecturas.')
        s = s.replace(ancla, '        </div>\n\n' + nuevo + '\n      </section>\n\n    </div>', 1)

    # Cada ilustración lleva al panel de su libro.
    for clave, archivo in LIBROS:
        viejo = '<figcaption>\n              <strong data-i18n="libro.%s.titulo">—</strong>' % clave
        nuevo_pie = ('<figcaption>\n              <strong><a href="#lectura-%s" '
                     'data-i18n="libro.%s.titulo">—</a></strong>' % (archivo, clave))
        if viejo in s:
            s = s.replace(viejo, nuevo_pie, 1)

    io.open(p, 'w', encoding='utf-8').write(s)
    print('  %d paneles de lectura' % len(LIBROS))


if __name__ == '__main__':
    main()
