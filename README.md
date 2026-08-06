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
| — | Hero: terracota plano, logo centrado y fotos de proyecto que suben con el scroll |
| `#estudio` | Manifiesto, frase de marca y cifras |
| `#servicios` | Los cinco servicios con su subtítulo y entregables |
| `#trabajo` | Rejilla de proyectos con fotografía real |
| — | Frase «Haz match con lo que vibre contigo» sobre verde profundo |
| `#proceso` | Los cuatro pasos de trabajo |
| `#recursos` | Plantillas y guías a la venta |
| `#contacto` | Formulario y contacto directo |

## Estructura de archivos

```
index.html
assets/
  css/main.css      sistema de diseño completo (tokens, componentes, responsive)
  css/fonts.css     @font-face de las tipografías autoalojadas
  fonts/*.woff2     Caveat + Inter (subsets latin y latin-ext, OFL 1.1)
  js/main.js        header, menú móvil, collage del hero, reveals, marquesina, formulario
  img/laconic-0*.jpg  fotografías de proyecto
  img/logo-zero.svg   símbolo del 0 (hereda color con currentColor)
  img/mark.svg        símbolo del 0 en crema
  img/favicon.svg     favicon
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
Biro Script Plus es un trazo de bolígrafo: en el manual titula secciones a tamaño
medio, así que en la web se usa como **acento sobre el titular**, no como titular
—a 100 px el trazo se rompe.

La paleta completa del manual está en los tokens: `--terra` Burnt Coral,
`--cream` Sanded Blush, `--ink` Night Moss, `--clay` Clay Heat, `--sand`
Pale Almond y `--deep` Deep Current (este último es el fondo de la sección de
la cita, `data-theme="deep"`).

Los titulares usan el patrón de la marca: la línea manuscrita arriba y la línea
en display debajo (`<h2 class="display rl"><span class="hand">…</span>…</h2>`).
La clase `rl` activa el revelado palabra a palabra.

## Movimiento

Todo con IntersectionObserver y un único bucle de `requestAnimationFrame`, sin
librerías, y desactivado con `prefers-reduced-motion`:

- **Hero**: el logotipo entra con un `clip-path` y las cinco fotos suben con
  velocidades distintas (`--rise` por pieza) mientras el escenario queda pegado.
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
- **Fotos del hero**: cinco `<img>` dentro de `.hero__tiles`. Se cambia el `src`
  y ya está; la posición y la velocidad de subida las controlan `.tile--1` … `.tile--5`
  en el CSS (`--rise` es cuánto sube cada una).
- **Proyectos**: cada `<figure class="work__item">` lleva su foto y su pie. Añadir
  o quitar piezas no rompe la rejilla.

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

Los cuatro proyectos de la sección de trabajo son reales — Quality Training,
Jordi Coll, Malhivern y Comercial Puig — y cada uno enlaza a sus dos piezas en
Instagram. Para que los vídeos se reproduzcan **dentro** de la web hace falta
tener los `.mp4` y servirlos desde `assets/video/` con `<video>`; enlazando a
Instagram el visitante sale del sitio.

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
