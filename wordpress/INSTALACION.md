# Pegar la web en WordPress como bloque de HTML

En esta carpeta hay cuatro archivos:

| Archivo | Qué es | Peso |
| --- | --- | --- |
| `widget-ca.html` | Catalán. Tipografías, fotos y vídeos por URL. | 158 KB |
| `widget-es.html` | Castellano, igual. | 158 KB |
| `widget-ca-autocontenido.html` | Catalán con las fotos y las tipografías dentro. | 5,4 MB |
| `widget-es-autocontenido.html` | Castellano, ídem. | 5,4 MB |

**Usa los de 158 KB.** Los autocontenidos meten 5,4 MB de texto en la base de
datos, el editor de WordPress se vuelve lento y el navegador no puede cachear las
fotos, así que la página carga peor en cada visita.

> **Y con vídeos da igual cuál elijas**: los reels nunca van dentro del archivo,
> ni en la versión autocontenida. Se sirven siempre por URL, así que hay que
> subir la carpeta `assets` y sustituir `__BASE__` en los dos casos. Es decir: la
> versión autocontenida ya no te ahorra el FTP. Usa la de 158 KB.

---

## Opción recomendada (`widget-ca.html` / `widget-es.html`)

### 1. Sube la carpeta `assets`

Por FTP o desde el gestor de archivos del hosting, sube la carpeta `assets/`
completa a:

```
/wp-content/uploads/laconic/assets/
```

Debe quedar así: `/wp-content/uploads/laconic/assets/css/`, `.../fonts/`,
`.../img/`, `.../js/`, `.../video/`. Son **91 archivos y unos 45 MB**, de los que
34 MB son los cuatro reels.

La carpeta se saca del repositorio: en GitHub, botón verde **Code → Download ZIP**
con la rama `claude/cs-creative-studio-website-6q44im` seleccionada, y de dentro
del ZIP solo hace falta `assets/`.

> No la subas desde la Biblioteca de medios: WordPress renombra los archivos y
> rompe las rutas. Tiene que ser por FTP o gestor de archivos.

> Si el hosting limita el peso por archivo, `malhivern-1.mp4` (12,9 MB) es el más
> grande. Los cuatro vídeos se pueden subir también a la Biblioteca de medios y
> pegar sus URL a mano en el HTML, buscando `assets/video/`.

### 2. Prepara el archivo

Abre `widget-ca.html` en un editor de texto y sustituye:

- `__BASE__` → `https://TUDOMINIO.com/wp-content/uploads/laconic/`
  (sale 94 veces; usa **reemplazar todo**. Ojo: **con la barra final.**)
- `__URL_ES__` → la URL de la página en castellano, por ejemplo
  `https://TUDOMINIO.com/es/`

En `widget-es.html` es lo mismo, pero el segundo marcador es `__URL_CA__`.

### 3. Crea la página en WordPress

1. **Páginas → Añadir nueva.**
2. Elige, si tu tema lo tiene, una plantilla **a ancho completo** o **sin
   título** (en Elementor: plantilla *Canvas*). No es imprescindible, pero queda
   mejor sin el título de la página encima.
3. Añade un bloque **HTML personalizado** (el de las comillas `</>`).
4. Pega **todo** el contenido del archivo.
5. Publica.

Repite con la versión en castellano en otra página (`/es/`).

### 4. Ajusta la cabecera (importante)

Si tu tema tiene cabecera **fija o pegada** arriba, dile al bloque su altura
para que nuestra cabecera y el hero queden justo debajo. En el archivo, busca:

```css
  --lac-top: 0px;
```

y pon la altura real, por ejemplo `--lac-top: 78px;`.

Si prefieres que nuestra cabecera no se quede pegada, cambia en el mismo archivo:

```css
#laconic-app .header { position: sticky;  →  position: static;
```

---

## Opción rápida (`*-autocontenido.html`)

Las fotos y las tipografías van dentro, así que sin tocar nada ya se ve casi todo:
solo hay que cambiar `__URL_ES__` o `__URL_CA__` por la URL de la otra página.

Lo que **no** funciona sin subir la carpeta es el bloque de trabajo: los cuatro
reels y sus imágenes de espera se sirven por URL, así que saldrán en blanco hasta
que subas `assets/` y sustituyas `__BASE__`. Sirve para enseñar el diseño; para
publicar, la de 158 KB.

---

## Qué hace el archivo para no pelearse con tu tema

Un tema y una web entera usan los mismos nombres (`.card`, `.section`, `.btn`,
`body`…), así que se pisarían. El archivo está preparado para evitarlo:

- Todo va dentro de `<div id="laconic-app">` y **cada** regla de CSS lleva ese
  identificador delante. Nuestras reglas ganan a las del tema por especificidad,
  y no salen del contenedor: el resto de tu web no se toca.
- El contenedor arranca con su propio reinicio, porque cualquier propiedad que el
  tema declare y nosotros no (fondos, bordes, subrayados, viñetas) se colaría.
- Los identificadores de las secciones van con el prefijo `lac-`.
- El bloque sale a todo el ancho de la ventana, aunque tu tema meta el contenido
  en una columna estrecha.
- El JavaScript solo mira dentro del contenedor y no toca nada de la página.

## Si algo no sale bien

| Síntoma | Causa y arreglo |
| --- | --- |
| No se ven las tipografías ni las fotos | `__BASE__` mal puesto. Comprueba que abre en el navegador `TUDOMINIO/wp-content/uploads/laconic/assets/css/main.css`. |
| El logo del hero no se queda quieto al bajar | Algún contenedor del tema tiene `overflow: hidden`, y eso rompe el `position: sticky`. Usa una plantilla a ancho completo o quita ese `overflow` para esa página. |
| La cabecera del tema tapa la nuestra | Pon la altura en `--lac-top`, como se explica arriba. |
| Aparece barra de scroll horizontal | Añade al final del `<style>`: `#laconic-app { overflow-x: clip; }` (ya viene puesto; si tu tema lo pisa, repítelo con `!important`). |
| Sale el título de la página encima | Cambia la plantilla de la página a una a ancho completo o sin título. |
| Los vídeos salen en negro o no arrancan | Comprueba que abre en el navegador `TUDOMINIO/wp-content/uploads/laconic/assets/video/quality-1.mp4`. Si da 404, faltan por subir; si da error de permisos, el hosting bloquea `.mp4` en `uploads` y hay que subirlos por la Biblioteca de medios. |
| Los vídeos tardan en empezar | Normal la primera vez. No se descargan hasta que el reel entra en pantalla, y el archivo está preparado para empezar sin bajarse entero. |

## Regenerar los archivos

Si se cambia un texto o una foto en la web, estos cuatro archivos se vuelven a
generar con:

```bash
python3 build/build.py          # las dos webs, catalán y castellano
python3 build/build_widget.py   # los cuatro archivos de esta carpeta
```
