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
| `index.html` | Home: hero, bienvenida, tratamientos (actuales y próximos), bloques de categoría, el método, para quién es, FAQ, presentación del estudio y llamada a la acción |
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

1. **Fotografías definitivas.** Las de ahora son las que envió el estudio,
   redimensionadas a 1400 px de ancho y comprimidas. Tras la sesión
   fotográfica profesional se sustituyen manteniendo los mismos nombres.
   Cada hueco de la web tiene su propia fotografía, sin repetir: los nombres
   dicen dónde va cada una (`hero-*`, `card-*`, `cat-*`, `collage-*`, `srv-*`,
   `met-*`, `about-*`, `gal-*`). Quedan dos ilustraciones vectoriales donde
   todavía no hay foto: `srv-capilar.svg` (micropigmentación capilar) y
   `srv-powder.svg` (labios), más `cta-wide.svg`, decorativa a propósito.
1b. **Consentimiento de imagen.** Varias fotos muestran rostros de clientas
   reconocibles, incluidas comparativas de antes y después. Antes de publicar
   hace falta su autorización por escrito.
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
8. **Logotipo.** Ya está el original en `assets/brand/`, recortado y con
   fondo transparente, en versión granate y crema. La cabecera alterna entre
   las dos según el fondo. Si el estudio envía el archivo vectorial (SVG),
   conviene sustituirlo: se verá más nítido en pantallas grandes.
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
--burgundy: #741c2d;   /* granate tomado del logotipo */
--cream:    #f6f1ec;   /* fondo general */
--gold:     #a98a63;   /* acento sutil */
--sans:     "Instrument Sans";   /* toda la web */
--track-lg: .22em;             /* el espaciado de los titulares */
```

Las tipografías están alojadas en el propio proyecto (`assets/fonts/`, con sus
`@font-face` en `assets/css/fonts.css`): cargan antes que desde un servicio
externo y no envían datos de las visitantes a terceros. Para añadir o cambiar
una familia:

```bash
python3 tools/fetch-fonts.py "Bodoni Moda:ital,wght@0,400;1,400"
```

Instrument Sans es la única tipografía de la web: una grotesca de trazo
uniforme y formas abiertas. Todo el carácter sale de **usarla en mayúsculas
con mucho aire entre letras**, no de mezclar familias ni de pesos extremos.
Al ser variable, un solo archivo por alfabeto cubre de la 400 a la 700 (92 KB
las cuatro caras).

El espaciado entre letras es una escala con nombre, no un número suelto:

| Token | Valor | Dónde |
|---|---|---|
| `--track-sm` | `.10em` | pies de foto, cifras |
| `--track-md` | `.16em` | botones, enlaces, epígrafes, subtítulos |
| `--track-lg` | `.22em` | titulares (`.display`, `.h2`) |
| `--track-xl` | `.34em` | menú, anuncio, rótulos pequeños y etiquetas |

Y el reparto de pesos:

- **400** en titulares y texto corrido.
- **500** en menú activo, botones, epígrafes y subtítulos.
- Nada por encima de la 500 salvo un `strong` puntual: el contraste lo dan el
  espaciado y el tamaño.

Van en mayúsculas el menú, el anuncio superior, el menú móvil, los titulares,
los subtítulos, las etiquetas, los pies de foto, las preguntas del FAQ y el
pie de página. **No** van en mayúsculas los textos largos: el párrafo de
bienvenida, los `.lead` y los cuerpos de texto, porque un párrafo entero
espaciado deja de leerse.

La palabra destacada de cada titular (`<em>`) no es cursiva ni negrita: es un
cambio de color. Sale de `--accent`, que vale granate sobre crema y moka en
los bloques de fondo oscuro, donde el granate se perdería.

### Crecer sin rehacer la web

La estructura está pensada para ampliarse:

- Los tratamientos son bloques `.service-row` en `servicios.html`: añadir uno
  nuevo es copiar un bloque y cambiar texto e imagen.
- La home tiene una retícula con dos pestañas (`tratamientos` /
  `próximamente`); mover un servicio de una a otra es cambiarlo de panel y
  quitarle la clase `tcard--soon`.
- Los bloques de categoría (`.cats`) admiten más columnas sin tocar el CSS.

## Movimiento

El movimiento sigue un mismo criterio en toda la web: entradas largas y
suaves, nada de rebotes ni desplazamientos bruscos.

- `.reveal` — el bloque aparece subiendo al entrar en pantalla.
- `.reveal--curtain` — los titulares se descubren de arriba abajo.
- `.media-in` — las fotografías entran con un ligero cambio de escala.
- `data-parallax="26"` — la imagen se desplaza más despacio que la página;
  el número son los píxeles de recorrido, y en negativo va al revés.
- La cabecera se aparta al bajar y vuelve al subir.
- La fotografía fija de la portada respira muy lentamente.
- Los botones se rellenan de granate desde abajo.

Todo se desactiva con `prefers-reduced-motion`, la preferencia del sistema
para quien marea el movimiento.

## Notas técnicas

- Sin frameworks: se publica tal cual en cualquier hosting estático.
- Responsive a partir de 360 px; puntos de ruptura en 1100, 900 y 560 px.
- Accesibilidad: navegación por teclado, `aria` en pestañas, acordeón y
  carrusel, y respeto de `prefers-reduced-motion`.
- Si el JavaScript no carga, el contenido sigue siendo visible y navegable.
- Las fotografías van a 1400 px de ancho y calidad 82: entre 80 y 350 KB
  cada una. Si más adelante se busca afinar la velocidad, el siguiente paso
  sería servirlas en WebP.
