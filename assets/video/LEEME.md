# Vídeos de los proyectos

Aquí van los reels. El generador los detecta solos: si un proyecto tiene vídeo,
su columna deja de ser una foto y pasa a ser el vídeo en marco vertical.

## Lo que hay ahora

| Archivo | Proyecto | Duración | Peso |
| --- | --- | --- | --- |
| `quality-1.mp4` | Quality Training — «Vols córrer ràpid?» / QT Endurance | 20 s | 5,3 MB |
| `malhivern-1.mp4` | Ratafia Malhivern — la ruta, la masia | 1:28 | 12,9 MB |
| `jordi-coll-1.mp4` | Jordi Coll — *El pont de les mentides* | 43 s | 4,5 MB |
| `puig-1.mp4` | Comercial Puig — el equipo en la tienda | 52 s | 10,5 MB |

Cada uno tiene su `-poster.jpg` al lado: es un fotograma del propio vídeo y hace
de imagen de espera. Si se borra, el generador usa la foto del proyecto.

Los cuatro vienen de los originales de Instagram, reconvertidos para web:
H.264, 720 × 1280, **CRF 25**, audio AAC 96 kbps estéreo y `+faststart` (el índice
al principio del archivo, para que empiecen a reproducirse sin descargarse
enteros).

El CRF es lo que manda en la nitidez. Con 30 se veían blandos en los planos con
movimiento —y estos son reels, van todos con movimiento—, así que están a 25.
Sube el peso al doble, pero no afecta a la carga de la página: con
`preload="metadata"` no se descarga nada hasta que el reel entra en pantalla.
Bajar de 25 no se nota en un marco de 300 px.

## Cómo añadir más

`<proyecto>-<número>.mp4`, y a su lado `<proyecto>-<número>-poster.jpg` si se
quiere un fotograma concreto de espera.

| Proyecto | Nombre de archivo |
| --- | --- |
| Quality Training | `quality-1.mp4`, `quality-2.mp4` |
| Ratafia Malhivern | `malhivern-1.mp4`, `malhivern-2.mp4` |
| Football 4 Stars | `f4s-1.mp4` |
| Maitasuna | `maitasuna-1.mp4` |
| Jordi Coll | `jordi-coll-1.mp4`, `jordi-coll-2.mp4` |
| F45 Training | `f45-1.mp4` |
| Comercial Puig | `puig-1.mp4`, `puig-2.mp4` |

Se muestran **como máximo dos por proyecto** (`MAX_REELS` en `build/build.py`).
También vale `.webm`; si están los dos formatos del mismo clip, gana el `.mp4`.

Para reconvertir un original de Instagram:

```bash
ffmpeg -i original.mp4 -c:v libx264 -crf 25 -preset slow -pix_fmt yuv420p \
  -vf scale=720:1280:flags=lanczos -r 30 -c:a aac -b:a 96k -ac 2 \
  -movflags +faststart quality-1.mp4
ffmpeg -ss 1.2 -i quality-1.mp4 -frames:v 1 -vf scale=720:-1 -q:v 3 \
  quality-1-poster.jpg
```

## Cómo se comportan en la web

- Arrancan solos, **sin sonido**, cuando entran en pantalla, y se paran al salir.
- El botón redondo activa el audio; solo puede sonar uno a la vez.
- Al hacer clic en el vídeo se pausa y se reanuda.
- Con `prefers-reduced-motion` no arrancan solos: se queda el póster.
- `preload="metadata"`: hasta que no entran en pantalla solo se descarga la
  cabecera del archivo, no el vídeo.

Después de dejar archivos aquí:

```bash
python3 build/build.py
python3 build/build_widget.py
```
