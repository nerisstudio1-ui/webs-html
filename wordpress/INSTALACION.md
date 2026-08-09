# Pegar la web en WordPress como bloque de HTML

Hay dos caminos. Los dos dan la misma web; cambia dónde viven las fotos.

## A. Copiar y pegar, sin FTP

**`widget-ca-copiar-pegar.html` · `widget-es-copiar-pegar.html` — 5,7 MB**

Las tipografías, las 31 fotos y las imágenes de espera de los vídeos van **dentro
del archivo**. Se abre, se copia todo y se pega. No hay que subir ninguna carpeta.

Lo único que queda fuera son los cuatro `.mp4`, porque 34 MB de vídeo dentro de
una entrada de WordPress no es viable. Se suben por **Medios → Añadir nuevo** —el
panel de siempre, sin FTP— y se pegan sus cuatro URL en el archivo, buscando:

```
__VIDEO_quality-1__      __VIDEO_malhivern-1__
__VIDEO_jordi-coll-1__   __VIDEO_puig-1__
```

Si no los sustituyes, la web funciona igual: en lugar del vídeo se queda su
imagen de espera, que es un fotograma del propio reel. No se ve roto.

**Lo que cuesta:** esos 5,7 MB se guardan en la base de datos, así que el editor
de WordPress va lento al abrir y guardar esa página. Y el navegador no puede
cachear las fotos por separado: cada visita se las baja otra vez.

## B. Con la carpeta subida, mucho más ligero

**`widget-ca.html` · `widget-es.html` — 158 KB**

Lo mismo, pero las fotos y las tipografías se cargan como archivos aparte. Pesa
40 veces menos en la base de datos y el navegador las cachea, así que la segunda
visita es casi instantánea. A cambio hay que subir la carpeta `assets` por FTP o
por el gestor de archivos del hosting.

**Empieza por A para tenerlo publicado, y pásate a B cuando tengas acceso al
FTP.** Cambiar de uno a otro es sustituir el contenido del bloque.

---

# A. Copiar y pegar

1. Abre `widget-ca-copiar-pegar.html` en un editor de texto (Notepad, TextEdit,
   VS Code… no en Word).
2. `Ctrl+A`, `Ctrl+C`.
3. En WordPress: **Páginas → Añadir nueva**, bloque **HTML personalizado** (el de
   las comillas `</>`), y pega.
4. Publica. Ya se ve la web.
5. Para los vídeos: **Medios → Añadir nuevo**, sube los cuatro `.mp4`, copia la
   URL de cada uno y sustituye su marcador en el bloque.

El enlace de idioma apunta a `/es/` en el archivo catalán y a `/` en el
castellano. Si tus páginas acaban en otra dirección, cambia ese enlace: sale tres
veces en cada archivo.

Sigue en el apartado **«Ajusta la cabecera»** si tu tema tiene cabecera fija.

---

# B. Con la carpeta subida

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

Si se cambia un texto o una foto en la web, los archivos de esta carpeta se
vuelven a generar con:

```bash
python3 build/build.py          # las dos webs, catalán y castellano
python3 build/build_widget.py   # los cuatro archivos de esta carpeta
```
