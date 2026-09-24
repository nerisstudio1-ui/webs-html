# Generar lo que va a producción

## Empaquetado

`empaquetar.py` genera las dos versiones de un solo archivo que hay en
`dist/`. Se ejecuta desde la raíz del proyecto:

```bash
python3 build/empaquetar.py                              # con ruta de ejemplo
python3 build/empaquetar.py https://midominio.com/media/ # con la ruta real
```

El argumento es la dirección desde la que se servirán las imágenes y los
vídeos, que no se pueden empotrar en el archivo (pesan demasiado). Si no se
pasa ninguno, queda un marcador de posición que hay que sustituir a mano.

### Qué genera

| Archivo | Para qué |
|---|---|
| `dist/cristina-falcon-completa.html` | Verla sin servidor. Todo dentro menos los vídeos. |
| `dist/cristina-falcon-widget.html` | Pegar en un bloque HTML de WordPress. |

En la versión de widget, **todo el CSS se encierra bajo `#cfm-web`** para
que no toque los estilos del tema: `:root` y `body` pasan a ser el propio
contenedor, y cada selector se antepone. Se respetan las `@font-face` y las
`@keyframes`, que no llevan alcance, y se entra dentro de las `@media` para
acotar lo de dentro.

Se añaden además unos ajustes finales: la cabecera deja de ser fija (si no,
se sale del bloque) y la portada baja de pantalla completa.

## Los medios para WordPress

`medios.py` arma el zip que se sube a la biblioteca de medios. Hay que
correrlo **después** de `empaquetar.py`, porque saca la lista leyendo el
widget ya generado: así el zip nunca se desalinea del HTML.

```bash
python3 build/medios.py     # deja dist/medios-wordpress.zip
```

Sale plano, con el nombre exacto que el widget espera. Si algún medio no
aparece en `assets/` o hay dos archivos con el mismo nombre, avisa y no toca
el zip.

## Los PDF de descarga

`pdf/` tiene las dos páginas de las que salen `biografia.pdf` y
`dossier-prensa.pdf`. Se editan como HTML normal y se regeneran con:

```bash
node build/pdf/generar.js   # escribe en assets/docs/
```

Levanta su propio servidor sobre la raíz del proyecto para que las fuentes y
el logotipo resuelvan igual que en la web, e imprime en A4 con Chromium.
Después hay que volver a correr `empaquetar.py` y `medios.py`, que los
llevan a `dist/`.

Ver `docs/WORDPRESS.md` para el procedimiento de subida.
