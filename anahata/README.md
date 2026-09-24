# ANAHATA · Web de Sara Viñas Gómez

Web corporativa estática (HTML + CSS + JS, sin dependencias ni framework).
Diseño minimalista y cercano, con la paleta tomada del logotipo: verde bosque, oro y cremas.

---

## ⚠️ Pendiente de confirmar con Sara

> Teléfono confirmado por Sara el 24/09: **664 60 74 64** (coincide con el rótulo del estudio).

1. **Fotografías.** Ya hay **6 huecos con fotos reales** de Sara (pilates, grupos, retiro y alimentación),
   procesadas desde `assets/img/originales/` con `_fotos.py`. **Siguen con marcador provisional**:
   las seis portadas (`hero-*`), `sobre-retrato`, `sobre-detalle`, `pilar-meditacion`,
   `servicio-meditacion`, `programa-membresia`, `programa-reto21`, `programa-privadas`,
   los cuatro `evento-*` y `cta-banner`. Lo más urgente es **una foto horizontal para la portada**
   y **un retrato vertical de Sara**.

2. **Vídeo.** `assets/video-original-yoga-brunch.mp4` (20 MB, H.264) está guardado pero **sin usar**:
   es demasiado largo y pesado para la portada, y este entorno no puede recortarlo ni recomprimirlo
   (el ffmpeg disponible no decodifica H.264). Hace falta una versión de **10-15 segundos, sin audio,
   1920×1080 y por debajo de 5 MB**. El CSS ya soporta vídeo de fondo en el hero (`.hero__media video`).
3. **Hosting.** Sara pide que lo gestionemos nosotras. El dominio está en **Hostinet** y la web
   anterior era un WordPress al que ya no puede acceder. Pendiente de contratar alojamiento y de
   añadir el nombre del proveedor a las páginas legales.
4. **Logotipo.** El logo se ha **vectorizado a SVG** a partir de la imagen enviada.
   Si Sara tiene el archivo original (AI, SVG o PNG con fondo transparente), sustituirlo mejora la fidelidad.
5. **Datos legales.** NIF y domicilio ya están puestos. Falta únicamente el **proveedor de hosting**
   en ambas páginas legales.
6. **Formulario.** Los mensajes deben llegar a **saravgyoga@gmail.com**. Todavía no está conectado
   a ningún servicio de envío. Ver «Conectar el formulario».

---

## Estructura

```
anahata/
├── landing.html          Landing de una página (todo en scroll)
├── index.html            Inicio de la web corporativa
├── sobre-mi.html         Sobre mí · trayectoria y origen de ANAHATA
├── servicios.html        Yoga (4 estilos), Pilates, Meditación, Alimentación
├── clases.html           Clases y programas + preguntas frecuentes
├── retiros.html          Retiros, eventos y talleres
├── contacto.html         Formulario, WhatsApp y datos de contacto
├── aviso-legal.html      Aviso legal
├── privacidad.html       Política de privacidad y cookies
├── assets/
│   ├── css/style.css     Toda la hoja de estilos
│   ├── js/main.js        Menú, scroll, acordeón, carrusel, formularios
│   └── img/              Logotipos SVG + marcadores de imagen
├── _build.py             Generador de las páginas (textos y contenido)
└── _gen_logo.py          Generador de los SVG del logotipo
```

## Dos formatos en el mismo proyecto

El proyecto incluye **las dos versiones**, que comparten estilos, logotipo e imágenes:

- **`landing.html`** — una sola página con todo el contenido en scroll y navegación por anclas.
  Es la más directa para captar reservas y para enviar por Instagram o WhatsApp.
- **`index.html` + el resto** — web corporativa de 8 páginas, mejor para posicionamiento (cada
  servicio tiene su propia URL) y para ir ampliando contenido.

Para que la landing sea la página principal del dominio, basta con renombrar:

```bash
mv index.html corporativa.html && mv landing.html index.html
```

(y después ajustar los enlaces del menú, que en la corporativa apuntan a las páginas internas).
Si tienes dudas, dímelo y lo dejo montado en un minuto.

## Cómo editar

Las páginas comparten cabecera, pie y bloques comunes, así que **los textos se editan en `_build.py`**
y después se regeneran los HTML:

```bash
python3 _build.py      # regenera los 8 .html
python3 _gen_logo.py   # solo si se toca el logotipo
```

Los datos del negocio (teléfono, email, redes, ciudad, dominio) están agrupados al principio de `_build.py`,
en el bloque `DATOS DEL NEGOCIO`. Cambiar ahí un dato lo actualiza en todas las páginas.

