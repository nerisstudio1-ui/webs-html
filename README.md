# Anuncio de vídeo — Neris Studio, webs a 299 €

Anuncio para Facebook hecho **en HTML**: una cinta de webs inclinadas en 3D
subiendo sobre un muro de tipografía gigante que repite `TU WEB / A 299 €`, y
un cierre con la oferta. Se exporta a MP4 listo para subir a Meta.

Duración 12 s · 30 fps · sin audio.

```
0,0 – 7,0 s   nueve webs pasan por la cinta (la prueba)
7,0 – 8,3 s   la cinta acelera y las saca de cuadro
7,0 – 8,9 s   la oferta entra como una tarjeta más y se endereza
8,9 – 12,0 s  cierre: 299 €, qué incluye y llamada a la acción
```

## Qué hay aquí

| Archivo | Para qué |
| --- | --- |
| `src/ad.html` | La página del anuncio. Ábrela en el navegador para previsualizar. |
| `src/ad.css` | Diseño y sistema de tokens. Arriba del todo está el plan de diseño. |
| `src/ad.js` | La línea de tiempo. Todo es función de `t`, no hay animaciones CSS. |
| `src/sites.js` | Las nueve webs de muestra que salen en las tarjetas. |
| `src/art.js` | Genera las imágenes en canvas (no hay ni una imagen externa). |
| `src/fonts.css` | Tipografías incrustadas en base64. Generado, no editar a mano. |
| `tools/render.mjs` | Exporta los MP4. |
| `tools/shots.mjs` | Saca fotogramas sueltos mientras diseñas. |
| `tools/build.py` | Empaqueta todo en un único `dist/ad.html`. |
| `tools/build_fonts.py` | Regenera `src/fonts.css`. |

## Previsualizar

```bash
python3 -m http.server -d src 8000   # y abre http://localhost:8000/ad.html
```

Los botones de abajo cambian de formato y pausan. También por URL:
`ad.html?f=9x16`.

## Exportar los vídeos

```bash
npm install
npm run render            # los cuatro formatos
npm run render -- 9x16    # solo uno
```

Salen en `dist/`:

| Archivo | Tamaño | Dónde va |
| --- | --- | --- |
| `neris-webs-299-feed-4x5.mp4` | 1080×1350 | Feed de Facebook e Instagram (**el principal**) |
| `neris-webs-299-reels-9x16.mp4` | 1080×1920 | Reels y Stories |
| `neris-webs-299-feed-1x1.mp4` | 1080×1080 | Feed cuadrado |
| `neris-webs-299-feed-3x4.mp4` | 1080×1440 | Feed 3:4 |

El render no graba la pantalla: mueve la línea de tiempo fotograma a fotograma,
captura cada uno y los junta con ffmpeg. Por eso el resultado es idéntico en
cada ejecución y no depende de lo rápido que vaya la máquina.

ffmpeg se busca solo; si tienes uno concreto: `FFMPEG=/ruta/a/ffmpeg npm run render`.

## Cambiar cosas

**El texto de la oferta** está en `buildOffer()`, dentro de `src/ad.js`.

**El precio del fondo** está en `buildMarquee()`, en la constante `words`. Las
dos líneas se justifican solas al mismo ancho, así que puedes cambiar las
palabras sin tocar nada más.

**Los tiempos** están todos juntos en el objeto `T` al principio de `src/ad.js`.

**Las webs de muestra** están en `src/sites.js`, una función por web. Si añades
o quitas alguna, la velocidad de la cinta se recalcula sola para que la última
llegue al centro justo al acabar la parte de muestra.

> Los nombres de las nueve webs (Casa Bruma, Nudo, Volta…) son inventados para
> el anuncio. Si las cambias por trabajos reales, revisa que tengas permiso del
> cliente para enseñarlos.

## Sobre las imágenes

No hay ninguna imagen externa: todas se pintan con canvas a partir de una
semilla fija. Eso mantiene el repo ligero, evita problemas de derechos de las
fotos de stock y hace que el render funcione sin conexión. Son texturas
abstractas, no fotos de personas — si quieres fotos reales en las webs de
muestra, habría que meter archivos y volver a mirar el peso del HTML.
