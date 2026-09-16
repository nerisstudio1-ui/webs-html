# Qué falta para cerrar la web

Estado a 16 de septiembre de 2026. Fecha objetivo: **primeros de noviembre**
(publicación del nuevo libro).

---

## 🔴 Bloqueante — sin esto no se puede publicar

### Dominio y alojamiento
No tiene ninguno de los dos. Hay que decidir el dominio (¿`cristinafalcon.com`?
¿`cristinafalconmaldonado.com`?), registrarlo y elegir alojamiento.
Cuanto antes se registre, mejor: el DNS tarda en propagarse.

### El libro nuevo de noviembre
Es el motivo de la web y ahora mismo es el único hueco grande. Falta:
- Título
- Editorial
- Portada
- Texto de presentación (2-3 frases)
- Fecha exacta de publicación
- Enlace de compra o de la editorial

### Datos para el aviso legal
Para `aviso-legal.html`: NIF, domicilio fiscal y email de contacto público.

> ⚠️ El CV que nos pasó incluye su **NIE y su dirección particular completa**.
> Ninguno de los dos está en la web ni en este repositorio, y no deben estar.
> Para el aviso legal se necesita un domicilio, pero conviene hablarlo con ella
> antes: si no tiene actividad económica declarada, el aviso legal puede
> resolverse de forma mucho más ligera.

### Email de contacto
Decidir si usa su correo personal o uno nuevo del dominio
(`contacto@sudominio.com`, recomendado). Va en `assets/js/config.js`.

### Confirmar el teléfono de WhatsApp
Ahora está puesto el **645 76 46 16**, que es el que dio en el formulario de
Neris Studio. Hay que confirmar que es el que quiere publicar.

---

## 🟠 Importante — la web funciona, pero se ve incompleta

### Portadas de los libros
Faltan las 12. Deben ir en `assets/img/obra/` como JPG o WebP, recorte
vertical 2:3, unos 600 × 900 px.

| Poesía | Infantil |
|---|---|
| Ítaca es nunca (Candaya, 2021) | Al otro lado (Akiara, 2021) |
| Borrar el paisaje (Candaya, 2014) | Siwar, el jaguar guardián (FCE, 2020) |
| Memoria errante (Candaya, 2009) | La palabra encantada (CEPLI, 2017) |
| Premura sagrada (Caracas, 1986) | Peperoncino (Giunti, 2014) |
| | Letras en los cordones (Kalandraka, 2012) |
| | 1, 2, 3, de repente en… (Edebé, 2011-2012) |
| | Guías infantiles de España (Susaeta, 2012-2018) |
| | Caja de cuentos y aventuras (2006) |

Las editoriales suelen facilitarlas en alta resolución si se piden.

### Fotos de la autora
Hacen falta tres, del material profesional que ya tiene:
- `assets/img/perfil/retrato-hero.jpg` — vertical 3:4, la de portada
- `assets/img/perfil/sobre-mi.jpg` — vertical 4:5
- `assets/img/perfil/polaroid.jpg` — cuadrada, más informal

### Galería
Hay ocho huecos. De lo que ha ido mandando encajan muy bien: las fotos de
infancia en Venezuela, el cartel del Festival Mundial de Poesía de Trujillo, la
firma de ejemplares, la presentación de *Letras en los cordones*, la lectura en
escena y el paisaje de los Andes.

### Reseñas
Las tres tarjetas están vacías. Para cada una: la cita, quién la firma y dónde
se publicó. Aunque sean solo dos reales, mejor dos verdaderas que tres
inventadas.

### Vídeos
Faltan los enlaces de YouTube. En `index.html`, cambiar `data-yt="VIDEO_ID_1"`
por el ID real del vídeo.

> El `.MOV` que mandó pesa solo 50 KB, así que probablemente no se subió
> entero. Además, los vídeos no deberían ir dentro del repositorio: lo suyo es
> subirlos a YouTube (aunque sea como «no listados») y enlazarlos.

### Descargas
Faltan los archivos de `assets/docs/`: dossier de prensa, biografía en PDF,
fragmento del libro nuevo y ZIP de fotos en alta. Si alguno no se va a usar,
se quita esa tarjeta de la sección.

---

## 🟡 Por confirmar

- **Derechos de la ilustración del logo.** Es de **Giulia Sagramola**. Ya está
  acreditada en el pie, pero conviene confirmar que el encargo cubre el uso en
  la web.
- **Redes sociales.** Instagram `@titiescribe` está enlazado; falta la URL
  exacta de su página de Facebook.
- **Enlaces de compra.** Ahora las fichas de libro no llevan botón. Decidir si
  enlazan a la editorial, a una librería o a nada.
- **Fecha de *Premura sagrada*.** La biografía y el CV dicen 1986; el listado de
  publicaciones dice 1987. En la web está puesto 1986.
- **Traducción al inglés.** Está hecha entera, pero es traducción nuestra:
  merece que ella la revise, sobre todo la biografía y la cita.

---

## ✅ Hecho

- Estructura completa de la landing con todas las secciones del brief
- Diseño editorial en su paleta (verdes, azules y tierra) con el ocre del logo
- Logotipo integrado en cabecera y pie, extraído en vectorial del PDF
- Biografía, trayectoria y las 12 fichas de libro con datos reales
- Bloque de antologías
- Español e inglés completos (154 claves, sin desajustes)
- WhatsApp flotante y enlace directo
- Galería con ampliación de imagen (teclado y ratón)
- Vídeos que no cargan YouTube hasta que se pulsa reproducir
- Formulario de contacto con antispam
- Sección de descargas
- Aviso legal redactado (a falta de datos)
- Responsive verificado en móvil, sin scroll horizontal
- Tipografías autoalojadas, sin peticiones a Google
- Accesibilidad: navegación por teclado, foco visible, `prefers-reduced-motion`
