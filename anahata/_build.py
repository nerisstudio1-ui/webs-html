# -*- coding: utf-8 -*-
"""Generador estático de la web de ANAHATA.
   Edita el contenido aquí y ejecuta:  python3 _build.py
   Salida: los .html de la raíz del proyecto."""
import os, re

# ============================ DATOS DEL NEGOCIO ============================
MARCA     = "ANAHATA"
TITULAR   = "Sara Viñas Gómez"
EMAIL     = "saravgyoga@gmail.com"
TEL       = "664607464"                 # confirmado por Sara (24/09) y visible en el rótulo del estudio
TEL_FMT   = "664 60 74 64"
WA        = "34" + TEL
WA_MSG    = "Hola%20Sara%2C%20me%20gustar%C3%ADa%20informarme%20sobre%20las%20clases%20de%20ANAHATA"
WA_URL    = f"https://wa.me/{WA}?text={WA_MSG}"
IG        = "https://www.instagram.com/saravgyoga/"
FB        = "https://www.facebook.com/people/Sara-Vinas-G%C3%B3mez/pfbid06JHJpnUKVaPrk51RJiH3VkkNQhAaW25DX8NyPRMMUbtA3BUvygtoCdssqahxWKQLl/"
DOMINIO   = "https://www.saravgyoga.com"
CIUDAD    = "Barcelona"
NIF       = "25199625C"
DIRECCION = "Carrer Xiprer 30-32, 1º 1ª · 08041 Barcelona"
GOOGLE_REVIEW = "https://g.page/r/CSeJ0912NzUzEAE/review"

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
<meta name="theme-color" content="#A18974">
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
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="saltar-al-contenido" href="#contenido">Saltar al contenido</a>'''

def aviso():
    return f'''
<div class="aviso" data-aviso>
  <span>Clases de yoga y pilates en {CIUDAD}, a domicilio y online · Nuevos retiros y talleres cada temporada.
  <a href="#retiros">Ver próximas fechas</a></span>
  <button class="aviso__cerrar" type="button" aria-label="Cerrar aviso" data-cerrar-aviso>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>
  </button>
