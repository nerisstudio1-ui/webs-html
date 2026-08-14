# Material de marca

Carpeta para los archivos originales que envía el estudio. Los nombres
importan: el HTML ya está preparado para apuntar a estas rutas.

## Logotipo

| Archivo | Versión | Dónde se usa |
|---|---|---|
| `logo-burgundy.svg` | Granate sobre fondo claro | Cabecera cuando está sobre crema |
| `logo-cream.svg` | Blanco / crema | Cabecera sobre foto, pie de página, menú móvil |
| `logo-brown.svg` | Marrón | Alternativa sobre fondos arena |

Preferible **SVG**. Si solo hay PNG, que sea de al menos 1200 px de ancho y
con fondo transparente.

### Cómo activarlo

En cada HTML, el logotipo está ahora escrito con tipografía:

```html
<a class="logo" href="index.html">
  <b>B<i>e</i>LA.</b>
  <span>Brow Design</span>
</a>
```

Al tener el archivo, se sustituye por:

```html
<a class="logo logo--img" href="index.html" aria-label="Bela Brow Studio and Beauty">
  <img src="assets/brand/logo-cream.svg" alt="Bela Brow Studio and Beauty">
</a>
```

La clase `logo--img` ya tiene su estilo en `assets/css/style.css`.

## Color de marca

El granate del logotipo es el color protagonista de toda la web. Está
definido en `assets/css/style.css` como `--burgundy`. Al recibir el SVG hay
que leer su valor real y ajustar esa variable (y `--burgundy-deep`, una
versión más oscura del mismo tono).

## Fotografías

Van en `assets/img/`, no aquí. Ver la tabla de proporciones del README
principal.
