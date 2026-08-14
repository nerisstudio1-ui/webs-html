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
profundo, el logotipo en la cabecera y en el inicio, el símbolo del **0** como remate, y
titulares que mezclan la manuscrita y la sans pesada dentro de la misma frase.

## Secciones (todas en `index.html`)

| Ancla (CA / ES) | Contenido |
| --- | --- |
| — | Inicio: fondo beige, el **logotipo en terracota** centrado, el claim y el filete «Based in Girona. Working beyond.» |
| — | Las **dos fotos a pantalla completa**, a sangre, una al lado de la otra |
| — | Declaración sobre terracota, centrada, sin botón |
| — | Tira de fotos que pasa en bucle |
| `#about` | Manifiesto, «Less noise. More meaning.» y las dos socias |
| — | La línea de servicios que pasa, fina y pequeña |
| `#serveis` / `#servicios` | Los cinco servicios: los nombres grandes y escalonados, y la definición del que está activo |
| `#projectes` / `#proyectos` | Los siete proyectos en retícula; cada ficha abre Instagram |
| `#contacte` / `#contacto` | Formulario y contacto directo |

Fuera desde la revisión de agosto de 2026: la FAQ, «com treballem», «el que
diuen» (reseñas), la cita «Menys soroll. Més sentit», el rótulo «Designed to
speak quietly» y la lista de marcas con las que ha trabajado el estudio.

## Material de marca

`assets/img/marca/flyer-cotxe-*.jpg` es la foto del flyer del estudio sobre un
coche. Ya no se usa en el inicio, pero se conserva por si sirve en otra sección.

Los cinco iconos del flyer siguen redibujados como SVG en `ICONOS` —el sol, la
pausa, el asterisco, la flecha y el cero— y acompañan a cada nombre de servicio.
Los textos de los servicios son los que escribió el estudio en la revisión de
agosto de 2026; la versión castellana es su traducción.

## Vídeos de los proyectos

Cuatro proyectos tienen reel en `assets/video`: **Quality Training**, **Ratafia
Malhivern**, **Jordi Coll** y **Comercial Puig**. Desde la revisión de agosto de
2026 los proyectos se enseñan en retícula, así que el reel ya no ocupa media
sección: es el medio de la ficha, recortado igual que las fotos, en bucle y sin
sonido. La retícula no cambia, y el material grabado no se pierde.

`PROYECTOS_CON_VIDEO = False` en `build/build.py` hace que todas las fichas
enseñen su foto y los vídeos se queden fuera. Es una línea.

El arranque **no depende de nuestro JavaScript**: el `<video>` lleva `autoplay
muted playsinline`, así que si un plugin de caché aplaza o rompe el guion, se
reproduce igual. Los navegadores no empiezan un vídeo silenciado hasta que está en
pantalla, así que no se descarga de más. Además lleva `class="skip-lazy"` y
`data-no-lazy` para que los plugins de carga diferida no le quiten el `src`, que es
lo que los deja en negro. El JavaScript solo los para al salir de pantalla, y quien
pide `prefers-reduced-motion` no ve ninguno arrancar solo.

Los detalles de formato y nombres están en `assets/video/LEEME.md`.

## Formulario de contacto