</div>'''

def pie(landing=False):
    if landing:
        enlaces_nav = [("#inicio", "Inicio"), ("#sobre-mi", "Sobre mí"), ("#servicios", "Servicios"),
                       ("#programas", "Clases y programas"), ("#retiros", "Retiros y eventos"),
                       ("#contacto", "Contacto")]
        enlaces_serv = [("#servicios", "Yoga"), ("#servicios", "Pilates Mat"),
                        ("#servicios", "Meditación y pranayamas"), ("#servicios", "Alimentación saludable"),
                        ("#programas", "Clases y programas"), ("#retiros", "Retiros y talleres")]
    else:
        enlaces_nav = NAV
        enlaces_serv = [("servicios.html", "Yoga"), ("servicios.html#pilates", "Pilates Mat"),
                        ("servicios.html#meditacion", "Meditación y pranayamas"),
                        ("servicios.html#alimentacion", "Alimentación saludable"),
                        ("clases.html", "Clases y programas"), ("retiros.html", "Retiros y talleres")]
    navegacion = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in enlaces_nav)
    servicios  = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in enlaces_serv)
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
        <ul>{navegacion}</ul>
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

def franja_cta(titulo, texto, imagen="retiro.jpg"):
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
    ("pilar-yoga.jpg", "Movimiento consciente",
     "Yoga Integral, Ashtanga, Vinyasa, Yin y Pilates Mat con implementos. Fuerza, movilidad y presencia en cada práctica.",
     "servicios.html", "Descubrir las prácticas"),
    ("kundalini.jpg", "Meditación y pranayamas",
     "Respiración consciente y quietud guiada para calmar la mente, regular el sistema nervioso y volver a tu centro.",
     "servicios.html#meditacion", "Aprender a respirar"),
    ("pilar-programas.jpg", "Retiros y programas",
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

# Reseñas reales publicadas en Google (facilitadas por Sara).
TESTIMONIOS = [
    ("Mi experiencia con Sara ha sido maravillosa. Los ejercicios de estiramiento, los de "
     "respiración, la paz interior que transmite y la cercanía y el cariño con el que te recibe "
     "hacen de sus clases una terapia tanto espiritual como física. Gracias, Sara.", "Maribel"),
    ("Llevo poco tiempo, pero el suficiente para ver que Sara es una grandísima persona y "
     "profesional. Me acogió súper bien desde el primer día y con mucho cariño, lo cual, al no "
     "conocer a nadie, te relaja bastante. Es muy cercana. Las clases me encantan, con su "
     "reflexión del día; son muy diferentes unas de otras, siempre te sorprende, y sobre todo "
     "salgo súper relajada y contenta.", "Lore Chavero"),
    ("No hay nada mejor que asistir a una clase donde, además de encontrar profesionalidad y una "
     "atención cuidadosa a la postura de cada participante, se perciban vocación, paz y cariño. "
     "El trabajo de Sara nace de la vocación, y eso es precisamente lo que lo hace verdaderamente "
     "excepcional.", "Maider Patiño"),
    ("Conocí a Sara tras una complicación quirúrgica en la que física y mentalmente mi cuerpo dijo "
     "«hasta aquí». Creo que en esta vida todo pasa por algo… conocerla ha supuesto un antes y un "
     "después. Físicamente voy notando una mejoría importante con sus clases de pilates, y "
     "mentalmente estoy trabajando en ver la vida desde otra perspectiva. ¡Un millón de gracias, "
     "Sara!", "Leire Iribarren García"),
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
    <p class="texto-centrado" style="margin-top:2rem">
      <a class="enlace-flecha" href="{GOOGLE_REVIEW}" target="_blank" rel="noopener">Ver reseñas en Google</a>
    </p>
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

# ========================= CLASES Y PROGRAMAS ==============================
PROGRAMAS = [
    ("programa-sueltas.jpg", "Clases sueltas",
     "Prueba una sesión sin compromiso o practica a tu ritmo cuando tu agenda lo permita. Yoga, pilates o meditación, en grupo o individual.",
     ["Sin permanencia", "Presencial u online", "Todos los niveles"]),
    ("comunidad.jpg", "Membresía mensual",
     "La opción para crear constancia. Practica cada semana con seguimiento cercano y acceso prioritario a talleres y eventos.",
     ["Clases semanales", "Acompañamiento continuo", "Prioridad en retiros"]),
    ("reto21.jpg", "Reto de 21 días",
     "Veintiún días para instalar un hábito consciente. Práctica guiada, respiración y pautas sencillas para sostener el cambio.",
     ["Práctica diaria guiada", "Materiales descargables", "Grupo de acompañamiento"]),
    ("sesion-privada.jpg", "Sesiones privadas",
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

# ==================== RETIROS, EVENTOS Y TALLERES ==========================
EVENTOS = [
    ("tribu.jpg", "Retiros de fin de semana", "Retiro",
     "Encuentros presenciales donde hacer tribu, para desconectar del ritmo diario y reconectar contigo. Movimiento, descanso, naturaleza y autocuidado profundo, siempre en entornos de naturaleza y silencio."),
    ("evento-brunch.jpg", "Yoga & brunch", "Evento",
     "Una mañana para moverte con calma y compartir mesa después. Práctica suave, respiración y un desayuno saludable en buena compañía."),
    ("aromaterapia.jpg", "Taller de aromaterapia", "Taller",
     "Descubre el poder de los aceites esenciales y cómo integrarlos en tu rutina para acompañar tu descanso, tu energía y tu estado de ánimo."),
    ("mujeres.jpg", "Yoga y menopausia", "Taller",
     "Una práctica específica para acompañar los cambios de esta etapa: movilidad, fuerza, respiración y herramientas para habitar el cuerpo con amabilidad."),
    ("familia.jpg", "Yoga en familia", "Evento",
     "Una experiencia para compartir con los peques de casa: juego, movimiento y respiración para crear vínculo y consciencia corporal desde la infancia."),
    ("kundalini.jpg", "Activación de la energía Kundalini", "Taller",
     "Un espacio para trabajar la energía desde la respiración, el movimiento y la meditación, despertando vitalidad y presencia."),
]

# =============================== CONTACTO ==================================
# ================================ LEGAL ====================================
ANCLAS = ["inicio", "sobre-mi", "servicios", "estilos", "beneficios", "modalidades",
          "programas", "galeria", "empezar", "retiros", "zonas", "opiniones", "faq",
          "contacto", "formacion"]

def enlaces_desde_legal(html):
    """En una página legal, las anclas de la landing necesitan la portada delante."""
    for a in ANCLAS:
        html = html.replace(f'href="#{a}"', f'href="index.html#{a}"')
    return html

def pagina_legal(titulo, pagina, desc, cuerpo):
    return enlaces_desde_legal(head(f"{titulo} · {MARCA}", desc, pagina)
    + aviso() + cabecera_landing().replace('class="cabecera cabecera--transparente"',
                                           'class="cabecera cabecera--solida"') + f'''
