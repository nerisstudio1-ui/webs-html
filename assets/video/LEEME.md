# Vídeos de los proyectos

Aquí van los reels. El generador los detecta solos: si un proyecto tiene vídeo,
su columna de la izquierda deja de ser una foto y pasa a ser el vídeo, con la
foto del proyecto como imagen de espera (póster).

## Cómo se llaman los archivos

`<proyecto>-<número>.mp4`

| Proyecto | Archivos |
| --- | --- |
| Quality Training | `quality-1.mp4`, `quality-2.mp4` |
| Ratafia Malhivern | `malhivern-1.mp4` |
| Football 4 Stars | `f4s-1.mp4` |
| Maitasuna | `maitasuna-1.mp4` |
| Jordi Coll | `jordi-coll-1.mp4`, `jordi-coll-2.mp4` |
| F45 Training | `f45-1.mp4` |
| Comercial Puig | `puig-1.mp4`, `puig-2.mp4` |

Se muestran **como máximo dos por proyecto** (`MAX_REELS` en `build/build.py`).
También vale `.webm`; si están los dos formatos del mismo clip, gana el `.mp4`.

## Cómo tienen que ser

- **Vertical 9:16** (1080 × 1920), como salen de Instagram.
- **`.mp4` con H.264 + AAC.** Es lo que descarga Instagram y lo que reproducen
  todos los navegadores.
- **Cortos y ligeros**: por debajo de 4 MB cada uno. Si pesan más, conviene
  bajar el bitrate: se reproducen sin sonido y en un marco pequeño, no hace
  falta calidad de cine.
- **Sin texto quemado importante en los bordes**, que el marco recorta un poco.

## Cómo se comportan en la web

- Arrancan solos, **sin sonido**, cuando entran en pantalla, y se paran al salir.
- El botón redondo activa el audio; solo puede sonar uno a la vez.
- Al hacer clic en el vídeo se pausa y se reanuda.
- Con `prefers-reduced-motion` no arrancan solos: se queda el póster.

Después de dejar los archivos aquí:

```bash
python3 build/build.py
python3 build/build_widget.py
```
