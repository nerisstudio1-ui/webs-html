# -*- coding: utf-8 -*-
"""Generador estático de la web de ANAHATA.
   Edita el contenido aquí y ejecuta:  python3 _build.py
   Salida: los .html de la raíz del proyecto."""
import os, re

# ============================ DATOS DEL NEGOCIO ============================
MARCA     = "ANAHATA"
TITULAR   = "Sara Viñas Gómez"
EMAIL     = "saravgyoga@gmail.com"
TEL       = "664607474"                 # confirmado por Sara (correo del 18/09)
TEL_FMT   = "664 60 74 74"
WA        = "34" + TEL
WA_MSG    = "Hola%20Sara%2C%20me%20gustar%C3%ADa%20informarme%20sobre%20las%20clases%20de%20ANAHATA"
WA_URL    = f"https://wa.me/{WA}?text={WA_MSG}"
IG        = "https://www.instagram.com/saravgyoga/"
FB        = "https://www.facebook.com/people/Sara-Vinas-G%C3%B3mez/pfbid06JHJpnUKVaPrk51RJiH3VkkNQhAaW25DX8NyPRMMUbtA3BUvygtoCdssqahxWKQLl/"
DOMINIO   = "https://www.saravgyoga.com"
CIUDAD    = "Barcelona"

# ============================== ICONOS =====================================
I = {
 "grupo":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="7" r="3"/><circle cx="17" cy="8" r="2.3"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><path d="M16.5 14.5c2.6.3 4.5 2.2 4.5 5"/></svg>',
 "persona":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="7.5" r="3.4"/><path d="M4.5 20.5c0-4 3.4-6.8 7.5-6.8s7.5 2.8 7.5 6.8"/></svg>',
 "casa":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 10.5 12 3.5l8.5 7"/><path d="M5.5 9.8V20h13V9.8"/><path d="M10 20v-5.5h4V20"/></svg>',
 "hoja":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><path d="M20 4c0 8-4.6 13-11 13-1.6 0-3-.3-4.2-.9C6.3 9.3 12 4.7 20 4Z"/><path d="M4 20c1.5-4 4-7 8-9.2"/></svg>',
 "online":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="4.5" width="19" height="13" rx="2"/><path d="M8.5 21h7M12 17.5V21"/></svg>',
 "loto":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19c-4 0-7.5-2.4-9-6 2.6-.6 4.9 0 6.6 1.4"/><path d="M12 19c4 0 7.5-2.4 9-6-2.6-.6-4.9 0-6.6 1.4"/><path d="M12 19c-2.4-2-3.6-4.4-3.6-7.2 0-2.6 1.2-5 3.6-6.8 2.4 1.8 3.6 4.2 3.6 6.8 0 2.8-1.2 5.2-3.6 7.2Z"/></svg>',
 "sobre":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="m3.5 6.5 8.5 6 8.5-6"/></svg>',
 "tel":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h3l1.5 4-2.2 1.6a12 12 0 0 0 5.6 5.6l1.6-2.2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2Z"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/></svg>',
 "reloj":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 1.8"/></svg>',
 "ig":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="1.1" fill="currentColor" stroke="none"/></svg>',
 "fb":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.25-1.5 1.55-1.5H16.7V3.6c-.29-.04-1.27-.12-2.41-.12-2.39 0-4.02 1.46-4.02 4.13V9.9H7.5V13h2.77v8h3.23Z"/></svg>',
 "wa":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.6 2 2.2 6.4 2.2 11.84c0 1.74.46 3.44 1.32 4.94L2.1 22l5.35-1.4a9.8 9.8 0 0 0 4.59 1.16h.01c5.43 0 9.84-4.4 9.84-9.84 0-2.63-1.02-5.1-2.88-6.96A9.77 9.77 0 0 0 12.04 2Zm0 17.9h-.01a8.2 8.2 0 0 1-4.15-1.14l-.3-.18-3.08.81.82-3.01-.2-.31a8.15 8.15 0 0 1-1.25-4.36c0-4.51 3.67-8.18 8.18-8.18a8.13 8.13 0 0 1 8.17 8.19c0 4.51-3.67 8.18-8.18 8.18Zm4.49-6.13c-.25-.12-1.46-.72-1.68-.8-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.15.16-.29.18-.53.06-.25-.13-1.04-.39-1.98-1.22-.73-.65-1.23-1.46-1.37-1.7-.14-.25-.02-.38.11-.5.11-.12.25-.29.37-.44.12-.15.16-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.86.84-.86 2.05s.89 2.38 1.01 2.54c.12.17 1.74 2.66 4.22 3.73.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.47-.07 1.46-.6 1.66-1.18.21-.58.21-1.07.15-1.17-.06-.11-.22-.17-.47-.29Z"/></svg>',
 "flecha":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M13 6.5 18.5 12 13 17.5"/></svg>',
 "corazon":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 20.5C6.5 16.4 3 13.2 3 9.6 3 6.9 5.1 5 7.6 5c1.7 0 3.4.9 4.4 2.4C13 5.9 14.7 5 16.4 5 18.9 5 21 6.9 21 9.6c0 3.6-3.5 6.8-9 10.9Z"/></svg>',
}

NAV = [
    ("index.html",     "Inicio"),
    ("sobre-mi.html",  "Sobre mí"),
    ("servicios.html", "Servicios"),
    ("clases.html",    "Clases y programas"),
    ("retiros.html",   "Retiros y eventos"),
    ("contacto.html",  "Contacto"),
]

# ============================== PLANTILLAS =================================
def head(titulo, desc, pagina, og="assets/img/logo-anahata.svg"):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{TITULAR}">
<meta name="theme-color" content="#3C4A31">
<link rel="canonical" href="{DOMINIO}/{pagina}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{MARCA}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMINIO}/{pagina}">
<meta property="og:image" content="{DOMINIO}/{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="saltar-al-contenido" href="#contenido">Saltar al contenido</a>'''

def aviso():
    return f'''
<div class="aviso" data-aviso>
  <span>Clases de yoga y pilates en {CIUDAD}, a domicilio y online · Nuevos retiros y talleres cada temporada.
  <a href="retiros.html">Ver próximas fechas</a></span>
  <button class="aviso__cerrar" type="button" aria-label="Cerrar aviso" data-cerrar-aviso>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>
  </button>
</div>'''

def cabecera(activa, sobre_imagen=False):
    clase = "cabecera cabecera--transparente" if sobre_imagen else "cabecera cabecera--solida"
    marca_actual = ' aria-current="page"'
    enlaces = "".join(
        '<a href="%s"%s>%s</a>' % (h, marca_actual if h == activa else "", t)
        for h, t in NAV[:-1])
    menu_movil = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''
<header class="{clase}" data-cabecera>
  <div class="cabecera__interior">
    <button class="hamburguesa" type="button" aria-label="Abrir menú" aria-expanded="false" data-menu-boton>
      <span></span><span></span><span></span>
    </button>
    <nav class="nav nav--principal" aria-label="Navegación principal">{enlaces}</nav>
    <a class="logo" href="index.html" aria-label="{MARCA} · inicio">
      <img class="logo__simbolo logo__simbolo--color" src="assets/img/logo-marca.svg" alt="" width="34" height="34">
      <img class="logo__simbolo logo__simbolo--crema" src="assets/img/logo-marca-crema.svg" alt="" width="34" height="34">
      <span class="logo__texto">{MARCA}</span>
    </a>
    <nav class="nav nav--fin" aria-label="Acciones">
      <a class="nav-enlace" href="contacto.html"{marca_actual if activa == "contacto.html" else ""}>Contacto</a>
      <a class="btn btn--linea" href="contacto.html#reservar">Reservar</a>
    </nav>
  </div>
</header>
<nav class="menu-movil" data-menu aria-label="Menú">
  {menu_movil}
  <a class="btn btn--solido" href="contacto.html#reservar">Reservar tu clase</a>
  <div class="menu-movil__pie">
    <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
    <a href="{WA_URL}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</nav>'''

def pie():
    servicios = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in [
        ("servicios.html", "Yoga"), ("servicios.html#pilates", "Pilates Mat"),
        ("servicios.html#meditacion", "Meditación y pranayamas"),
        ("servicios.html#alimentacion", "Alimentación saludable"),
        ("clases.html", "Clases y programas"), ("retiros.html", "Retiros y talleres")])
    return f'''
<footer class="pie">
  <div class="contenedor">
    <div class="pie__grid">
      <div>
        <img class="pie__logo" src="assets/img/logo-anahata-crema.svg" alt="{MARCA}" width="150" height="265" loading="lazy">
        <p>Yoga, pilates y meditación para acompañarte hacia una vida más consciente, equilibrada y plena.</p>
        <div class="redes">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{I["ig"]}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I["fb"]}</a>
          <a href="{WA_URL}" target="_blank" rel="noopener" aria-label="WhatsApp">{I["wa"]}</a>
        </div>
      </div>
      <div>
        <h4>Navegación</h4>
        <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)}</ul>
      </div>
      <div>
        <h4>Prácticas</h4>
        <ul>{servicios}</ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:+34{TEL}">{TEL_FMT}</a></li>
          <li>{CIUDAD} · a domicilio · online</li>
          <li>Retiros en todo el territorio nacional</li>
        </ul>
      </div>
    </div>
    <div class="pie__legal">
      <p>© <span data-anio>2026</span> {MARCA} · {TITULAR}</p>
      <nav aria-label="Legal">
        <a href="aviso-legal.html">Aviso legal</a>
        <a href="privacidad.html">Política de privacidad</a>
        <a href="privacidad.html#cookies">Cookies</a>
      </nav>
    </div>
  </div>
</footer>
<a class="whatsapp" href="{WA_URL}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{I["wa"]}</a>
<script src="assets/js/main.js" defer></script>
</body>
</html>'''