<main id="contenido">
<section class="seccion">
  <div class="contenedor medida">
    <span class="eyebrow">Información legal</span>
    <h1 style="font-size:clamp(2.2rem,4.5vw,3.2rem);margin-bottom:1.6rem">{titulo}</h1>
    {cuerpo}
  </div>
</section>
</main>''' + pie(landing=True))

AVISO_LEGAL = f'''
    <p class="nota-formulario" style="background:var(--arena);padding:16px 20px;border-radius:var(--radio-img)">
      <strong>Pendiente:</strong> falta indicar el proveedor de hosting cuando esté contratado. Este texto es una base
      orientativa y no sustituye el asesoramiento de un profesional.</p>
    <h3 style="margin-top:2.4rem">1. Datos identificativos</h3>
    <p>En cumplimiento de la Ley 34/2002, de Servicios de la Sociedad de la Información y Comercio Electrónico (LSSI-CE),
    se informa de los siguientes datos del titular de este sitio web:</p>
    <ul style="margin-bottom:1.2rem">
      <li>· <strong>Titular:</strong> {TITULAR}</li>
      <li>· <strong>NIF:</strong> {NIF}</li>
      <li>· <strong>Domicilio:</strong> {DIRECCION}, España</li>
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
      <strong>Pendiente:</strong> falta nombrar al proveedor de hosting y, si se usa, el de email marketing,
      en el apartado de encargados del tratamiento. Texto orientativo, no sustituye asesoramiento profesional.</p>
    <h3 style="margin-top:2.4rem">1. Responsable del tratamiento</h3>
    <p>{TITULAR} · NIF {NIF} · {DIRECCION}, España · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
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
    <p>Las tipografías están alojadas en el propio servidor, de modo que la navegación no genera conexiones con terceros.
    Si en el futuro se añaden herramientas de analítica, vídeos incrustados o píxeles de redes sociales, será necesario
    incorporar un banner de consentimiento de cookies.</p>'''



# ====================== BLOQUES DE CONTENIDO AMPLIADO ======================

ESTILOS_RESUMEN = [
    ("Yoga Integral", "Movimiento consciente, respiración, meditación y trabajo energético en una misma práctica. Para quien busca una experiencia profunda y transformadora."),
    ("Ashtanga Yoga", "Secuencia fija enlazada con la respiración. Fortalece, mejora la resistencia y cultiva disciplina y presencia."),
    ("Vinyasa Yoga", "Movimiento fluido sincronizado con la respiración. Cada clase es distinta y se adapta al ritmo del grupo."),
    ("Yin Yoga", "Posturas sostenidas durante varios minutos para llegar a los tejidos profundos, soltar tensión y calmar el sistema nervioso."),
]

BENEFICIOS = [
    ("Fuerza y estabilidad", "Trabajamos la musculatura profunda y el suelo pélvico para una base corporal estable y saludable."),
    ("Movilidad y postura", "Ganarás elasticidad, coordinación y una alineación más consciente en tu día a día."),
    ("Calma y descanso", "La respiración consciente y la quietud guiada ayudan a regular el sistema nervioso y a gestionar el estrés."),
    ("Energía y vitalidad", "Los pranayamas mejoran la capacidad pulmonar, liberan tensiones internas y equilibran tu energía."),
    ("Presencia", "Aprenderás a habitar tu cuerpo y a sostener la atención en lo que está pasando ahora."),
    ("Comunidad", "En las clases grupales se crea una energía compartida que motiva y acompaña la constancia."),
]

IMPLEMENTOS = ["Bandas elásticas", "Aro mágico", "Fitball", "Softball",
               "Bloques", "Sliders", "Rulo", "Pica"]

PASOS = [
    ("Escríbeme", "Cuéntame en qué momento estás, si has practicado antes y qué te gustaría trabajar. Por WhatsApp o con el formulario."),
    ("Lo vemos juntas", "Elegimos el estilo, el formato y el horario que mejor encajan contigo. Te paso las tarifas sin compromiso."),
    ("Reservas tu plaza", "Y empiezas a practicar. Si es tu primera vez, iremos paso a paso: la práctica se adapta a ti, no al revés."),
]


def bloque_formacion():
    items = "".join(f'<span class="zona">{t}</span>' for t, _ in FORMACION[:-1])
    return f'''
