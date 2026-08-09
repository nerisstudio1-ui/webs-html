# Pegar la web en WordPress como bloque de HTML

Hay dos caminos. Los dos dan la misma web; cambia dónde viven las fotos.

## A. Copiar y pegar, sin FTP

**`widget-ca-copiar-pegar.html` · `widget-es-copiar-pegar.html` — 6 MB**

Las tipografías, las 31 fotos y las imágenes de espera de los vídeos van **dentro
del archivo**. Se abre, se copia todo y se pega. No hay que subir ninguna carpeta.

Lo único que queda fuera son los cuatro `.mp4`, porque 34 MB de vídeo dentro de
una entrada de WordPress no es viable: el archivo ya apunta a los cuatro reels
que están subidos en la Biblioteca de medios, en
`/wp-content/uploads/2026/08/`. No hay que sustituir nada. Si algún día se
vuelven a subir y cambian de nombre, sus direcciones están en
`VIDEOS_WORDPRESS`, en `build/build_widget.py`.

**Lo que cuesta:** esos 6 MB se guardan en la base de datos, así que el editor
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
5. Haz el paso de **«Confirma el correo del formulario»**, aquí abajo. Es una vez
   y sin él los mensajes no llegan.

6. **Vacía la caché.** Ver «Si en el editor se ve y en la web no» más abajo. Sin
   esto la web pública puede seguir mostrando la versión anterior durante horas.

Sigue en el apartado **«Ajusta la cabecera»** si tu tema tiene cabecera fija.

---

# Las dos páginas y el enlace de idioma

Los archivos ya llevan puesto el enlace a la otra lengua, y esperan esta
estructura:

| Página | Dirección que espera el archivo | Cómo se monta en WordPress |
| --- | --- | --- |
| Catalán | `https://tudominio.com/` | **Ajustes → Lectura → Tu página de inicio es: una página estática → Página de inicio:** la página en catalán |
| Castellano | `https://tudominio.com/es/` | Una página normal con el **slug** `es` (el campo *Enlace permanente* de la página) |

Es decir: el catalán es la portada del sitio, y el castellano es una página cuyo
enlace permanente acaba en `/es/`. Si lo montas así, los tres enlaces `CA / ES`
funcionan sin tocar nada.

**Si prefieres otra dirección** —`/castellano/`, `/es-es/`, un subdominio— se
cambia con un buscar y reemplazar en el archivo, antes de pegarlo:

- en el archivo **catalán**: `href="/es/"` → tu dirección (sale **3 veces**)
- en el archivo **castellano**: `href="/"` → la dirección de la catalana (**3 veces**)

Las direcciones pueden ir completas (`https://tudominio.com/castellano/`) o desde
la raíz (`/castellano/`). Desde la raíz es mejor: así siguen funcionando cuando el
sitio cambie de dominio.

---

# Si en el editor se ve y en la web no

Este es el fallo más habitual y **no es del archivo**: el editor de WordPress te
muestra lo que acabas de guardar, mientras la web pública sirve una **copia
guardada (caché)** de antes. Se nota porque falta algo que sí está en el editor
—el crédito del pie, los vídeos, un texto nuevo— y a menudo se ve distinto en el
móvil que en el ordenador, porque cada uno tiene su propia copia.

**Comprobarlo en diez segundos:** abre tu web añadiendo algo al final de la
dirección, por ejemplo `https://tudominio.com/?x=1`. Con eso casi ninguna caché
responde, así que si **así sí se ve bien**, el archivo está perfecto y lo único que
falta es vaciar la caché.

**Vaciarla, por este orden:**

1. **En el hosting.** En Hostinger: **hPanel → Rendimiento → Caché** (o *Optimización
   del sitio web*) → **Vaciar caché**. Es la que más manda.
2. **En WordPress**, si tienes un plugin de caché (LiteSpeed Cache, WP Rocket,
   W3 Total Cache, WP Super Cache): en su menú, **Purgar todo / Vaciar toda la
   caché**.
3. **En Elementor:** **Elementor → Herramientas → Regenerar CSS y datos**, y en la
   misma pantalla **Sincronizar biblioteca**.
4. **En tu navegador:** `Ctrl+Shift+R` (Mac: `Cmd+Shift+R`), o ábrela en una
   ventana privada. En el móvil, ventana de incógnito.
5. **Si hay Cloudflare** delante del dominio: **Caching → Configuration →
   Purge Everything**.

**Para saber qué versión está publicada de verdad:** en la web pública, `Ctrl+U`
(ver código fuente) y busca `Generado`. Sale la fecha y la hora del archivo que
está sirviendo. Si no coincide con la del archivo que pegaste, es caché.