def orn():
    return f'<div class="ornamento">{I["corazon"]}</div>'

def hero_interior(titulo, bajada, imagen, alt):
    return f'''
<section class="hero hero--interior">
  <div class="hero__media"><img src="assets/img/{imagen}" alt="{alt}" width="1920" height="900" fetchpriority="high"></div>
  <div class="contenedor">
    <div class="hero__contenido">
      <p class="miga"><a href="index.html">Inicio</a> · {titulo}</p>
      <h1>{titulo}</h1>
      <p>{bajada}</p>
    </div>
  </div>
</section>'''

def franja_cta(titulo, texto, imagen="cta-banner.svg"):
    return f'''
<section class="franja">
  <div class="franja__media"><img src="assets/img/{imagen}" alt="" loading="lazy" width="1920" height="900"></div>
  <div class="contenedor franja__contenido revelar">
    <h2>{titulo}</h2>
    <p class="lead">{texto}</p>
    <div class="botonera botonera--centro mt-l">
      <a class="btn btn--claro" href="contacto.html#reservar">Reservar tu clase</a>
      <a class="btn btn--linea-clara" href="{WA_URL}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
    </div>
  </div>
</section>'''

def escribir(nombre, html):
    with open(nombre, "w", encoding="utf-8") as f:
        f.write(re.sub(r"\n{3,}", "\n\n", html).strip() + "\n")

# =============================== INICIO ====================================
JSONLD = f'''
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "@id": "{DOMINIO}/#anahata",
  "name": "{MARCA}",
  "alternateName": "{TITULAR} · Yoga y Pilates",
  "description": "Clases de yoga, pilates y meditación en {CIUDAD}, a domicilio, al aire libre y online. Retiros, talleres y programas de bienestar integral.",
  "url": "{DOMINIO}",
  "email": "{EMAIL}",
  "telephone": "+34{TEL}",
  "image": "{DOMINIO}/assets/img/logo-anahata.svg",
  "founder": {{ "@type": "Person", "name": "{TITULAR}" }},
  "areaServed": ["{CIUDAD}", "Cataluña", "País Vasco", "Cantabria", "Comunidad Valenciana", "Andalucía"],
  "address": {{ "@type": "PostalAddress", "addressLocality": "{CIUDAD}", "addressCountry": "ES" }},
  "sameAs": ["{IG}", "{FB}"],
  "knowsAbout": ["Yoga Integral", "Ashtanga Yoga", "Vinyasa Yoga", "Yin Yoga", "Pilates Mat", "Meditación", "Pranayama", "Alimentación saludable"]
}}
</script>'''

PILARES = [
    ("pilar-yoga.svg", "Movimiento consciente",
     "Yoga Integral, Ashtanga, Vinyasa, Yin y Pilates Mat con implementos. Fuerza, movilidad y presencia en cada práctica.",
     "servicios.html", "Descubrir las prácticas"),
    ("pilar-meditacion.svg", "Meditación y pranayamas",
     "Respiración consciente y quietud guiada para calmar la mente, regular el sistema nervioso y volver a tu centro.",
     "servicios.html#meditacion", "Aprender a respirar"),
    ("pilar-programas.svg", "Retiros y programas",
     "Retiros de fin de semana, talleres temáticos, membresías y el reto de 21 días para crear constancia y transformación.",
     "retiros.html", "Ver experiencias"),
]

MODALIDADES = [
    ("grupo", "Clases grupales",
     f"Sesiones en grupo donde se crea una energía compartida, motivadora y cercana. Ideales para quienes disfrutan del movimiento en comunidad y buscan constancia y acompañamiento. Imparto en diferentes espacios compartidos de {CIUDAD}."),
    ("persona", "Sesiones personalizadas",
     f"Clases individuales adaptadas a tus necesidades, objetivos y ritmo. Un espacio íntimo para profundizar, corregir, avanzar y trabajar desde la atención plena, en diferentes espacios compartidos de {CIUDAD}."),
    ("casa", "A domicilio",
     "Sesiones privadas en la comodidad de tu hogar. Perfectas para quienes prefieren practicar sin desplazamientos y en su propio espacio."),
    ("hoja", "Clases al aire libre",
     "Prácticas en entornos naturales que potencian la conexión, la energía y la sensación de libertad. Yoga, pilates y meditación en contacto con la naturaleza."),
    ("online", "Clases online",
     "Sesiones en directo o grabadas para que puedas practicar desde cualquier lugar del mundo. Flexibles, accesibles y pensadas para acompañarte en tu día a día."),
]

def bloque_modalidades(titulo=True):
    items = "".join(f'''
      <article class="modalidad revelar">
        <div class="modalidad__icono">{I[ic]}</div>
        <div><h4>{t}</h4><p>{d}</p></div>
      </article>''' for ic, t, d in MODALIDADES)
    cab = '''
    <div class="texto-centrado medida" style="margin-bottom:clamp(30px,4vw,56px)">
      <span class="eyebrow">Modalidades</span>
      <h2>Practica donde y como mejor te acompañe</h2>
      <p class="lead" style="margin-top:1.2rem">Cada persona y cada momento piden algo distinto. Elige el formato que encaje con tu vida.</p>
    </div>''' if titulo else ""
    return f'''
<section class="seccion" id="modalidades">
  <div class="contenedor">
    {cab}
    <div class="medida">{items}</div>
  </div>
</section>'''

# Testimonios: marcadores a la espera de las reseñas reales de Google.
TESTIMONIOS = [
    ("Pendiente de recibir", "Reseña de Google"),
    ("Pendiente de recibir", "Reseña de Google"),
    ("Pendiente de recibir", "Reseña de Google"),
]
def bloque_testimonios():
    tarjetas = "".join(f'''
      <article class="testimonio">
        <div class="testimonio__estrellas" aria-label="5 sobre 5">★★★★★</div>
        <p>«{txt}»</p>
        <div class="testimonio__autor">{autor}</div>
      </article>''' for txt, autor in TESTIMONIOS)
    return f'''
<section class="seccion seccion--crema" id="opiniones">
  <div class="contenedor">
    <div class="texto-centrado medida" style="margin-bottom:clamp(30px,4vw,56px)">
      {orn()}
      <span class="eyebrow">Opiniones</span>
      <h2>Lo que cuentan quienes practican conmigo</h2>
    </div>
    <div class="revelar" data-carrusel>
      <div class="testimonios">{tarjetas}</div>
      <div class="carrusel-controles">
        <button type="button" aria-label="Anterior" data-carrusel-anterior>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H6M11 5.5 5 12l6 6.5"/></svg>
        </button>
        <button type="button" aria-label="Siguiente" data-carrusel-siguiente>{I["flecha"]}</button>
      </div>
    </div>
  </div>
</section>'''

def bloque_newsletter():
    return f'''
<section class="seccion seccion--compacta seccion--verde">
  <div class="contenedor duo" style="align-items:center">
    <div class="revelar">
      <span class="eyebrow">Newsletter</span>
      <h2>Respira con nosotras cada mes</h2>
      <p class="lead" style="margin-top:1rem">Recibe las próximas fechas de clases, retiros y talleres, además de prácticas sencillas para cuidarte en tu día a día.</p>
    </div>
    <div class="revelar" data-retardo="120">
      <form class="newsletter" data-formulario novalidate>
        <label class="solo-lectores" for="news-email">Tu correo electrónico</label>
        <input id="news-email" type="email" name="email" placeholder="tu@email.com" required autocomplete="email">
        <button class="btn btn--oro" type="submit">Suscribirme</button>
        <p class="nota-formulario" style="color:#CFCBBC;flex:1 1 100%">Sin spam. Puedes darte de baja cuando quieras.</p>
        <p class="nota-formulario" style="color:#EBD5A8;flex:1 1 100%" data-aviso-form hidden></p>
      </form>
    </div>
  </div>
</section>'''

def bloque_zonas(verde=False):
    zonas = "".join(f'<span class="zona">{z}</span>' for z in
                    ["País Vasco", "Cantabria", "Cataluña", "Comunidad Valenciana", "Andalucía"])
    clase = "seccion seccion--verde" if verde else "seccion seccion--arena"
    return f'''
<section class="{clase}" id="zonas">
  <div class="contenedor duo">
    <div class="revelar">
      <span class="eyebrow">Dónde practicamos</span>
      <h2>Clases en {CIUDAD} y retiros por toda España</h2>
      <p style="margin-top:1.2rem">Imparto clases de yoga, pilates y meditación en el área de {CIUDAD}, en diferentes espacios de bienestar y también en formato individual para quienes buscan un acompañamiento más íntimo y adaptado.</p>
      <p>Y si prefieres practicar desde casa, las clases online llegan a cualquier rincón del mundo.</p>
    </div>
    <div class="revelar" data-retardo="120">
      <h4 style="margin-bottom:1.2rem">Retiros y eventos</h4>
      <div class="zonas">{zonas}</div>
      <p style="margin-top:1.6rem">Y próximamente, ANAHATA viajará fuera del territorio español, expandiéndose para llegar a nuevos lugares y personas.</p>
    </div>
  </div>
</section>'''

