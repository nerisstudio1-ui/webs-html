# Laconic Studio — landing

Landing de una sola página para **Laconic Studio**. HTML + CSS + JS, sin
dependencias ni proceso de build: se abre con doble clic.

Todo el branding sale de la identidad de la marca: terracota, crema y verde
profundo, logotipo manuscrito con el símbolo del **0**, y titulares que combinan
la manuscrita con la sans pesada.

## Secciones (todas en `index.html`)

| Ancla | Contenido |
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
| `--hand` | Caveat 500 | logotipo y líneas manuscritas (`class="hand"`) |
| `--sans` | Inter 800 | titulares pesados; Inter 400 para texto |

Los titulares usan el patrón de la marca: la línea manuscrita arriba y la línea
en sans pesada debajo (`<h2 class="big"><span class="hand">…</span>…</h2>`).

## Cómo se cambian las cosas

- **Logo**: es el logotipo real, vectorizado a partir de la pieza de marca:
  `assets/img/logo-laconic.svg` (logotipo manuscrito) y `assets/img/logo-zero.svg`
  (el cero). Los dos están declarados como `<symbol>` en un sprite al principio
  de `index.html` (`#lg-word` y `#lg-zero`) y se usan con `<use>`, así que heredan
  el color de la sección con `currentColor`. Si aparece el archivo original del
  estudio, basta sustituir el `<path>` de cada `<symbol>`.
  Nota: la manuscrita de los titulares (`class="hand"`) sí es una tipografía
  (Caveat), la más parecida al trazo de la marca.
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