<section class="seccion seccion--compacta" id="formacion">
  <div class="contenedor medida texto-centrado">
    <span class="eyebrow">Formación</span>
    <h2 style="font-size:clamp(1.5rem,2.2vw,2rem)">Aprendizaje continuo</h2>
    <p style="margin-top:1rem">Creo en la evolución personal como práctica diaria. Esta es la base desde la que acompaño.</p>
    <div class="zonas" style="justify-content:center;margin-top:1.5rem">{items}</div>
    <p class="nota-formulario" style="margin-top:1.2rem">Y ampliando: próximamente en Yogagara (India) y Astrología Psicológica.</p>
  </div>
</section>'''

def bloque_estilos_resumen(fondo="seccion--crema"):
    items = "".join(f'''
      <article class="tarjeta-texto revelar" data-retardo="{i*80}">
        <div class="numero">{str(i+1).zfill(2)}</div>
        <h3>{t}</h3>
        <p style="margin:.4rem 0 0">{d}</p>
      </article>''' for i, (t, d) in enumerate(ESTILOS_RESUMEN))
    return f'''
<section class="seccion {fondo}" id="estilos">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(30px,4vw,54px)">
      {orn()}
      <span class="eyebrow">Estilos de yoga</span>
      <h2>Cuatro caminos, un mismo equilibrio</h2>
      <p class="lead" style="margin-top:1.1rem">Cada estilo aporta algo distinto. Elegimos juntas el que mejor acompaña tu cuerpo y tu momento.</p>
    </div>
    <div class="grid grid-4">{items}</div>
    <div class="botonera botonera--centro mt-l">
      <a class="btn btn--linea" href="#contacto">Consultar horarios y tarifas</a>
    </div>
  </div>
</section>'''

def bloque_beneficios(fondo=""):
    items = "".join(f'''
      <article class="beneficio revelar" data-retardo="{(i%3)*80}">
        <span class="beneficio__num">{str(i+1).zfill(2)}</span>
        <h4>{t}</h4>
        <p>{d}</p>
      </article>''' for i, (t, d) in enumerate(BENEFICIOS))
    return f'''
<section class="seccion {fondo}" id="beneficios">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(30px,4vw,54px)">
      <span class="eyebrow">Qué vas a notar</span>
      <h2>Cuidarte desde la presencia</h2>
    </div>
    <div class="grid grid-3">{items}</div>
  </div>
</section>'''

def bloque_implementos():
    chips = "".join(f'<span class="zona">{i}</span>' for i in IMPLEMENTOS)
    return f'''
