# CALMA · barre studio — web

Sitio web estático (HTML + CSS + JS, sin dependencias ni build) para **CALMA barre studio**,
estudio boutique de barre en Collado Villalba (Madrid).

## Cómo verla

Abre `index.html` en el navegador. No necesita servidor ni instalación.
(Para publicarla vale cualquier hosting estático: GitHub Pages, Netlify, Vercel…)

## Estructura

```
index.html              todas las secciones de la web
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
| Powder Pink  | `#E8D3D2` | Detalles y acentos                    |
| Soft Gold    | `#B89A68` | Líneas, iconos y detalles premium     |
| Taupe        | `#8E7C70` | Textos secundarios                    |
| Dark Taupe   | `#3F3936` | Texto principal y secciones oscuras   |

Tipografías: **Instrument Serif** (títulos) y **Montserrat** (textos), servidas desde
`assets/fonts/` — no dependen de Google Fonts, así que se ven igual siempre y la web
carga más rápido. Todas con licencia SIL Open Font (uso comercial permitido).

Para cambiar la tipografía de los titulares basta con editar la variable `--font-display`
al principio de `assets/css/styles.css`. Además de Instrument Serif están descargadas
**Newsreader**, **Jost**, **Instrument Sans**, **Bodoni Moda**, **Marcellus** e **Italiana**.

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

## Pendiente de la clienta (busca `TODO CLIENTA` en `index.html`)

- [ ] **Fotos reales del estudio** → ahora mismo `hero`, `calma`, `barre`, `clases` y
      `est-1..4` son recortes de `estudio-render.png` (la imagen que subió la clienta).
      Para cambiarlas basta con sustituir los `.jpg` de `assets/img/` con los mismos nombres.
- [ ] **Retrato** de la fundadora → `assets/img/retrato.svg`, y quitar el `<figcaption>Foto próximamente</figcaption>`.
- [x] **Logotipo** → hecho. A partir de `Logo calma barre.jpg` se han generado
      `logo.png` (tinta original, fondo transparente) y `logo-cream.png` (versión clara
      para el pie oscuro). Se usan en cabecera, inicio y pie.
- [ ] **Enlace de reservas** → se cambia en UN solo sitio: la variable `RESERVAS_URL`
      al principio de `assets/js/main.js`. Todos los botones "Primera clase gratis"
      pasan a apuntar ahí automáticamente.
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
