# Guardar las consultas del formulario en Google Sheets

Con esto, cada vez que alguien envíe el formulario de contacto de la web, se añade una fila a una hoja de Google Sheets (se abre y se descarga como Excel) y llega un aviso por correo. El formulario sigue abriendo WhatsApp o el correo como hasta ahora.

Se hace una sola vez y lo tiene que hacer quien tenga la cuenta de Google donde se quieran guardar las consultas (la de Patricia).

## 1. Crear la hoja

1. Entrar en **sheets.google.com** con la cuenta de Google y crear una hoja en blanco. Ponerle nombre, por ejemplo «Consultas web MOA».
2. Menú **Extensiones → Apps Script**. Se abre una pestaña con un editor de código.
3. Borrar todo lo que haya y pegar el contenido de **`google-sheets/Codigo.gs`**.
4. Si el aviso debe llegar a otro correo, cambiarlo en la línea `var AVISO_EMAIL = ...`. Para no recibir avisos, dejarlo así: `var AVISO_EMAIL = '';`
5. Guardar (icono del disquete).

## 2. Publicarla como aplicación web

1. Botón azul **Implementar → Nueva implementación**.
2. En el engranaje de «Seleccionar tipo», elegir **Aplicación web**.
3. Rellenar:
   - Descripción: `Formulario web MOA`
   - Ejecutar como: **Yo**
   - Quién tiene acceso: **Cualquier usuario**
4. **Implementar**. Google pedirá autorizar el acceso: elegir la cuenta → «Configuración avanzada» → «Ir a … (no seguro)» → **Permitir**. (El aviso sale porque el script lo has creado tú y no está verificado por Google; es normal.)
5. Copiar la **URL de la aplicación web**. Es algo como `https://script.google.com/macros/s/AKfy…/exec`.

## 3. Conectarla a la web

Pasarme esa URL. La pongo en `SHEET_URL`, dentro de `build.py`, regenero los archivos de WordPress y se vuelven a pegar.

## Qué se guarda

Fecha, nombre, teléfono (si lo ha puesto), servicio, mensaje, si lo envió por WhatsApp o por correo, el idioma y la página.

## Protección de datos

En la hoja se guardan datos personales. Conviene:

- Mencionarlo en la política de privacidad (qué datos, para qué, cuánto tiempo y que se guardan en Google).
- No compartir la hoja con nadie que no los necesite.
- Borrar de vez en cuando las consultas antiguas que ya no hagan falta.
