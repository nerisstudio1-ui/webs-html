#!/usr/bin/env python3
"""
Apunta todos los botones de reserva de la web a la plataforma de reservas
(Momoyoga) y vuelve a generar los archivos.

    python3 configurar-reservas.py https://www.momoyoga.com/calmabarrestudio
    python3 configurar-reservas.py --whatsapp      (volver a WhatsApp)

La dirección se escribe DENTRO del HTML, no la pone el guion: así los
botones funcionan aunque WordPress se coma el JavaScript.

El botón flotante de abajo sigue siendo de WhatsApp a propósito: una cosa
es reservar y otra preguntar.
"""
import pathlib, re, subprocess, sys

RAIZ = pathlib.Path(__file__).parent
# Reservar es cosa de Momoyoga; el botón flotante es para preguntar
WA = 'https://wa.me/34646206292?text=%C2%A1Hola%2C%20Roc%C3%ADo!%20Tengo%20una%20duda%20sobre%20CALMA'

def aplicar(destino: str, es_whatsapp: bool):
    p = RAIZ / 'index.html'
    html = p.read_text()

    # Todos los enlaces con data-book menos el botón flotante
    def cambia(m):
        etiqueta = m.group(0)
        if 'sticky-book' in etiqueta:
            return etiqueta
        etiqueta = re.sub(r'href="[^"]*"', f'href="{destino}"', etiqueta)
        if not es_whatsapp and 'target=' not in etiqueta:
            etiqueta = etiqueta.replace('data-book', 'data-book target="_blank" rel="noopener"')
        return etiqueta
    html, n = re.subn(r'<a [^>]*\bdata-book\b[^>]*>', cambia, html)

    # El botón flotante, siempre a WhatsApp
    html = re.sub(r'(<a class="sticky-book"[^>]*?href=")[^"]*(")', r'\1' + WA + r'\2', html)

    # La fila de Reservas en Contacto
    texto = 'WhatsApp' if es_whatsapp else 'Reserva online'
    html = re.sub(r'(<li><span>Reservas</span><a[^>]*>)[^<]*(</a>)',
                  r'\g<1>' + texto + r'\g<2>', html)

    # La respuesta de "¿Cómo reservo?" en las preguntas frecuentes
    respuesta = ('Por WhatsApp, con el botón de <strong>"Primera clase gratis"</strong>.'
                 if es_whatsapp else
                 'Desde la <strong>plataforma de reservas</strong>, con cualquier botón de '
                 'reserva de la web. Si prefieres preguntar antes, escríbenos por WhatsApp.')
    html = re.sub(r'(<summary>¿Cómo reservo\?</summary>\s*<div class="acc__body"><p>).*?(</p>)',
                  r'\g<1>' + respuesta + r'\g<2>', html, flags=re.S)
    p.write_text(html)
    print(f'· {n} enlaces de reserva apuntando a {destino[:60]}')

    for guion in ('build-elementor.py', 'build-single-file.py'):
        subprocess.run([sys.executable, str(RAIZ / guion)], check=True,
                       stdout=subprocess.DEVNULL)
    print('· archivos regenerados')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(1)
    if sys.argv[1] == '--whatsapp':
        aplicar(WA, True)
    else:
        url = sys.argv[1]
        if not url.startswith('https://'):
            print('La dirección tiene que empezar por https://'); sys.exit(1)
        aplicar(url, False)