def pagina_inicio():
    pilares = "".join(f'''
      <article class="tarjeta revelar" data-retardo="{i*110}">
        <div class="tarjeta__media"><img src="assets/img/{img}" alt="{tit}" loading="lazy" width="1200" height="900"></div>
        <h3>{tit}</h3>
        <p>{txt}</p>
        <a class="enlace-flecha" href="{url}">{cta}</a>
      </article>''' for i, (img, tit, txt, url, cta) in enumerate(PILARES))

    return (head(f"{MARCA} · Yoga, Pilates y Meditación en {CIUDAD} | {TITULAR}",
                 f"Clases de yoga, pilates y meditación en {CIUDAD}, a domicilio, al aire libre y online. Retiros, talleres y programas para tu bienestar integral con {TITULAR}.",
                 "index.html")
    + aviso() + cabecera("index.html", sobre_imagen=True) + f'''
<main id="contenido">

<section class="hero">
  <div class="hero__media">
    <img src="assets/img/hero-inicio.svg" alt="Práctica de yoga consciente" width="1920" height="1280" fetchpriority="high">
  </div>
  <div class="contenedor">
    <div class="hero__contenido">
    <span class="eyebrow">Yoga · Pilates · Conexión · Transformación · Amor</span>
    <h1>Bienestar consciente<span class="cursiva">para cuerpo, mente y espíritu</span></h1>
    <p>Yoga, pilates y meditación en {CIUDAD}, a domicilio, al aire libre y online. Un espacio para escucharte, habitar tu cuerpo y volver a ti.</p>
    <div class="botonera mt-l">
      <a class="btn btn--claro" href="contacto.html#reservar">Reservar tu clase</a>
      <a class="btn btn--linea-clara" href="servicios.html">Ver servicios</a>
    </div>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="contenedor manifiesto revelar">
    {orn()}
    <p>ANAHATA es un espacio holístico donde cuerpo, mente y espíritu vuelven a encontrarse. Lejos de las prisas y los resultados inmediatos, te acompaño con prácticas que cultivan equilibrio, presencia y hábitos saludables.</p>
    <p class="firma">Sara Viñas</p>
  </div>
</section>

<section class="seccion seccion--crema">
  <div class="contenedor">
    <div class="grid grid-3">{pilares}</div>
  </div>
</section>

<section class="seccion">
  <div class="contenedor duo">
    <div class="duo__media duo__media--alta revelar">
      <img src="assets/img/sobre-retrato.svg" alt="{TITULAR}, profesora de yoga y pilates" loading="lazy" width="900" height="1200">
    </div>
    <div class="revelar" data-retardo="120">
      <span class="eyebrow">Sobre mí</span>
      <h2>Mi historia y el origen de ANAHATA</h2>
      <p style="margin-top:1.4rem">Mi nombre es Sara. Nací en Zaragoza, aunque la vida me ha llevado a vivir en diferentes ciudades de España, cada una aportando algo esencial a mi camino.</p>
      <p>En 2016 comenzó mi transformación. Tras dos grandes pérdidas familiares, decidí convertir ese dolor en una oportunidad para reenfocar mi vida y reconectar conmigo misma. Puse el foco en volver a estudiar y formarme en aquello que me hacía sentir en equilibrio.</p>
      <p>Así nace ANAHATA, un espacio holístico que hoy es un proyecto vivo, en constante renovación, que se expande más allá de un lugar físico.</p>
      <a class="enlace-flecha mt-l" href="sobre-mi.html">Conocer mi trayectoria</a>
    </div>
  </div>
</section>

{bloque_modalidades()}

{franja_cta("Tu práctica empieza con una respiración",
            "Cuéntame qué necesitas y encontramos juntas el formato, el estilo y el ritmo que mejor te acompañan.")}

{bloque_zonas()}
{bloque_testimonios()}
{bloque_newsletter()}
</main>''' + JSONLD + pie())

# ============================== SOBRE MÍ ===================================
FORMACION = [
    ("Pilates Mat", "Técnica, control y consciencia corporal"),
    ("Yoga · 300 h", "Formación completa de profesorado"),
    ("Mindfulness", "Atención plena aplicada a la práctica"),
    ("Nutrición", "Alimentación consciente y equilibrada"),
    ("Masaje Ayurvédico", "Trabajo corporal desde la tradición"),
    ("Yoga y Menopausia", "Acompañamiento en cada etapa"),
    ("Energía Kundalini", "Activación y trabajo energético"),
    ("En curso", "Yogagara (India) y Astrología Psicológica"),
]

def pagina_sobre_mi():
    formacion = "".join(f'''
      <article class="tarjeta-texto revelar" data-retardo="{(i%4)*90}">
        <div class="numero">{str(i+1).zfill(2)}</div>
        <h4>{t}</h4>
        <p style="margin:.5rem 0 0">{d}</p>
      </article>''' for i, (t, d) in enumerate(FORMACION))

    return (head(f"Sobre mí · {TITULAR} | {MARCA}",
                 f"Conoce a {TITULAR}, profesora de yoga y pilates. El origen de ANAHATA, mi formación y la manera en que acompaño a cada persona.",
                 "sobre-mi.html")
    + aviso() + cabecera("sobre-mi.html", sobre_imagen=True)
    + hero_interior("Sobre mí",
                    "Mi historia y el origen de ANAHATA.",
                    "hero-sobre-mi.svg", f"{TITULAR}") + f'''
<main id="contenido">

<section class="seccion">
  <div class="contenedor duo">
    <div class="duo__media duo__media--alta revelar">
      <img src="assets/img/sobre-retrato.svg" alt="{TITULAR}" loading="lazy" width="900" height="1200">
    </div>
    <div class="revelar" data-retardo="120">
      <span class="eyebrow">Mi camino</span>
      <h2>Del dolor al equilibrio</h2>
      <p style="margin-top:1.4rem">Mi nombre es Sara. Nací en Zaragoza, aunque la vida me ha llevado a vivir en diferentes ciudades de España, cada una aportando algo esencial a mi camino.</p>
      <p>En 2016 comenzó mi transformación. Tras dos grandes pérdidas familiares, decidí convertir ese dolor en una oportunidad para reenfocar mi vida y reconectar conmigo misma.</p>
      <p>Puse el foco en volver a estudiar y formarme en aquello que me hacía sentir en equilibrio: Pilates Mat, Yoga (300 h), Mindfulness, Nutrición, Masaje Ayurvédico, Yoga y Menopausia y Activación de la Energía Kundalini.</p>
      <p>Actualmente sigo ampliando mi formación —próximamente en Yogagara (India) y Astrología Psicológica— porque creo profundamente en el aprendizaje continuo y en la evolución personal.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--crema">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(30px,4vw,56px)">
      {orn()}
      <span class="eyebrow">El origen</span>
      <h2>Así nace ANAHATA</h2>
    </div>
    <div class="medida revelar">
      <p class="lead">Todo este recorrido me llevó a dedicarme a lo que realmente me apasiona: ofrecer clases de yoga y pilates y acompañar a las personas en la creación de consciencia corporal, mental y espiritual, para que puedan encontrar equilibrio y bienestar en su día a día.</p>
      <p>Así nace ANAHATA, un espacio holístico que comenzó como un centro físico en Etxebarri, un lugar al que guardo un agradecimiento infinito. Por amor, cambié de ciudad y traspasé el centro, permitiendo que ANAHATA siguiera su propio proceso natural de transformación.</p>
      <p>Hoy ANAHATA es un proyecto vivo, en constante renovación, que se expande más allá de un lugar físico. Mi propósito es crear espacios —presenciales y online— que puedan llegar a cualquier rincón del mundo, acompañando a cada persona en su camino hacia una vida más consciente, equilibrada y plena.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--verde">
  <div class="contenedor">
    <div class="cita revelar">
      <figure>
        <blockquote>Anahata es el centro del corazón: el lugar donde el cuerpo y la consciencia se encuentran. Ahí es donde trabajamos.</blockquote>
        <figcaption>{TITULAR}</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(30px,4vw,56px)">
      <span class="eyebrow">Formación</span>
      <h2>Aprendizaje continuo</h2>
      <p class="lead" style="margin-top:1.2rem">Creo en la evolución personal como práctica diaria. Esta es la base desde la que acompaño.</p>
    </div>
    <div class="grid grid-4">{formacion}</div>
  </div>
</section>

<section class="seccion seccion--crema">
  <div class="contenedor duo duo--invertido">
    <div class="duo__media revelar">
      <img src="assets/img/sobre-detalle.svg" alt="Detalle de una práctica de yoga" loading="lazy" width="1200" height="900">
    </div>
    <div class="revelar" data-retardo="120">
      <span class="eyebrow">Mi propósito</span>
      <h2>Crear espacios donde puedas escucharte</h2>
      <p style="margin-top:1.4rem">Mi misión es crear espacios donde puedas escucharte, habitar tu cuerpo, calmar la mente y nutrir tu energía a través de prácticas que acompañan tu bienestar físico, emocional y espiritual.</p>
      <div class="botonera mt-l">
        <a class="btn btn--solido" href="servicios.html">Ver mis prácticas</a>
        <a class="btn btn--linea" href="contacto.html#reservar">Reservar una sesión</a>
      </div>
    </div>
  </div>
</section>

{franja_cta("¿Empezamos juntas?",
            "Tanto si es tu primera clase como si llevas años practicando, adaptamos la sesión a tu momento.")}
</main>''' + pie())

