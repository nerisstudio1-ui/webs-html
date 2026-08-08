# Laconic Studio — web

Web de una sola página para **Laconic Studio**, en **catalán y castellano**.
HTML + CSS + JS, sin dependencias ni frameworks.

- `index.html` — catalán (versión por defecto)
- `es/index.html` — castellano

Las dos se generan desde `build/build.py`, donde vive todo el contenido en los dos
idiomas. Para cambiar un texto se edita ahí y se ejecuta:

```bash
python3 build/build.py
```

Así las dos versiones no se desincronizan. El selector CA/ES está en la cabecera
y en el pie, y las páginas se declaran entre sí con `hreflang`.

Todo el branding sale de la identidad de la marca: terracota, crema y verde
profundo, el símbolo del **0** como marca en la cabecera, el logotipo en el inicio, y
titulares que mezclan la manuscrita y la sans pesada dentro de la misma frase.

## Secciones (todas en `index.html`)

| Ancla (CA / ES) | Contenido |
| --- | --- |
| — | Inicio: fondo beige, el **logotipo en terracota** centrado y las piezas de proyecto subiendo hasta salir por arriba |
| — | Declaración sobre terracota, centrada, con la manuscrita dentro de la frase |
| — | Tira de fotos que pasa en bucle, con **LACONIC STUDIO** grande debajo |
| `#estudio` | Manifiesto, equipo y las siete marcas con las que ha trabajado el estudio |
| `#servicios` | Los cinco servicios con su subtítulo y entregables |
| `#trabajo` | Los siete proyectos, con su vídeo si lo hay y si no la fotografía |
| — | Frase «Haz match con lo que vibre contigo» sobre verde profundo |
| `#proceso` | Los cuatro pasos de trabajo |
| `#faq` | Seis preguntas frecuentes, en acordeón |
| `#resenyes` | Reseñas de clientes (solo aparece si hay citas en `RESENAS`) |
| `#contacto` | Formulario y contacto directo |

## Reseñas: pendientes de las citas

`RESENAS` en `build/build.py` está **vacío a propósito**: una reseña son palabras
de otra persona y no se inventan. En cuanto lleguen tres o cuatro se añaden ahí
—nombre, marca y la cita en los dos idiomas— y la sección aparece sola, sin tocar
nada más. Mientras esté vacía no se dibuja.

Las respuestas del FAQ sí están escritas, pero solo dicen cosas que ya están en
la web (servicios, proceso, equipo, idiomas, Barcelona y remoto). Conviene que
las repase el estudio antes de publicar.

## Material de marca

`assets/img/marca/flyer-cotxe-*.jpg` es la foto del flyer del estudio sobre un
coche. Ya no se usa en el inicio, pero se conserva por si sirve en otra sección.

Los cinco servicios y sus subtítulos son **los del flyer**, con sus cinco iconos
redibujados como SVG en `ICONOS`: el sol, la pausa, el asterisco, la flecha y el
cero. El reclamo del inicio también sale de ahí.

## Vídeos de los proyectos

Cuatro proyectos ya tienen su reel en `assets/video`: **Quality Training**,
**Ratafia Malhivern**, **Jordi Coll** y **Comercial Puig**. El generador los
detecta solos: si un proyecto tiene vídeo, su columna deja de ser una foto y pasa
a ser el reel en marco vertical; si no lo tiene, se queda la foto. El póster es un
fotograma del propio vídeo.

Arrancan sin sonido al entrar en pantalla, se paran al salir, y el botón redondo
activa el audio de uno (solo puede sonar uno a la vez). Con `preload="metadata"`
no se descargan hasta que hacen falta.

Los detalles de formato y nombres están en `assets/video/LEEME.md`.

## Versión para WordPress

En `wordpress/` hay la web preparada para pegarla en un bloque de **HTML
personalizado**, con todo aislado para que el tema y la web no se pisen. Los pasos
están en `wordpress/INSTALACION.md`. Se regenera con:

