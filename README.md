# Anuncio de vídeo — Neris Studio, webs a 299 €

Anuncio para Facebook hecho **en HTML** y exportado a MP4. Arranca con el precio
a pantalla completa, pasa nueve webs inclinadas en 3D sobre azul eléctrico, y
cierra con la oferta, que entra como una tarjeta más de la cinta y se endereza.

Duración 12 s · 30 fps · sin audio.

```
0,0 – 1,3 s   el gancho se monta solo y el 299 € entra de golpe
1,3 – 7,8 s   nueve webs suben por la cinta, scrolleando (la prueba)
     ~4,9 s   una de ellas se pone de frente un momento
7,8 – 8,9 s   la cinta acelera y las saca de cuadro
7,8 – 12,0 s  cierre: aterriza con rebote, 299 € y llamada a la acción
```

## Qué hay aquí

| Archivo | Para qué |
| --- | --- |
| `src/ad.html` | La página del anuncio. Ábrela en el navegador para previsualizar. |
| `src/ad.css` | Diseño y sistema de tokens. Arriba del todo está el plan de diseño. |
| `src/ad.js` | La línea de tiempo. Todo es función de `t`, no hay animaciones CSS. |
| `src/sites.js` | Las nueve webs de muestra que salen en las tarjetas. |
| `src/art.js` | Dibuja las imágenes en canvas (no hay ni un archivo de imagen). |
| `src/fonts.css` | Tipografías incrustadas en base64. Generado, no editar a mano. |
| `src/fonts/` | Montserrat en TTF (SIL Open Font License). |
| `tools/render.mjs` | Exporta los MP4. |
| `tools/shots.mjs` | Saca fotogramas sueltos mientras diseñas. |
| `tools/build_preview.py` | Genera `dist/preview.html`, una página con reproductor. |
| `tools/build.py` | Empaqueta el anuncio solo en un único `dist/ad.html`. |
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

## Diseño

- **Color.** Azul eléctrico `#0B1BC4` como fondo de todo el vídeo, con caída a
  `#061073` en las esquinas. Blanco para las tarjetas. Un único color chillón,
  el lima `#D6FF3D`, y se gasta entero en el precio.
- **Tipografía.** Montserrat en todo el anuncio: 900 para el precio, 700 para
  los titulares, 700 cursiva para las frases que venden, 500 para el texto
  corrido. Geist Mono solo en las etiquetas pequeñas de las esquinas.
- **Movimiento.** Una sola cinta. El gancho, las webs y la oferta van todos
  sobre ella; la oferta es el último objeto de la cinta y por eso frena y se
  gira en vez de aparecer de la nada.
- **Las webs están vivas.** Cada tarjeta es una ventana de 760 px sobre una
  página de 900, y la página se desplaza dentro de su tarjeta mientras cruza
  el cuadro. No son capturas quietas: se ven como pantallas en uso, y además
  da tiempo a enseñar más de cada web.
- **Destello.** Una banda de luz cruza cada tarjeta al pasar por el centro,
  en modo `screen`, para que se lean como objetos físicos y no como recortes
  pegados sobre el azul.
- **Momento héroe.** Hacia los 4,9 s una de las webs se endereza, se acerca a
  cámara y vuelve a la fila. Rompe el metrónomo de la cinta y da un respiro
  antes del cierre. Se elige con la constante `HERO` en `src/ad.js`.

## Cambiar cosas

**El texto del gancho** está en `buildHook()`, dentro de `src/ad.js`.
**El texto de la oferta**, en `buildOffer()`, justo debajo.
**Los tiempos**, todos juntos en el objeto `T` al principio de `src/ad.js`.
**Los colores**, en el bloque `:root` de `src/ad.css`.

**Las webs de muestra** están en `src/sites.js`, una función por web. Si añades
o quitas alguna, la velocidad de la cinta se recalcula sola para que la última
llegue al centro justo al acabar la parte de muestra.

## Dos avisos antes de publicarlo

**Las webs son inventadas.** Casa Bruma, Volta, Ferra y las demás no existen;
están hechas para el anuncio. Así el vídeo dice «hacemos webs así» sin
atribuir ninguna a un cliente concreto. Si las cambias por trabajos reales,
pide permiso a cada cliente antes de enseñarlos.

**Las imágenes están dibujadas por código, no son fotos.** En el entorno donde
se construyó esto no hay acceso a bancos de imágenes, así que cada escena —la
taza de café, la pista de pádel, el escenario, el atardecer— está pintada en
canvas con `src/art.js`. Quedan bien y hacen que cada web se distinga, pero son
ilustraciones. Si quieres fotografías de verdad, hay que meter archivos en el
proyecto y sustituir las llamadas a `ART.bg(...)` en `src/sites.js` por rutas a
esas fotos, con su licencia comprobada.

## Tipografías

Montserrat (`src/fonts/`) se distribuye bajo la SIL Open Font License 1.1, que
permite uso comercial. El resto de familias que usan las webs de muestra
(Work Sans, Outfit, Lora, Instrument Serif, Geist Mono) también son OFL.
