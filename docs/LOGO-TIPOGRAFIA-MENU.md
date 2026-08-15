# Logo, tipografía y menú

Las tres cosas que quedan distintas al diseño en cuanto instalas la home, y qué
hacer con cada una.

---

## 1. El logo no es igual

**Por qué.** Tu logotipo es lettering hecho a mano: la B lleva un rasgo
ornamental y "Visual" / "Experiences" van en una caligráfica que no existe como
fuente web. En la plantilla está **reconstruido con dos widgets de Encabezado**
(Playfair Display + Pinyon Script) para que se viera algo mientras tanto. Nunca
va a coincidir así, porque no es una fuente: es un dibujo.

**La solución es sustituirlo por el SVG.** Un logo debe ir siempre como imagen
vectorial, no como texto: se ve nítido a cualquier tamaño y pesa poquísimo.

### Exportarlo de Figma

1. Selecciona el grupo del logotipo en el panel de capas.
2. Panel derecho → Export → formato **SVG** → Export.
3. Hazlo con cada versión: el de cabecera en blanco, el oscuro, y el de cada
   submarca (Visual/Brands, Experiences…).

### Permitir SVG en WordPress

WordPress bloquea los SVG por defecto, porque un SVG puede llevar código dentro.
Dos caminos:

- **Recomendado:** instala el plugin gratuito **Safe SVG**. Limpia el archivo al
  subirlo, así que puedes subir SVG sin riesgo.
- **Rápido:** Elementor → Ajustes → Avanzado → *Enable Unfiltered File Uploads*.
  Solo si los archivos son tuyos y salen de tu Figma.

### Cambiarlo en la plantilla

En la home, dentro del header:

1. Borra los dos widgets de Encabezado del logotipo (*This is* y *BLOMSTRA*).
2. Arrastra un widget **Imagen** en su lugar y sube el SVG.
3. Estilo → Ancho: unos 190 px en escritorio.

Lo mismo en las tarjetas de "Dos formas de habitar Blomstra" y en el wordmark
gigante del pie.

> Si prefieres no pelearte con SVG, un PNG a 3x con fondo transparente también
> vale. Se ve bien, solo pesa más.

---

## 2. La tipografía tampoco

**Por qué.** Las de tu diseño no son de Google Fonts. La de titulares es una
didone de contraste alto, y la caligráfica es otra fuente aparte. Puse
**Playfair Display**, **Pinyon Script** y **Montserrat** como sustitutas de
trabajo, y así está anotado en el código.

**Lo que necesito de ti:** los nombres reales. En Figma, selecciona un titular
y mira el panel derecho, sección Typography: ahí aparece el nombre exacto. Con
eso te digo si son de pago y de dónde sacarlas.

### Cuando tengas los archivos

El subidor de fuentes de Elementor es de pago, así que **te lo he resuelto en
el tema hijo**. Solo tienes que:

1. Dejar los archivos en `wp-content/themes/blomstra-child/assets/fonts/`,
   nombrados `familia-peso-estilo.woff2` — por ejemplo
   `blomstra-display-400-normal.woff2`.
2. Ya está. Aparecen en Elementor en un grupo llamado **Blomstra**, dentro del
   selector de tipografías.

Los detalles están en el README de esa carpeta.

### Cambiarlas de golpe

No vayas widget a widget. Elementor → menú hamburguesa (arriba a la izquierda)
→ **Ajustes del sitio** → **Tipografía**. Ahí cambias las cuatro tipografías
globales y se propaga a todo el sitio.

> Antes de comprar nada, comprueba que la licencia incluye **webfont**. Muchas
> licencias de escritorio no permiten usar la fuente en una web.

---

## 3. El menú no está enlazado

Aquí falta un paso que aún no habíamos dado. La hamburguesa de la plantilla es
un icono decorativo: no abre nada, porque **el menú de verdad no vive en la
página, vive en el header del sitio**.

Sin Elementor Pro no hay Theme Builder, así que el header se monta con un
plugin gratuito. Tres pasos:

