# CALMA · barre studio — web

Sitio web estático (HTML + CSS + JS, sin dependencias ni build) para **CALMA barre studio**,
estudio boutique de barre en Collado Villalba (Madrid).

## Cómo verla

Abre `index.html` en el navegador. No necesita servidor ni instalación.
(Para publicarla vale cualquier hosting estático: GitHub Pages, Netlify, Vercel…)

## Estructura

```
index.html              todas las secciones de la web
calma-web.html          la web entera en un solo archivo, para subirla a
                        cualquier hosting o a WordPress (se regenera con
                        `python3 build-single-file.py`)
assets/css/fonts.css    tipografías alojadas en el propio proyecto
assets/css/styles.css   estilos (paleta y tipografías del manual de marca)
assets/js/main.js       animaciones e interacciones
assets/fonts/           Cormorant Garamond, Montserrat y Jost en .woff2
assets/img/             imágenes (ahora mismo, placeholders provisionales)
```

## Identidad aplicada

| Color        | HEX       | Uso                                   |
|--------------|-----------|---------------------------------------|
| Cream        | `#F7F1EA` | Fondo principal                       |
| Nude         | `#DCC8B8` | Fondos secundarios                    |
| Powder Pink  | `#E8D3D2` | Sin uso en la web, a petición de la clienta |
| Soft Gold    | `#B89A68` | Sin uso en la web, a petición de la clienta |
| Taupe        | `#8E7C70` | Textos secundarios                    |
| Dark Taupe   | `#3F3936` | Texto principal y secciones oscuras   |

Tipografías: **Instrument Serif** (títulos) y **Montserrat** (textos), servidas desde
`assets/fonts/` — no dependen de Google Fonts, así que se ven igual siempre y la web
carga más rápido. Todas con licencia SIL Open Font (uso comercial permitido).

Para cambiar la tipografía de los titulares basta con editar la variable `--font-display`
al principio de `assets/css/styles.css`. Además de Instrument Serif están descargadas
**Newsreader**, **Jost**, **Instrument Sans**, **Bodoni Moda**, **Marcellus** e **Italiana**.

### Acento de la interfaz

Los detalles (antetítulos, filetes, subrayados, viñetas, estados hover) usan
Taupe en lugar del dorado del manual, porque la clienta prefirió dejar fuera
el dorado y el rosa empolvado. Se controla desde dos variables al principio
de `styles.css`: `--accent` y `--accent-strong`. Para recuperar el dorado
basta con ponerles `#B89A68` y `#9C8154`.

### Dirección visual

Suave y luminosa: esquinas redondeadas, botones de píldora, composición
centrada y mucho aire. El inicio va a pantalla completa con la foto del
estudio, texto y botón en tonos claros sobre un velo cálido.

## Secciones

1. **Inicio** — imagen a pantalla completa, logo, slogan y botón de primera clase gratis
2. **¿Qué es CALMA?** — concepto y filosofía del estudio
3. **Barre** — qué es, para quién es, y los seis conceptos clave
4. **Las clases** — duración, estructura, material y niveles
5. **Tarifas** — primera clase gratis y bonos mensuales
6. **Sobre mí** — presentación personal y trayectoria
7. **El estudio** — mosaico de fotografías del espacio
8. **Preguntas frecuentes**
9. **Contacto y ubicación** — dirección, email, Instagram, reservas y mapa

Además, intercaladas: *Lo que vas a notar* (beneficios), *Para quién es CALMA*
(tres perfiles), *Tu primera clase paso a paso* (cuatro pasos) y una banda de
Instagram antes del contacto.

## Pendiente de la clienta (busca `TODO CLIENTA` en `index.html`)

- [ ] **Fotos reales del estudio** → ahora mismo `hero`, `calma`, `barre`, `clases` y
      `est-1..4` salen de las imágenes que subió la clienta: el hero, `calma` y el
      mosaico de `estudio-render.png`; `barre`, `clases` y `retrato` de las fotos
      `src-*` (los originales se conservan en `assets/img/`).
      Para cambiarlas basta con sustituir los `.jpg` de `assets/img/` con los mismos nombres.
- [ ] **Retrato de la fundadora** → ahora en "Sobre mí" hay una foto de estudio,
      no la suya. Sustituir `assets/img/retrato.jpg` cuando la tenga.
- [x] **Logotipo** → hecho. A partir de `Logo calma barre.jpg` se han generado
      `logo.png` (tinta original, fondo transparente) y `logo-cream.png` (versión clara
      para el pie oscuro). Se usan en cabecera, inicio y pie.
- [x] **Número de WhatsApp** → hecho: 646 20 62 92 (Rocío). Se cambia en la
      variable `WHATSAPP` al principio de `assets/js/main.js`. Si algún día hay
      plataforma de reservas online, se pega en `RESERVAS_URL` (justo debajo)
      y esa manda sobre el WhatsApp.

## Subir la web a un hosting

**Un solo archivo.** `calma-web.html` lleva dentro los estilos, el JavaScript,
las tipografías y las imágenes. Se sube tal cual y funciona: no hay rutas que
se puedan romper. Pesa unos 3,7 MB.

**Por carpetas.** La otra opción es subir `index.html` junto a la carpeta
`assets/` completa, respetando la estructura. Carga más rápido (el navegador
guarda en caché las imágenes y las tipografías por separado) y es lo
recomendable si la web va a tener dominio propio.

Después de cualquier cambio en `index.html`, `assets/css/` o `assets/js/`,
hay que regenerar el archivo único con `python3 build-single-file.py`.
- [ ] **Horarios**, si en algún momento se quieren publicar en la web (ahora no aparecen).
- [ ] **Teléfono**, si quieres que aparezca.

- [ ] **Textos legales**: aviso legal, privacidad y cookies (enlaces del pie).

## Notas

- El formulario de contacto no tiene servidor: abre el gestor de correo del visitante
  con el mensaje ya redactado hacia `Calma.barrestudio@gmail.com`.
  Si se prefiere recibirlo por email automáticamente, se puede conectar a Formspree,
  Netlify Forms o similar cambiando el `action` del `<form>`.
- Todas las animaciones se desactivan solas si el visitante tiene activado
  "reducir movimiento" en su sistema.