# ============================== SERVICIOS ==================================
ESTILOS_YOGA = [
    ("Yoga Integral", "Cuerpo, mente y espíritu",
     "Una práctica completa que combina movimiento consciente, respiración, meditación y trabajo energético. El Yoga Integral busca armonizar cuerpo, mente y espíritu, creando sesiones equilibradas que se adaptan a cada persona y a cada momento. Es ideal para quienes desean una experiencia profunda, sensible y transformadora."),
    ("Ashtanga Yoga", "Dinámico y estructurado",
     "Un estilo dinámico y estructurado que sigue una secuencia fija de posturas enlazadas a través de la respiración. Ashtanga fortalece el cuerpo, mejora la resistencia y cultiva disciplina y presencia. Perfecto para quienes buscan una práctica intensa, fluida y con enfoque en la evolución personal."),
    ("Vinyasa Yoga", "Creativo y fluido",
     "Práctica creativa y fluida donde el movimiento se sincroniza con la respiración. Cada clase es diferente y se adapta al ritmo del grupo, creando secuencias dinámicas que aportan fuerza, flexibilidad y conexión. Ideal para quienes disfrutan del movimiento consciente y la libertad en la práctica."),
    ("Yin Yoga", "Suave y meditativo",
     "Un estilo suave, meditativo y profundo que trabaja desde la quietud. Las posturas se mantienen durante varios minutos para acceder a los tejidos más internos, liberar tensiones y equilibrar el sistema nervioso. Yin Yoga es perfecto para quienes buscan calma, introspección y un espacio de descanso consciente."),
]

def pagina_servicios():
    estilos = "".join(f'''
      <article class="estilo revelar">
        <div>
          <h3>{t}</h3>
          <p class="estilo__etiqueta">{et}</p>
        </div>
        <p>{d}</p>
      </article>''' for t, et, d in ESTILOS_YOGA)

    return (head(f"Servicios · Yoga, Pilates y Meditación | {MARCA}",
                 "Yoga Integral, Ashtanga, Vinyasa, Yin Yoga, Pilates Mat con implementos, meditación, pranayamas y alimentación saludable. Descubre todas las prácticas de ANAHATA.",
                 "servicios.html")
    + aviso() + cabecera("servicios.html", sobre_imagen=True)
    + hero_interior("Servicios",
                    "Prácticas que cultivan equilibrio, presencia y hábitos saludables.",
                    "hero-servicios.svg", "Clase grupal de yoga") + f'''
<main id="contenido">

<section class="seccion" id="yoga">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(36px,5vw,70px)">
      {orn()}
      <span class="eyebrow">Yoga</span>
      <h2>Estilos de yoga que ofrezco</h2>
      <p class="lead" style="margin-top:1.2rem">Cuatro caminos distintos hacia el mismo lugar: tu equilibrio. Elegimos juntas el que mejor acompaña tu momento.</p>
    </div>
    <div class="medida">{estilos}</div>
  </div>
</section>

<section class="seccion seccion--crema" id="pilates">
  <div class="contenedor duo">
    <div class="duo__media duo__media--alta revelar">
      <img src="assets/img/servicio-pilates.svg" alt="Clase de Pilates Mat" loading="lazy" width="1000" height="1000">
    </div>
    <div class="revelar" data-retardo="120">
      <span class="eyebrow">Pilates</span>
      <h2>Pilates Mat con diferentes implementos</h2>
      <p style="margin-top:1.4rem">El Pilates Mat es una práctica enfocada en la fuerza, la estabilidad y la consciencia corporal. A través del control, la precisión y la respiración, trabajamos la musculatura profunda, mejoramos la postura y fortalecemos el cuerpo de forma funcional.</p>
      <p>En mis clases incorporo diferentes implementos —bandas elásticas, aro mágico, fitball, softball, bloques, sliders, rulo y pica— que permiten adaptar la intensidad, profundizar en la técnica y hacer la práctica más dinámica y completa. Estos elementos ayudan a activar zonas específicas, mejorar la movilidad y acompañar el movimiento de forma segura y consciente.</p>
      <p>Además, el Pilates Mat contribuye a ganar elasticidad, mejorar la coordinación y fortalecer el suelo pélvico, favoreciendo una base corporal estable y saludable para el día a día.</p>
      <p>Es una disciplina ideal para quienes buscan cuidarse desde la presencia, mejorar su alineación, prevenir molestias y conectar con su cuerpo de manera equilibrada y consciente.</p>
    </div>
  </div>
</section>

<section class="seccion" id="meditacion">
  <div class="contenedor duo duo--invertido">
    <div class="duo__media duo__media--alta revelar">
      <img src="assets/img/servicio-meditacion.svg" alt="Meditación guiada" loading="lazy" width="1000" height="1000">
    </div>
    <div class="revelar" data-retardo="120">
      <span class="eyebrow">Meditación</span>
      <h2>Meditación y pranayamas</h2>
      <p style="margin-top:1.4rem">La meditación y los pranayamas son prácticas esenciales para cultivar calma, claridad y equilibrio interior. A través de técnicas de respiración consciente y momentos de quietud guiada, te acompaño a conectar con tu energía, regular el sistema nervioso y habitar el presente con más serenidad.</p>
      <p>Los pranayamas —ejercicios de control y expansión de la respiración— ayudan a mejorar la capacidad pulmonar, liberar tensiones internas, equilibrar la energía y preparar el cuerpo y la mente para la práctica física. Son herramientas poderosas para gestionar el estrés, aumentar la vitalidad y profundizar en la conexión contigo.</p>
      <p>La meditación te invita a observar, a sentir y a crear un espacio de silencio donde puedas escucharte. Trabajamos diferentes técnicas: atención plena, visualizaciones, escaneo corporal, meditación guiada y prácticas de presencia que te ayudan a encontrar estabilidad emocional y claridad mental.</p>
      <p><strong>Es un espacio para respirar, soltar, reconectar y volver a tu centro, volver a ti.</strong></p>
    </div>
  </div>
</section>

<section class="seccion seccion--arena" id="alimentacion">
  <div class="contenedor duo">
    <div class="duo__media revelar">
      <img src="assets/img/pilar-programas.svg" alt="Alimentación saludable" loading="lazy" width="1200" height="900">
    </div>
    <div class="revelar" data-retardo="120">
      <span class="eyebrow">Nutrición consciente</span>
      <h2>Alimentación saludable</h2>
      <p style="margin-top:1.4rem">La alimentación saludable empieza por elegir alimentos que te nutran y combinarlos de forma adecuada para mejorar la digestión, la energía y el bienestar. En este espacio te acompaño a entender qué mezclas favorecen tu cuerpo, cuáles generan más ligereza y cómo crear platos sencillos, equilibrados y llenos de vida.</p>
      <p>Es una manera práctica y consciente de cuidarte desde dentro, escuchando tu cuerpo y aprendiendo a alimentarte de forma más natural y armoniosa.</p>
      <a class="enlace-flecha mt-l" href="contacto.html">Consultar disponibilidad</a>
    </div>
  </div>
</section>

{bloque_modalidades()}

{franja_cta("¿No sabes por dónde empezar?",
            "Escríbeme y valoramos juntas qué práctica encaja mejor contigo, tu cuerpo y tu momento vital.")}

{bloque_zonas()}
</main>''' + pie())

# ========================= CLASES Y PROGRAMAS ==============================
PROGRAMAS = [
    ("programa-sueltas.svg", "Clases sueltas",
     "Prueba una sesión sin compromiso o practica a tu ritmo cuando tu agenda lo permita. Yoga, pilates o meditación, en grupo o individual.",
     ["Sin permanencia", "Presencial u online", "Todos los niveles"]),
    ("programa-membresia.svg", "Membresía mensual",
     "La opción para crear constancia. Practica cada semana con seguimiento cercano y acceso prioritario a talleres y eventos.",
     ["Clases semanales", "Acompañamiento continuo", "Prioridad en retiros"]),
    ("programa-reto21.svg", "Reto de 21 días",
     "Veintiún días para instalar un hábito consciente. Práctica guiada, respiración y pautas sencillas para sostener el cambio.",
     ["Práctica diaria guiada", "Materiales descargables", "Grupo de acompañamiento"]),
    ("programa-privadas.svg", "Sesiones privadas",
     "Un espacio íntimo, diseñado para ti. Trabajamos tus objetivos, corregimos y profundizamos desde la atención plena.",
     ["100 % personalizada", "En estudio, a domicilio u online", "Sesión suelta o bono"]),
]

