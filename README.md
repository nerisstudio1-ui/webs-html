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

Tipografías: **Cormorant Garamond** (títulos) y **Montserrat** (textos), servidas desde
`assets/fonts/` — no dependen de Google Fonts, así que se ven igual siempre y la web
carga más rápido. Para el logotipo se usa **Jost Thin**, la tipografía libre más parecida
al logo original. Las tres tienen licencia SIL Open Font (uso comercial permitido).

## Secciones

Anuncio · Hero · Franja de valores · El estudio · Qué es barre · Clases ·
Cita de marca · Horarios · Tarifas · Sobre mí · Galería · FAQ · Contacto · Pie.

## Pendiente de la clienta (busca `TODO CLIENTA` en `index.html`)

- [ ] **Fotos reales** → sustituir los `.svg` de `assets/img/` (mismos nombres, o cambiar el `src`).
- [ ] **Retrato** de la fundadora → `assets/img/retrato.svg`, y quitar el `<figcaption>Foto próximamente</figcaption>`.
- [ ] **Logotipo** → ahora está recompuesto con Jost Thin. Para usar el archivo original,
      guardarlo como `assets/img/logo.svg` y sustituir el bloque `.logo` de la cabecera
      por `<img src="assets/img/logo.svg" alt="CALMA barre studio" width="180">`
      (hay un comentario en el HTML justo encima indicándolo).
- [ ] **Enlace de reservas** → hay 3 sitios marcados con `TODO`; hoy apuntan a `#contacto`.
- [ ] **Horarios reales** (sección `#horarios`, la estructura ya está lista).
- [ ] **Tarifas definitivas** (sección `#tarifas`; los importes actuales son orientativos).
- [ ] **Dirección exacta y teléfono** (sección `#contacto`).
- [ ] **Textos legales**: aviso legal, privacidad y cookies (enlaces del pie).

## Notas

- El formulario de contacto no tiene servidor: abre el gestor de correo del visitante
  con el mensaje ya redactado hacia `Calma.barrestudio@gmail.com`.
  Si se prefiere recibirlo por email automáticamente, se puede conectar a Formspree,
  Netlify Forms o similar cambiando el `action` del `<form>`.
- Todas las animaciones se desactivan solas si el visitante tiene activado
  "reducir movimiento" en su sistema.
