# Blomstra — WordPress + Elementor

Paso del diseño de Figma `WEBSIDE_BLOMSTRA` a un sitio WordPress construido con
Elementor.

## Estado

| Pieza | Estado |
|---|---|
| Tema hijo de Hello Elementor | Listo |
| Kit de Elementor (estructura + empaquetado) | Listo, **con valores placeholder** |
| Paleta y tipografía reales del diseño | **Bloqueado** — falta el export de Figma |
| Maquetado de header, footer y páginas | **Bloqueado** — falta el export de Figma |

**Por qué está bloqueado:** este entorno no tiene acceso de red a `figma.com`
ni a `api.figma.com` (403 del proxy de egreso). El enlace al archivo no se puede
abrir desde aquí. En [`docs/INTAKE-DISENO.md`](docs/INTAKE-DISENO.md) están las
tres formas de hacerme llegar el diseño.

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
