# Revisión de Cristina · primera tanda, 21 de septiembre

Los quince puntos de sus mensajes, y qué se ha hecho con cada uno.

## ✅ Hechos

| # | Lo que pidió | Cómo ha quedado |
|---|---|---|
| 1 | Su nombre con los dos apellidos en la presentación | «Cristina Falcón Maldonado». Fuera el «Hola, soy Cristina» |
| 2 | El logotipo, más grande | De 3,1 a 4,2 rem de alto. La cabecera crece con él |
| 3 | El verso «La vida era más que lo que nos dijeron» | Arriba a la derecha de la portada, manuscrito, con la fuente debajo. En móvil pasa bajo el nombre, que en la esquina no cabe |
| 4 | No resaltar lo de la revista Álabe | Retirado de la trayectoria. En su lugar entra «Casa Victoria Mancera», que sí está vigente |
| 6 | Otra manuscrita parecida | Cedarville Cursive: trazo de pluma, fina e inclinada. Se le mandan nueve alternativas por si prefiere otra |
| 7 | Las dos fotos de pequeña | Las dos, al principio de la galería: la de blanco y negro sola y la que está con su hermano |
| 8 | Una imagen de manos | La de la mano con el poema al lado |
| 9 | La foto con su editora de Candaya y el cuadro | Puesta. Es el cuadro de la ballena de la portada de *Ítaca es nunca* |
| 11 | La Guarida ya no está en activo | Pasa a pasado en la biografía y en la trayectoria: «durante años dirigió» |
| 12 | Un verde más luminoso | Mismo tono, más saturación y más luz. De `#1F3D33` a `#255647`. En pantalla ya se lee como verde |
| 13 | Quitar «de Valera a Cuenca, pasando por Bolonia» | Ahora pone «Venezuela · Italia · España», que es la opción que ella daba con Bolonia dentro |
| 14 | Simplificar «cuatro poemarios y una veintena de…» | «Poesía» y debajo «Libros para niños y jóvenes» |
| 15 | Que cada libro lleve a su ficha, no a la portada de la editorial | Hecho con las direcciones que mandó. Dos libros que no tenían enlace ya lo tienen |

## ⏳ Pendientes de que ella mande material

| # | Lo que pidió | Qué hace falta |
|---|---|---|
| 5 | Los prólogos de sus poemarios | Los textos. Dijo que los enviaría |
| 10 | Un par de vídeos más | Los archivos |
| — | Las portadas que faltan, en mejor resolución | Siguen siendo siete: *Memoria errante*, *Borrar el paisaje*, *1, 2, 3, de repente en…*, *Peperoncino*, *Guías infantiles*, *La palabra encantada* y *Caja de cuentos* |

## Los enlaces de cada libro · punto 15

Ella mandó las direcciones el 24 de septiembre y ya están puestas:

| Libro | A dónde lleva |
|---|---|
| Ítaca es nunca | `candaya.com/libro/itaca-es-nunca/` |
| Borrar el paisaje | `candaya.com/libro/borrar-el-paisaje/` |
| Memoria errante | `candaya.com/libro/memoria-errante/` |
| Al otro lado | `akiarabooks.com/es/libro/al-otro-lado/` (ya estaba) |
| Siwar, el jaguar guardián | `fondodeculturaeconomica.com/Ficha/9786071668851/F` |
| La palabra encantada | la guía del CEPLI en `uclm.es` — **antes no tenía enlace** |
| Peperoncino | `giuntialpunto.it/products/peperoncino-1-propedeutica-9788809772366` — **antes no tenía enlace** |
| Letras en los cordones | `kalandraka.com/letras-en-los-cordones-castellano` |

Tres apuntes sobre cómo han quedado:

- La de *Peperoncino* venía con la coletilla de seguimiento de la tienda
  (`?pr_prod_strat=…&pr_rec_id=…`). Se ha quitado: son parámetros de
  recomendación de la sesión de quien copió el enlace, no forman parte de la
  dirección del libro y caducan.