### Paso 1 — Crear el menú

**Apariencia → Menús** → Crear menú nuevo → nómbralo `Principal`.

Añade las páginas (About, Services, Lookbook, Contact us…). Si aún no existen,
créalas vacías en Páginas → Añadir nueva; ya les pondremos contenido.

Abajo, en *Ajustes del menú*, marca la ubicación **Menú principal**. El tema
hijo ya tiene registradas dos ubicaciones, `Menú principal` y `Menú del pie`.

### Paso 2 — Instalar el constructor de header

Plugins → Añadir nuevo → busca **Elementor Header & Footer Builder** (de
Brainstorm Force) → Instalar → Activar.

### Paso 3 — Montar el header

Tienes el header ya hecho en `00-header.json`. No hay que maquetarlo.

1. **Plantillas → Plantillas guardadas → Importar plantillas** → sube
   `00-header.json`.
2. **Apariencia → Header Footer Builder → Añadir nuevo**.
   - Tipo de plantilla: **Header**
   - Mostrar en: **Todo el sitio**
   - Publica.
3. **Editar con Elementor** → icono de carpeta (Añadir plantilla) →
   *Mis plantillas* → inserta **Blomstra — Header**.

Trae la barra de aviso, el logotipo centrado, el selector de idioma y el botón
de WhatsApp, con los colores y la tipografía del diseño ya puestos.

### Paso 3 bis — Meter el menú de verdad

En el hueco de la izquierda hay un **icono de hamburguesa decorativo**. Va ahí
de relleno: el widget del menú pertenece al plugin, así que no puedo dejarlo
puesto desde fuera — si lo hiciera, la plantilla fallaría al importarla en una
instalación que no tenga el plugin activo.

Cambiarlo es un minuto:

1. Selecciona el icono de hamburguesa y **bórralo**.
2. En ese mismo contenedor (el de la izquierda, `bl-header__menu-slot`),
   arrastra el widget **Navigation Menu**.
3. Ajustes del widget:
   - **Menu**: `Principal`
   - **Layout**: `Dropdown` — así sale como hamburguesa, igual que el diseño
   - **Breakpoint**: `All devices`, para que sea hamburguesa también en escritorio
4. Estilo → Toggle Button → color **blanco**, para que case con el header.

### Cosas que querrás retocar

| Qué | Dónde |
|---|---|
| El número de WhatsApp | Botón WHATS → Enlace. Ahora apunta a `wa.me/34600000000` |
| El texto de la barra de aviso | Primer contenedor. Si no la quieres, bórralo |
| El logotipo | Los dos textos del centro, cuando tengas el SVG (ver arriba) |

> El header va sobre greige con el logotipo en blanco, que es como aparece en
> escritorio. En el portal en móvil tu diseño lo invierte a fondo crema con todo
> en oscuro; eso está pendiente de que confirmes si es intencionado
> (`docs/INCONSISTENCIAS.md`).

### Paso 4 — Quitar el header duplicado de la home

La plantilla de la home lleva dentro su propia barra de aviso y su propio
header, que puse solo para poder previsualizarla suelta. Una vez tengas el
header del sitio funcionando, **abre la home en Elementor y borra los dos
primeros contenedores**, o los verás repetidos:

1. El de la barra de aviso (la franja fina de arriba).
2. El del header (hamburguesa + logotipo + botón WHATS).

Se borran desde el **Navegador de Elementor** (`Ctrl/Cmd + I`), que es lo más
cómodo para no equivocarse de contenedor.

---

## Resumen de lo que necesito de ti

| Qué | Para qué |
|---|---|
| Los SVG del logotipo, en sus versiones clara y oscura | Que el logo sea el tuyo |
| El nombre exacto de las dos tipografías | Saber si son de pago y cómo conseguirlas |
| Los archivos de fuente, si ya los tienes | Dejarlas instaladas |
| Qué páginas van en el menú y en qué orden | Montar la navegación |