> Mientras trabajes en la web, lo cómodo es dejar la caché desactivada en el
> hosting y activarla al terminar.

---

# Confirma el correo del formulario (una sola vez)

Los mensajes del formulario llegan a **itslaconicstudio@gmail.com** a través de
FormSubmit, que no necesita cuenta, clave ni plugin. Solo pide confirmar, una vez,
que esa dirección acepta recibirlos. Y solo se puede hacer con la web publicada.

1. Abre la página publicada y ve a **Contacto**.
2. Rellena el formulario con cualquier cosa —«prueba» en todos los campos vale— y
   envíalo.
3. En la bandeja de **itslaconicstudio@gmail.com** llega un correo de FormSubmit
   con un enlace de activación. Púlsalo. Si no aparece, mira en **Spam**.
4. Envía el formulario otra vez. Ese segundo mensaje ya tiene que llegar a la
   bandeja, con el asunto *Nuevo mensaje desde la web*.

Hazlo en la página en catalán **y** en la castellana solo si están en dominios
distintos; si comparten dominio, con una vez basta.

Cuando funciona, el visitante no sale de la página: el botón se apaga un momento y
debajo aparece «Recibido. Te respondemos en menos de 48 horas laborables». Si el
servicio se cae, el aviso cambia y da el correo del estudio para escribir a mano,
así que ningún mensaje se pierde en silencio.

> Para cambiar la dirección de destino, se edita `EMAIL` en `build/build.py` y se
> vuelve a generar. La confirmación hay que repetirla con la dirección nueva.

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
- Las entradas al hacer scroll llevan red de seguridad: si un plugin de caché
  rompiera el guion, en lugar de quedarse media web escondida se muestra todo, sin
  animaciones. Y los vídeos arrancan por su cuenta, sin depender del guion.

## Si algo no sale bien

| Síntoma | Causa y arreglo |
| --- | --- |
| No se ven las tipografías ni las fotos | `__BASE__` mal puesto. Comprueba que abre en el navegador `TUDOMINIO/wp-content/uploads/laconic/assets/css/main.css`. |
| El logo del hero no se queda quieto al bajar | Algún contenedor del tema tiene `overflow: hidden`, y eso rompe el `position: sticky`. Usa una plantilla a ancho completo o quita ese `overflow` para esa página. |
| La cabecera del tema tapa la nuestra | Pon la altura en `--lac-top`, como se explica arriba. |
| Aparece barra de scroll horizontal | Añade al final del `<style>`: `#laconic-app { overflow-x: clip; }` (ya viene puesto; si tu tema lo pisa, repítelo con `!important`). |
| Sale el título de la página encima | Cambia la plantilla de la página a una a ancho completo o sin título. |
| Falta algo que en el editor sí se ve | Caché. Ver «Si en el editor se ve y en la web no». |
| Los vídeos salen en negro o no arrancan | Comprueba que abre en el navegador `TUDOMINIO/wp-content/uploads/laconic/assets/video/quality-1.mp4`. Si da 404, faltan por subir; si da error de permisos, el hosting bloquea `.mp4` en `uploads` y hay que subirlos por la Biblioteca de medios. |
| Se ve la foto de espera del reel y no arranca | Primero, caché. Si con `?x=1` tampoco arranca: los vídeos llevan `autoplay muted playsinline`, así que empiezan solos sin depender de nuestro guion. Si aun así no lo hacen, el navegador lo está impidiendo (móvil en **ahorro de batería** o **ahorro de datos**): aparece el círculo de play y basta con tocar el vídeo. Si un plugin de **carga diferida (lazy load)** los toca a pesar de `skip-lazy`, quítalos de su lista de excepciones o desactiva la carga diferida de vídeos. |
| El formulario dice «Recibido» pero no llega nada | Falta el paso de confirmación de FormSubmit, o el correo de activación está en Spam. Repite «Confirma el correo del formulario». |
| El formulario dice «No hemos podido enviarlo» | El servicio no contesta. Comprueba que abre en el navegador `https://formsubmit.co`; si está caído, se recupera solo. Mientras tanto, el aviso da el correo del estudio. |
| Los vídeos tardan en empezar | Normal la primera vez. No se descargan hasta que el reel entra en pantalla, y el archivo está preparado para empezar sin bajarse entero. |

## Regenerar los archivos

Si se cambia un texto o una foto en la web, los archivos de esta carpeta se
vuelven a generar con:

```bash
python3 build/build.py          # las dos webs, catalán y castellano
python3 build/build_widget.py   # los cuatro archivos de esta carpeta
```
