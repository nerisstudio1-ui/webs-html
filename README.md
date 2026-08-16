# Bela Brow Studio & Beauty — sitio web

Web estática (HTML + CSS + JS, sin dependencias ni build) para el estudio de
micropigmentación de cejas **Bela Brow Studio & Beauty**, especializado en la
técnica Hair Stroke.

Estética minimalista y premium: granate/burdeos como color protagonista sobre
blanco roto y tonos arena, acentos dorados sutiles, amplios espacios en blanco
y tipografía elegante. Las imágenes son las protagonistas de cada bloque.

## Páginas

### Landing y páginas, las dos cosas

`index.html` es una **landing**: una sola página que lleva a un sitio, pedir
cita. El menú no salta de archivo, salta de sección, y el formulario está
dentro.

Las otras cuatro páginas **siguen existiendo** como detalle ampliado. No es
indecisión, es que cada una sirve para un tráfico distinto:

- **Instagram** manda gente al enlace de la bio. Ahí gana la landing: una
  pantalla, un objetivo, sin menú donde perderse.
- **Google** necesita páginas. Con una sola se compite por una palabra; con
  cinco, por «micropigmentación de cejas», «laminado», «hair stroke» y el
  nombre de la ciudad cuando haya dirección.

Desde la landing se llega a ellas solo por dos sitios, los que amplían de
verdad: «ver la carta completa» y «nuestra historia». Y desde el pie. Su menú
devuelve siempre a la landing, a la sección que toca.

| Archivo | Contenido |
|---|---|
| `index.html` | **Landing.** Hero, franja de marca, declaración, 01 pilares, 02 antes/después, llamada intermedia, 03 el método, 04 la carta, 05 por qué aquí, el estudio por dentro, 06 para quién es, 07 dudas, las hermanas, 08 pedir cita y cierre |
| `servicios.html` | Cejas realistas (Hair Stroke), estudio previo y diseño, laminado y henna; sección «próximamente» y criterio de tarifas |
| `metodo.html` | Las 4 fases del método, cuidados durante la cicatrización y tipos de piel |
| `estudio.html` | **Sobre nosotras**, con cabecera de revista: la fotografía del estudio a sangre en blanco y negro, el rótulo grande encima y el retrato de las dos hermanas montado sobre las dos cosas. Después el relato a dos columnas con su cita, la especialización, la galería y el cierre con el nombre del estudio |
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
   `met-*`, `about-*`, `gal-*`). `hero-portada.jpg` es la imagen de marca de
   la portada: lleva el logotipo incrustado, así que va sin texto encima. Quedan dos ilustraciones vectoriales donde
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

Dos familias con papeles muy distintos:

- **Instrument Sans** — grotesca de trazo uniforme. Es la voz que explica:
  texto corrido, menú, botones y rótulos.
- **Playfair Display** — serif de alto contraste. Aparece **solo en cursiva**,
  en la palabra destacada de cada titular. Es la que pone el carácter, en la
  línea del propio logotipo.

Las dos son variables: un archivo por alfabeto cubre todo el rango de pesos.

El patrón de cada titular es siempre el mismo: sans en caja baja con una
palabra en cursiva serif. «Un cuidado *completo* de la mirada», «Antes /
*después*», «Cuatro pasos, *sin prisa*». En el HTML basta con envolver esa
palabra en `<em>`.

Van en mayúsculas con espaciado solo los rótulos: menú, anuncio superior,
epígrafes, botones, etiquetas y pies de foto. Los titulares y los textos van
en caja baja.

El espaciado entre letras es una escala con nombre, no un número suelto:

| Token | Valor | Dónde |
|---|---|---|
| `--track-sm` | `.10em` | pies de foto, cifras |
| `--track-md` | `.16em` | botones, enlaces, epígrafes |
| `--track-lg` | `.24em` | rótulos medianos |
| `--track-xl` | `.34em` | menú, anuncio, etiquetas |

La palabra destacada toma su color de `--accent`: granate sobre crema y moka
en los bloques de fondo oscuro, donde el granate se perdería.

### El criterio de la landing

Una landing no es una web con menos páginas: es una página con **un solo
objetivo**. Aquí, pedir cita. De ahí tres decisiones:

- **El recorrido persuade en orden.** Gancho (portada) → promesa
  (declaración) → qué hacemos (01) → **prueba** (02, el antes/después) →
  cómo lo hacemos, que quita el miedo (03) → qué puedes reservar (04) → por
  qué nosotras (05) → es para ti (06) → objeciones (07) → **reservar** (08).
- **La llamada aparece tres veces**: al entrar, justo después de la prueba
  (la franja `.band`) y al final, con el formulario. Más el botón fijo de la
  cabecera y el de WhatsApp.
- **El menú no te saca de la página.** Son anclas, y se resalta la sección en
  la que estás (`[data-spy]` en el JavaScript). `scroll-padding-top` evita
  que la cabecera pegajosa tape el destino.

### El criterio de las secciones

La portada no es una sucesión de bloques centrados: es lo que la haría
parecer una plantilla. Cada sección entra por un sitio distinto.

- **Nada va centrado.** Los encabezados son asimétricos: número al margen,
  titular a la izquierda, descripción a la derecha, y una línea fina arriba.
  La clase es `.head`, con `.head__n`, `.head__t` y `.head__d`.
- **Las secciones van numeradas** (01 a 07), en cursiva serif. Es lo que le da
  el aire de índice de revista.
- **Un solo momento de letra grande.** El bloque `.claim` es el único sitio
  donde la tipografía grita, con las fotografías engarzadas dentro de la
  frase. El resto de la página es discreto a propósito: si todo grita, no
  destaca nada.
- **Las tarjetas no miden todas igual.** Los tres pilares van escalonados
  (`.pillars--stagger`) y las de la fila alternan altura.

### El trato de las fotografías

Las fotografías tienen dos papeles y se distinguen a simple vista:

- **A color** las que enseñan el trabajo: los tres pilares, la carta de
  tratamientos y el antes/después. Son la prueba.
- **En monocromo cálido** las de ambiente: el estudio, el material, las manos,
  los óvalos del titular y el fondo del cierre. Llevan la clase `.tone`, y al
  pasar el ratón por encima recuperan el color.

Así el color deja de ser ruido y pasa a significar algo: donde hay color, hay
resultado. Es lo que unifica un material fotográfico desigual mientras no
llegue la sesión profesional.

El fondo tampoco es plano: hay un grano muy fino sobre toda la página
(`body::after`). No se ve, se nota — quita el aire de pantalla.

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

- **La fila de tratamientos se arrastra** con el ratón (en táctil ya lo hace
  el navegador) y una barra debajo dice por dónde vas. Se sale del contenedor
  por los dos lados a propósito: la fila muere en el borde de la pantalla.
- **En el método, la columna izquierda se queda quieta** mientras los cuatro
  pasos suben, y se enciende el que estás leyendo.
- **La franja de marca sigue al desplazamiento**: al bajar acelera, al subir
  va hacia el otro lado, y parada vuelve a su velocidad de crucero.
- **El comparador de antes y después** es un `input` de rango invisible sobre
  la fotografía, así que funciona con ratón, con el dedo y con el teclado.
- **El titular grande entra palabra a palabra**, subiendo desde su propia
  línea. El JavaScript parte solo los nodos de texto, así que las fotografías
  engarzadas en la frase y la cursiva se quedan como están.
- **Una línea fina arriba** dice cuánto queda de página.
- **La fotografía de portada se aleja** despacio mientras se baja.
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
