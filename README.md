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
profundo, logotipo manuscrito con el símbolo del **0**, y titulares que combinan
la manuscrita con la sans pesada.

## Secciones (todas en `index.html`)

| Ancla (CA / ES) | Contenido |
| --- | --- |
| — | Inicio: foto a sangre oscurecida, logotipo gigante con una pieza cruzada y el filete con los dos rótulos |
| — | Declaración sobre terracota, centrada, con la manuscrita dentro de la frase |
| — | Tira de cinco fotos a sangre que sube con el scroll, con el titular gigante detrás |
| `#estudio` | Manifiesto, frase de marca y cifras |
| `#servicios` | Los cinco servicios con su subtítulo y entregables |
| `#trabajo` | Los siete proyectos, con su vídeo si lo hay y si no la fotografía |
| — | Frase «Haz match con lo que vibre contigo» sobre verde profundo |
| `#proceso` | Los cuatro pasos de trabajo |
| `#recursos` | Plantillas y guías a la venta |
| `#contacto` | Formulario y contacto directo |

## Vídeos de los proyectos

Los reels van en `assets/video` con el nombre del proyecto: `quality-1.mp4`,
`malhivern-1.mp4`… El generador los detecta solos. Si un proyecto tiene vídeo, su
columna deja de ser una foto y pasa a ser el reel en marco vertical, con la foto
del proyecto como póster; si no lo tiene, se queda la foto. Arrancan sin sonido
al entrar en pantalla, se paran al salir, y el botón redondo activa el audio de
uno (solo puede sonar uno a la vez).

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
| `--terra` | `#C95948` | hero, secciones de servicios y contacto, acentos |
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

- **Inicio**: el logotipo entra con un `clip-path` sobre la foto, y detrás la
  pieza cruzada, el subtítulo y el filete aparecen escalonados.
- **Tira**: las cinco fotos suben a velocidades distintas (`--rise` por pieza)
  mientras entran en pantalla, y quedan a ras al llegar.
- **Titulares**: cada palabra sube desde su propia caja, en cascada.
- **Cabecera**: cambia de color según el tema de la sección que cruza
  (`data-theme` → `data-on`), y el enlace de la sección visible se subraya.
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
- **Fotos del inicio**: `HERO_FONDO` es la foto a sangre y `HERO_CHIP` la pieza
  que se cruza con el logotipo (`build/build.py`). Las cinco de la tira están en
  `TIRA`, y su velocidad de subida la controlan `.strip__cell--1` … `--5` en el
  CSS (`--rise` es cuánto sube cada una). Las del panel de servicios, en
  `COLLAGE`.
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

- **Textos y precios**: los pies de los proyectos, las cifras del manifiesto y los
  precios de recursos son propuestas con el tono de la marca. Conviene repasarlos.
- **Formulario**: no tiene backend; compone un correo con los datos y abre el
  cliente de email. Para recibirlo en un servidor, cambiar el atributo `data-mailto`
  del `<form>` por `action` + `method` (Formspree, Netlify Forms, etc.).
- **Recursos**: los botones «Lo quiero» abren un correo. Al conectar Stripe,
  Gumroad o Shopify basta con cambiar el `href`.
- **Dominio y metadatos**: revisar `<link rel="canonical">` y las etiquetas Open
  Graph con la URL definitiva.

## Accesibilidad y rendimiento

- Sin peticiones externas: tipografías autoalojadas, símbolo en SVG.
- Navegación por teclado con `:focus-visible`, enlace de salto al contenido y menú
  móvil con `aria-hidden`.
- Las animaciones de entrada solo se aplican si hay JavaScript, y el collage se
  muestra ya colocado con `prefers-reduced-motion`.