```bash
python3 build/build_widget.py
```

## Estructura de archivos

```
index.html                 catalán (generado)
es/index.html              castellano (generado)
build/build.py             contenido en los dos idiomas + generador de las páginas
build/build_widget.py      generador de la versión para WordPress
contenido/textos-cliente.md   material que envió el estudio
assets/
  css/main.css             sistema de diseño completo (tokens, componentes, responsive)
  css/fonts.css            @font-face de las tipografías autoalojadas
  fonts/*.woff2            Biro Script Plus + Raleway 300–800 (subsets latin y latin-ext)
  js/main.js               cabecera, menú, collage, reveals, reels, marquesina, formulario
  img/proyectos/*.jpg      fotos de los proyectos, en 700 y 1100 px
  img/logo-laconic.svg     logotipo vectorizado
  img/logo-zero.svg        el 0 (hereda color con currentColor)
  img/logo-lockup.svg      el lockup con EST · STUDIO · 2024
  img/favicon.svg          favicon
  video/                   los reels; ver LEEME.md
wordpress/                 los cuatro archivos para pegar + INSTALACION.md
```

Para probar en local:

```bash
python3 -m http.server 8000   # http://localhost:8000
```

## Sistema de diseño

Todo se controla desde los tokens de `:root` en `assets/css/main.css`:

| Token | Valor | Uso |
| --- | --- | --- |
| `--terra` | `#C95948` | declaración, tira, servicios, acentos |
| `--cream` | `#F9F0E1` | fondo base y texto sobre terracota |
| `--ink` | `#1C2825` | secciones oscuras, botones, titulares sobre crema |
| `--text` | `#1C2825` | texto sobre crema (el mismo verde) |
| `--hand` | Biro Script Plus | líneas manuscritas (`class="hand"`) |
| `--display` | Raleway 700 | titulares (`class="display"`) |
| `--sans` | Raleway 300/400/500 | texto corrido y antetítulos |

Las dos son las tipografías del manual de identidad, autoalojadas en
`assets/fonts` (convertidas a woff2 desde los originales y subsetadas a latín).
Biro Script Plus es un trazo de bolígrafo, y por encima de unos 100 px se rompe.
Por eso nunca titula sola: va **dentro del titular**, al mismo cuerpo que la
Raleway, en el tramo de frase que tiene que cambiar de voz.

La paleta completa del manual está en los tokens: `--terra` Burnt Coral,
`--cream` Sanded Blush, `--ink` Night Moss, `--clay` Clay Heat, `--sand`
Pale Almond y `--deep` Deep Current (este último es el fondo de la sección de
la cita, `data-theme="deep"`).

Los titulares mezclan las dos tipografías **dentro de la misma frase**: Raleway
800 y, a media frase, Biro Script Plus al mismo cuerpo
(`<h2 class="display rl">Cada marca comunica, <span class="hand">però no totes
connecten</span>.</h2>`). Es el papel que en las webs editoriales hace la cursiva
de una serif: cambia la voz sin cambiar de tamaño ni de línea. La clase `rl`
activa el revelado palabra a palabra.

**Aviso sobre las fotos**: seis de las que envió el estudio son collages de dos o
tres imágenes montadas (`f45-2`, `f45-3`, `jordi-coll-1`, `puig-2`, `quality-2` y
`maitasuna-3`). A tamaño grande se les ve la costura, así que la portada de cada
proyecto y las fotos a sangre usan solo tomas sueltas; está anotado en
`build/build.py`.

## Movimiento

Todo con IntersectionObserver y un único bucle de `requestAnimationFrame`, sin
librerías, y desactivado con `prefers-reduced-motion`:

- **Inicio**: el logotipo entra recortándose de arriba abajo, y el nombre, el
  reclamo y el filete después, escalonados.
- **Piezas del inicio**: suben a velocidades distintas (`--rise` por pieza)
  mientras el escenario queda pegado, pasan por detrás del logotipo y salen por
  el borde de arriba.
