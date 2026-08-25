# ArTnia — web

Web de una sola página para **ArTnia** (*Lo sueñas, lo creamos*): material educativo
manipulativo, placas personalizadas para seños y detalles para comuniones y bodas.

HTML, CSS y JS puros, sin dependencias ni build. Se abre haciendo doble clic en
`index.html` o se sube tal cual a cualquier hosting.

## Estructura

```
index.html                 Toda la página
assets/css/styles.css      Estilos (paleta y tipografías al principio)
assets/css/fonts.css       Tipografías autoalojadas (no dependen de internet)
assets/js/main.js          Menú móvil, animación al hacer scroll, año del pie
assets/fonts/              Poppins + Yellowtail en .woff2
assets/img/                Imágenes (ahora mismo, marcadores de posición)
```


## Catálogo publicado

**Material educativo** (10 productos) — Calendario escolar 49,90 € · Material Protagonista
49,90 € · El número protagonista 49,90 € · La palabra secreta 49,90 € · Rutinas de clase
49,90 € · Árbol de las estaciones y festividades 54,90 € · Tiempo atmosférico 44,90 € ·
Asistencia 44,90 € · Cumplemeses 34,90 € · Lee, crea y escribe 24,90 €.

**Para el cole** — Placas personalizadas de seño (a consultar) · Medallas de graduación:
grabada 3,50 €, con nombre a relieve 4 €, con círculo + nombre + sombrero a relieve 4,50 €.

**Para los peques** — Cumple mes 21,90 € · Placas para la habitación 39,90 € ·
Placa «Mi primer año» 49,90 €.

**Comuniones y bodas** — Placa identificativa de silla (a consultar) · Libro de firmas
44,90 € · Marcasitios desde 1 € · Llaveros 2,80 € · Marcapáginas grabados 3 € ·
Marcapáginas infantiles 3 € · Abridores 2,70 € · Espejos 2,70 € · Joyeros 5,50 € ·
Libreta y lápiz 4,80 € · Portalápiz y lápiz 6 € · Tres en raya 3,20 €.

Para añadir, quitar o cambiar el precio de un producto, edita directamente la ficha en
`index.html` (busca el nombre del producto).

## Secciones

1. **Cabecera** con el logo y el menú (se convierte en desplegable en móvil).
2. **Portada** — material educativo, con dos llamadas a la acción.
3. **Statement** — el problema/deseo de la clienta, en grande.
4. **Qué puedes encontrar** — las cuatro familias de producto.
5. **Material educativo** — las 10 fichas con descripción y precio.
6. **Para el cole** — placas de seño y medallas de graduación (con tabla de modelos).
7. **Para los peques** — cumple mes, placas de habitación y «Mi primer año».
8. **Comuniones y bodas** — los 12 detalles, en fichas compactas.
9. **Personalización** — el 100 % personalizable y los 3 pasos del encargo.
10. **Valores** — banda burdeos con hecho a mano / para el aula / con tu nombre.
11. **Sobre mí** — Davinia y el origen del nombre.
12. **Contacto** — WhatsApp e Instagram.

## Paleta

Sacada del logo, usada con moderación: fondos crema y blanco, el burdeos para
tipografía y una sola banda, y el verde menta como acento.

| Color | Código | Uso |
|---|---|---|
| Burdeos | `#6E1524` | Titulares, botones, banda de valores |
| Burdeos oscuro | `#4C0E19` | Bloque de contacto |
| Burdeos claro | `#9A3B4A` | Textos en cursiva, detalles |
| Verde menta | `#D6F3E2` | Cabecera, portada, pie |
| Menta suave | `#EDFAF3` | Fondo de la sección de personalización |
| Crema | `#FBF6F0` | Fondo general |
| Arena | `#F3E7DE` | Sección de categorías |

Se cambian todos en un sitio: las variables `:root` de `assets/css/styles.css`.

## Qué falta por poner (pendiente de material real)

- **Logo**: ahora está escrito con tipografía. Para usar el logo original, guarda el
  archivo como `assets/img/logo.png` y sustituye en `index.html` el
  `<span class="logo__word">ArTnia</span>` por
  `<img src="assets/img/logo.png" alt="ArTnia" class="logo__img">` (ya hay un
  comentario en el sitio exacto).
- **Fotos**: los `.svg` de `assets/img/` y `assets/img/productos/` son marcadores.
  Se sustituyen por las fotos reales manteniendo el mismo nombre de archivo (cambiando la
  extensión en el `src` de `index.html`, p. ej. `calendario-escolar.jpg`):
  - `hero.svg` — foto principal (vertical)
  - `detalle.svg` — detalle de un acabado
  - `cat-material.svg`, `cat-placas.svg`, `cat-detalles.svg` — las categorías (vertical 3:4)
  - `personalizable.svg` — piezas personalizadas
  - `davinia.svg` — foto de Davinia (aquí va la foto de ella con una placa)
  - `productos/*.svg` — una por producto, con el nombre del producto (horizontal 4:3)
- **WhatsApp**: cambiar `https://wa.me/34600000000` por el número real.
- **Instagram**: cambiar `https://instagram.com/` por el perfil real.
- Faltan por añadir el resto de productos y precios cuando lleguen las fotos.

## Ver la web en local

```bash
npx serve .        # o simplemente abrir index.html en el navegador
```

## Tipografías

Poppins y Yellowtail (SIL Open Font License), descargadas y servidas desde el propio
proyecto para que la web cargue rápido y funcione aunque no haya acceso a Google Fonts.
