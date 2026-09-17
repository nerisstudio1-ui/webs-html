# Empaquetado

`empaquetar.py` genera las dos versiones de un solo archivo que hay en
`dist/`. Se ejecuta desde la raíz del proyecto:

```bash
python3 build/empaquetar.py                              # con ruta de ejemplo
python3 build/empaquetar.py https://midominio.com/media/ # con la ruta real
```

El argumento es la dirección desde la que se servirán las imágenes y los
vídeos, que no se pueden empotrar en el archivo (pesan demasiado). Si no se
pasa ninguno, queda un marcador de posición que hay que sustituir a mano.

## Qué genera

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

Ver `docs/WORDPRESS.md` para el procedimiento de subida.