- La de *La palabra encantada* no es una ficha de editorial sino una guía de
  lectura del CEPLI, así que su botón pone «Ver la guía de lectura» y no «Ver
  en la editorial», que sería engañoso.
- Esa misma dirección es la **versión en inglés** del sitio de la UCLM
  (`uclm.es/en/…`). Se ha dejado tal cual porque es la que ella dio y
  funciona; si existe la equivalente en español, mejor usar esa.

Desde aquí no se puede abrir ninguna de estas webs para comprobarlas, así que
**conviene pinchar los ocho botones una vez publicada la web.**

## Las descargas

El PDF de la biografía ya no menciona *Álabe* (punto 4). De paso, tanto la
biografía como el dossier de prensa hablan de «La Guarida» en pasado, igual
que la web (punto 11). Los dos se regeneran con `node build/pdf/generar.js`.


---

# Segunda tanda · 24 de septiembre

Cinco ajustes más, por correo, antes de salir de viaje. Vuelve el jueves con
el resto del material.

## ✅ Hechos

| # | Lo que pidió | Cómo ha quedado |
|---|---|---|
| 1 | «Poemarios» y «Libros para niños y jóvenes» | El tercer bloque de la portada. Antes ponía «Poesía» |
| 2 | En obra: «Poesía» y «Literatura infantil y juvenil» | Las dos pestañas. La marquesina de arriba se mueve con ellas, que usa la misma etiqueta |
| 3 | La reseña de Pedro Cerrillo | Séptima del bloque. Cierra la rejilla en 3×2, que antes quedaba coja |
| 4 | Fuera «escribo para adultos y para niños» | Quitado del bloque de la portada, que era donde se decía suelto |

## ⏳ A medias

**Punto 5 · La ilustración de portada y el prólogo de cada poemario.**

De las portadas que mandó se sacan ya los prologuistas, y están puestos en la
ficha de cada libro:

| Poemario | Prólogo |
|---|---|
| Memoria errante | Ramón Palomares |
| Borrar el paisaje | Margot Carrillo Pimentel |
| Ítaca es nunca | sin confirmar |

Falta lo demás:

- **Los textos de los prólogos.** Sin ellos no hay apartado que montar.
- **Las ilustraciones sueltas** (la ballena, el dibujo a tinta, el sello de
  migración). Llegaron dentro del correo, no como archivos, y a ese tamaño no
  sirven para la web.
- **Las dos portadas de Candaya completas** (*Memoria errante* en rojo y
  *Borrar el paisaje* en turquesa). Mismo caso: hacen falta los archivos.

## ⚠️ El zip venía cambiado

El `fotos-portada-retrato.zip` que se adjuntó no es de este proyecto: dentro
hay `portada-cejas.jpg` y `chio-retrato-2.jpg`, que son de la web de Chío. Hay
que volver a mandarlo.

## Material que llegó y está sin decidir

- **La portada de *El puente es la palabra*** (antología de Caritas Venezuela).
  Extraída del PDF y guardada en `assets/img/obra/el-puente-es-la-palabra.jpg`,
  a 1126 × 1819. **No está puesta en la web**: el bloque de antologías es un
  párrafo de texto con seis títulos, y poner la portada de uno solo queda
  raro. Hay que decidir si van las seis o ninguna.
- **Dos biografías nuevas** (`Autora BIO 1` y `Autora BIO 2`). La primera es la
  versión lírica, la de los pájaros y las casas en los árboles; da para mejorar
  el «Sobre mí». La segunda trae toda la faceta de diseño gráfica, que hoy no
  está en la web: el concurso de la imagen de Ibiza Patrimonio de la Humanidad,
  la identidad de la Red Internacional de Universidades Lectoras. Hay que
  preguntarle si quiere que entre.

### Un dato que no cuadra

La web dice que *Memoria errante* la llevó al teatro **Dèria Teatre**. La
biografía nueva dice **«Deia Teatre y Lamina Teatre»**: cambia la grafía y
aparece una segunda compañía. Hay que confirmar cuál es la buena.
