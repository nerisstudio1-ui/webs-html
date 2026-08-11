# Blomstra — WordPress + Elementor

Paso del diseño de Figma `WEBSIDE_BLOMSTRA` a un sitio WordPress construido con
Elementor. Va con **Elementor gratuito**, sin Pro, lo que condiciona el header,
el footer y los formularios; está resuelto en la guía de montaje.

## Estado

| Pieza | Estado |
|---|---|
| Tema hijo de Hello Elementor | Listo |
| Paleta y tipografía del diseño → kit de Elementor | Listo |
| Hoja de estilos del diseño (`blomstra.css`) | Portal, servicios y detalle |
| Prototipo del portal | Listo y verificado contra el diseño |
| Prototipo de servicios | Listo y verificado contra el diseño |
| Plantilla de Elementor del portal | Generada |
| Home | Contenido inventariado; **sin maquetar** |
| Formularios y cuestionario | **Sin maquetar** |
| Imágenes y logotipos reales | **Faltan** |

## Cómo está montado

El diseño **no** vive en los ajustes de Elementor, sino en un CSS versionado:

```
Elementor  →  estructura (contenedores flex) + una clase CSS por elemento
blomstra.css  →  todo lo visual
```

Se hace así por tres razones: no depende de controles de estilo que son de
Elementor Pro, el diseño queda en git en vez de dentro de la base de datos, y
los prototipos de `prototype/` enlazan ese mismo CSS, así que no pueden
desincronizarse del sitio real.

## Estructura

```
wordpress/themes/blomstra-child/
  style.css                  Tema hijo: resets y accesibilidad
  functions.php              Encolado, menús, soporte de header/footer
  assets/css/blomstra.css    EL DISEÑO. Tokens + todas las pantallas
elementor-kit/
  manifest.json              Metadatos del kit
  site-settings.json         Colores y tipografía globales
  content/page/*.json        Plantillas de página
prototype/                   Prototipos HTML para validar contra el Figma
tools/
  build-kit.sh               Empaqueta el kit en dist/*.zip
  build-templates.py         Genera las plantillas de Elementor
docs/                        Guía de montaje, contenido e incidencias
```

## Uso

```bash
python3 tools/build-templates.py   # regenera elementor-kit/content/page/
./tools/build-kit.sh               # -> dist/blomstra-kit.zip
```

Los prototipos se abren directamente en el navegador desde `prototype/`.

## Documentación

- [`docs/GUIA-MONTAJE-WORDPRESS.md`](docs/GUIA-MONTAJE-WORDPRESS.md) — instalación paso a paso
- [`docs/INCONSISTENCIAS.md`](docs/INCONSISTENCIAS.md) — **léelo**: decisiones de diseño pendientes que bloquean
- [`docs/CONTENIDO-HOME.md`](docs/CONTENIDO-HOME.md) — todo el copy de la home transcrito
- [`docs/ARQUITECTURA-OBSERVADA.md`](docs/ARQUITECTURA-OBSERVADA.md) — mapa de pantallas
- [`docs/INTAKE-DISENO.md`](docs/INTAKE-DISENO.md) — qué falta por recibir

## Nota sobre las tipografías

Las del diseño no son de Google Fonts: el wordmark usa una didone con la B
adornada y una itálica caligráfica. Mientras no lleguen, el proyecto usa
**Playfair Display**, **Pinyon Script** y **Montserrat** como sustitutas, y los
lockups están reconstruidos con texto. Lo correcto es que los lockups lleguen
como **SVG** desde Figma; están aislados en `.bl-lockup` para poder cambiarlos
por un `<img>` sin tocar nada más.
