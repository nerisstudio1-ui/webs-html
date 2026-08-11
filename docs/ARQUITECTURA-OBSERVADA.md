# Arquitectura observada del diseño

Leído de la **captura del canvas completo** de Figma (vista alejada). Es lo
único del diseño a lo que he tenido acceso, así que todo lo de aquí es
estructura aproximada, no medidas. Se confirma y se corrige cuando lleguen los
frames a resolución legible.

## Inventario de pantallas

Se distinguen unos **10 frames de escritorio**, agrupados en cuatro bloques:

| Bloque | Frames | Qué parece ser |
|---|---|---|
| A | 1 corto | Pantalla de dos columnas, quizá un selector o una portada |
| B | 2 largos | Las páginas principales. Scroll largo, muchas secciones |
| C | 5 medianos | Flujo tipo cuestionario por pasos ("01", "02 Identidad visual") |
| D | 2 largos | Páginas de formulario extenso |
| — | 1 mini | Paleta de color (muestra de 4 tonos) |

## Estructura de los frames largos (bloque B)

De arriba abajo, lo que se alcanza a distinguir:

1. **Hero** — fondo crema, titular centrado en serif, texto de apoyo
2. **Sección con imagen grande** — en una de las variantes, foto en blanco y negro a sangre
3. **Bloque de collage** — rejilla irregular de imágenes con texto intercalado
4. **Sección oscura** — franja marrón muy oscuro / casi negro, titular claro
5. **Dos tarjetas** — dos bloques gemelos con logo, texto y botón
6. **Sección de cuatro columnas** — probablemente servicios o proceso
7. **Franja oscura con imagen** — texto a la izquierda, imagen a la derecha, botón
8. **"Manifiesto"** — fondo con patrón de rayas verticales beige, texto largo centrado
9. **Bloques imagen + texto** — dos, alternando lado
10. **CTA de cierre** — texto centrado y botón
11. **Footer** — oscuro/beige, con el wordmark **BLOMSTRA** en grande

## Paleta aparente

Family de **beige, crema y marrón**, muy sobria:

- Beige / taupe medio (el fondo dominante)
- Crema claro, casi hueso
- Marrón muy oscuro, casi negro (secciones de contraste)
- Un acento **lavanda** que aparece en uno de los frames del bloque C

Los HEX **no son recuperables** de la captura: hace falta el frame de la paleta
a resolución real, o los valores de Dev Mode.

## Tipografía aparente

- **Titulares**: serif con contraste alto y remates finos, en varios sitios en
  cursiva. Estilo Didone / Playfair. El logotipo usa esa misma familia.
- **Cuerpo**: sans-serif de palo seco, pequeña y con interlineado amplio.

Las familias exactas hay que confirmarlas: si no son de Google Fonts, en
Elementor gratuito **no hay uploader de fuentes** y habría que cargarlas a mano
con `@font-face` desde el tema hijo.

## Idioma

El diseño está en **español**.

## Consecuencias para el montaje

1. **Los bloques C y D son mucho formulario.** Confirma la necesidad de Fluent
   Forms Lite con multi-step (ver la guía de montaje, 4.2). El flujo por pasos
   con numeración "01 / 02" y lista lateral de secciones es un formulario
   multipaso con indicador de progreso, no páginas sueltas.
2. **Bastantes secciones a ancho completo con fondo propio.** Encaja bien con
   contenedores flex de nivel raíz.
3. **La sección del patrón de rayas** necesita un fondo repetido: o imagen
   exportada de Figma, o `repeating-linear-gradient` en CSS. Prefiero lo
   segundo, pesa menos y escala mejor.
4. **El collage de imágenes irregular** es lo más delicado de reproducir sin
   Pro. Se resolverá con contenedores anidados y `object-fit`.
