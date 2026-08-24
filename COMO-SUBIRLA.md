# CALMA · cómo poner la web en Hostinger

La web va como archivos sueltos, **sin WordPress**. Así no hay tema
ni plugins que puedan romperla, que es lo que estaba pasando con el
menú del móvil dentro de Elementor.

## Lo que necesitas

Un solo archivo: **`calma-web-hostinger.zip`** (1,5 MB).
Dentro va `index.html` y la carpeta `assets` con las fotos, los
estilos, el guion y las tipografías.

## Pasos

1. Entra en **hPanel** de Hostinger.
2. Menú de la izquierda → **Archivos** → **Administrador de archivos**.
3. Abre la carpeta **`public_html`**.
4. Botón **Subir** (flecha hacia arriba, arriba a la derecha) y elige
   `calma-web-hostinger.zip`.
5. Cuando termine, **clic derecho sobre el zip → Extraer**. Deja la
   ruta que te propone (`public_html`) y acepta.
6. Borra el zip, que ya no hace falta.

Y ya está. La web se ve en tu dominio.

## Aviso importante

En `public_html` está ahora mismo tu WordPress. Al extraer ahí,
`index.html` convive con `index.php`: **el servidor da preferencia a
`index.html`**, así que tu dominio pasará a mostrar esta web y no la
de WordPress.

Si prefieres probarla antes sin tocar lo que hay:

- En el paso 3, crea una carpeta nueva (botón **Carpeta**), llámala
  `calma`, entra dentro y sube ahí el zip.
- La verás en **tu-dominio.com/calma/**
- Cuando te convenza, movemos los archivos a `public_html` y listo.

## Para volver atrás

Borra `index.html` y la carpeta `assets` de `public_html`. WordPress
vuelve a aparecer solo, sin haber tocado nada suyo.

## Cambios más adelante

Cualquier cambio lo hago yo aquí, te paso el zip nuevo y repites los
pasos 4 y 5 (extraer sobreescribiendo). No hay que tocar nada más.

## Lo que queda pendiente

- La foto de "Sobre mí" **no es Rocío**: es una imagen de archivo.
  Hay que cambiarla por una suya.
- Las fotos del estudio son del render, no del estudio real.
- Aviso legal, privacidad y cookies están sin enlazar en el pie.