FAQ = [
    ("¿Necesito experiencia previa?",
     "No. Las clases se adaptan a cada persona y a cada momento. Si es tu primera vez, iremos paso a paso: lo importante es que la práctica se ajuste a ti, y no al revés."),
    ("¿Qué necesito para practicar?",
     "Ropa cómoda, una esterilla y ganas de escucharte. En las clases de Pilates Mat trabajamos con distintos implementos; te indico en cada sesión si necesitas alguno."),
    ("¿Cuáles son las tarifas?",
     "Cada propuesta se adapta al formato, la frecuencia y el lugar de la práctica. Escríbeme por WhatsApp o rellena el formulario y te envío las tarifas actualizadas sin compromiso."),
    ("¿Qué horarios hay disponibles?",
     "Los horarios se organizan por temporada y según los espacios donde imparto. Consúltame la disponibilidad actual y buscamos el hueco que mejor te encaje."),
    ("¿Puedo practicar si tengo una lesión o molestia?",
     "En la mayoría de casos sí, adaptando la práctica. Cuéntamelo antes de empezar para poder proponerte variantes seguras; si es necesario, te recomendaré consultarlo antes con tu profesional sanitario."),
    ("¿Cómo son las clases online?",
     "En directo o grabadas, para que puedas practicar desde cualquier lugar. Solo necesitas conexión, un espacio tranquilo y tu esterilla."),
]

def pagina_clases():
    programas = "".join(f'''
      <article class="tarjeta revelar" data-retardo="{(i%2)*110}">
        <div class="tarjeta__media"><img src="assets/img/{img}" alt="{t}" loading="lazy" width="1200" height="900"></div>
        <h3>{t}</h3>
        <p>{d}</p>
        <ul style="margin:0 0 1.3rem">{"".join(f'<li style="font-size:.9rem;padding-left:20px;position:relative"><span style="position:absolute;left:0;color:var(--oro)">·</span>{b}</li>' for b in bullets)}</ul>
        <a class="enlace-flecha" href="contacto.html#reservar">Consultar e inscribirme</a>
      </article>''' for i, (img, t, d, bullets) in enumerate(PROGRAMAS))

    faq = "".join(f'''
      <div class="acordeon__item">
        <button class="acordeon__boton" type="button" aria-expanded="false">
          <span>{p}</span><span aria-hidden="true">+</span>
        </button>
        <div class="acordeon__panel"><div><p>{r}</p></div></div>
      </div>''' for p, r in FAQ)

    return (head(f"Clases y programas · {MARCA}",
                 "Clases sueltas, membresía mensual, reto de 21 días y sesiones privadas de yoga y pilates. Elige el formato que mejor acompaña tu momento.",
                 "clases.html")
    + aviso() + cabecera("clases.html", sobre_imagen=True)
    + hero_interior("Clases y programas",
                    "Elige cómo quieres acompañarte: una clase suelta, un mes completo o un reto que te sostenga.",
                    "hero-clases.svg", "Sala de práctica") + f'''
<main id="contenido">

<section class="seccion">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(36px,5vw,64px)">
      {orn()}
      <span class="eyebrow">Formatos</span>
      <h2>Programas para crear constancia</h2>
      <p class="lead" style="margin-top:1.2rem">La transformación no llega con un esfuerzo puntual, sino con la constancia amable. Estas son las formas de practicar conmigo.</p>
    </div>
    <div class="grid grid-2">{programas}</div>
  </div>
</section>

<section class="seccion seccion--verde seccion--compacta">
  <div class="contenedor duo">
    <div class="revelar">
      <span class="eyebrow">Tarifas y horarios</span>
      <h2>Cada propuesta se adapta a ti</h2>
      <p class="lead" style="margin-top:1.2rem">Los horarios se organizan por temporada y las tarifas dependen del formato, la frecuencia y el lugar de la práctica. Escríbeme y te lo cuento todo sin compromiso.</p>
    </div>
    <div class="revelar" data-retardo="120" style="display:flex;flex-direction:column;justify-content:center;gap:14px">
      <a class="btn btn--oro btn--bloque" href="{WA_URL}" target="_blank" rel="noopener">Consultar por WhatsApp</a>
      <a class="btn btn--linea-clara btn--bloque" href="contacto.html#reservar">Escribir por el formulario</a>
      <p class="nota-formulario" style="color:#CFCBBC;text-align:center">Respondo personalmente en 24-48 h.</p>
    </div>
  </div>
</section>

{bloque_modalidades()}

<section class="seccion seccion--crema">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(30px,4vw,50px)">
      <span class="eyebrow">Dudas frecuentes</span>
      <h2>Antes de tu primera clase</h2>
    </div>
    <div class="medida acordeon revelar" data-acordeon>{faq}</div>
  </div>
</section>

{franja_cta("Reserva tu plaza",
            "Dime qué práctica te interesa y en qué momento del día te viene bien. Te confirmo disponibilidad enseguida.")}
</main>''' + pie())

# ==================== RETIROS, EVENTOS Y TALLERES ==========================
EVENTOS = [
    ("retiro-finde.svg", "Retiros de fin de semana", "Retiro",
     "Encuentros presenciales donde hacer tribu, para desconectar del ritmo diario y reconectar contigo. Movimiento, descanso, naturaleza y autocuidado profundo, siempre en entornos de naturaleza y silencio."),
    ("evento-brunch.svg", "Yoga & brunch", "Evento",
     "Una mañana para moverte con calma y compartir mesa después. Práctica suave, respiración y un desayuno saludable en buena compañía."),
    ("evento-aromaterapia.svg", "Taller de aromaterapia", "Taller",
     "Descubre el poder de los aceites esenciales y cómo integrarlos en tu rutina para acompañar tu descanso, tu energía y tu estado de ánimo."),
    ("evento-menopausia.svg", "Yoga y menopausia", "Taller",
     "Una práctica específica para acompañar los cambios de esta etapa: movilidad, fuerza, respiración y herramientas para habitar el cuerpo con amabilidad."),
    ("evento-familia.svg", "Yoga en familia", "Evento",
     "Una experiencia para compartir con los peques de casa: juego, movimiento y respiración para crear vínculo y consciencia corporal desde la infancia."),
    ("pilar-meditacion.svg", "Activación de la energía Kundalini", "Taller",
     "Un espacio para trabajar la energía desde la respiración, el movimiento y la meditación, despertando vitalidad y presencia."),
]

def pagina_retiros():
    tarjetas = "".join(f'''
      <article class="tarjeta revelar" data-retardo="{(i%3)*100}">
        <div class="tarjeta__media"><img src="assets/img/{img}" alt="{t}" loading="lazy" width="1200" height="900"></div>
        <span class="eyebrow" style="margin-bottom:.5rem">{et}</span>
        <h3>{t}</h3>
        <p>{d}</p>
        <a class="enlace-flecha" href="contacto.html#reservar">Quiero información</a>
      </article>''' for i, (img, t, et, d) in enumerate(EVENTOS))

    return (head(f"Retiros, eventos y talleres · {MARCA}",
                 "Retiros de fin de semana, yoga & brunch, talleres de aromaterapia, yoga y menopausia, yoga en familia y activación de la energía Kundalini.",
                 "retiros.html")
    + aviso() + cabecera("retiros.html", sobre_imagen=True)
    + hero_interior("Retiros, eventos y talleres",
                    "Experiencias para desconectar del ritmo diario y reconectar contigo.",
                    "hero-retiros.svg", "Retiro de yoga en la naturaleza") + f'''
<main id="contenido">

<section class="seccion">
  <div class="contenedor manifiesto revelar">
    {orn()}
    <p>Encuentros presenciales donde hacer tribu. Movimiento, descanso, naturaleza y autocuidado profundo, siempre en entornos de silencio.</p>
  </div>
</section>

<section class="seccion seccion--crema">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(36px,5vw,64px)">
      <span class="eyebrow">Propuestas</span>
      <h2>Experiencias de temporada</h2>
      <p class="lead" style="margin-top:1.2rem">Cada temporada preparo nuevas fechas. Escríbeme para conocer las próximas o para organizar una experiencia a medida para tu grupo.</p>
    </div>
    <div class="grid grid-3">{tarjetas}</div>
  </div>
</section>

<section class="seccion">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(30px,4vw,50px)">
      {orn()}
      <span class="eyebrow">Programas y retos</span>
      <h2>Constancia, transformación y equilibrio</h2>
    </div>
    <div class="grid grid-3 medida" style="max-width:1000px">
      <article class="tarjeta-texto revelar"><div class="numero">01</div><h4>Reto de 21 días</h4><p style="margin:.5rem 0 0">El tiempo justo para instalar un hábito consciente, con práctica guiada y acompañamiento.</p></article>
      <article class="tarjeta-texto revelar" data-retardo="100"><div class="numero">02</div><h4>Hábitos conscientes</h4><p style="margin:.5rem 0 0">Programas para integrar movimiento, respiración y alimentación en tu día a día.</p></article>
      <article class="tarjeta-texto revelar" data-retardo="200"><div class="numero">03</div><h4>Membresías mensuales</h4><p style="margin:.5rem 0 0">Practica cada semana con seguimiento cercano y prioridad en retiros y talleres.</p></article>
    </div>
    <div class="botonera botonera--centro mt-l">
      <a class="btn btn--linea" href="clases.html">Ver todos los programas</a>
    </div>
  </div>
</section>

{bloque_zonas(verde=True)}

{franja_cta("¿Organizamos un retiro para tu grupo?",
            "Diseño experiencias a medida para grupos, empresas y celebraciones. Cuéntame tu idea y la hacemos posible.")}

{bloque_newsletter()}
</main>''' + pie())

