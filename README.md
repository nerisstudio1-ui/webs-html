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
2. **Portada** — la foto del aula a un lado, saliéndose por el borde de la pantalla, y
   el texto al otro sobre el beige. Sin nada encima de la foto. En móvil la foto va
   arriba y el texto debajo.
3. **Statement** — el problema/deseo de la clienta, en grande.
4. **Qué puedes encontrar** — las cuatro familias de producto.
5. **Material educativo** — las 10 fichas con descripción y precio.
6. **Para el cole** — placas de seño y medallas de graduación (con tabla de modelos).
7. **Para los peques** — cumple mes, placas de habitación y «Mi primer año».
8. **Comuniones y bodas** — los 12 detalles, en fichas compactas.
9. **Galería** — mosaico con 24 fotos de trabajos ya hechos.
10. **Personalización** — el 100 % personalizable.
11. **Cómo funciona** — los cuatro pasos del encargo.
12. **Pedidos grandes** — graduaciones, comuniones, bodas y aulas completas.
13. **Valores** — banda burdeos con hecho a mano / para el aula / con tu nombre.
14. **Sobre mí** — Davinia y el origen del nombre.
15. **Preguntas frecuentes** — siete preguntas desplegables.
16. **Contacto** — WhatsApp e Instagram.

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
| Beige | `#F5EEE3` | Fondo general |
| Beige claro | `#FAF5EC` | Material educativo, galería y preguntas |
| Arena | `#EADDCA` | Categorías y pedidos grandes |

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

## Condiciones publicadas

Confirmadas por Davinia y ya en la web (preguntas frecuentes, franja bajo los pasos
del encargo y pie del bloque de contacto):

- **Plazo**: unos 15 días desde que se cierran los detalles.
- **Pedido mínimo**: no hay, ni siquiera en marcasitios o llaveros.
- **Pago**: al terminar el producto, por Bizum o transferencia. Sin señal.

## Datos pendientes de confirmar con Davinia

- **Envíos** — si hace envíos, a dónde y cuánto cuestan. (Se retiró de la web el texto
  «Envíos a toda España», que era una suposición.)
- **Precio de las placas de seño y de las placas de silla**, que ahora ponen «Consultar».

## El móvil

La web se rehízo para móvil porque a una columna se iba a 28.000 px de alto. Ahora:

- Las fichas de producto llevan la foto arriba y el texto debajo. La foto conserva su
  propia forma (las hay verticales, cuadradas y apaisadas) con un tope de alto del
  78 % del ancho de la pantalla, encuadrada un poco por encima del centro.
- La galería pasa de mosaico a una tira que se desliza con el dedo.
- Las categorías van de dos en dos, y los pasos y los valores ponen el número o el
  icono al lado del título en vez de encima.

Con eso la página baja de 28.000 a unos 23.300 px.

## Cómo generar el código para un widget de HTML

La web está escrita como página propia, así que su CSS lleva reglas para `*`, `html`
y `body`. Pegada tal cual dentro del widget de una plataforma, esas reglas se aplican
a **toda** la página de la plataforma (le cambian la tipografía, el fondo y el
`box-sizing`), y a la vez los estilos de la plataforma pisan los de la web: el logo
salía a tamaño natural y el menú se partía en dos líneas.

`construir_widget.py` (en el scratchpad de la sesión) genera la versión para pegar:

1. Mete todo el CSS dentro de `#artnia-web` con un pequeño analizador de bloques, de
   modo que `:root`, `html` y `body` pasan a ser el propio contenedor y `*` pasa a ser
   `#artnia-web *`. Los `@keyframes` se dejan intactos y los `@media` se procesan por
   dentro.
2. Cambia las alturas en `vh` por píxeles: dentro de un widget la ventana no es la de
   la web.
3. Añade un bloque de blindaje con `!important` en el logo y en las fotos, porque las
   plataformas suelen forzar `img{width:100% !important}`.
4. Saca el contenedor a ancho completo con `margin-left:calc(50% - 50vw)`, ya que el
   widget suele vivir dentro de una columna estrecha.
5. Incrusta las fotos en el propio código, así no dependen del repositorio.

Comprobado contra una página que imita a una plataforma hostil: el contenedor ocupa
todo el ancho, el logo mide lo que debe, no hay fotos rotas, el contenido se ve con y
sin JavaScript, y la página de la plataforma se queda como estaba.

### Fichas con varias fotos

El calendario escolar y el árbol de las estaciones se venden por lo que traen dentro,
así que su ficha enseña todas las piezas de una vez: la foto grande arriba y una tira
de miniaturas justo debajo (`.card__tira`). Todas se ven a la vez, sin flechas ni nada
que haya que pulsar, porque en el widget no corre JavaScript.

Las dos fotos grandes son verticales (3:4) y el recorte a 4/3 se comía la cabecera y el
pie del calendario, así que esas fichas llevan `.card--album` y se enseñan enteras.

Las fotos que solo salen en las tiras y en el mosaico se ven a 90-140 px, así que se
guardan a 180-260 px en vez de al tamaño de una ficha. Con eso la versión alta bajó de
1,8 a 1,6 MB **aunque tiene nueve fotos más**.

Falta por recibir: del árbol de las estaciones hay diez fotos de piezas y solo llegaron
cuatro (primavera, otoño, Navidad y Carnaval). Faltan, entre otras, «Día del libro:
Libros» y «Verano: Helados».

### El tamaño del código pegado

Incrustar las 67 fotos en base64 deja el archivo en 2,2 MB y la plataforma lo corta o lo
rechaza al guardar sin avisar: se sigue viendo la versión anterior. Con 164 KB sí entra,
así que el techo está entre medias.

Bajar el peso a base de comprimir mucho el JPEG (calidad 38, fotos a 300 px) sí entra,
pero las fotos se ven mal. La salida es **WebP**, que a igualdad de vista pesa un 30 %
menos que el JPEG, y repartir el peso según lo que cada foto ocupa de verdad en pantalla:
la portada y las categorías se ven grandes y van finas, y lo que se recorta son las 52
fichas pequeñas del catálogo.

`fotos.py` guarda esa tabla y `construir_v2.py` genera cada versión con `NIVEL=`:

| Nivel | Tamaño | Portada | Categorías | Fichas |
| --- | --- | --- | --- | --- |
| `alto` | 1,6 MB | 1300 px | 640 px | 460 px |
| `medio` | 1,1 MB | 1100 px | 520 px | 360 px |
| `bajo` | 820 KB | 1000 px | 460 px | 270 px |

El logo lleva transparencia, así que sigue en PNG, reducido a 256 colores (a 64 se
notaban escalones en la letra). Con `TROZO=1` sale solo la cabecera, la portada y las
categorías, que es el archivo de prueba para comprobar el widget en 30 segundos.

Las cuatro versiones pasan la misma comprobación contra la plataforma simulada: ancho
completo, logo a 68 px, cero fotos rotas, cero bloques invisibles sin JavaScript y la
página de la plataforma intacta.
