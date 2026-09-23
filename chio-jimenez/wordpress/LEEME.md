# Versión para WordPress

Dos archivos, según dónde vaya la web.

## `chio-jimenez-elementor-lienzo.html`  ← el habitual

Para una página con la plantilla **Elementor Lienzo**, que es una página en
blanco, sin cabecera ni pie del tema. La web va entera, con su menú y su
selector de idioma, igual que en la vista previa.

Pasos:

1. Edita la página con Elementor.
2. Engranaje abajo a la izquierda → **Plantilla de página: Elementor Lienzo**.
3. Arrastra el widget **HTML** a la página.
4. Pega dentro todo el contenido de este archivo y publica.

## `chio-jimenez-widget-sin-cabecera.html`

Para insertar la web dentro de una página que ya trae la cabecera de
WordPress. Se retira el menú propio, para no tener dos, y el selector de
idioma pasa a la portada.

## Las fotos

Las dos versiones leen las imágenes de la carpeta de Medios indicada en la
línea 11:

```js
window.CJ_IMAGENES = "https://orange-gull-246246.hostingersite.com/wp-content/uploads/2026/09/";
```

Las 38 imágenes de `assets/img/` tienen que estar subidas a Medios con su
nombre original. Si WordPress renombrara alguna (ocurre cuando ya existe un
archivo con ese nombre), esa foto no aparecería: hay que volver a subirla
con el nombre correcto.

Al cambiar de dominio, basta con editar esa línea.

## Regenerar estos archivos

Después de tocar la web hay que volver a generarlos:

```bash
cd chio-jimenez
python3 tools/generar-widget.py --con-cabecera -o wordpress/chio-jimenez-elementor-lienzo.html
python3 tools/generar-widget.py               -o wordpress/chio-jimenez-widget-sin-cabecera.html
```

Con `--base <url>` se cambia la carpeta de Medios sin editar nada a mano.

## Por qué no vale `index.html`

`index.html` es un documento completo: el CSS y el JavaScript están en
archivos aparte y las fotos van por rutas relativas. Al pegarlo en WordPress
solo sobrevive el cuerpo, así que la página sale sin estilos y sin fotos.
Estos dos archivos llevan el CSS y el JavaScript dentro, y las rutas de las
imágenes apuntan a Medios.