# =============================== CONTACTO ==================================
def pagina_contacto():
    opciones = ["Clases grupales", "Sesión personalizada", "Clases a domicilio",
                "Clases al aire libre", "Clases online", "Membresía mensual",
                "Reto de 21 días", "Retiros y experiencias", "Talleres y eventos",
                "Alimentación saludable", "Otra consulta"]
    select = "".join(f'<option value="{o}">{o}</option>' for o in opciones)

    return (head(f"Contacto y reservas · {MARCA}",
                 f"Reserva tu clase de yoga, pilates o meditación con {TITULAR}. Escríbeme por WhatsApp, correo o a través del formulario.",
                 "contacto.html")
    + aviso() + cabecera("contacto.html", sobre_imagen=True)
    + hero_interior("Contacto",
                    "Cuéntame qué necesitas y encontramos juntas la práctica que mejor te acompaña.",
                    "hero-contacto.svg", "Espacio de práctica") + f'''
<main id="contenido">

<section class="seccion" id="reservar">
  <div class="contenedor duo" style="align-items:flex-start">
    <div class="revelar">
      <span class="eyebrow">Reservas</span>
      <h2>Escríbeme</h2>
      <p class="lead" style="margin-top:1.2rem">Respondo personalmente cada mensaje en un plazo de 24-48 h. Si prefieres una respuesta rápida, WhatsApp es la vía más directa.</p>

      <div style="margin-top:clamp(32px,4vw,48px)">
        <div class="dato">
          <div class="dato__icono">{I["wa"]}</div>
          <div><h4>WhatsApp</h4><a href="{WA_URL}" target="_blank" rel="noopener">{TEL_FMT}</a></div>
        </div>
        <div class="dato">
          <div class="dato__icono">{I["sobre"]}</div>
          <div><h4>Correo</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        </div>
        <div class="dato">
          <div class="dato__icono">{I["tel"]}</div>
          <div><h4>Teléfono</h4><a href="tel:+34{TEL}">{TEL_FMT}</a></div>
        </div>
        <div class="dato">
          <div class="dato__icono">{I["pin"]}</div>
          <div><h4>Dónde</h4><p>{CIUDAD} · a domicilio · al aire libre · online</p></div>
        </div>
        <div class="dato">
          <div class="dato__icono">{I["reloj"]}</div>
          <div><h4>Horarios</h4><p>Por temporada. Consúltame la disponibilidad actual.</p></div>
        </div>
      </div>

      <div class="redes" style="margin-top:2rem">
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram" style="border-color:rgba(190,169,141,.7);color:var(--verde)">{I["ig"]}</a>
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook" style="border-color:rgba(190,169,141,.7);color:var(--verde)">{I["fb"]}</a>
      </div>
    </div>

    <div class="revelar" data-retardo="120">
      <form class="formulario tarjeta-texto" data-formulario novalidate>
        <h3>Formulario de contacto</h3>
        <div class="campo--doble">
          <div class="campo">
            <label for="nombre">Nombre y apellidos *</label>
            <input id="nombre" name="nombre" type="text" required autocomplete="name">
          </div>
          <div class="campo">
            <label for="telefono">Teléfono</label>
            <input id="telefono" name="telefono" type="tel" autocomplete="tel">
          </div>
        </div>
        <div class="campo">
          <label for="email">Correo electrónico *</label>
          <input id="email" name="email" type="email" required autocomplete="email">
        </div>
        <div class="campo">
          <label for="interes">¿Qué te interesa?</label>
          <select id="interes" name="interes">{select}</select>
        </div>
        <div class="campo">
          <label for="mensaje">Cuéntame *</label>
          <textarea id="mensaje" name="mensaje" required placeholder="Tu experiencia previa, qué buscas, qué días te vendrían bien…"></textarea>
        </div>
        <label class="consentimiento">
          <input type="checkbox" name="consentimiento" required>
          <span>He leído y acepto la <a href="privacidad.html">política de privacidad</a> y el tratamiento de mis datos para responder a esta consulta. *</span>
        </label>
        <button class="btn btn--solido btn--bloque" type="submit">Enviar mensaje</button>
        <p class="nota-formulario">* Campos obligatorios. Tus datos solo se utilizan para responderte.</p>
        <p class="nota-formulario" style="color:#9A4A2A" data-aviso-form hidden></p>
      </form>
    </div>
  </div>
</section>

<section class="seccion seccion--crema seccion--compacta">
  <div class="contenedor texto-centrado medida">
    {orn()}
    <h2>¿Prefieres que te escriba yo?</h2>
    <p class="lead" style="margin-top:1.2rem">Suscríbete y recibe las próximas fechas de clases, retiros y talleres.</p>
    <form class="newsletter" data-formulario novalidate style="margin:2rem auto 0;justify-content:center">
      <label class="solo-lectores" for="news-email-contacto">Tu correo electrónico</label>
      <input id="news-email-contacto" type="email" name="email" placeholder="tu@email.com" required autocomplete="email"
             style="background:var(--blanco);border-color:rgba(190,169,141,.6);color:var(--tinta)">
      <button class="btn btn--solido" type="submit">Suscribirme</button>
      <p class="nota-formulario" style="flex:1 1 100%" data-aviso-form hidden></p>
    </form>
  </div>
</section>

{bloque_zonas(verde=True)}
</main>''' + pie())

# ================================ LEGAL ====================================
def pagina_legal(titulo, pagina, desc, cuerpo):
    return (head(f"{titulo} · {MARCA}", desc, pagina)
    + aviso() + cabecera("", sobre_imagen=False) + f'''
<main id="contenido">
<section class="seccion">
  <div class="contenedor medida">
    <span class="eyebrow">Información legal</span>
    <h1 style="font-size:clamp(2.2rem,4.5vw,3.2rem);margin-bottom:1.6rem">{titulo}</h1>
    {cuerpo}
  </div>
</section>
</main>''' + pie())

AVISO_LEGAL = f'''
    <p class="nota-formulario" style="background:var(--arena);padding:16px 20px;border-radius:var(--radio-img)">
      <strong>Nota para Sara:</strong> revisa y completa los datos marcados entre corchetes antes de publicar la web
      (NIF, domicilio fiscal y datos del proveedor de hosting). Este texto es una base orientativa y no sustituye
      el asesoramiento de un profesional.</p>
    <h3 style="margin-top:2.4rem">1. Datos identificativos</h3>
    <p>En cumplimiento de la Ley 34/2002, de Servicios de la Sociedad de la Información y Comercio Electrónico (LSSI-CE),
    se informa de los siguientes datos del titular de este sitio web:</p>
    <ul style="margin-bottom:1.2rem">
      <li>· <strong>Titular:</strong> {TITULAR}</li>
      <li>· <strong>NIF:</strong> [pendiente]</li>
      <li>· <strong>Domicilio:</strong> [pendiente] · {CIUDAD}, España</li>
      <li>· <strong>Correo electrónico:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>· <strong>Teléfono:</strong> {TEL_FMT}</li>
      <li>· <strong>Actividad:</strong> clases de yoga, pilates y meditación, retiros, talleres y acompañamiento en bienestar integral.</li>
    </ul>
    <h3 style="margin-top:2rem">2. Objeto</h3>
    <p>Este sitio web tiene como finalidad informar sobre los servicios de {MARCA} y facilitar el contacto con las personas interesadas.
    El acceso y uso del sitio atribuye la condición de usuario e implica la aceptación de las presentes condiciones.</p>
    <h3 style="margin-top:2rem">3. Propiedad intelectual</h3>
    <p>Los contenidos de este sitio (textos, imágenes, logotipo, diseño y código) son titularidad de {TITULAR} o se utilizan con
    la correspondiente autorización. Queda prohibida su reproducción o distribución sin consentimiento expreso.</p>
    <h3 style="margin-top:2rem">4. Responsabilidad</h3>
    <p>La información publicada tiene carácter divulgativo y no sustituye en ningún caso el consejo médico o sanitario.
    Si tienes una lesión, estás embarazada o padeces alguna patología, consulta con un profesional de la salud antes de comenzar la práctica.</p>
    <h3 style="margin-top:2rem">5. Legislación aplicable</h3>
    <p>Las presentes condiciones se rigen por la legislación española. Para cualquier controversia serán competentes los
    juzgados y tribunales del domicilio del titular, salvo que la normativa de consumo disponga otro fuero.</p>'''