Los mensajes **llegan por correo** a `hello@laconicstudio.es` a través de
[FormSubmit](https://formsubmit.co), que no pide cuenta, clave ni plugin: basta
con que la dirección esté en el `action` del formulario.

Falta **confirmar la dirección una sola vez**, y solo se puede hacer desde la web
ya publicada. Ojo: la dirección cambió en agosto de 2026 de `itslaconicstudio@gmail.com`
a `hello@laconicstudio.es`, así que la confirmación hay que **rehacerla** con la
nueva: se envía el formulario, FormSubmit manda un correo a la bandeja del
estudio con un enlace, se pulsa, y desde ese momento entran todos los mensajes.
El paso está detallado en [`wordpress/INSTALACION.md`](wordpress/INSTALACION.md).

Cómo se comporta:

- Con JavaScript, el envío ocurre **sin salir de la página**: el botón se apaga
  mientras va y debajo aparece «Recibido. Te respondemos en menos de 48 horas
  laborables». Si el servicio no contesta, el aviso pasa a dar la dirección de
  correo para escribir a mano, así que el mensaje no se pierde en silencio.
- Sin JavaScript, el `<form>` se envía como siempre a `action` y responde la
  página de gracias del propio servicio.
- El asunto del correo lleva el idioma de la página (`(CA)` o `(ES)`), y va un
  campo trampa `_honey` para el spam automático.

Se cambia de servicio en `build/build.py`, en `FORM_ACTION`, `FORM_AJAX` y
`FORM_OCULTOS`, con **Web3Forms** y **Formspree** anotados ahí como alternativas.
Dejando `FORM_ACTION` vacío, el formulario vuelve al modo de reserva: compone el
correo y abre el cliente de email del visitante. Un plugin tipo Contact Form 7 no
sirve, porque su shortcode no se ejecuta dentro de un bloque de HTML personalizado.

## Versión para WordPress

En `wordpress/` hay la web preparada para pegarla en un bloque de **HTML
personalizado**, con todo aislado para que el tema y la web no se pisen, en dos
versiones:

- `widget-*-copiar-pegar.html` (3 MB) — tipografías, fotos y pósters dentro del
  archivo, y los cuatro vídeos apuntando a la Biblioteca de medios. Se pega y ya
  está: nada que subir, nada que sustituir. Las URL de los vídeos están en
  `VIDEOS_WORDPRESS` (`build/build_widget.py`).
- `widget-*.html` (130 KB) — lo mismo con los archivos aparte. Mucho más ligero en
  la base de datos y cacheable, pero hay que subir `assets/` por FTP.

Los cuatro llevan la fecha y hora de generación en el comentario de cabecera
(`Generado: …`). Sirve para saber qué versión está publicada de verdad: si en la
web pública falta algo que en el editor sí se ve, es caché, y ese sello lo confirma.

La estructura que esperan los enlaces de idioma: la página **catalana es la portada**
del sitio y la **castellana** es una página con el slug **`es`**. Si van a otras
direcciones, se cambian los tres enlaces de cada archivo. Todo detallado, con el
apartado de caché, en `wordpress/INSTALACION.md`.

Los pasos están en `wordpress/INSTALACION.md`. Se regenera con:

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
  js/main.js               cabecera, menú, reveals, servicios, vídeos, marquesina, formulario
  img/proyectos/*.jpg      fotos de los proyectos, en 700 y 1100 px
  img/logo-laconic.svg     logotipo vectorizado
  img/logo-zero.svg        el 0 (hereda color con currentColor)
  img/logo-lockup.svg      el lockup con EST · STUDIO · 2024
  img/favicon.svg          favicon
  video/                   los reels; ver LEEME.md
wordpress/                 los cuatro archivos para pegar + INSTALACION.md
                           (dos por idioma: 130 KB y copiar-pegar)
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

Otras cinco traían un marco blanco dentro del propio archivo (`jordi-coll-3`,
`maitasuna-2`, `malhivern-1`, `malhivern-3` y `puig-3`). Están recortadas, así que
ya no son 4:5 y el generador lee el tamaño real de cada archivo con `medidas()` en
lugar de darlo por hecho.

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
- **Formulario**: queda **confirmar la dirección en FormSubmit** enviando el
  formulario una vez desde la web publicada y pulsando el enlace del correo que
  llega. Hay que rehacerlo con `hello@laconicstudio.es`, y ese buzón tiene que
  existir. Hasta que se haga, los mensajes no entran en la bandeja.
- **Dominio y metadatos**: revisar `<link rel="canonical">` y las etiquetas Open
  Graph con la URL definitiva.

Pendiente de la revisión de agosto de 2026, todo por material que no llegó con
el PDF de cambios:

- **Las dos fotos del inicio**: el estudio dijo que adjuntaba las escogidas. Van
  dos de las que hay; se cambian en `HERO_DUO` (`build/build.py`).
- **La selección de fotos del about**: igual. Van siete en `TIRA`.
- **La foto de cada proyecto**: la retícula usa la portada que ya tenía cada uno
  (`portada` en `PROYECTOS`).
- **El enlace de Instagram de tres proyectos**: Football 4 Stars, Maitasuna y F45
  Training no tienen ninguno en `piezas`, así que su ficha se dibuja sin enlace.
  En cuanto lleguen, la ficha pasa a ser enlace sola.
- **La frase del claim**: el PDF pide «Contingut que connecta.» y añade «(tot
  seguit, una frase)». Está puesta la primera parte; si esperaban una segunda
  frase, falta el texto.

## Accesibilidad y rendimiento

- Sin peticiones externas: tipografías autoalojadas, símbolo en SVG.
- Navegación por teclado con `:focus-visible`, enlace de salto al contenido y menú
  móvil con `aria-hidden`.
- Las animaciones de entrada solo se aplican si hay JavaScript, y el collage se
  muestra ya colocado con `prefers-reduced-motion`.
