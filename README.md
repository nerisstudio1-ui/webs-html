# Blomstra — WordPress + Elementor

Paso del diseño de Figma `WEBSIDE_BLOMSTRA` a un sitio WordPress construido con
Elementor. Va con **Elementor gratuito**, sin Pro, lo que condiciona el header,
el footer y los formularios; está resuelto en la guía de montaje.

## Estado

| Pieza | Estado |
|---|---|
| Tema hijo de Hello Elementor | Listo |
| Paleta y tipografía del diseño → kit de Elementor | Listo |
| Plantillas con widgets nativos (0 widgets HTML) | Portal y home |
| Prototipo del portal | Listo y verificado contra el diseño |
| Prototipo de servicios | Listo y verificado contra el diseño |
| Prototipo de la home | Listo, 14 secciones con el copy real |
| Plantilla de Elementor de la página de servicios | **Pendiente** |
| Formularios y cuestionario | **Sin maquetar** |
| Imágenes y logotipos reales | **Faltan** |

## Cómo está montado

**Todo con widgets nativos de Elementor**, y los estilos puestos en los
controles del editor. Las plantillas no llevan ni un widget HTML: textos,
colores, tipografías y espaciados se cambian desde Elementor sin tocar código.

En el CSS del tema hijo queda solo lo que Elementor no sabe hacer, y cada
bloque de `blomstra.css` explica por qué está ahí:

| Qué | Por qué no puede ir en Elementor |
|---|---|
| Proporciones de los huecos de imagen | Elementor solo da altura fija, no proporción |
| Reparto a partes iguales en una fila | Evita tener que marcarlo hijo a hijo |
| Rayas del manifiesto | Es un degradado repetido, no un fondo de los que admite |
| Wordmark del pie | Va a sangre y no debe partirse en dos líneas |
| Tema invertido del portal en móvil | Son dos temas del mismo bloque, no un ajuste responsive |

Los HTML de `prototype/` **no son la entrega**: son la referencia visual con la
que se contrastó el diseño contra el Figma antes de montarlo. Tienen su propia
hoja de estilos en `prototype/assets/`.

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
