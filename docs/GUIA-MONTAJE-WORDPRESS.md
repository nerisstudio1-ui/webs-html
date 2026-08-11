# Montaje del sitio Blomstra en WordPress + Elementor

Guía de la instalación limpia hasta tener el diseño puesto. Los pasos 1–3 se
pueden hacer ya; el 4 depende de que llegue el diseño (ver
[INTAKE-DISENO.md](./INTAKE-DISENO.md)).

---

## 1. Base de WordPress

Plugins y tema mínimos:

| Pieza | Cuál | Nota |
|---|---|---|
| Tema padre | **Hello Elementor** | Tema oficial, sin estilos propios que estorben. |
| Tema activo | **Blomstra Child** | Está en `wordpress/themes/blomstra-child/`. |
| Constructor | **Elementor** (gratuito) | Imprescindible. |
| Constructor | **Elementor Pro** | Necesario para header, footer y popups. Sin Pro, ver nota abajo. |

Instalación del tema hijo:

1. Instala y activa **Hello Elementor** desde Apariencia → Temas.
2. Comprime la carpeta `wordpress/themes/blomstra-child/` en un `.zip`.
3. Apariencia → Temas → Añadir nuevo → Subir tema → sube el zip → **Activar**.

> El tema hijo debe activarse él, no Hello Elementor. Hello queda de padre.

**Si no hay Elementor Pro:** el header y el footer no se pueden construir con
Elementor. Alternativas: montarlos con el plugin gratuito *ElementsKit Lite* /
*JetThemeCore*, o dejarlos en el tema hijo como `header.php` / `footer.php`.
Dime cuál prefieres antes de que lo maquete, porque cambia bastante el trabajo.

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
tocar widget por widget.

```bash
./tools/build-kit.sh
# genera dist/blomstra-kit.zip
```

En WordPress: **Elementor → Herramientas → Importar/Exportar kit → Importar kit**
y sube `dist/blomstra-kit.zip`.

> Los valores actuales de `elementor-kit/site-settings.json` son **placeholders**
> marcados como tal. No son los colores del diseño de Figma: los sustituyo en
> cuanto pueda ver el archivo.

---

## 4. Maquetado de las páginas

Pendiente del diseño. El plan de trabajo es:

1. **Traducir el Figma a estructura de contenedores.** Cada sección del diseño
   pasa a ser un contenedor flex de nivel raíz con su ancho, padding y fondo.
2. **Header y footer** como plantillas de Theme Builder, con condición
   "Todo el sitio".
3. **Home** y páginas interiores como plantillas de página.
4. **Responsive**: revisar en 1024 px y 767 px, que son los breakpoints
   configurados en el kit.
5. Exportar todo de vuelta a `elementor-kit/content/` para que quede
   versionado en el repo y sea reinstalable.

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