PRIVACIDAD = f'''
    <p class="nota-formulario" style="background:var(--arena);padding:16px 20px;border-radius:var(--radio-img)">
      <strong>Nota para Sara:</strong> completa los datos entre corchetes y revisa el apartado de encargados de tratamiento
      con tu proveedor de hosting y de email marketing. Texto orientativo, no sustituye asesoramiento profesional.</p>
    <h3 style="margin-top:2.4rem">1. Responsable del tratamiento</h3>
    <p>{TITULAR} · NIF [pendiente] · {CIUDAD}, España · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <h3 style="margin-top:2rem">2. Finalidad</h3>
    <p>Los datos que facilitas a través del formulario de contacto se tratan para responder a tu consulta, gestionar la reserva
    de clases o experiencias y, si lo autorizas expresamente, enviarte información sobre próximas actividades (newsletter).</p>
    <h3 style="margin-top:2rem">3. Legitimación</h3>
    <p>La base legal es tu consentimiento, otorgado al marcar la casilla correspondiente, y la ejecución de la relación
    precontractual o contractual derivada de la reserva de servicios.</p>
    <h3 style="margin-top:2rem">4. Conservación</h3>
    <p>Los datos se conservan mientras dure la relación y, posteriormente, durante los plazos legalmente exigibles.
    En el caso de la newsletter, hasta que solicites la baja.</p>
    <h3 style="margin-top:2rem">5. Destinatarios</h3>
    <p>No se ceden datos a terceros salvo obligación legal. Se utilizan proveedores de servicios (hosting y gestión de correo)
    que actúan como encargados del tratamiento: [proveedor de hosting] y [proveedor de email marketing].</p>
    <h3 style="margin-top:2rem">6. Derechos</h3>
    <p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a
    <a href="mailto:{EMAIL}">{EMAIL}</a>. También puedes reclamar ante la Agencia Española de Protección de Datos
    (<a href="https://www.aepd.es" target="_blank" rel="noopener">aepd.es</a>).</p>
    <h3 id="cookies" style="margin-top:2.6rem">7. Política de cookies</h3>
    <p>Esta web no utiliza cookies propias de analítica ni de publicidad. Únicamente se emplea el almacenamiento local del
    navegador para recordar si has cerrado el aviso superior, un dato técnico que no identifica a ninguna persona y que
    permanece en tu dispositivo.</p>
    <p>Se cargan tipografías desde Google Fonts, lo que implica una conexión a servidores de Google. Si en el futuro se añaden
    herramientas de analítica, vídeos incrustados o píxeles de redes sociales, será necesario incorporar un banner de
    consentimiento de cookies.</p>'''


# =============================== LANDING ===================================
# Versión de una sola página: todo el contenido en scroll, orientada a conversión.
NAV_LANDING = [("#sobre-mi","Sobre mí"), ("#servicios","Servicios"), ("#programas","Programas"),
               ("#retiros","Retiros"), ("#opiniones","Opiniones"), ("#contacto","Contacto")]

def cabecera_landing():
    enlaces = "".join('<a href="%s">%s</a>' % (h, t) for h, t in NAV_LANDING[:-1])
    movil = "".join('<a href="%s">%s</a>' % (h, t) for h, t in NAV_LANDING)
    return f'''
<header class="cabecera cabecera--transparente" data-cabecera>
  <div class="cabecera__interior">
    <button class="hamburguesa" type="button" aria-label="Abrir menú" aria-expanded="false" data-menu-boton>
      <span></span><span></span><span></span>
    </button>
    <nav class="nav nav--principal" aria-label="Navegación principal">{enlaces}</nav>
    <a class="logo" href="#inicio" aria-label="{MARCA}">
      <img class="logo__simbolo logo__simbolo--color" src="assets/img/logo-marca.svg" alt="" width="34" height="34">
      <img class="logo__simbolo logo__simbolo--crema" src="assets/img/logo-marca-crema.svg" alt="" width="34" height="34">
      <span class="logo__texto">{MARCA}</span>
    </a>
    <nav class="nav nav--fin" aria-label="Acciones">
      <a class="nav-enlace" href="#contacto">Contacto</a>
      <a class="btn btn--linea" href="#contacto">Reservar</a>
    </nav>
  </div>
</header>
<nav class="menu-movil" data-menu aria-label="Menú">
  {movil}
  <a class="btn btn--solido" href="#contacto">Reservar tu clase</a>
  <div class="menu-movil__pie">
    <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
    <a href="{WA_URL}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</nav>'''

SERVICIOS_LANDING = [
    ("Yoga", "Integral · Ashtanga · Vinyasa · Yin",
     "Cuatro estilos para cuatro momentos: desde la práctica dinámica y estructurada hasta la quietud profunda del Yin. Movimiento consciente, respiración y trabajo energético para armonizar cuerpo, mente y espíritu."),
    ("Pilates Mat", "Con diferentes implementos",
     "Fuerza, estabilidad y consciencia corporal. Trabajamos la musculatura profunda con bandas, aro mágico, fitball, bloques, sliders, rulo y pica, mejorando la postura, la elasticidad y el suelo pélvico."),
    ("Meditación y pranayamas", "Calma y claridad",
     "Respiración consciente y quietud guiada para regular el sistema nervioso, gestionar el estrés y habitar el presente. Atención plena, visualizaciones, escaneo corporal y prácticas de presencia."),
    ("Alimentación saludable", "Nutrirte desde dentro",
     "Aprende qué alimentos y combinaciones favorecen tu digestión y tu energía, y cómo crear platos sencillos, equilibrados y llenos de vida. Cuidarte de forma natural y armoniosa."),
]