> Si prefieres no usar Python, puedes editar los `.html` directamente: son ficheros estáticos normales.
> En ese caso, recuerda que un cambio en la cabecera o el pie hay que repetirlo en las 8 páginas.

## Procesar fotos nuevas

Los originales se guardan en `assets/img/originales/` y se recortan a cada hueco con:

```bash
python3 _fotos.py
```

Las asignaciones (origen → destino, tamaño y foco vertical del recorte) están en la lista
`TRABAJOS` del propio script. Ajustar el foco entre 0 (arriba) y 1 (abajo) sirve para que
no se corten las caras.

## Sustituir las imágenes

Cada marcador es un `.svg` dentro de `assets/img/`. Para poner las fotos reales:

1. Guarda la foto como `.jpg` con **el mismo nombre** del marcador (por ejemplo `hero-inicio.jpg`).
2. Busca y reemplaza la extensión en `_build.py` (`hero-inicio.svg` → `hero-inicio.jpg`) y regenera.

| Archivo | Dónde aparece | Formato recomendado |
|---|---|---|
| `hero-inicio` | Portada | horizontal, 1920×1280 |
| `hero-sobre-mi`, `hero-servicios`, `hero-clases`, `hero-retiros`, `hero-contacto` | Cabecera de cada página | horizontal, 1920×900 |
| `sobre-retrato` | Retrato de Sara (inicio y sobre mí) | vertical, 900×1200 |
| `sobre-detalle` | Sobre mí | horizontal, 1200×900 |
| `pilar-yoga`, `pilar-meditacion`, `pilar-programas` | Tres tarjetas de inicio | horizontal, 1200×900 |
| `servicio-pilates`, `servicio-meditacion` | Servicios | cuadrada, 1000×1000 |
| `programa-*` (4) | Clases y programas | horizontal, 1200×900 |
| `retiro-finde`, `evento-*` (4) | Retiros y eventos | horizontal, 1200×900 |
| `cta-banner` | Franjas de llamada a la acción | horizontal, 1920×900 |

**Optimiza siempre antes de subir**: JPG de calidad 80, máximo ~300 KB por imagen.
Las fotos de portada admiten hasta ~500 KB.

## Conectar el formulario

Ahora mismo, si alguien envía el formulario, se muestra un aviso pidiendo que escriba por correo o WhatsApp
(así no se pierde ningún mensaje). Para activarlo de verdad, la opción más sencilla es
[Formspree](https://formspree.io) (plan gratuito suficiente):

1. Crea una cuenta con `saravgyoga@gmail.com` y copia el ID del formulario.
2. En `_build.py`, en `pagina_contacto()`, añade el `action` y el `method` a la etiqueta `<form>`:

```html
<form class="formulario tarjeta-texto" data-formulario novalidate
      action="https://formspree.io/f/TU_ID" method="POST">
```

3. Haz lo mismo con los formularios de newsletter (o conéctalos a Mailchimp / MailerLite).
4. Regenera con `python3 _build.py` y prueba un envío real.

## Publicar

Es una web estática: basta con subir el contenido de esta carpeta por FTP a la raíz del hosting
(o a la carpeta `public_html`). No necesita base de datos ni PHP.

Antes de publicar:

- [ ] Completar los huecos de imagen que siguen con marcador
- [ ] Completar los datos de aviso legal y privacidad
- [ ] Conectar el formulario y probar un envío
- [ ] Cambiar `DOMINIO` en `_build.py` si el dominio final no es `www.saravgyoga.com`

## Detalles técnicos

- **Logotipo:** cuatro variantes en `assets/img/` — `logo-anahata.svg` (completo),
  `logo-anahata-crema.svg` (para fondos oscuros: pie y portada de la landing),
  `logo-simbolo.svg` (solo el símbolo) y `logo-marca.svg` (versión compacta de la cabecera),
  cada uno con su versión en crema donde hace falta.
- **Tipografías:** Cormorant Garamond (titulares) y Jost (texto), cargadas desde Google Fonts.
- **Accesibilidad:** navegación por teclado, textos alternativos, foco visible, enlace de salto al contenido
  y respeto por `prefers-reduced-motion`.
- **SEO:** títulos y descripciones por página, Open Graph, enlaces canónicos y datos estructurados
  `HealthAndBeautyBusiness` (schema.org) en la portada.
- **Cookies:** la web no usa cookies de analítica ni de publicidad. Solo guarda en el navegador si has
  cerrado el aviso superior. Si más adelante se añade Google Analytics o vídeos incrustados,
  habrá que poner un banner de consentimiento.
- **Navegadores:** probada en Chromium. Usa CSS Grid, `aspect-ratio` y `backdrop-filter`
  (compatible con todos los navegadores actuales).
