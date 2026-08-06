# Pegar la web en WordPress como bloque de HTML

En esta carpeta hay cuatro archivos:

| Archivo | Qué es | Peso |
| --- | --- | --- |
| `widget-ca.html` | Catalán. Las tipografías y las fotos se cargan por URL. | 130 KB |
| `widget-es.html` | Castellano, igual. | 130 KB |
| `widget-ca-autocontenido.html` | Catalán con todo dentro (nada que subir). | 2,9 MB |
| `widget-es-autocontenido.html` | Castellano, ídem. | 2,9 MB |

**Usa los de 130 KB.** Los autocontenidos sirven para una prueba rápida, pero
meten 2,9 MB de texto en la base de datos y el editor de WordPress se vuelve
lento; además el navegador no puede cachear las fotos, así que la página carga
peor cada vez.

> **Con vídeos**: los reels nunca van dentro del archivo, ni en la versión
> autocontenida. Se sirven siempre por URL, así que si hay vídeos hay que subir
> la carpeta `assets` igualmente y sustituir `__BASE__` también en la versión
> autocontenida.

---

## Opción recomendada (`widget-ca.html` / `widget-es.html`)

### 1. Sube la carpeta `assets`

Por FTP o desde el gestor de archivos del hosting, sube la carpeta `assets/`
completa a:

```
/wp-content/uploads/laconic/assets/
```

Debe quedar así: `/wp-content/uploads/laconic/assets/css/`, `.../fonts/`,
`.../img/`, `.../js/`.

> No la subas desde la Biblioteca de medios: WordPress renombra los archivos y
> rompe las rutas. Tiene que ser por FTP o gestor de archivos.

### 2. Prepara el archivo

Abre `widget-ca.html` en un editor de texto y sustituye:

- `__BASE__` → `https://TUDOMINIO.com/wp-content/uploads/laconic/`
  (sale 59 veces; usa **reemplazar todo**. Ojo: **con la barra final.**)
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

No hay que subir nada: se pega y funciona. Solo hay que cambiar `__URL_ES__` o
`__URL_CA__` por la URL de la otra página. Ojo con lo del peso que se explica
arriba: úsalo para enseñarlo, no para dejarlo publicado.

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

## Regenerar los archivos

Si se cambia un texto o una foto en la web, estos cuatro archivos se vuelven a
generar con:

```bash
python3 build/build.py          # las dos webs, catalán y castellano
python3 build/build_widget.py   # los cuatro archivos de esta carpeta
```
