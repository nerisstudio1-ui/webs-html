# Chío Jiménez · Maquillaje profesional

Landing page estática (HTML + CSS + JS, sin dependencias ni build).

```
chio-jimenez/
├── index.html
└── assets/
    ├── styles.css
    ├── script.js
    └── img/          ← aquí van todas las fotos
```

## Cómo subir las fotos

Sube los archivos a `chio-jimenez/assets/img/` con **exactamente estos nombres**.
No hay que tocar el código: cada foto aparece sola en su sitio.

### Imágenes principales

| Nombre del archivo  | Dónde aparece                        | Formato recomendado          |
|---------------------|--------------------------------------|------------------------------|
| `hero.jpg`          | Fondo de la portada, a pantalla completa | Horizontal, 2400×1600 px |
| `chio-retrato.jpg`  | Retrato en la sección «Sobre mí»     | Vertical 3:4, 1200×1600 px   |
| `og.jpg`            | Miniatura al compartir en WhatsApp / redes | Horizontal, 1200×630 px |

### Portfolio

| Nombre del archivo | Categoría           |
|--------------------|---------------------|
| `novia-01.jpg`     | Novias y eventos    |
| `novia-02.jpg`     | Novias y eventos    |
| `novia-03.jpg`     | Novias y eventos    |
| `evento-01.jpg`    | Novias y eventos    |
| `moda-01.jpg`      | Moda y publicidad   |
| `moda-02.jpg`      | Moda y publicidad   |
| `moda-03.jpg`      | Moda y publicidad   |
| `av-01.jpg`        | Audiovisuales       |
| `av-02.jpg`        | Audiovisuales       |
| `av-03.jpg`        | Audiovisuales       |
| `creativo-01.jpg`  | Creativo            |
| `creativo-02.jpg`  | Creativo            |

Mientras una foto no exista, su hueco se muestra en gris con el nombre del
archivo que le corresponde. Así se ve de un vistazo qué falta por subir.

Para añadir, quitar o reordenar fotos del portfolio, edita la lista `PHOTOS`
al principio de `assets/script.js`.

**Peso:** exporta en JPG de calidad 80 y máximo 2400 px de lado largo.
Cada foto debería quedar por debajo de 500 KB para que la web cargue rápido.

## Diseño

Fondo claro y una sola tipografía, **Archivo** (Google Fonts), en todos los
tamaños. Sin serif ni cursivas: el peso visual lo llevan las fotos, no la
decoración.

Los colores están definidos como variables al principio de `assets/styles.css`.
Para cambiar el fondo o el color del texto basta con tocar `--bg` y `--fg`.

## Logo

`logo-negro.png` y `logo-blanco.png` están generados a partir del PDF original
con fondo transparente. El negro es el que usa la web; el blanco queda
disponible por si algún soporte lleva fondo oscuro.

## Idiomas

La web está en español e inglés. El selector ES/EN está en la cabecera.
Detecta el idioma del navegador la primera vez y luego recuerda la elección.

Los textos en inglés están en el objeto `I18N.en` de `assets/script.js`.
Los textos en español están directamente en `index.html`.

## Contacto

Teléfono de WhatsApp y email se configuran en un único sitio: la constante
`CONTACT` al principio de `assets/script.js`. En `index.html` aparecen también
en los enlaces de la sección de contacto y el pie.

## Formulario

No necesita servidor. Al enviar, compone el mensaje y abre WhatsApp o el
gestor de correo del visitante con todos los datos ya rellenos.

## Publicar

Es una web estática: vale cualquier hosting. Sube el contenido de la carpeta
`chio-jimenez/` a la raíz del dominio `chiojimenez.makeup`.

Para probarla en local:

```bash
cd chio-jimenez
python3 -m http.server 8000
# abrir http://localhost:8000
```
