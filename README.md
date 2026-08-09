# BELA. Brow Design — sitio web

Web estática (HTML + CSS + JS, sin dependencias ni build) para un centro de
microblading y micropigmentación. Estética editorial: retícula amplia,
tipografía de alto contraste y paleta burdeos sobre crema tomada del logo.

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Home: hero partido, carrusel de tratamientos, categorías, método, testimonios, FAQ, journal, CTA |
| `servicios.html` | Ficha de cada técnica (cejas, labios, mirada) + tabla de tarifas |
| `metodo.html` | Las 4 fases del método, cuidados post-tratamiento, tipos de piel |
| `estudio.html` | Fundadora, forma de trabajar, galería del espacio, reseñas |
| `contacto.html` | Formulario de reserva, horarios, datos e indicaciones previas |

## Ver la web en local

Abriendo `index.html` con doble clic funciona. Para que todo se comporte
igual que en producción, mejor con un servidor:

```bash
python3 -m http.server 8000
# luego abre http://localhost:8000
```

## Qué hay que personalizar antes de publicar

Todo el contenido es **de ejemplo**. Estos son los puntos a sustituir:

1. **Fotos.** Las imágenes de `assets/img/*.svg` son marcadores de posición
   generados con los colores de marca. Sustituye cada una por una foto real
   con el mismo nombre (`hero-left.jpg`, `srv-microblading.jpg`, …) y cambia
   la extensión en el `src` de los HTML. Proporciones usadas:
   - `hero-*` → vertical 6:7
   - `srv-*`, `cat-*` → vertical 4:5
   - `journal-*`, `studio-2` → horizontal 4:3
   - `cta-wide` → panorámica 2:1
2. **Datos de contacto.** Dirección, teléfono, WhatsApp, email, Instagram y
   horario aparecen en el pie de las 5 páginas y en `contacto.html`.
3. **Precios y duraciones.** En `servicios.html` (fichas y tabla de tarifas)
   y en las tarjetas del carrusel de `index.html`.
4. **Textos legales.** Los enlaces «Aviso legal · Privacidad · Cookies» del
   pie no apuntan a ninguna página todavía.
5. **Mapa.** El iframe de `contacto.html` usa unas coordenadas de ejemplo de
   OpenStreetMap; cámbialas por la ubicación real.
6. **Formularios.** Los de reserva y newsletter son una demostración: hoy
   solo muestran un mensaje de confirmación en pantalla y **no envían nada**.
   Hay que conectarlos a un servicio de formularios o al gestor de citas.

## Estructura

```
index.html  servicios.html  metodo.html  estudio.html  contacto.html
assets/
  css/style.css   sistema de diseño completo, comentado por secciones
  js/main.js      menú móvil, slideshow, pestañas, acordeón FAQ, animaciones
  img/            imágenes (marcadores de posición) y favicon
```

### Tokens de diseño

Los colores y tipografías salen de variables CSS en `:root`
(`assets/css/style.css`). Cambiar la marca entera es cambiar esas variables:

```css
--burgundy: #4a171c;   /* color del logo */
--cream:    #f6f1ec;   /* fondo general */
--serif:    "Playfair Display", serif;  /* titulares y logotipo */
--sans:     "Jost", sans-serif;         /* texto y navegación */
```

Las tipografías se cargan desde Google Fonts. Si prefieres no depender de un
servicio externo, descarga los `.woff2` a `assets/fonts/` y sustituye el
`<link>` de las cabeceras por reglas `@font-face`.

## Notas técnicas

- Sin frameworks: se puede publicar tal cual en GitHub Pages, Netlify o
  cualquier hosting estático.
- Responsive a partir de 360 px; puntos de ruptura en 1100, 900 y 560 px.
- Accesibilidad: navegación por teclado, `aria` en pestañas, acordeón y
  carrusel, y respeto de `prefers-reduced-motion`.
- Si el JavaScript no carga, el contenido sigue siendo visible y navegable.
