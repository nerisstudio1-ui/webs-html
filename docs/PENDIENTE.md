# Qué falta para cerrar la web

Estado tras recibir el material de la clienta (16 de septiembre de 2026).
Fecha objetivo: **primeros de noviembre**, con la salida del nuevo libro.

---

## 🔴 Bloqueante

### El libro nuevo de noviembre
Es el motivo de la web y sigue siendo el único hueco grande. Falta **todo**:
título, editorial, portada, texto de presentación, fecha exacta y enlace.
Ahora mismo ese bloque se ve con un marcador de posición.

### Un retrato en condiciones
**Este es el punto más delicado.** En el brief ponía «tengo material
profesional», pero de las 48 imágenes recibidas no hay ningún retrato suyo
utilizable a tamaño grande:

- La foto buena —la de la biblioteca, apoyada en la mano— está a **128 × 140
  píxeles**. Es un recorte de miniatura; ampliada se deshace.
- Lo demás son fotos de acto y de viaje, correctas para la galería pero no
  para presidir la portada.

De momento la portada usa la foto del páramo andino, que le va muy bien al
tema de su obra, pero está a 768 px de ancho y ella sale de lejos.

**Lo que hace falta:** o el archivo original de la foto de la biblioteca, o
una sesión de retrato. Si hay presupuesto y tiempo antes de noviembre, una
sesión sencilla cambia la web por completo.

### Dominio y alojamiento
No tiene ninguno de los dos. Hay que decidir dominio
(¿`cristinafalcon.com`?), registrarlo y elegir alojamiento. El DNS tarda en
propagarse: cuanto antes, mejor.

### Datos para el aviso legal
Faltan **NIF, domicilio fiscal y dominio**. El email ya está puesto.

> El CV que mandó lleva su NIE y su dirección particular. Lo he sacado de la
> carpeta del proyecto (`material-privado/`, que está excluida del control de
> versiones). El repositorio es privado, así que no ha habido exposición
> pública, pero esos archivos siguen en el historial de los commits que ella
> subió: si algún día el repositorio se hace público, hay que limpiarlo antes.

---

## 🟠 Importante

### Faltan 7 portadas
Ya están puestas 5: *Ítaca es nunca*, *Premura sagrada*, *Al otro lado*,
*Siwar el jaguar guardián* y *Letras en los cordones*.

Faltan:

| Libro | Editorial | Dónde pedirla |
|---|---|---|
| Memoria errante (2009) | Candaya | candaya.com |
| Borrar el paisaje (2014) | Candaya | candaya.com |
| 1, 2, 3, de repente en… | Edebé | — |
| Peperoncino (2014) | Giunti (Florencia) | — |
| Guías infantiles de España | Susaeta | — |
| La palabra encantada (2017) | CEPLI-UCLM | — |
| Caja de cuentos y aventuras (2006) | F. Turismo de Cuenca | — |

Las dos de Candaya son las más urgentes, porque son poesía y van en la
primera pestaña. Las editoriales suelen darlas en alta si se piden.

### Vídeos
Siguen sin enlaces. El `.MP4` que subió (10 MB) no debería ir en el
repositorio: lo suyo es subirlo a YouTube, aunque sea como «no listado», y
pasarme el enlace. Luego se cambia `data-yt="VIDEO_ID_1"` en `index.html`.

### Descargas
Faltan los archivos de `assets/docs/`: dossier de prensa, biografía en PDF,
fragmento del libro nuevo y ZIP de fotos en alta.

> El dossier de Candaya de *Ítaca es nunca* que mandó serviría muy bien como
> dossier de prensa, si ella está de acuerdo.

### URL de Facebook
Solo tenemos el nombre, «Cristina Falcón». Hace falta la dirección exacta.
Instagram (`@titiescribe`) ya está enlazado.

---

## 🟡 Por confirmar

- **Derechos de la ilustración del logo**, de Giulia Sagramola. Ya está
  acreditada en el pie; confirmar que el encargo cubre el uso web.
- **Las reseñas.** Las seis citas salen del dossier de Candaya y de la reseña
  de Josu Landa. Conviene que ella confirme que puede publicarlas y que la
  atribución es correcta.
- **Fecha de *Premura sagrada*.** La biografía y el CV dicen 1986; el listado
  de publicaciones dice 1987. En la web está 1986.
- **Traducción al inglés.** Está completa, pero es nuestra: merece que ella la
  revise, sobre todo la biografía, la cita y las reseñas traducidas.
- **Pies de foto de la galería.** Los he escrito interpretando las imágenes;
  puede que alguno no acierte con el sitio o el acto.

---

## ✅ Hecho

- Landing completa con todas las secciones del brief
- Diseño editorial en su paleta, con el ocre del logotipo como acento
- Logotipo vectorizado desde el PDF: marca, texto y favicon
- Biografía, trayectoria y 12 fichas de libro con datos reales
- **5 portadas reales** colocadas, sin recortes, alineadas por la base
- **Galería de 10 fotos** en mosaico, con ampliación y pies descriptivos
- **6 reseñas de prensa reales**: La Vanguardia, QuéLeer, Olcades Poesía,
  El Nacional, Ciudad Literaria y Josu Landa
- Enlaces a Candaya, Kalandraka, FCE y Akiara en las fichas
- Bloque de antologías
- Español e inglés completos (174 claves, sin desajustes)
- WhatsApp flotante, galería con teclado, vídeos que no cargan solos
- Formulario con antispam, aviso legal redactado
- Responsive verificado, sin scroll horizontal
- Tipografías autoalojadas, sin peticiones a Google
- Todas las imágenes con dimensiones declaradas (sin saltos de maquetación)