- **Tira**: pasa en bucle con una animación CSS; el carril se duplica en el JS
  para que no se vea la costura, y se para al pasar el ratón.
- **Titulares**: cada palabra sube desde su propia caja, en cascada.
- **Cabecera**: siempre clara; se le pone sombra al despegarse y se esconde al
  bajar. El enlace de la sección visible se subraya.
- **Servicios**: la foto pegada al scroll cambia con el servicio activo, por
  ratón o por posición.
- **Trabajo**: cada foto se mueve en paralaje dentro de su marco.
- **Proceso**: el raíl se rellena y los puntos se encienden al pasar.
- **Cursor**: punto que crece sobre elementos interactivos (solo ratón).

## Cómo se cambian las cosas

- **Logo**: vectorizado de los archivos oficiales del estudio:
  `logo-laconic.svg` (logotipo), `logo-zero.svg` (el cero) y `logo-lockup.svg`
  (con EST · STUDIO · 2024). Los tres van como `<symbol>` en un sprite al
  principio de `index.html` (`#lg-word`, `#lg-zero`, `#lg-lockup`) y se usan con
  `<use>`, así que heredan el color de la sección con `currentColor`.
- **Fotos del inicio**: las cinco piezas que suben están en `HERO_TILES`, y su
  recorrido lo controlan
  `.tile--1` … `--5` en el CSS (`--rise` es cuánto sube cada una). Las de la tira
  en bucle, en `TIRA`; las del panel de servicios, en `COLLAGE`.
- **Proyectos**: cada `<article class="slab">` lleva su medio (vídeo o foto) y su
  texto, y alterna lado con `slab--flip`. Todo sale de `PROYECTOS` en
  `build/build.py`: añadir o quitar proyectos no rompe nada.

## Nota de contraste

Con estos tres colores, crema sobre terracota da 3.7:1 y verde sobre terracota
3.6:1. Es suficiente para titulares y texto grande (WCAG AA los admite desde
3:1), pero se queda por debajo del 4.5:1 que pide el texto pequeño. Por eso en
las secciones de terracota el texto va en crema a opacidad plena y los
subtítulos en negrita. Crema sobre verde profundo da 13.5:1, sin problema.

## Contenido del cliente

Todo el material que envió el estudio está recogido en
`contenido/textos-cliente.md`: equipo, textos, paleta del manual y los enlaces de
las piezas publicadas de cada proyecto.

Los siete proyectos de la sección de trabajo son reales, y los que tienen piezas
publicadas —Quality Training, Jordi Coll, Malhivern y Comercial Puig— enlazan a
Instagram. En cuanto los `.mp4` estén en `assets/video`, el vídeo se ve **dentro**
de la web y el enlace pasa a ser secundario («Míralo en Instagram»); mientras no
estén, el enlace es la única forma de ver la pieza y el visitante sale del sitio.

## Pendiente de revisar

- **Textos**: los pies de los proyectos son propuestas escritas con el tono de la
  marca; conviene repasarlos. Las cifras inventadas («48 h», «100 % a medida») y
  la sección de plantillas de pago **se han quitado**: no las envió el estudio.
  Si quieren vender recursos, hay que decidir qué y a qué precio.
- **Formulario**: no tiene backend; compone un correo con los datos y abre el
  cliente de email. Para recibirlo en un servidor, cambiar el atributo `data-mailto`
  del `<form>` por `action` + `method` (Formspree, Netlify Forms, etc.).
- **Dominio y metadatos**: revisar `<link rel="canonical">` y las etiquetas Open
  Graph con la URL definitiva.

## Accesibilidad y rendimiento

- Sin peticiones externas: tipografías autoalojadas, símbolo en SVG.
- Navegación por teclado con `:focus-visible`, enlace de salto al contenido y menú
  móvil con `aria-hidden`.
- Las animaciones de entrada solo se aplican si hay JavaScript, y el collage se
  muestra ya colocado con `prefers-reduced-motion`.