<section class="seccion seccion--compacta">
  <div class="contenedor duo">
    <div class="duo__media revelar">
      <img src="assets/img/pilates.jpg" alt="Clase de Pilates Mat en el suelo" loading="lazy" width="1200" height="900">
    </div>
    <div class="revelar" data-retardo="100">
      <span class="eyebrow">Pilates Mat</span>
      <h2>Con implementos, para llegar más lejos</h2>
      <p style="margin-top:1.1rem">En mis clases incorporo distintos implementos que permiten adaptar la intensidad, profundizar en la técnica y hacer la práctica más dinámica y completa. Ayudan a activar zonas concretas, mejorar la movilidad y acompañar el movimiento de forma segura.</p>
      <div class="zonas" style="margin-top:1.4rem">{chips}</div>
    </div>
  </div>
</section>'''

def bloque_pasos(fondo="seccion--verde"):
    items = "".join(f'''
      <article class="paso revelar" data-retardo="{i*90}">
        <span class="paso__num">{i+1}</span>
        <h3>{t}</h3>
        <p>{d}</p>
      </article>''' for i, (t, d) in enumerate(PASOS))
    return f'''
<section class="seccion {fondo}" id="empezar">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(30px,4vw,54px)">
      <span class="eyebrow">Cómo empezar</span>
      <h2>Tres pasos y estás dentro</h2>
    </div>
    <div class="grid grid-3">{items}</div>
    <div class="botonera botonera--centro mt-l">
      <a class="btn btn--oro" href="{WA_URL}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
    </div>
  </div>
</section>'''


def bloque_faq():
    faq = "".join(f'''
      <div class="acordeon__item">
        <button class="acordeon__boton" type="button" aria-expanded="false">
          <span>{p}</span><span aria-hidden="true">+</span>
        </button>
        <div class="acordeon__panel"><div><p>{r}</p></div></div>
      </div>''' for p, r in FAQ)
    return f'''
<section class="seccion" id="faq">
  <div class="contenedor">
    <div class="medida texto-centrado" style="margin-bottom:clamp(28px,3.5vw,46px)">
      <span class="eyebrow">Dudas frecuentes</span>
      <h2>Antes de tu primera clase</h2>
    </div>
    <div class="medida acordeon revelar" data-acordeon>{faq}</div>
  </div>
</section>'''

# =============================== LANDING ===================================
# Versión de una sola página: todo el contenido en scroll, orientada a conversión.
# Tres entradas a cada lado del logotipo, para que quede centrado de verdad.
NAV_IZQ = [("#sobre-mi", "Sobre mí"), ("#servicios", "Servicios"), ("#programas", "Programas")]
NAV_DER = [("#retiros", "Retiros"), ("#contacto", "Contacto")]
NAV_LANDING = NAV_IZQ + NAV_DER + [("#opiniones", "Opiniones")]

def cabecera_landing():
    enlaces = "".join('<a href="%s">%s</a>' % (h, t) for h, t in NAV_IZQ)
    enlaces_der = "".join('<a href="%s">%s</a>' % (h, t) for h, t in
                          [("#opiniones", "Opiniones")] + NAV_DER)
    movil = "".join('<a href="%s">%s</a>' % (h, t) for h, t in
                    NAV_IZQ + [("#opiniones", "Opiniones")] + NAV_DER)
    return f'''
