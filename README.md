# Cristina Falcón Maldonado — web de autora

Landing page estática (HTML + CSS + JavaScript, sin frameworks ni build) para
la escritora **Cristina Falcón Maldonado**: poeta, narradora y traductora.

Proyecto de [Neris Studio](https://nerisstudio.com) · Ref. brief NW-260916-DO8W

---

## Cómo verla en local

No hace falta compilar nada. Basta con servir la carpeta:

```bash
python3 -m http.server 8000
# abrir http://localhost:8000
```

Abrir `index.html` directamente con doble clic también funciona, aunque el
formulario de contacto necesita servidor para enviar.

---

## Estructura

```
index.html              La página entera
aviso-legal.html        Aviso legal y privacidad
assets/
  css/
    styles.css          Todos los estilos (comentado por secciones)
    fonts.css           Tipografías autoalojadas
  fonts/                Archivos .woff2 (Playfair Display, Inter, Caveat)
  js/
    config.js           ← Teléfono, email y ajustes. EMPIEZA POR AQUÍ
    i18n.js             ← Todos los textos, en español e inglés
    main.js             Comportamiento (menú, idioma, galería, formulario…)
  img/
    logo.svg            Logotipo completo (ilustración de Giulia Sagramola)
    logo-marca.svg      Solo la ilustración
    logo-texto.svg      Solo el texto del logotipo
    perfil/             Fotos de la autora
    obra/               Portadas de los libros y miniaturas de vídeo
    galeria/            Fotos de la galería
  docs/                 PDFs descargables (dossier, biografía…)
```

### Dónde se cambia cada cosa

| Quiero cambiar… | Archivo |
|---|---|
| Cualquier texto (ES o EN) | `assets/js/i18n.js` |
| Teléfono de WhatsApp o email | `assets/js/config.js` |
| Colores y tipografías | `assets/css/styles.css`, bloque `:root` |
| Fotos | Sustituir el archivo en `assets/img/` con el mismo nombre |
| Vídeos de YouTube | `index.html`, atributo `data-yt="ID_DEL_VIDEO"` |

---

## Idiomas

La web está en español e inglés. El idioma se elige así, por orden:

1. El parámetro `?lang=en` en la URL (útil para compartir enlaces).
2. El último idioma elegido, guardado en el navegador.
3. El idioma del navegador.
4. Español.

Para añadir o cambiar un texto hay que editarlo en **los dos idiomas** dentro
de `assets/js/i18n.js`. Si falta una clave en inglés, esa frase se queda en
español en lugar de desaparecer.

---

## Formulario de contacto

Usa [FormSubmit](https://formsubmit.co), que no necesita servidor propio.

**Para activarlo (una sola vez):**

1. Poner el email de destino en `assets/js/config.js`.
2. Enviar un mensaje de prueba desde la web ya publicada.
3. FormSubmit manda un correo de confirmación a ese email: hay que pulsar el
   enlace. A partir de ahí, los mensajes llegan solos.

Lleva un campo trampa antispam (`_honey`) invisible para las personas.

---

## Privacidad y RGPD

- Las **tipografías están autoalojadas**: no se hace ninguna petición a
  servidores de Google, que es lo que exige la normativa europea.
- Los **vídeos de YouTube no se cargan hasta que alguien pulsa reproducir**, y
  se sirven desde `youtube-nocookie.com`.
- La web **no usa cookies** de seguimiento ni analítica. Lo único que guarda en
  el navegador es el idioma elegido.
- `aviso-legal.html` está redactado pero **le faltan los datos de la titular**
  (NIF, domicilio fiscal, email y dominio). Hay que completarlo antes de publicar.

---

## Publicación

Al ser una web estática vale cualquier alojamiento. Opciones, de más simple a
más completa:

- **Netlify** o **Cloudflare Pages**: se conecta el repositorio y se publica
  solo en cada cambio. Gratis, HTTPS incluido, dominio propio configurable.
- **GitHub Pages**: gratis, directamente desde este repositorio.
- **Hosting clásico** (Hostinger, Webempresa…): subir la carpeta por FTP.

La clienta **no tiene dominio ni hosting**, así que hay que registrar el
dominio y decidir alojamiento antes de la fecha de publicación.

---

## Compatibilidad

Funciona en las versiones actuales de Chrome, Firefox, Safari y Edge, en
escritorio y móvil. Usa `color-mix()` y propiedades modernas de CSS
(disponibles en todos los navegadores desde 2023).

Sin JavaScript la página se sigue viendo y leyendo entera en español; lo que se
pierde es el cambio de idioma, la galería ampliada y el envío del formulario.
