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

1. **Apariencia → Header Footer Builder → Añadir nuevo**.
2. Tipo de plantilla: **Header**. Mostrar en: **Todo el sitio**. Publica.
3. Edita con Elementor y monta el header: el logo (widget Imagen), y el widget
   **Navigation Menu** que aporta este plugin.
4. En ese widget, Layout → **Dropdown**, para que salga como hamburguesa igual
   que en tu diseño. Ahí eliges también el menú `Principal` y el color y la
   tipografía.

### Paso 4 — Quitar el header duplicado de la home

La plantilla de la home lleva un header dentro, que puse solo para poder
previsualizarla suelta. Una vez tengas el header del sitio funcionando, **abre
la home en Elementor y borra ese contenedor**, o te saldrán dos.

Es el primer contenedor de la página: el que tiene el icono de hamburguesa, el
logotipo y el botón WHATS.

---

## Resumen de lo que necesito de ti

| Qué | Para qué |
|---|---|
| Los SVG del logotipo, en sus versiones clara y oscura | Que el logo sea el tuyo |
| El nombre exacto de las dos tipografías | Saber si son de pago y cómo conseguirlas |
| Los archivos de fuente, si ya los tienes | Dejarlas instaladas |
| Qué páginas van en el menú y en qué orden | Montar la navegación |
