# Cómo ponerla en WordPress

Hay tres caminos. Están de mejor a peor.

---

## 1. Subirla como archivos (recomendado)

Es una web estática: no necesita WordPress para nada. Se sube tal cual y
convive con el WordPress existente en una carpeta aparte.

1. Descomprimir `cristina-falcon-web.zip`.
2. Subir por FTP el **contenido** de la carpeta (no la carpeta) a donde vaya
   a vivir. Por ejemplo `/public_html/cristina/`.
3. Queda en `tudominio.com/cristina/`.

Si la web de Cristina va a ser el sitio principal, se sube a la raíz y punto.
En ese caso WordPress sobra.

**Ventajas:** funciona exactamente como la has visto. Nada se pelea con
nada. Carga rápido.

---

## 2. Bloque HTML personalizado dentro de una página

Para esto está `cristina-falcon-widget.html`. Pero **hay que subir antes las
imágenes y los vídeos**, porque un bloque solo guarda texto.

1. **Subir los medios.** En WordPress, *Medios → Añadir nuevo*, y subir todo
   lo que hay en `assets/img/` y `assets/video/`. Son unos 30 archivos.

   > Cuidado: WordPress cambia el nombre si ya existe otro igual, y les pone
   > la fecha en la ruta. Conviene subirlos de una vez y anotar la carpeta
   > que sale, del tipo `/wp-content/uploads/2026/11/`.

2. **Poner esa ruta en el archivo.** Abrir `cristina-falcon-widget.html` con
   un editor de texto y sustituir todas las apariciones de
   `https://TU-DOMINIO.com/wp-content/uploads/cristina/` por la ruta real.

3. **Pegar.** Crear una página, añadir un bloque *HTML personalizado* y pegar
   dentro todo el archivo.

4. **Quitarle al tema la cabecera y el pie** en esa página, o usar una
   plantilla en blanco. Si no, la web aparece embutida entre el menú y el pie
   del tema, y queda rarísimo.

**Lo que se pierde por este camino:**

- La cabecera deja de ir fija: se queda quieta arriba del bloque. Si fuera
  fija se saldría del bloque y se plantaría encima del menú del tema.
- La portada baja de pantalla completa a un 82% de alto, porque encima hay
  cabecera del tema y debajo, pie.
- El aviso legal enlaza a un archivo aparte que en este montaje no existe:
  hay que crear esa página en WordPress y corregir el enlace.
- Cualquier plugin de caché o de optimización que toque el CSS o el JS puede
  romperlo. Es lo que más falla en la práctica.

Los estilos van todos encerrados bajo `#cfm-web`, así que **no tocan el
tema**: eso está comprobado.

---

## 3. Un solo archivo, todo dentro

`cristina-falcon-completa.html` lleva estilos, guiones, tipografías e
imágenes dentro del propio archivo, en base64. Se abre con doble clic y
funciona sin servidor.

Pesa **4,8 MB** y no vale para un bloque de WordPress: el editor se atraganta
con un pegado así de grande.

Sirve para otra cosa: enseñárselo a Cristina por email, o guardarlo como
copia de cómo quedó. Los vídeos no van dentro (pesan 12 MB), así que esos
siguen enlazados.

---

## Qué haría yo

Registrar el dominio y subir la web por FTP, camino 1. Son diez minutos y
queda tal como se diseñó.

Meter una landing de pantalla completa dentro de un bloque de WordPress es
pelearse con el tema para siempre: cada actualización del tema o cada plugin
de caché puede descolocarla.