<header class="cabecera cabecera--transparente" data-cabecera>
  <div class="cabecera__interior">
    <a class="logo" href="#inicio" aria-label="{MARCA}">
      <img class="logo__simbolo logo__simbolo--color" src="assets/img/logo-marca.svg" alt="" width="34" height="34">
      <img class="logo__simbolo logo__simbolo--crema" src="assets/img/logo-marca-crema.svg" alt="" width="34" height="34">
      <span class="logo__texto">{MARCA}</span>
    </a>
    <nav class="nav nav--principal" aria-label="Navegación principal">
      {enlaces}{enlaces_der}
      <a class="btn btn--linea" href="#contacto">Reservar</a>
    </nav>
    <button class="hamburguesa" type="button" aria-label="Abrir menú" aria-expanded="false" data-menu-boton>
      <span></span><span></span><span></span>
    </button>
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
      <article class="tarjeta-texto revelar" data-retardo="{(i%4)*90}">
        <div class="numero">{str(i+1).zfill(2)}</div>
        <h3>{t}</h3>
        <p style="margin:.4rem 0 1rem">{d}</p>
        <ul style="margin:0 0 1.2rem">{"".join(f'<li style="font-size:.88rem;padding-left:16px;position:relative"><span style="position:absolute;left:0;color:var(--melocoton-2)">·</span>{b}</li>' for b in bullets)}</ul>
        <a class="enlace-flecha" style="margin-top:auto;align-self:flex-start" href="#contacto">Quiero información</a>
      </article>''' for i, (img, t, d, bullets) in enumerate(PROGRAMAS))

    eventos = "".join(f'''
      <article class="tarjeta-texto revelar" data-retardo="{(i%3)*80}">
        <span class="eyebrow" style="margin-bottom:.5rem">{et}</span>
        <h3>{t}</h3>
        <p style="margin:.4rem 0 1.1rem">{d}</p>
        <a class="enlace-flecha" style="margin-top:auto;align-self:flex-start" href="#contacto">Quiero información</a>
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
    <img src="assets/img/portada.jpg" alt="Clase de Pilates Mat en el estudio de ANAHATA" width="1920" height="1280" fetchpriority="high">
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
      <img src="assets/img/sara.jpg" alt="Sara Viñas con sus alumnas en el estudio"
           loading="lazy" width="900" height="1200">
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

{bloque_formacion()}
{bloque_estilos_resumen("")}
{bloque_implementos()}
{bloque_beneficios("seccion--crema")}

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

{bloque_pasos()}

<section class="seccion" id="retiros">
  <div class="contenedor">
    <figure class="banda-foto revelar">
      <img src="assets/img/tribu.jpg" alt="Grupo de alumnas y alumnos de ANAHATA" loading="lazy" width="1400" height="1050">
    </figure>
    <div class="medida texto-centrado" style="margin:clamp(40px,5vw,64px) auto clamp(32px,4vw,52px)">
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
    <p class="texto-centrado" style="margin-top:2rem">
      <a class="enlace-flecha" href="{GOOGLE_REVIEW}" target="_blank" rel="noopener">Ver reseñas en Google</a>
    </p>
  </div>
</section>

{bloque_faq()}

<section class="seccion seccion--crema" id="contacto">
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


def enlaces_de_landing(html):
    """En la landing todo vive en una sola página: los enlaces a páginas
       internas pasan a ser anclas. Las legales siguen siendo páginas."""
    cambios = [
        ("contacto.html#reservar", "#contacto"),
        ("contacto.html", "#contacto"),
        ("servicios.html#pilates", "#servicios"),
        ("servicios.html#meditacion", "#servicios"),
        ("servicios.html#alimentacion", "#servicios"),
        ("servicios.html", "#servicios"),
        ("clases.html", "#programas"),
        ("retiros.html", "#retiros"),
        ("sobre-mi.html", "#sobre-mi"),
        ("index.html", "#inicio"),
    ]
    for viejo, nuevo in cambios:
        html = html.replace(f'href="{viejo}"', f'href="{nuevo}"')
    return html

# =============================== GENERAR ===================================
if __name__ == "__main__":
    # La landing es la web: se publica como index.html
    escribir("index.html", enlaces_de_landing(pagina_landing()))
    escribir("aviso-legal.html", pagina_legal("Aviso legal", "aviso-legal.html",
             f"Aviso legal de {MARCA} · {TITULAR}.", AVISO_LEGAL))
    escribir("privacidad.html",  pagina_legal("Política de privacidad y cookies", "privacidad.html",
             f"Política de privacidad y cookies de {MARCA} · {TITULAR}.", PRIVACIDAD))
    print("Web generada:", ", ".join(sorted(f for f in os.listdir('.') if f.endswith('.html'))))
