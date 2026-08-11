# Blomstra — WordPress + Elementor

Paso del diseño de Figma `WEBSIDE_BLOMSTRA` a un sitio WordPress construido con
Elementor.

## Estado

Va con **Elementor gratuito**, sin Pro. Eso condiciona el header, el footer y
los formularios; está resuelto en la guía de montaje.

| Pieza | Estado |
|---|---|
| Tema hijo de Hello Elementor | Listo |
| Kit de Elementor (estructura + empaquetado) | Listo, **con valores placeholder** |
| Ruta de montaje sin Elementor Pro | Resuelta y documentada |
| Paleta y tipografía reales del diseño | **Bloqueado** — faltan los frames |
| Maquetado de header, footer y páginas | **Bloqueado** — faltan los frames |

**Por qué está bloqueado:** este entorno no tiene acceso de red a `figma.com`
ni a `api.figma.com` (403 del proxy de egreso). El enlace al archivo no se puede
abrir desde aquí, así que el diseño tiene que llegar como imágenes exportadas.
La captura del canvas completo recibida hasta ahora sirve para entender la
arquitectura, pero no tiene resolución para leer textos ni medir nada.
En [`docs/INTAKE-DISENO.md`](docs/INTAKE-DISENO.md) está qué hace falta.

## Estructura

```
wordpress/themes/blomstra-child/   Tema hijo (style.css + functions.php)
elementor-kit/                     Kit de Elementor sin comprimir
  manifest.json                    Metadatos del kit
  site-settings.json               Colores globales, tipografía, botones
  content/page/                    Plantillas de página (vacío por ahora)
tools/build-kit.sh                 Empaqueta elementor-kit/ en dist/*.zip
docs/                              Guía de montaje e intake de diseño
design-input/                      Destino de los exports de Figma
```

## Uso

```bash
./tools/build-kit.sh          # -> dist/blomstra-kit.zip
```

Después: WordPress → Elementor → Herramientas → Importar/Exportar kit.

Los pasos completos, en [`docs/GUIA-MONTAJE-WORDPRESS.md`](docs/GUIA-MONTAJE-WORDPRESS.md).
