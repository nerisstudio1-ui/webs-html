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

**Material educativo** (11 productos) — Calendario escolar 49,90 € · Material Protagonista
49,90 € · El número protagonista 49,90 € · La palabra secreta 49,90 € · Rutinas de clase
49,90 € · Árbol de las estaciones y festividades 54,90 € · Tiempo atmosférico 44,90 € ·
Asistencia 44,90 € · Cumplemeses 34,90 € · Casas de los días de la semana 79,90 € ·
Lee, crea y escribe 24,90 €.

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
| Verde menta | `#D8F8E9` | Cabecera, portada, pie (es el verde exacto del logo) |
| Menta suave | `#EEFBF5` | Fondo de la sección de personalización |
| Crema | `#FBF6F0` | Fondo general |
| Arena | `#F3E7DE` | Sección de categorías |

Además, **cada familia de producto tiene su propio color**, sacado de las propias piezas,
para que la web no sea toda igual. Cada sección solo declara su acento y las fichas,
precios, botones y bordes de dentro lo heredan (variable `--acento`):

| Sección | Acento | Fondo |
|---|---|---|
| Material educativo | Burdeos `#6E1524` | Crema cálido `#FDF8F1` |
| Para el cole | Turquesa `#16757D` (el de las placas) | `#E0F3F4` |
| Para los peques | Rosa `#B03F63` | `#FBEAEF` |
| Comuniones y bodas | Verde oliva `#4E6B41` (el de las cintas) | `#ECF2E5` |

Se cambian todos en un sitio: las variables `:root` de `assets/css/styles.css`.

## Qué falta por poner (pendiente de material real)

- ~~Logo~~ ✅ puesto (`assets/img/logo.png`, con el fondo recortado y transparente).
  El verde menta de toda la web es exactamente el del logo (`#D8F8E9`).
- ~~Fotos de producto~~ ✅ puestas. Están en `assets/img/productos/`, con el nombre del
  producto (`calendario-escolar.jpg`). Las que llevan `-2`, `-3`… son fotos adicionales
  del mismo producto, guardadas para futuras galerías.
- **Falta la foto de Davinia** para «Sobre mí»: ahora hay una placa en la mano
  (`assets/img/davinia.jpg`). Se sustituye por su foto manteniendo el nombre.
- Queda por decidir si el **portalápiz (6 €)** encaja mejor en «Para los peques» que en
  los detalles de comunión, donde está ahora.
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
