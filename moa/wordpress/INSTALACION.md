# MOA en WordPress · cómo pegarla

Tres archivos, uno por idioma. Cada uno lleva **todo dentro** (estilos, animaciones, logos y la foto de Patricia), así que no hay que subir nada por FTP: se abre, se copia y se pega.

| Archivo | Idioma | Página de WordPress |
|---|---|---|
| `moa-wordpress-ca.html` | Català | Página de inicio (`/`) |
| `moa-wordpress-es.html` | Castellano | Página con el slug `es` (`/es/`) |
| `moa-wordpress-en.html` | English | Página con el slug `en` (`/en/`) |

## 1. Crear las tres páginas

Para cada idioma:

1. **Páginas → Añadir nueva**. Título: `MOA` (o `MOA · ES`, `MOA · EN`; el título no se ve).
2. A la derecha, en **Plantilla**, elige la que no tenga cabecera ni pie del tema: suele llamarse *Lienzo en blanco*, *Ancho completo sin título*, *Blank* o, con Elementor, *Elementor Canvas*. MOA trae su propia cabecera y su propio pie; con la plantilla normal saldrían duplicados.
3. Añade un bloque **HTML personalizado** (el icono `</>`).
4. Abre el archivo del idioma con un editor de texto (Bloc de notas, TextEdit, VS Code… **no Word**), `Ctrl+A`, `Ctrl+C`, y pégalo en el bloque.
5. En **Enlace permanente** pon el slug: nada para el catalán, `es` para el castellano y `en` para el inglés.
6. **Publicar**.

Después: **Ajustes → Lectura → Tu página de inicio muestra: una página estática → Portada:** la página en catalán.

> Con **Elementor**: en vez del bloque HTML personalizado, arrastra el widget **HTML** a una sección de ancho completo y pega ahí. El resto es igual.

## 2. Vaciar la caché

Si tienes un plugin de caché (LiteSpeed, WP Rocket, W3 Total Cache…) o la caché de Hostinger, **purga la caché** después de publicar. Si no, la web pública puede seguir mostrando la versión anterior durante horas.

Para saber qué versión está publicada: en la web, `Ctrl+U` (ver código fuente) y busca `Generado`. Sale la fecha y hora de cuando se creó el archivo.

## 3. Si se ve raro

- **La cabecera de MOA queda tapada al bajar.** El tema tiene una cabecera fija propia (pasa si no se ha podido elegir una plantilla en blanco). Busca en el archivo `--moa-top:0px;` y pon la altura de la cabecera del tema, por ejemplo `--moa-top:80px;`.
- **Las animaciones no salen pero el contenido se ve entero.** Algún plugin de optimización está aplazando o combinando el JavaScript. La web está preparada para mostrarse completa igualmente; si quieres las animaciones, excluye esta página de la opción *"Retrasar / diferir JavaScript"* del plugin.
- **Aparecen párrafos vacíos o etiquetas `<p>` sueltas.** Se ha pegado en el bloque *Párrafo* o en el editor visual. Tiene que ser el bloque *HTML personalizado* (o el widget *HTML* de Elementor).

## 4. Vídeo de portada (cuando lo tengamos)

1. Sube el `.mp4` a **Medios → Añadir nuevo** y copia su URL (algo como `/wp-content/uploads/2026/11/portada.mp4`).
2. Pásamela: la pongo en `VIDEO_PORTADA`, dentro de `build_wordpress.py`, y regenero los tres archivos.

El vídeo no va dentro del archivo a propósito: varios MB de vídeo en una página de WordPress harían el editor lentísimo.

## 5. Cookies y avisos legales

La web carga contenido de terceros que hay que declarar en el aviso de cookies:

- **Instagram** (los dos vídeos incrustados). Instagram puede instalar cookies propias al cargarlos.
- **Google Fonts** (tipografías Bricolage Grotesque y Montserrat).

Para cumplir con el RGPD y la LSSI conviene un banner de cookies (Complianz o CookieYes, en la configuración de WordPress). También faltan las páginas de aviso legal, privacidad y cookies.

## 6. Cambios más adelante

No se editan estos archivos a mano. Los textos están en `src/i18n.py` y el diseño en `src/template.html`; después se ejecuta:

    python3 build.py
    python3 build_wordpress.py

y se vuelve a pegar el archivo del idioma que haya cambiado (sustituyendo todo el contenido del bloque).

## Bueno saber

- Cada archivo pesa unos 660 KB porque lleva los logos y la foto dentro. Se guarda en la base de datos de WordPress, así que el editor puede tardar un segundo más en abrir esa página. Para la visita no hay diferencia apreciable.
- Todo el código va dentro de `<div id="moa-app">` con estilos encapsulados: no cambia nada del resto del sitio y el tema no puede descolocar la web de MOA. Se ha probado dentro de un tema con estilos que chocan a propósito (otros tamaños de letra, botones forzados con `!important`, columnas estrechas): se ve igual que la web suelta.
- El formulario de contacto abre WhatsApp o el correo con el mensaje ya escrito; no necesita ningún plugin.
