# Laconic Studio — web

Sitio estático (HTML + CSS + JS, sin dependencias ni build) para **Laconic Studio**,
con la misma estructura que una web de estudio creativo tipo `thecscreativestudio.com`
(inicio, estudio, servicios, trabajo, tienda, contacto) y el branding de Laconic:
terracota, crema y verde profundo, manuscrita + sans pesada, y el símbolo del **0**.

## Páginas

| Archivo | Contenido |
| --- | --- |
| `index.html` | Hero con logo y collage que sube, declaración de estudio, texto sobredimensionado, índice numerado, frase con palabra rotatoria, claims y contacto |
| `estudio.html` | Manifiesto largo, reglas del estudio, paleta de marca y FAQ |
| `servicios.html` | Los 5 servicios en detalle (`#content`, `#social`, `#design`, `#ads`, `#ugc`), packs y FAQ |
| `trabajo.html` | Fichas de proyecto (`#pure`, `#paipai`, `#nocturna`, `#estudio-b`, `#raiz`) |
| `tienda.html` | Recursos descargables, cómo funciona y FAQ |
| `contacto.html` | Formulario, contacto directo y qué pasa después |

## Estructura

```
assets/
  css/main.css     sistema de diseño completo (tokens, componentes, responsive)
  css/fonts.css    @font-face de las tipografías autoalojadas
  fonts/*.woff2    Caveat + Inter (subsets latin y latin-ext, OFL 1.1)
  js/main.js       header, menú móvil, acordeón, reveals, marquee, formulario
  img/mark.svg     símbolo "0" de la marca
  img/favicon.svg  favicon
```

Se abre directamente con doble clic o, para probar en local:

```bash
python3 -m http.server 8000   # http://localhost:8000
```

## Sistema de diseño

Todo se controla desde los tokens de `:root` en `assets/css/main.css`:

| Token | Valor | Uso |
| --- | --- | --- |
| `--terra` | `#C0574A` | color principal, héroes y acentos |
| `--cream` | `#F8EDDD` | fondo base y texto sobre terracota |
| `--ink` | `#1E3538` | secciones oscuras, botones |
| `--text` | `#2B2724` | texto sobre crema |
| `--hand` | Caveat | titulares manuscritos (`class="hand"`) |
| `--sans` | Inter | texto y titulares pesados |

Las escalas de tipografía (`--step--1` … `--step-5`) y el espaciado son fluidos con
`clamp()`, así que no hay saltos entre móvil y escritorio.

## Pendiente de conectar / revisar

- **Collage del hero**: las seis piezas son placeholders SVG
  (`assets/img/proyecto-01.svg` … `-06.svg`). Se sustituyen cambiando el `src`
  de cada `<img>` del hero, sin tocar el CSS.
- **Logo**: el hero compone el logotipo con el símbolo del 0 y la manuscrita.
  Si hay logo original en SVG o PNG, se cambia ese bloque por
  `<img class="hero__logo-img" src="assets/img/logo-laconic.svg" alt="Laconic Studio">`
  (queda indicado en un comentario dentro de `index.html`).
- **Imágenes de proyecto**: las fichas de `trabajo.html` usan bloques de color
  generados con CSS (clases `.ph`, con la etiqueta «Muestra de estudio»). Para
  poner material real, sustituir `<div class="ph ...">…</div>` por
  `<img src="assets/img/…" alt="…">` dentro de `.card__media` y quitar `.badge`.
- **Textos y precios**: los casos, cifras y precios de packs y tienda son propuestas de
  ejemplo redactadas con el tono de la marca. Hay que revisarlos antes de publicar.
- **Formulario**: `contacto.html` no tiene backend; compone un correo con los datos y
  abre el cliente de email. Para recibirlo en un servidor, sustituir el atributo
  `data-mailto` del `<form>` por `action` + `method` (Formspree, Netlify Forms, etc.).
- **Tienda**: los botones «Lo quiero» abren un correo. Al conectar Stripe, Gumroad o
  Shopify basta con cambiar el `href` de esos botones.
- **Dominio y metadatos**: revisar `<link rel="canonical">` en `index.html` y las
  etiquetas Open Graph con la URL definitiva.

## Accesibilidad y rendimiento

- Sin peticiones externas: tipografías autoalojadas, gráficos en SVG/CSS.
- Navegación por teclado con `:focus-visible`, enlace de salto al contenido, acordeón
  con `aria-expanded` y menú móvil con `aria-hidden`.
- Las animaciones de entrada solo se aplican si hay JavaScript, y se desactivan con
  `prefers-reduced-motion`.