def pagina_landing():
    servicios = "".join(f'''
      <article class="tarjeta-texto revelar" data-retardo="{i*90}">
        <div class="numero">{str(i+1).zfill(2)}</div>
        <h3>{t}</h3>
        <p class="estilo__etiqueta" style="margin:.2rem 0 1rem">{et}</p>
        <p style="margin:0">{d}</p>
      </article>''' for i, (t, et, d) in enumerate(SERVICIOS_LANDING))

    modalidades = "".join(f'''
      <article class="modalidad revelar">
        <div class="modalidad__icono">{I[ic]}</div>
        <div><h4>{t}</h4><p>{d}</p></div>
      </article>''' for ic, t, d in MODALIDADES)

    programas = "".join(f'''
      <article class="tarjeta revelar" data-retardo="{(i%4)*90}">
        <div class="tarjeta__media"><img src="assets/img/{img}" alt="{t}" loading="lazy" width="1200" height="900"></div>
        <h3>{t}</h3>
        <p>{d}</p>
        <a class="enlace-flecha" href="#contacto">Quiero información</a>
      </article>''' for i, (img, t, d, _b) in enumerate(PROGRAMAS))

    eventos = "".join(f'''
      <article class="tarjeta revelar" data-retardo="{(i%3)*90}">
        <div class="tarjeta__media"><img src="assets/img/{img}" alt="{t}" loading="lazy" width="1200" height="900"></div>
        <span class="eyebrow" style="margin-bottom:.5rem">{et}</span>
        <h3>{t}</h3>
        <p>{d}</p>
      </article>''' for i, (img, t, et, d) in enumerate(EVENTOS))

    testimonios = "".join(f'''
      <article class="testimonio">
        <div class="testimonio__estrellas" aria-label="5 sobre 5">★★★★★</div>
        <p>«{txt}»</p>
        <div class="testimonio__autor">{autor}</div>
      </article>''' for txt, autor in TESTIMONIOS)

    zonas = "".join(f'<span class="zona">{z}</span>' for z in
                    ["País Vasco", "Cantabria", "Cataluña", "Comunidad Valenciana", "Andalucía"])

    opciones = ["Clases grupales", "Sesión personalizada", "Clases a domicilio", "Clases al aire libre",
                "Clases online", "Membresía mensual", "Reto de 21 días", "Retiros y experiencias",
                "Talleres y eventos", "Alimentación saludable", "Otra consulta"]
    select = "".join(f'<option value="{o}">{o}</option>' for o in opciones)

    return (head(f"{MARCA} · Yoga, Pilates y Meditación en {CIUDAD} | {TITULAR}",
                 f"Clases de yoga, pilates y meditación en {CIUDAD}, a domicilio, al aire libre y online. Retiros, talleres y programas para tu bienestar integral con {TITULAR}.",
                 "landing.html")
    + aviso() + cabecera_landing() + f'''
<main id="contenido">

<section class="hero hero--landing" id="inicio">
  <div class="hero__media">
    <img src="assets/img/hero-inicio.svg" alt="Práctica de yoga consciente" width="1920" height="1280" fetchpriority="high">
  </div>
  <div class="contenedor hero__contenido hero__contenido--centrado">
    <img class="hero__logo" src="assets/img/logo-anahata-crema.svg"
         alt="{MARCA} · Yoga, Pilates, Conexión, Transformación, Amor" width="300" height="530">
    <h1>Bienestar consciente<span class="cursiva">para cuerpo, mente y espíritu</span></h1>
    <p>Yoga, pilates y meditación en {CIUDAD}, a domicilio, al aire libre y online.</p>
    <div class="botonera botonera--centro mt-l">
      <a class="btn btn--claro" href="#contacto">Reservar tu clase</a>
      <a class="btn btn--linea-clara" href="#servicios">Ver servicios</a>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="contenedor manifiesto revelar">
    {orn()}
    <p>ANAHATA es un espacio holístico donde cuerpo, mente y espíritu vuelven a encontrarse. Lejos de las prisas y los resultados inmediatos, te acompaño con prácticas que cultivan equilibrio, presencia y hábitos saludables.</p>
    <p class="firma">Sara Viñas</p>
  </div>
</section>

<section class="seccion seccion--crema" id="sobre-mi">
  <div class="contenedor duo">
    <div class="duo__media duo__media--alta revelar">
      <img src="assets/img/sobre-retrato.svg" alt="{TITULAR}" loading="lazy" width="900" height="1200">
    </div>
    <div class="revelar" data-retardo="120">
      <span class="eyebrow">Sobre mí</span>
      <h2>Mi historia y el origen de ANAHATA</h2>
      <p style="margin-top:1.4rem">Mi nombre es Sara. Nací en Zaragoza, aunque la vida me ha llevado a vivir en diferentes ciudades de España, cada una aportando algo esencial a mi camino.</p>
      <p>En 2016 comenzó mi transformación. Tras dos grandes pérdidas familiares, decidí convertir ese dolor en una oportunidad para reenfocar mi vida y reconectar conmigo misma. Me formé en Pilates Mat, Yoga (300 h), Mindfulness, Nutrición, Masaje Ayurvédico, Yoga y Menopausia y Activación de la Energía Kundalini, y sigo ampliando formación —próximamente en Yogagara (India) y Astrología Psicológica—.</p>
      <p>Así nace ANAHATA, un espacio holístico que comenzó como centro físico en Etxebarri y hoy es un proyecto vivo que se expande más allá de un lugar físico: presencial y online, para llegar a cualquier rincón del mundo.</p>
    </div>
  </div>
</section>

<section class="seccion" id="servicios">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(36px,5vw,64px)">
      {orn()}
      <span class="eyebrow">Servicios</span>
      <h2>Prácticas que te acompañan</h2>
      <p class="lead" style="margin-top:1.2rem">Elegimos juntas el camino que mejor encaja con tu cuerpo y tu momento vital.</p>
    </div>
    <div class="grid grid-2">{servicios}</div>
  </div>
</section>

<section class="seccion seccion--arena" id="modalidades">
  <div class="contenedor">
    <div class="texto-centrado medida" style="margin-bottom:clamp(30px,4vw,56px)">
      <span class="eyebrow">Modalidades</span>
      <h2>Practica donde y como mejor te acompañe</h2>
    </div>
    <div class="medida">{modalidades}</div>
  </div>
</section>

<section class="seccion" id="programas">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(36px,5vw,64px)">
      {orn()}
      <span class="eyebrow">Clases y programas</span>
      <h2>Programas para crear constancia</h2>
      <p class="lead" style="margin-top:1.2rem">Las tarifas y los horarios se adaptan al formato, la frecuencia y el lugar de la práctica. Escríbeme y te lo cuento sin compromiso.</p>
    </div>
    <div class="grid grid-4">{programas}</div>
  </div>
</section>

{franja_cta("Tu práctica empieza con una respiración",
            "Cuéntame qué necesitas y encontramos juntas el formato, el estilo y el ritmo que mejor te acompañan.")}

<section class="seccion" id="retiros">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(36px,5vw,64px)">
      <span class="eyebrow">Retiros, eventos y talleres</span>
      <h2>Experiencias para hacer tribu</h2>
      <p class="lead" style="margin-top:1.2rem">Encuentros presenciales para desconectar del ritmo diario y reconectar contigo, siempre en entornos de naturaleza y silencio.</p>
    </div>
    <div class="grid grid-3">{eventos}</div>
  </div>
</section>

<section class="seccion seccion--verde" id="zonas">
  <div class="contenedor duo">
    <div class="revelar">
      <span class="eyebrow">Dónde practicamos</span>
      <h2>Clases en {CIUDAD} y retiros por toda España</h2>
      <p style="margin-top:1.2rem">Imparto clases de yoga, pilates y meditación en el área de {CIUDAD}, en diferentes espacios de bienestar y también en formato individual. Y si prefieres practicar desde casa, las clases online llegan a cualquier rincón del mundo.</p>
    </div>
    <div class="revelar" data-retardo="120">
      <h4 style="margin-bottom:1.2rem">Retiros y eventos</h4>
      <div class="zonas">{zonas}</div>
      <p style="margin-top:1.6rem">Y próximamente, ANAHATA viajará fuera del territorio español, expandiéndose para llegar a nuevos lugares y personas.</p>
    </div>
  </div>
</section>

<section class="seccion seccion--crema" id="opiniones">
  <div class="contenedor">
    <div class="texto-centrado medida" style="margin-bottom:clamp(30px,4vw,56px)">
      {orn()}
      <span class="eyebrow">Opiniones</span>
      <h2>Lo que cuentan quienes practican conmigo</h2>
    </div>
    <div class="revelar" data-carrusel>
      <div class="testimonios">{testimonios}</div>
      <div class="carrusel-controles">
        <button type="button" aria-label="Anterior" data-carrusel-anterior>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H6M11 5.5 5 12l6 6.5"/></svg>
        </button>
        <button type="button" aria-label="Siguiente" data-carrusel-siguiente>{I["flecha"]}</button>
      </div>
    </div>
  </div>
</section>

<section class="seccion" id="contacto">
  <div class="contenedor duo" style="align-items:flex-start">
    <div class="revelar">
      <span class="eyebrow">Contacto y reservas</span>
      <h2>Escríbeme</h2>
      <p class="lead" style="margin-top:1.2rem">Respondo personalmente cada mensaje en un plazo de 24-48 h. Si prefieres una respuesta rápida, WhatsApp es la vía más directa.</p>
      <div style="margin-top:clamp(32px,4vw,48px)">
        <div class="dato"><div class="dato__icono">{I["wa"]}</div>
          <div><h4>WhatsApp</h4><a href="{WA_URL}" target="_blank" rel="noopener">{TEL_FMT}</a></div></div>
        <div class="dato"><div class="dato__icono">{I["sobre"]}</div>
          <div><h4>Correo</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
        <div class="dato"><div class="dato__icono">{I["tel"]}</div>
          <div><h4>Teléfono</h4><a href="tel:+34{TEL}">{TEL_FMT}</a></div></div>
        <div class="dato"><div class="dato__icono">{I["pin"]}</div>
          <div><h4>Dónde</h4><p>{CIUDAD} · a domicilio · al aire libre · online</p></div></div>
      </div>
      <div class="redes" style="margin-top:2rem">
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram" style="border-color:rgba(190,169,141,.7);color:var(--verde)">{I["ig"]}</a>
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook" style="border-color:rgba(190,169,141,.7);color:var(--verde)">{I["fb"]}</a>
      </div>
    </div>
    <div class="revelar" data-retardo="120">
      <form class="formulario tarjeta-texto" data-formulario novalidate>
        <h3>Formulario de contacto</h3>
        <div class="campo--doble">
          <div class="campo"><label for="l-nombre">Nombre y apellidos *</label>
            <input id="l-nombre" name="nombre" type="text" required autocomplete="name"></div>
          <div class="campo"><label for="l-telefono">Teléfono</label>
            <input id="l-telefono" name="telefono" type="tel" autocomplete="tel"></div>
        </div>
        <div class="campo"><label for="l-email">Correo electrónico *</label>
          <input id="l-email" name="email" type="email" required autocomplete="email"></div>
        <div class="campo"><label for="l-interes">¿Qué te interesa?</label>
          <select id="l-interes" name="interes">{select}</select></div>
        <div class="campo"><label for="l-mensaje">Cuéntame *</label>
          <textarea id="l-mensaje" name="mensaje" required placeholder="Tu experiencia previa, qué buscas, qué días te vendrían bien…"></textarea></div>
        <label class="consentimiento">
          <input type="checkbox" name="consentimiento" required>
          <span>He leído y acepto la <a href="privacidad.html">política de privacidad</a> y el tratamiento de mis datos para responder a esta consulta. *</span>
        </label>
        <button class="btn btn--solido btn--bloque" type="submit">Enviar mensaje</button>
        <p class="nota-formulario">* Campos obligatorios. Tus datos solo se utilizan para responderte.</p>
        <p class="nota-formulario" style="color:#9A4A2A" data-aviso-form hidden></p>
      </form>
    </div>
  </div>
</section>

{bloque_newsletter()}
</main>''' + JSONLD + pie())

# =============================== GENERAR ===================================
if __name__ == "__main__":
    escribir("index.html",       pagina_inicio())
    escribir("landing.html",     pagina_landing())
    escribir("sobre-mi.html",    pagina_sobre_mi())
    escribir("servicios.html",   pagina_servicios())
    escribir("clases.html",      pagina_clases())
    escribir("retiros.html",     pagina_retiros())
    escribir("contacto.html",    pagina_contacto())
    escribir("aviso-legal.html", pagina_legal("Aviso legal", "aviso-legal.html",
             f"Aviso legal de {MARCA} · {TITULAR}.", AVISO_LEGAL))
    escribir("privacidad.html",  pagina_legal("Política de privacidad y cookies", "privacidad.html",
             f"Política de privacidad y cookies de {MARCA} · {TITULAR}.", PRIVACIDAD))
    print("Web generada:", ", ".join(sorted(f for f in os.listdir('.') if f.endswith('.html'))))
