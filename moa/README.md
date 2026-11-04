# MOA · Moviment i Salut

Web de una sola página para MOA, el proyecto de Patricia Dorado Trainer en Martorell, en tres idiomas.

| Archivo | Idioma |
|---|---|
| `index.html` | Català (versión principal, como marca el brandbook) |
| `es.html` | Castellano |
| `en.html` | English |

Cada página enlaza a las otras dos con el selector CA · ES · EN de la cabecera, el menú móvil y el pie.

## WordPress

`moa-3-idiomas.html` (y `wordpress/moa-wordpress-3-idiomas.html`/`.txt`) es una sola página con los tres idiomas y selector instantáneo; la genera `build.py` junto con las otras.

`wordpress/moa-wordpress-ca.html`, `-es.html` y `-en.html` son la misma web lista para pegar en un bloque de **HTML personalizado**, con todo dentro y los estilos encapsulados para que el tema no la descoloque. Instrucciones en `wordpress/INSTALACION.md`. Se regeneran con `python3 build_wordpress.py` (después de `build.py`).

## Cómo editar

Los tres HTML se generan automáticamente; no se editan a mano.

- `src/template.html`: diseño, estilos y animaciones (común a los tres idiomas).
- `src/i18n.py`: todos los textos en catalán, castellano e inglés.
- Después de cualquier cambio: `python3 build.py` (avisa si falta algún texto en algún idioma).

## Recursos

- `assets/logos-moa/`: logos de MOA en SVG (firma catalana, castellana e inglesa, logotipo y símbolo A) en verde, violeta, crema, carbón y blanco.
- `assets/pdt-logo-*.svg`: logotipo de Patricia Dorado Trainer.
- `assets/favicon.svg`: símbolo A crema sobre violeta.

## Identidad (brandbook MOA, edición 04)

- Colores: crema `#FEF7E5`, violeta `#9242F3`, verde `#3BC65F`, carbón `#2B2D2B`, blanco.
- Tipografías: Bricolage Grotesque (títulos) y Montserrat (texto), desde Google Fonts.
- El verde no se usa para texto sobre crema (contraste insuficiente).

## Animaciones

Pantalla de entrada, cintas de texto que reaccionan a la velocidad y dirección del scroll, titulares que aparecen palabra a palabra, fotos que se descubren, parallax, letras M·O·A que entran con el scroll, servicios con scroll horizontal anclado (en móvil se deslizan con el dedo), contadores, opiniones en movimiento continuo y botones magnéticos. Si el dispositivo tiene activado "reducir movimiento", todo se muestra sin animaciones.

## Pendiente

- Fotos: los huecos "Foto: ..." se sustituyen en `src/template.html` por `<img class="ph" src="fotos/..." alt="...">`.
- Vídeo de portada: dejar el archivo en `fotos/portada.mp4` (H.264, sin sonido, idealmente vertical o 4:5, menos de 8 MB). Se reproduce solo en bucle; si no existe, se ve el hueco de foto.
- Horario lunes y miércoles 18:00–19:00: no publicado porque estaba en duda.
- Formulario: abre WhatsApp o el email con el mensaje escrito. Para recibirlo directamente, conectar un servicio como Formspree.
- Textos legales (aviso legal, privacidad, cookies).
- Las reseñas de Google se muestran en castellano (idioma original) en las tres versiones.
