# Bela Brow Studio & Beauty — sitio web

Web estática (HTML + CSS + JS, sin dependencias ni build) para el estudio de
micropigmentación de cejas **Bela Brow Studio & Beauty**, especializado en la
técnica Hair Stroke.

Estética minimalista y premium: granate/burdeos como color protagonista sobre
blanco roto y tonos arena, acentos dorados sutiles, amplios espacios en blanco
y tipografía elegante. Las imágenes son las protagonistas de cada bloque.

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Home: hero, tratamientos (actuales y próximos), bloques de categoría, el método, para quién es, FAQ, crecimiento del estudio y llamada a la acción |
| `servicios.html` | Cejas realistas (Hair Stroke), estudio previo y diseño, laminado y henna; sección «próximamente» y criterio de tarifas |
| `metodo.html` | Las 4 fases del método, cuidados durante la cicatrización y tipos de piel |
| `estudio.html` | La historia de las dos hermanas, filosofía, especialización, galería y hacia dónde va el estudio |
| `contacto.html` | Formulario de cita, contacto directo, hueco para la reserva online e indicaciones previas |

## Ver la web

### Vista previa en una sola página

`tools/build-preview.py` empaqueta las cinco páginas en un único HTML
autocontenido (CSS, JS e ilustraciones incrustados, navegación por hash), útil
para enseñar la web sin necesidad de hosting:

```bash
python3 tools/build-preview.py   # genera bela-preview.html
```

El archivo generado no se versiona. Es solo para enseñar el diseño: la web que
se publica es la de los cinco archivos HTML.

### En local

Abriendo `index.html` con doble clic funciona. Para que se comporte igual que
en producción, mejor con un servidor:

```bash
python3 -m http.server 8000
# luego abre http://localhost:8000
```

## Qué ya está conectado

- **Botón flotante de WhatsApp** en todas las páginas (`+34 611 599 132`).
- **Formulario de cita** (`contacto.html`): sin servidor detrás, compone la
  solicitud con todos los campos y la abre en WhatsApp o en el gestor de correo
  ya escrita. Al contratar hosting basta con sustituir ese bloque de
  `assets/js/main.js` por el envío real.
- Enlaces a Instagram (`@micropigmentacionbela`) y teléfono.
- Horario de atención: L-V 9:00–20:00 y sábados 10:00–14:00.

## Qué falta por decidir o sustituir

1. **Fotografías.** Las imágenes de `assets/img/*.svg` son ilustraciones
   vectoriales de cejas generadas a medida, pensadas como muestra hasta la
   sesión fotográfica. Sustituye cada archivo por la foto real con el mismo
   nombre (`hero-left.jpg`, `srv-hairstroke.jpg`, …) y cambia la extensión en
   el `src` de los HTML. Proporciones usadas:
   - `hero-*` → vertical 6:7
   - `srv-*`, `cat-*` → vertical 4:5
   - `journal-*`, `studio-2` → horizontal 4:3
   - `cta-wide` → panorámica 2:1
2. **Dirección del estudio y mapa.** Sin determinar. Ahora la web dice que se
   confirma al reservar; hay un bloque preparado en `contacto.html`.
2b. **Correo profesional.** Pendiente de crear junto con el dominio. Hasta
   entonces la web no muestra ningún email y el formulario envía por WhatsApp
   (`EMAIL` en `assets/js/main.js` activa el envío por correo al rellenarse).
3. **Tarifas.** No hay precios publicados: la web explica que se presupuesta
   tras el estudio previo. Cuando estén cerradas, la sección «tarifas» de
   `servicios.html` está lista para recibirlas.
4. **Versión en inglés.** Pendiente. La estructura está preparada para
   duplicar las páginas en `/en/` y añadir un selector ES/EN en la cabecera.
5. **Reserva de citas online.** Hay un bloque reservado en `contacto.html`
   para insertar el widget del sistema que se contrate (Booksy, Treatwell,
   Calendly…).
6. **Textos legales.** Los enlaces «Aviso legal · Privacidad · Cookies» del
   pie todavía no apuntan a ninguna página. Son necesarios antes de publicar,
   sobre todo porque el formulario recoge datos personales.
7. **Dominio y hosting.** No hay ninguno contratado. Al ser una web estática
   se puede publicar en GitHub Pages, Netlify o cualquier hosting básico.
8. **Logo original.** El logotipo de la cabecera está recreado con tipografía.
   Los archivos originales van en `assets/brand/` (ver el README de esa
   carpeta); al añadirlos hay que ajustar `--burgundy` al granate real.
9. **Confirmar el teléfono.** El 611 599 132 viene del formulario inicial;
   falta confirmar que es el número de contacto del estudio.

## Estructura

```
index.html  servicios.html  metodo.html  estudio.html  contacto.html
assets/
  css/style.css   sistema de diseño completo, comentado por secciones
  js/main.js      menú móvil, slideshow, pestañas, acordeón FAQ, formulario
  img/            ilustraciones de muestra y favicon
```

### Tokens de diseño

Colores y tipografías salen de variables CSS en `:root`
(`assets/css/style.css`). Cambiar la marca entera es cambiar esas variables:

```css
--burgundy: #4a171c;   /* granate protagonista */
--cream:    #f6f1ec;   /* fondo general */
--gold:     #a98a63;   /* acento sutil */
--serif:    "Playfair Display", serif;  /* titulares y logotipo */
--sans:     "Jost", sans-serif;         /* texto y navegación */
```

Las tipografías se cargan desde Google Fonts. Si prefieres no depender de un
servicio externo, descarga los `.woff2` a `assets/fonts/` y sustituye el
`<link>` de las cabeceras por reglas `@font-face`.

### Crecer sin rehacer la web

La estructura está pensada para ampliarse:

- Los tratamientos son bloques `.service-row` en `servicios.html`: añadir uno
  nuevo es copiar un bloque y cambiar texto e imagen.
- La home tiene un carrusel con dos pestañas (`tratamientos` /
  `próximamente`); mover un servicio de una a otra es cambiarlo de panel y
  quitarle la etiqueta `tag-soon`.
- Los bloques de categoría (`.cats`) admiten más columnas sin tocar el CSS.

## Notas técnicas

- Sin frameworks: se publica tal cual en cualquier hosting estático.
- Responsive a partir de 360 px; puntos de ruptura en 1100, 900 y 560 px.
- Accesibilidad: navegación por teclado, `aria` en pestañas, acordeón y
  carrusel, y respeto de `prefers-reduced-motion`.
- Si el JavaScript no carga, el contenido sigue siendo visible y navegable.
- Las ilustraciones de muestra son SVG con miles de trazos: pesan poco pero
  dan trabajo de pintado al navegador. Al sustituirlas por fotografías reales
  (JPG/WebP) la web irá más ligera todavía.
