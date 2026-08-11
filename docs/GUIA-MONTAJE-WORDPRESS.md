# Montaje del sitio Blomstra en WordPress + Elementor

Guía de la instalación limpia hasta tener el diseño puesto. Los pasos 1–3 se
pueden hacer ya; el 4 depende de recibir los frames del diseño (ver
[INTAKE-DISENO.md](./INTAKE-DISENO.md)).

> **Este proyecto va con Elementor gratuito.** Eso condiciona bastante el
> montaje y está resuelto abajo, en la sección "Las tres limitaciones del
> gratuito". Si en algún momento aparece una licencia Pro, varios de esos
> rodeos se pueden eliminar.

---

## 1. Base de WordPress

| Pieza | Cuál | Por qué |
|---|---|---|
| Tema padre | **Hello Elementor** | Tema oficial, sin estilos propios que estorben. |
| Tema activo | **Blomstra Child** | Está en `wordpress/themes/blomstra-child/`. |
| Constructor | **Elementor** (gratuito) | El maquetado. |
| Header/footer | **Elementor Header & Footer Builder** | Gratuito, de Brainstorm Force. Sustituye al Theme Builder de Pro. |
| Formularios | **Fluent Forms Lite** o **WPForms Lite** | Elementor gratuito no trae widget de formulario. |

Instalación del tema hijo:

1. Instala y activa **Hello Elementor** desde Apariencia → Temas.
2. Comprime la carpeta `wordpress/themes/blomstra-child/` en un `.zip`.
3. Apariencia → Temas → Añadir nuevo → Subir tema → sube el zip → **Activar**.

> Se activa el tema **hijo**, no Hello Elementor. Hello queda de padre.
> El hijo ya declara `add_theme_support('header-footer-elementor')`, que es lo
> que necesita el plugin de header/footer para poder reemplazarlos.

---

## 2. Ajustes previos de Elementor

Elementor → Ajustes:

- **General → Deshabilitar los colores por defecto**: activado.
- **General → Deshabilitar las fuentes por defecto**: activado.
  (Así los estilos del tema no pisan a los del kit.)
- **Funciones → Contenedor Flexbox**: activado. Todo el maquetado usa
  contenedores flex, no las secciones antiguas.

Ajustes → Enlaces permanentes → **Nombre de la entrada**.

---

## 3. Importar el kit de estilos globales

El kit lleva la paleta, la tipografía y los estilos de botón como **globales**,
de forma que un cambio de color se propaga a todo el sitio en vez de tener que
tocar widget por widget. La importación de ajustes del sitio **sí funciona en
Elementor gratuito**.

```bash
./tools/build-kit.sh
# genera dist/blomstra-kit.zip
```

En WordPress: **Elementor → Herramientas → Importar/Exportar kit → Importar kit**
y sube `dist/blomstra-kit.zip`.

> Los valores actuales de `elementor-kit/site-settings.json` son **placeholders**
> marcados como tal. No son los colores del diseño: se sustituyen cuando lleguen
> los frames.

---

## 4. Las tres limitaciones del gratuito, y cómo se resuelven

### 4.1 No hay Theme Builder → header y footer

Sin Pro no se pueden crear plantillas de header/footer con condiciones de
visualización. La solución es el plugin **Elementor Header & Footer Builder**
(slug `header-footer-elementor`), que añade un tipo de contenido propio:

1. Apariencia → **Header Footer Builder** → Añadir nuevo.
2. Tipo de plantilla: **Header** (o Footer), Mostrar en: **Todo el sitio**.
3. Editar con Elementor y maquetar.

El plugin aporta además los widgets que faltan para un header: **Navigation
Menu**, **Site Logo**, **Site Title**, **Search**, **Copyright**. El menú se
gestiona desde Apariencia → Menús, en la posición `main` que registra el tema
hijo.

**Header sticky:** también es de Pro. Se resuelve con CSS en el tema hijo
(`position: sticky; top: 0; z-index: 100;` sobre el contenedor del header).
Lo añado cuando maquete el header.

### 4.2 No hay widget de formulario

Por el diseño se ven **dos páginas de formulario largo** y un **flujo tipo
cuestionario por pasos** (las pantallas "01 / 02 / Identidad visual" con lista
de secciones y campos de opción). Eso es bastante formulario, y Elementor
gratuito no trae ninguno.

Recomendación: **Fluent Forms Lite**. En la versión gratuita ya trae pasos
múltiples (multi-step), campos condicionales y buena maquetación, que es
exactamente lo que pide ese flujo. WPForms Lite es más simple pero deja el
multi-step para la versión de pago.

El formulario se construye en el plugin y se inserta en la página con su
shortcode dentro de un widget de Elementor. El estilo visual se ajusta con CSS
en el tema hijo para que case con el diseño.

### 4.3 No hay popups ni plantillas de entrada única

Si el diseño los necesita, lo vemos al revisar los frames. Los popups no tienen
buen equivalente gratuito; las plantillas de entrada/archivo se resuelven con
los `single.php` / `archive.php` del tema hijo.

---

## 5. Maquetado de las páginas

Pendiente de los frames. El plan es:

1. **Traducir cada frame a contenedores.** Cada sección del diseño pasa a ser un
   contenedor flex de nivel raíz con su ancho, padding y fondo.
2. **Header y footer** con Header Footer Builder (4.1).
3. **Home y páginas interiores** como páginas de WordPress con plantilla
   *Elementor Full Width* o *Canvas*.
4. **Formularios** en Fluent Forms, insertados por shortcode (4.2).
5. **Responsive**: revisar en 1024 px y 767 px, los breakpoints del kit.
6. Exportar todo a `elementor-kit/content/` para que quede versionado y
   reinstalable.

---

## Qué hace el repo y qué no

Este repositorio **no es un WordPress funcionando**. Es el material de origen:

```
wordpress/themes/blomstra-child/   Tema hijo, para subir a Apariencia > Temas
elementor-kit/                     Kit de Elementor, se empaqueta con tools/build-kit.sh
docs/                              Esta guía y el intake de diseño
design-input/                      Aquí van los exports de Figma
dist/                              Salida generada (no se versiona)
```

Para verlo funcionando hace falta un WordPress —local (LocalWP, XAMPP) o en
hosting— donde importar estas piezas.
