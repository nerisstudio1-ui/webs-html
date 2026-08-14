#!/usr/bin/env python3
"""
Genera la web de Laconic Studio en catalán y castellano.

    python3 build/build.py

Escribe `index.html` (catalán, raíz) y `es/index.html` (castellano). Todo el
contenido vive en este archivo: para cambiar un texto se edita aquí y se vuelve
a ejecutar, así las dos versiones no se desincronizan nunca.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------- #
# Logo: los tres SVG oficiales se convierten en un sprite de <symbol>
# --------------------------------------------------------------------------- #


def leer_svg(nombre):
    s = (ROOT / 'assets/img' / nombre).read_text(encoding='utf-8')
    return (re.search(r'viewBox="([^"]+)"', s).group(1),
            re.search(r'(<path[^>]+/>)', s).group(1))


VB_WORD, P_WORD = leer_svg('logo-laconic.svg')
VB_ZERO, P_ZERO = leer_svg('logo-zero.svg')
VB_LOCK, P_LOCK = leer_svg('logo-lockup.svg')

# Los cinco iconos que el estudio usa junto a cada servicio en su flyer:
# un sol pequeño, la pausa, un asterisco, la flecha y el cero.
ICONOS = {
    'ic-sol': '<g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">'
              '<circle cx="12" cy="12" r="3.2"/>'
              '<path d="M12 1.6v3.2M12 19.2v3.2M1.6 12h3.2M19.2 12h3.2'
              'M4.6 4.6l2.3 2.3M17.1 17.1l2.3 2.3M19.4 4.6l-2.3 2.3M6.9 17.1l-2.3 2.3"/></g>',
    'ic-pausa': '<g fill="currentColor"><rect x="7" y="3" width="3.4" height="18" rx="1.7"/>'
                '<rect x="13.6" y="3" width="3.4" height="18" rx="1.7"/></g>',
    'ic-asterisc': '<g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">'
                   '<path d="M12 1.5v21M2.9 6.8l18.2 10.4M21.1 6.8L2.9 17.2"/></g>',
    'ic-fletxa': '<g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
                 'stroke-linejoin="round"><path d="M5.5 18.5L18.5 5.5"/><path d="M8.7 5.5h9.8v9.8"/></g>',
    'ic-cercle': '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2.4"/>',
}

SPRITE = (
    '<!-- Logo oficial de la marca vectorizado: el cero, el logotipo y el lockup,\n'
    '     más los iconos de los servicios. Todos heredan color con currentColor. -->\n'
    '<svg class="sprite" aria-hidden="true" focusable="false">\n'
    f'  <symbol id="lg-zero" viewBox="{VB_ZERO}">{P_ZERO}</symbol>\n'
    f'  <symbol id="lg-word" viewBox="{VB_WORD}">{P_WORD}</symbol>\n'
    f'  <symbol id="lg-lockup" viewBox="{VB_LOCK}">{P_LOCK}</symbol>\n'
    + ''.join(f'  <symbol id="{k}" viewBox="0 0 24 24">{v}</symbol>\n'
              for k, v in ICONOS.items())
    + '</svg>'
)

# Un icono por servicio, en el orden del flyer
ICONO_SERVICIO = ['ic-sol', 'ic-pausa', 'ic-asterisc', 'ic-fletxa', 'ic-cercle']

# --------------------------------------------------------------------------- #
# Proyectos. Las descripciones en catalán son las que escribió el estudio en las
# tarjetas de cada carpeta; la versión castellana es su traducción.
# --------------------------------------------------------------------------- #

PROYECTOS = [
    dict(
        slug='quality', portada=1, fotos=3,
        nombre='Quality Training',
        sector=dict(ca='Entrenament', es='Entrenamiento'),
        texto=dict(
            ca='Hem transformat el coneixement tècnic de Quality Training en contingut '
               'atractiu per a xarxes socials, reforçant la seva imatge de marca, la '
               'connexió amb la comunitat i la captació de nous clients.',
            es='Transformamos el conocimiento técnico de Quality Training en contenido '
               'atractivo para redes sociales, reforzando su imagen de marca, la '
               'conexión con la comunidad y la captación de nuevos clientes.'),
        servicios=dict(ca=['Creació de contingut', 'Social media'],
                       es=['Creación de contenido', 'Social media']),
        piezas=['https://www.instagram.com/p/DYzzgzto1uT/',
                'https://www.instagram.com/p/DZIkSk0s2Yc/'],
    ),
    dict(
        slug='malhivern', portada=2, fotos=4,
        nombre='Ratafia Malhivern',
        sector=dict(ca='Licors artesans', es='Licores artesanos'),
        texto=dict(
            ca='Estratègia de continguts, direcció creativa i gestió de xarxes socials '
               'per construir una marca propera, autèntica i amb una identitat pròpia.',
            es='Estrategia de contenidos, dirección creativa y gestión de redes sociales '
               'para construir una marca cercana, auténtica y con identidad propia.'),
        servicios=dict(ca=['Estratègia', 'Direcció creativa', 'Social media'],
                       es=['Estrategia', 'Dirección creativa', 'Social media']),
        piezas=['https://www.instagram.com/p/DZKUPZXNnqz/'],
    ),
    dict(
        slug='f4s', portada=1, fotos=4,
        nombre='Football 4 Stars',
        sector=dict(ca='Futbol formatiu', es='Fútbol formativo'),
        texto=dict(
            ca='Hem impulsat la presència digital de Football 4 Stars amb contingut '
               'aspiracional, estratègic i orientat a la captació.',
            es='Impulsamos la presencia digital de Football 4 Stars con contenido '
               'aspiracional, estratégico y orientado a la captación.'),
        servicios=dict(ca=['Social media', 'Creació de contingut'],
                       es=['Social media', 'Creación de contenido']),
        piezas=[],
    ),
    dict(
        slug='maitasuna', portada=1, fotos=4,
        nombre='Maitasuna',
        sector=dict(ca='Pizza artesana', es='Pizza artesana'),
        texto=dict(
            ca="Hem treballat una estratègia de contingut centrada en humanitzar la "
               "marca i potenciar la figura de l'Alain, transmetent l'essència artesana "
               "i propera de Maitasuna.",
            es='Trabajamos una estrategia de contenido centrada en humanizar la marca y '
               'potenciar la figura de Alain, transmitiendo la esencia artesana y '
               'cercana de Maitasuna.'),
        servicios=dict(ca=['Creació de contingut', 'Social media'],
                       es=['Creación de contenido', 'Social media']),
        piezas=[],
    ),
    dict(
        slug='jordi-coll', portada=2, fotos=3,
        nombre='Jordi Coll',
        sector=dict(ca='Marca personal', es='Marca personal'),
        texto=dict(
            ca="Hem treballat l'estratègia de continguts de Jordi Coll, creant reels per "
               "potenciar la seva marca personal i promocionar el llançament d'"
               "<em>El pont de les mentides</em>.",
            es='Trabajamos la estrategia de contenidos de Jordi Coll, creando reels para '
               'potenciar su marca personal y promocionar el lanzamiento de '
               '<em>El pont de les mentides</em>.'),
        servicios=dict(ca=['Estratègia', 'Reels'], es=['Estrategia', 'Reels']),
        piezas=['https://www.instagram.com/p/DVgLjIqjHTp/',
                'https://www.instagram.com/p/DVxsEDcjHw5/'],
    ),
    dict(
        slug='f45', portada=1, fotos=3,
        nombre='F45 Training',
        sector=dict(ca='Esdeveniment', es='Evento'),
        texto=dict(
            ca="Vam crear contingut audiovisual per a la inauguració de F45, capturant "
               "l'energia de l'esdeveniment i reforçant la imatge de marca amb peces "
               "pensades per a xarxes socials.",
            es='Creamos contenido audiovisual para la inauguración de F45, capturando la '
               'energía del evento y reforzando la imagen de marca con piezas pensadas '
               'para redes sociales.'),
        servicios=dict(ca=['Creació de contingut', 'Vídeo'],
                       es=['Creación de contenido', 'Vídeo']),
        piezas=[],
    ),
    dict(
        slug='puig', portada=3, fotos=3,
        nombre='Comercial Puig',
        sector=dict(ca='Distribució', es='Distribución'),
        texto=dict(
            ca='Creem contingut que apropa Comercial Puig als seus clients, mostrant el '
               "valor dels seus productes, l'assessorament personalitzat i el dia a dia "
               "d'un negoci familiar.",
            es='Creamos contenido que acerca Comercial Puig a sus clientes, mostrando el '
               'valor de sus productos, el asesoramiento personalizado y el día a día de '
               'un negocio familiar.'),
        servicios=dict(ca=['Creació de contingut', 'Social media'],
                       es=['Creación de contenido', 'Social media']),
        piezas=['https://www.instagram.com/p/Daiq_1ztSC-/',
                'https://www.instagram.com/p/DT24wj7iAJN/'],
    ),
]

# Descripción de cada foto para el atributo alt
ALT = {
    'quality-1': dict(ca='Corredor en un camí amb un pi al fons',
                      es='Corredor en un camino con un pino al fondo'),
    'quality-2': dict(ca='Entrenament de força amb manuelles al gimnàs',
                      es='Entrenamiento de fuerza con mancuernas en el gimnasio'),
    'quality-3': dict(ca="Entrenador amb la samarreta de Quality Training parlant amb un client",
                      es='Entrenador con la camiseta de Quality Training hablando con un cliente'),
    'malhivern-1': dict(ca='Ampolla de ratafia Malhivern amb llum càlida',
                        es='Botella de ratafía Malhivern con luz cálida'),
    'malhivern-2': dict(ca='Ampolla de ratafia sobre pedra amb plantes aromàtiques',
                        es='Botella de ratafía sobre piedra con plantas aromáticas'),
    'malhivern-3': dict(ca='Ampolles de licor artesà en una lleixa de pedra',
                        es='Botellas de licor artesano en una estantería de piedra'),
    'malhivern-4': dict(ca='Prestatge amb la gamma de licors Sol i Serena',
                        es='Estantería con la gama de licores Sol i Serena'),
    'f4s-1': dict(ca='Entrenament de futbol formatiu al camp',
                  es='Entrenamiento de fútbol formativo en el campo'),
    'f4s-2': dict(ca='Jugador conduint la pilota entre cons',
                  es='Jugador conduciendo el balón entre conos'),
    'f4s-3': dict(ca='Partit d\'entrenament en un camp de gespa artificial',
                  es='Partido de entrenamiento en un campo de césped artificial'),
    'maitasuna-1': dict(ca='Pizza artesana acabada de sortir del forn',
                        es='Pizza artesana recién salida del horno'),
    'maitasuna-2': dict(ca="Mans pastant massa amb la jaqueta de l'obrador",
                        es='Manos amasando con la chaquetilla del obrador'),
    'maitasuna-3': dict(ca='Pizzes en caixes preparades per servir',
                        es='Pizzas en cajas preparadas para servir'),
    'jordi-coll-1': dict(ca="Exemplar d'El pont de les mentides en una presentació",
                         es='Ejemplar de El pont de les mentides en una presentación'),
    'jordi-coll-2': dict(ca='Públic assistint a la presentació del llibre',
                         es='Público asistiendo a la presentación del libro'),
    'jordi-coll-3': dict(ca='Lector amb el llibre signat a la llibreria',
                         es='Lector con el libro firmado en la librería'),
    'f45-1': dict(ca='Assistent a la inauguració de F45',
                  es='Asistente a la inauguración de F45'),
    'f45-2': dict(ca='Detall d\'un entrenament en parella a F45',
                  es='Detalle de un entrenamiento en pareja en F45'),
    'f45-3': dict(ca='Rètol de F45 Training al box',
                  es='Rótulo de F45 Training en el box'),
    'puig-1': dict(ca='Ampolla de vi a la mà en el punt de venda',
                   es='Botella de vino en la mano en el punto de venta'),
    'puig-2': dict(ca='Productes de Comercial Puig al taulell',
                   es='Productos de Comercial Puig en el mostrador'),
    'puig-3': dict(ca='Retrat en blanc i negre a la botiga',
                   es='Retrato en blanco y negro en la tienda'),
}

# --------------------------------------------------------------------------- #
# Textos de la web
# --------------------------------------------------------------------------- #

T = {
    'ca': dict(
        lang='ca', otra='es', otra_nombre='ES', propia_nombre='CA',
        titulo='Laconic Studio | Estudi creatiu de contingut, social media i estratègia',
        descripcion='Laconic Studio: creació de contingut, social media i estratègia digital. '
                    'Less noise. More meaning.',
        saltar='Salta al contingut',
        nav=[('#about', 'About'), ('#serveis', 'Serveis'),
             ('#projectes', 'Projectes'), ('#contacte', 'Contacte')],
        nav_movil=[('#about', 'About', 'qui som'), ('#serveis', 'Serveis', 'què fem'),
                   ('#projectes', 'Projectes', 'què hem fet'),
                   ('#contacte', 'Contacte', 'escriu-nos')],
        cta='Parlem', menu_abrir='Obre el menú',
        hero_nota='Estudi creatiu · Girona',
        # Las dos mitades del filete del inicio, en inglés en los dos idiomas
        hero_izq='Based in Girona.', hero_der='Working beyond.',
        reclamo='Contingut que connecta.',
        k_sobre='About',
        # La manuscrita va dentro de la frase, como la cursiva de la referencia
        declaracion='Ajudem a marques a deixar empremta '
                    '<span class="hand">(de la de veritat)</span>.',
        id_estudio='about', id_servicios='serveis', id_trabajo='projectes',
        id_contacto='contacte',
        k_estudio='L\'estudi',
        h_estudio='Cada marca comunica, <span class="hand">però no totes connecten</span>.',
        cuerpo_estudio=[
            'Som un estudi creatiu especialitzat en xarxes socials, creació de contingut i '
            'estratègia digital. Treballem amb marques que volen construir una presència '
            'coherent, autèntica i amb criteri, creant contingut que connecti amb les '
            'persones i tingui un objectiu darrere.',
            'Ens impliquem en cada projecte com si fos nostre: analitzem, planifiquem, '
            'gravem, editem i pensem cada detall perquè cada publicació sumi i tingui '
            'sentit dins d\'una estratègia.'],
        # Cierre del párrafo del about: en Raleway, no en manuscrita
        nota_estudio='Busquem marques que vulguin deixar empremta.',
        equipo=[('Núria', 'Creative &amp; Founder'), ('Júlia', 'Strategist &amp; Founder')],
        equipo_nota='Som dues, i ens agrada que sigui així. Parles directament amb qui '
                    'pensa, crea i executa. I si no podem fer-ho bé, preferim dir que no.',
        k_servicios='Serveis',
        # (número, nombre, nombre corto para la línea que pasa, definición)
        servicios=[
            ('01', 'Content creation', 'Content creation',
             'Creem contingut que expliqui qui ets, què fas i per què t\'haurien de mirar. '
             'Pensem la idea, gravem i editem perquè cada peça tingui un motiu i una raó de '
             'ser. Volem apropar-vos al vostre públic objectiu de la manera en la qual '
             'estigueu més còmodes.'),
            ('02', 'Social Media', 'Social Media',
             'Ens encarreguem de les teves xarxes perquè tu puguis centrar-te en el teu '
             'negoci. Planifiquem, publiquem i gestionem el dia a dia del perfil.'),
            ('03', 'Ads &amp; Campaigns', 'Ads &amp; campaigns',
             'Fem que el contingut arribi més lluny. Creem i gestionem campanyes pensades '
             'per arribar a les persones adequades i aconseguir un objectiu concret a '
             'través de Meta Ads.'),
            ('04', 'UGC', 'UGC',
             'Creem contingut com ho faria una persona real. Vídeos naturals, propers i '
             'pensats per connectar amb el públic sense que sembli un anunci.'),
            ('05', 'Graphic Design &amp; Brand Identity', 'Graphic Design',
             'Donem forma visual a les idees que hi ha darrere de la teva marca. Treballem '
             'la teva identitat i creem les peces gràfiques necessàries perquè sigui '
             'coherent, reconeixible i tingui personalitat.'),
        ],
        btn_presupuesto='Demana pressupost',
        k_trabajo='Projectes',
        h_trabajo='Get people <span class="hand">talking</span> about your brand.',
        pieza='Peça', reel_sonido='Activa el so', reel_silencio='Silencia el so',
        ver_instagram='Mira-ho a Instagram',
        proyecto_ver='Obre el perfil a Instagram',
        k_contacto='Contacte',
        h_contacto='Això comença <span class="hand">amb un missatge</span>.',
        lead_contacto='Explica\'ns qui ets i què t\'està frenant. Et respondrem en menys de '
                      '48 hores. O la Núria o la Júlia &#128578;',
        dm='DM a @laconicstudio_',
        f_nombre='El teu nom', f_marca='Marca o projecte', f_email='Email',
        f_necesitas='Què necessites', f_cuentanos='Explica\'ns',
        f_placeholder='Explica\'ns el que vulguis i en parlem.',
        f_enviar='Envia el missatge',
        f_asunto='Nou missatge des de la web',
        f_nota_envio='Et responem al correu que ens deixis. No el fem servir per a res més.',
        f_enviando='Enviant…',
        f_ok_envio='Rebut. Et responem en menys de 48 hores laborables.',
        f_error='No hem pogut enviar-ho. Escriu-nos directament a ',
        f_nota='En enviar s\'obre el teu client de correu amb el missatge ja redactat.',
        f_ok='Obrim el teu client de correu amb el missatge llest. Si no s\'obre, escriu-nos a ',
        pie_ubicacion='Based in Girona. Working beyond.',
        pie_credito='Web feta per', pie_credito_quien='Neris Studio',
        pie_nav=[('#about', 'About'), ('#serveis', 'Serveis'),
                 ('#projectes', 'Projectes'), ('#contacte', 'Contacte')],
    ),
    'es': dict(
        lang='es', otra='ca', otra_nombre='CA', propia_nombre='ES',
        titulo='Laconic Studio | Estudio creativo de contenido, social media y estrategia',
        descripcion='Laconic Studio: creación de contenido, social media y estrategia digital. '
                    'Less noise. More meaning.',
        saltar='Saltar al contenido',
        nav=[('#about', 'About'), ('#servicios', 'Servicios'),
             ('#proyectos', 'Proyectos'), ('#contacto', 'Contacto')],
        nav_movil=[('#about', 'About', 'quiénes somos'), ('#servicios', 'Servicios', 'qué hacemos'),
                   ('#proyectos', 'Proyectos', 'qué hemos hecho'),
                   ('#contacto', 'Contacto', 'escríbenos')],
        cta='Hablemos', menu_abrir='Abrir el menú',
        hero_nota='Estudio creativo · Girona',
        hero_izq='Based in Girona.', hero_der='Working beyond.',
        reclamo='Contenido que conecta.',
        k_sobre='About',
        # El claim traducido: en la web catalana va «Contingut que connecta.»
        declaracion='Ayudamos a marcas a dejar huella '
                    '<span class="hand">(de la de verdad)</span>.',
        id_estudio='about', id_servicios='servicios', id_trabajo='proyectos',
        id_contacto='contacto',
        k_estudio='El estudio',
        h_estudio='Cada marca comunica, <span class="hand">pero no todas conectan</span>.',
        cuerpo_estudio=[
            'Somos un estudio creativo especializado en redes sociales, creación de contenido '
            'y estrategia digital. Trabajamos con marcas que quieren construir una presencia '
            'coherente, auténtica y con criterio, creando contenido que conecte con las '
            'personas y tenga un objetivo detrás.',
            'Nos implicamos en cada proyecto como si fuera nuestro: analizamos, planificamos, '
            'grabamos, editamos y pensamos cada detalle para que cada publicación sume y '
            'tenga sentido dentro de una estrategia.'],
        nota_estudio='Buscamos marcas que quieran dejar huella.',
        equipo=[('Núria', 'Creative &amp; Founder'), ('Júlia', 'Strategist &amp; Founder')],
        equipo_nota='Somos dos, y nos gusta que sea así. Hablas directamente con quien '
                    'piensa, crea y ejecuta. Y si no podemos hacerlo bien, preferimos decir que no.',
        k_servicios='Servicios',
        servicios=[
            ('01', 'Content creation', 'Content creation',
             'Creamos contenido que explique quién eres, qué haces y por qué deberían '
             'mirarte. Pensamos la idea, grabamos y editamos para que cada pieza tenga un '
             'motivo y una razón de ser. Queremos acercaros a vuestro público objetivo de '
             'la manera en la que estéis más cómodos.'),
            ('02', 'Social Media', 'Social Media',
             'Nos encargamos de tus redes para que tú puedas centrarte en tu negocio. '
             'Planificamos, publicamos y gestionamos el día a día del perfil.'),
            ('03', 'Ads &amp; Campaigns', 'Ads &amp; campaigns',
             'Hacemos que el contenido llegue más lejos. Creamos y gestionamos campañas '
             'pensadas para llegar a las personas adecuadas y conseguir un objetivo '
             'concreto a través de Meta Ads.'),
            ('04', 'UGC', 'UGC',
             'Creamos contenido como lo haría una persona real. Vídeos naturales, cercanos '
             'y pensados para conectar con el público sin que parezca un anuncio.'),
            ('05', 'Graphic Design &amp; Brand Identity', 'Graphic Design',
             'Damos forma visual a las ideas que hay detrás de tu marca. Trabajamos tu '
             'identidad y creamos las piezas gráficas necesarias para que sea coherente, '
             'reconocible y tenga personalidad.'),
        ],
        btn_presupuesto='Pedir presupuesto',
        k_trabajo='Proyectos',
        h_trabajo='Get people <span class="hand">talking</span> about your brand.',
        pieza='Pieza', reel_sonido='Activar el sonido', reel_silencio='Silenciar',
        ver_instagram='Verlo en Instagram',
        proyecto_ver='Abre el perfil en Instagram',
        k_contacto='Contacto',
        h_contacto='Esto empieza <span class="hand">con un mensaje</span>.',
        lead_contacto='Cuéntanos quién eres y qué te está frenando. Te responderemos en menos '
                      'de 48 horas. O Núria o Júlia &#128578;',
        dm='DM a @laconicstudio_',
        f_nombre='Tu nombre', f_marca='Marca o proyecto', f_email='Email',
        f_necesitas='Qué necesitas', f_cuentanos='Cuéntanos',
        f_placeholder='Cuéntanos lo que quieras y hablamos.',
        f_enviar='Enviar mensaje',
        f_asunto='Nuevo mensaje desde la web',
        f_nota_envio='Te respondemos al correo que nos dejes. No lo usamos para nada más.',
        f_enviando='Enviando…',
        f_ok_envio='Recibido. Te respondemos en menos de 48 horas laborables.',
        f_error='No hemos podido enviarlo. Escríbenos directamente a ',
        f_nota='Al enviar se abre tu cliente de correo con el mensaje ya redactado.',
        f_ok='Abrimos tu cliente de correo con el mensaje listo. Si no se abre, escríbenos a ',
        pie_ubicacion='Based in Girona. Working beyond.',
        pie_credito='Web hecha por', pie_credito_quien='Neris Studio',
        pie_nav=[('#about', 'About'), ('#servicios', 'Servicios'),
                 ('#proyectos', 'Proyectos'), ('#contacto', 'Contacto')],
    ),
}

EMAIL = 'hello@laconicstudio.es'
INSTAGRAM = 'https://www.instagram.com/laconicstudio_/'
NERIS = 'https://www.nerisstudio.com'

# A dónde llega el formulario.
#
# FormSubmit envía el mensaje por correo a EMAIL y no pide cuenta, clave ni
# plugin: basta con que la dirección aparezca en el action. La primera vez hay
# que confirmarla una sola vez —ver wordpress/INSTALACION.md—: se envía el
# formulario desde la web publicada, FormSubmit manda un correo a EMAIL con un
# enlace, se pulsa, y desde ese momento todos los mensajes entran en la bandeja.
#
# Alternativas que también funcionan dentro de un bloque de HTML de WordPress;
# solo cambia esta casilla:
#   Web3Forms   https://web3forms.com    FORM_ACTION = 'https://api.web3forms.com/submit'
#                                        FORM_AJAX   = igual que FORM_ACTION
#                                        FORM_OCULTOS = {'access_key': 'la-clave'}
#   Formspree   https://formspree.io     FORM_ACTION = 'https://formspree.io/f/xxxxxxx'
#                                        FORM_AJAX   = igual que FORM_ACTION
#
# Vacío = sin servicio: el formulario compone el correo y abre el cliente de
# email del visitante (mailto). Es el modo de reserva y pierde a quien usa
# webmail, así que solo para pruebas en local.
#
# Un plugin tipo Contact Form 7 no sirve aquí: su shortcode no se ejecuta dentro
# de un bloque de HTML personalizado.
FORM_ACTION = f'https://formsubmit.co/{EMAIL}'

# La misma dirección en la variante que contesta en JSON. Con ella el envío
# ocurre sin salir de la página. Si el visitante no tiene JS, el <form> se envía
# como siempre a FORM_ACTION y responde la página de gracias del servicio.
FORM_AJAX = f'https://formsubmit.co/ajax/{EMAIL}'

# Campos de control del servicio. En FormSubmit empiezan por guion bajo:
#   _captcha  false, porque su reCAPTCHA intermedio corta el envío desde la web
#   _template table, para que el correo llegue ordenado y no en un párrafo
#   _honey    trampa para robots: si llega con algo escrito, se descarta el envío
FORM_OCULTOS = {'_captcha': 'false', '_template': 'table', '_honey': ''}
DOMINIO = 'https://laconicstudio.com'

# Fotos del collage: proyecto y número de foto. COLLAGE alimenta el panel de
# servicios; HERO_FONDO es la foto a sangre del inicio, HERO_CHIP la pieza
# pequeña que se cruza con el logotipo, y TIRA la banda de cinco fotos que sube
# con el scroll por delante del titular gigante.
COLLAGE = [('malhivern', 3), ('quality', 1), ('maitasuna', 1), ('puig', 3), ('f4s', 1)]
# Ojo: varias fotos del estudio son collages de dos o tres imágenes montadas, y
# a sangre se les ve la costura. Las que se usan grandes son de una sola toma:
# collages detectados y descartados aquí: f45-2, f45-3, jordi-coll-1, puig-2,
# quality-2 y maitasuna-3.
# Foto de marca del estudio (el flyer sobre el coche), no una foto de proyecto
HERO_FOTO = 'marca/flyer-cotxe'
HERO_ANCHOS = (900, 1600)

# Las DOS fotos del inicio, a sangre y a toda la altura de la pantalla.
#
# PENDIENTE: el estudio dijo que adjuntaba las dos escogidas y no llegaron con el
# PDF. Mientras tanto van dos de una sola toma (nunca collages: a este tamaño se
# les vería la costura) y verticales, que es lo que pide el formato. Al recibir
# las suyas, se dejan en assets/img/proyectos con el nombre que toque y se cambia
# esta línea; no hay nada más que tocar.
HERO_DUO = [('maitasuna', 1), ('puig', 3)]

# La tira que pasa en bucle en el about. PENDIENTE: aquí también dijeron que
# adjuntaban «una selección de las más top» y no llegó; van siete de una sola toma.
TIRA = [('quality', 1), ('f45', 1), ('maitasuna', 1), ('f4s', 1), ('malhivern', 2),
        ('jordi-coll', 2), ('malhivern', 3)]

# --------------------------------------------------------------------------- #
# Vídeos. Se detectan solos: basta dejar los archivos en assets/video con el
# nombre del proyecto, `<slug>-1.mp4`, `<slug>-2.mp4`… Si un proyecto tiene
# vídeos, su columna de la izquierda pasa a ser el reel (con la foto como
# póster). Si no los tiene, se queda la foto. No hay nada que tocar aquí.
# --------------------------------------------------------------------------- #

# Fotos que son collages de dos o tres imágenes montadas, o que tienen una
# costura visible. No se usan en ningún sitio donde se vean grandes.
COLAJES = {'f45-2', 'f45-3', 'jordi-coll-1', 'puig-2', 'quality-2', 'maitasuna-3',
           'malhivern-1', 'puig-1', 'f4s-3', 'quality-4'}
IMG_DIR = ROOT / 'assets/img/proyectos'


def extras_de(slug, portada, cuantas=2):
    """Las demás fotos sueltas del proyecto, para la galería de su bloque."""
    numeros = []
    for ruta in IMG_DIR.glob(f'{slug}-*-700.jpg'):
        resto = ruta.stem[len(slug) + 1:-4]   # quita el slug y el '-700'
        if resto.isdigit() and int(resto) != portada and f'{slug}-{resto}' not in COLAJES:
            numeros.append(int(resto))
    return sorted(numeros)[:cuantas]


VIDEO_DIR = ROOT / 'assets/video'
FORMATOS = ('.mp4', '.webm')   # si están los dos del mismo clip, gana el mp4
MAX_REELS = 2

# Las fichas de proyecto de los cuatro que tienen reel enseñan el vídeo en bucle
# y sin sonido, recortado igual que las fotos: la retícula no cambia, y el
# material que grabó el estudio no se pierde. En False, todas enseñan su foto.
PROYECTOS_CON_VIDEO = True


def poster_de(nombre_video):
    """Fotograma del propio vídeo, si se ha extraído; si no, None."""
    ruta = VIDEO_DIR / (pathlib.Path(nombre_video).stem + '-poster.jpg')
    return ruta.name if ruta.exists() else None


def videos_de(slug):
    """Devuelve los nombres de archivo de los vídeos del proyecto, ordenados."""
    if not VIDEO_DIR.is_dir():
        return []
    por_clip = {}
    for ruta in VIDEO_DIR.iterdir():
        if ruta.suffix.lower() not in FORMATOS or not ruta.stem.startswith(slug + '-'):
            continue
        # El resto del nombre tiene que ser el número de la pieza
        resto = ruta.stem[len(slug) + 1:]
        if not resto.isdigit():
            continue
        clip = int(resto)
        anterior = por_clip.get(clip)
        if anterior is None or FORMATOS.index(ruta.suffix.lower()) < FORMATOS.index(anterior.suffix.lower()):
            por_clip[clip] = ruta
    return [por_clip[k].name for k in sorted(por_clip)][:MAX_REELS]


def medidas(slug, n):
    """Tamaño real del archivo. Varias fotos venían con un marco blanco dentro y
    al recortarlo dejaron de ser 4:5, así que no se puede dar por hecho."""
    from PIL import Image
    with Image.open(IMG_DIR / f'{slug}-{n}-1100.jpg') as im:
        return im.size


def foto(prefix, slug, n, sizes, lang, loading='lazy', clases=''):
    alt = ALT.get(f'{slug}-{n}', {}).get(lang, '')
    cls = f' class="{clases}"' if clases else ''
    ancho, alto = medidas(slug, n)
    return (f'<img{cls} src="{prefix}assets/img/proyectos/{slug}-{n}-1100.jpg" '
            f'srcset="{prefix}assets/img/proyectos/{slug}-{n}-700.jpg 700w, '
            f'{prefix}assets/img/proyectos/{slug}-{n}-1100.jpg 1100w" sizes="{sizes}" '
            f'width="{ancho}" height="{alto}" alt="{alt}" loading="{loading}" decoding="async">')


def render(lang):
    t = T[lang]
    if FORM_ACTION:
        # El asunto va por idioma, para saber de qué página viene el mensaje.
        ocultos = dict(FORM_OCULTOS)
        ocultos['_subject'] = f'{t["f_asunto"]} ({lang.upper()})'
        ocultos_form = ''.join(
            f'\n            <input type="hidden" name="{k}" value="{v}">'
            for k, v in ocultos.items())
        # data-envia: si hay JS, el mensaje se manda desde aquí y la visita no
        # sale de la página. Sin JS, el action normal hace el trabajo.
        atributos_form = (
            f' action="{FORM_ACTION}" method="POST"'
            f' data-envia="{FORM_AJAX}" data-correo="{EMAIL}"'
            f' data-enviando="{t["f_enviando"]}" data-hecho="{t["f_ok_envio"]}"'
            f' data-error="{t["f_error"]}"')
        nota_form = t['f_nota_envio']
    else:
        atributos_form = f' data-mailto="{EMAIL}" data-ok="{t["f_ok"]}"'
        ocultos_form = ''
        nota_form = t['f_nota']
    prefix = '' if lang == 'ca' else '../'
    url_otra = 'es/' if lang == 'ca' else '../'
    p = []
    w = p.append

    # ---------------------------------------------------------------- cabeza
    w(f'''<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['titulo']}</title>
<meta name="description" content="{t['descripcion']}">
<meta name="theme-color" content="#c95948">
<link rel="canonical" href="{DOMINIO}/{'' if lang == 'ca' else 'es/'}">
<link rel="alternate" hreflang="ca" href="{DOMINIO}/">
<link rel="alternate" hreflang="es" href="{DOMINIO}/es/">
<link rel="alternate" hreflang="x-default" href="{DOMINIO}/">
<link rel="icon" href="{prefix}assets/img/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="{t['titulo']}">
<meta property="og:description" content="{t['descripcion']}">
<link rel="preload" href="{prefix}assets/fonts/raleway-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}assets/fonts/raleway-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}assets/fonts/biro-script-plus.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.classList.add("has-js");</script>
<link rel="stylesheet" href="{prefix}assets/css/fonts.css">
<link rel="stylesheet" href="{prefix}assets/css/main.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Laconic Studio",
  "description": "{t['descripcion']}",
  "email": "{EMAIL}",
  "areaServed": "ES",
  "sameAs": ["{INSTAGRAM}"]
}}
</script>
</head>
<body>
{SPRITE}

<div class="grain" aria-hidden="true"></div>
<div class="cursor" aria-hidden="true"></div>
<a class="skip" href="#{t['id_estudio']}">{t['saltar']}</a>

<header class="header">
  <div class="wrap header__inner">
    <a class="brand" href="#top" aria-label="Laconic Studio">
      <svg class="brand__zero" viewBox="{VB_ZERO}" aria-hidden="true"><use href="#lg-zero"/></svg>
    </a>

    <nav class="nav" aria-label="{t['k_estudio']}">''')
    for href, texto in t['nav']:
        w(f'      <a href="{href}">{texto}</a>')
    w(f'''    </nav>

    <div class="header__right">
      <p class="lang" aria-label="Idioma">
        <span aria-current="true">{t['propia_nombre']}</span>
        <a href="{url_otra}" hreflang="{t['otra']}">{t['otra_nombre']}</a>
      </p>
      <a class="btn btn--ink header__cta" href="#{t['id_contacto']}">
        <span>{t['cta']}</span><span class="arrow" aria-hidden="true">&rarr;</span>
      </a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="{t['menu_abrir']}">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>

<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
  <nav>''')
    for href, texto, nota in t['nav_movil']:
        w(f'    <a href="{href}">{texto} <span>{nota}</span></a>')
    w(f'''  </nav>
  <div class="mobile-menu__foot">
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <a href="{INSTAGRAM}" target="_blank" rel="noopener">@laconicstudio_</a>
    <a href="{url_otra}" hreflang="{t['otra']}">{t['otra_nombre']}</a>
  </div>
</div>

<main id="top">

  <!-- Inici: el logotip sobre beix i, tot seguit, dues fotos a pantalla completa -->
  <section class="hero" data-theme="cream">
    <div class="hero__stage">
      <h1 class="hero__logo">
        <span class="visually-hidden">Laconic Studio</span>
        <svg class="hero__word" viewBox="{VB_WORD}" aria-hidden="true"><use href="#lg-word"/></svg>
        <span class="hero__name" aria-hidden="true">studio</span>
      </h1>
      <p class="hero__claim">{t['reclamo']}</p>

      <div class="hero__rule">
        <span>{t['hero_izq']}</span>
        <i aria-hidden="true"></i>
        <span>{t['hero_der']}</span>
      </div>
    </div>
  </section>

  <!-- Les dues fotos del començament, a sang i a tota l'alçada de la pantalla -->
  <div class="duo" data-theme="cream">
    <figure class="duo__half">{foto(prefix, HERO_DUO[0][0], HERO_DUO[0][1], '50vw', lang, 'eager')}</figure>
    <figure class="duo__half">{foto(prefix, HERO_DUO[1][0], HERO_DUO[1][1], '50vw', lang, 'eager')}</figure>
  </div>

  <!-- Declaració: bloc de color, centrat, sense botó i amb menys aire -->
  <section class="decl decl--tight slab-top" data-theme="terra">
    <div class="wrap wrap--narrow center">
      <p class="kicker kicker--center fade">{t['k_sobre']}</p>
      <p class="decl__text display rl">{t['declaracion']}</p>
    </div>
  </section>

  <!-- Tira de fotos que passa en bucle -->
  <div class="strip" data-theme="terra">
    <div class="strip__band">
      <div class="strip__track">''')
    for slug, n in TIRA:
        w(f'        <figure class="strip__cell">{foto(prefix, slug, n, "22vw", lang)}</figure>')
    w(f'''      </div>
    </div>
  </div>

  <!-- Estudi -->
  <section class="section slab-top" data-theme="cream" id="{t['id_estudio']}">
    <div class="wrap">
      <p class="kicker fade">{t['k_estudio']}</p>
      <h2 class="display rl">
        {t['h_estudio']}
      </h2>

      <div class="manifesto__grid manifesto__grid--simple">
        <div class="body-col fade">
          <p class="claim">Less noise. <em>More meaning.</em></p>''')
    for parrafo in t['cuerpo_estudio']:
        w(f'          <p>{parrafo}</p>')
    w(f'''          <p class="body-col__cierre">{t['nota_estudio']}</p>
        </div>
      </div>

      <div class="team fade" data-delay="2">''')
    for nombre, rol in t['equipo']:
        w(f'''        <div class="person">
          <svg class="person__mark" viewBox="{VB_ZERO}" aria-hidden="true"><use href="#lg-zero"/></svg>
          <span class="person__name">{nombre}</span>
          <span class="person__role">{rol}</span>
        </div>''')
    w(f'''        <div class="person">
          <p class="person__note">{t['equipo_nota']}</p>
        </div>
      </div>

    </div>
  </section>

  <!-- La línia de serveis, fina i petita -->
  <div class="marquee marquee--fina" data-theme="ink" aria-hidden="true">
    <div class="marquee__track">''')
    for _, _, corto, _ in t['servicios']:
        w(f'      <span>{corto}</span>')
    w(f'''    </div>
  </div>

  <!-- Serveis: els noms grans i escalonats, i a sota la definició del que està actiu -->
  <section class="section slab-top" data-theme="terra" id="{t['id_servicios']}">
    <div class="wrap">
      <p class="kicker fade">{t['k_servicios']}</p>
      <h2 class="visually-hidden">{t['k_servicios']}</h2>

      <div class="svc" data-svc-list>
        <ol class="svc__noms">''')
    for i, (num, nombre, _, _) in enumerate(t['servicios']):
        w(f'''          <li class="svc__nom{' is-active' if i == 0 else ''}" data-svc="{i}">
            <button type="button" aria-controls="svc-def-{i}" aria-expanded="{'true' if i == 0 else 'false'}">
              <svg class="svc__icon" viewBox="0 0 24 24" aria-hidden="true"><use href="#{ICONO_SERVICIO[i]}"/></svg>
              <span class="svc__etiqueta">{nombre}</span><sup>{num}</sup>
            </button>
          </li>''')
    w('        </ol>\n\n        <div class="svc__defs">')
    for i, (_, nombre, _, definicion) in enumerate(t['servicios']):
        w(f'''          <div class="svc__def{' is-on' if i == 0 else ''}" id="svc-def-{i}" data-svc-def="{i}">
            <h3 class="svc__def-nom">{nombre}</h3>
            <p>{definicion}</p>
          </div>''')
    w(f'''        </div>

        <p class="svc__cta fade">
          <a class="btn btn--cream btn--lg" href="#{t['id_contacto']}"><span>{t['btn_presupuesto']}</span><span class="arrow" aria-hidden="true">&rarr;</span></a>
        </p>
      </div>
    </div>
  </section>

  <!-- Projectes: una graella de fitxes; cada una obre l'Instagram -->
  <section class="section section--tight slab-top" data-theme="cream" id="{t['id_trabajo']}">
    <div class="wrap">
      <p class="kicker fade">{t['k_trabajo']}</p>
      <h2 class="display rl">
        {t['h_trabajo']}
      </h2>

      <div class="obras">''')
    for pr in PROYECTOS:
        vids = videos_de(pr['slug']) if PROYECTOS_CON_VIDEO else []
        url = pr['piezas'][0] if pr['piezas'] else ''
        # Sin enlace no hay <a>: una ficha que no lleva a ninguna parte no debe
        # anunciarse como enlace.
        abre = (f'<a class="obra fade" href="{url}" target="_blank" rel="noopener" '
                f'aria-label="{pr["nombre"]} &mdash; {t["proyecto_ver"]}">' if url
                else '<article class="obra obra--sense-enllac fade">')
        cierra = '</a>' if url else '</article>'
        w(f'        {abre}')
        w('          <div class="obra__media">')
        if vids:
            poster = poster_de(vids[0])
            ruta_poster = (f'{prefix}assets/video/{poster}' if poster else
                           f'{prefix}assets/img/proyectos/{pr["slug"]}-{pr["portada"]}-700.jpg')
            w(f'''            <video class="obra__video skip-lazy" src="{prefix}assets/video/{vids[0]}"
              poster="{ruta_poster}" autoplay muted loop playsinline preload="metadata"
              data-no-lazy="1" data-skip-lazy="true" aria-hidden="true" tabindex="-1"></video>''')
        else:
            w('            ' + foto(prefix, pr['slug'], pr['portada'],
                                    '(min-width: 900px) 46vw, 100vw', lang))
        w(f'''          </div>
          <h3 class="obra__nom">{pr['nombre']}</h3>
          <p class="obra__sector">{pr['sector'][lang]}</p>
        {cierra}''')
    w(f'''      </div>
    </div>
  </section>

  <!-- Contacte -->
  <section class="section slab-top" data-theme="ink" id="{t['id_contacto']}">
    <div class="wrap">
      <p class="kicker fade">{t['k_contacto']}</p>
      <h2 class="display rl">
        {t['h_contacto']}
      </h2>

      <div class="contact">
        <div class="fade">
          <p class="lead">{t['lead_contacto']}</p>
          <ul class="contact__direct">
            <li><a class="link-line" href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a class="link-line" href="{INSTAGRAM}" target="_blank" rel="noopener">{t['dm']}</a></li>
          </ul>
        </div>

        <div class="fade" data-delay="1">
          <!-- El mensaje llega por correo a través del servicio de FORM_ACTION.
               Si esa casilla se deja vacía en build/build.py, el formulario pasa
               al modo de reserva: abre el cliente de email del visitante. -->
          <form class="form"{atributos_form}>{ocultos_form}
            <div class="form__row">
              <div class="field">
                <label for="nombre">{t['f_nombre']}</label>
                <input id="nombre" name="nombre" type="text" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="marca">{t['f_marca']}</label>
                <input id="marca" name="marca" type="text" autocomplete="organization">
              </div>
            </div>
            <div class="field">
              <label for="email">{t['f_email']}</label>
              <input id="email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="field">
              <span id="servicios-label" class="field__label">{t['f_necesitas']}</span>
              <div class="chips" role="group" aria-labelledby="servicios-label">''')
    for _, _, corto, _ in t['servicios']:
        w(f'                <label class="chip"><input type="checkbox" name="servicio" '
          f'value="{corto}"><span>{corto}</span></label>')
    w(f'''              </div>
            </div>
            <div class="field">
              <label for="mensaje">{t['f_cuentanos']}</label>
              <textarea id="mensaje" name="mensaje" rows="4" placeholder="{t['f_placeholder']}"></textarea>
            </div>
            <div>
              <button class="btn btn--cream btn--lg" type="submit"><span>{t['f_enviar']}</span><span class="arrow" aria-hidden="true">&rarr;</span></button>
            </div>
            <p class="note" data-form-status role="status">{nota_form}</p>
          </form>
        </div>
      </div>
    </div>
  </section>

</main>

<footer class="footer" data-theme="ink">
  <div class="wrap">
    <svg class="footer__word" viewBox="{VB_LOCK}" aria-hidden="true"><use href="#lg-lockup"/></svg>
    <ul class="footer__rows">
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
      <li>{t['pie_ubicacion']}</li>
      <li class="footer__nav">''')
    for href, texto in t['pie_nav']:
        w(f'        <a href="{href}">{texto}</a>')
    w(f'''        <a href="{url_otra}" hreflang="{t['otra']}">{t['otra_nombre']}</a>
      </li>
    </ul>
    <p class="footer__copy">
      <span>&copy; <span data-year>2026</span> Laconic Studio</span>
      <span class="footer__credito">{t['pie_credito']}
        <a href="{NERIS}" target="_blank" rel="noopener">{t['pie_credito_quien']}</a></span>
    </p>
  </div>
</footer>

<script src="{prefix}assets/js/main.js" defer></script>
</body>
</html>''')
    return '\n'.join(p) + '\n'


def main():
    ROOT.joinpath('index.html').write_text(render('ca'), encoding='utf-8')
    es = ROOT / 'es'
    es.mkdir(exist_ok=True)
    es.joinpath('index.html').write_text(render('es'), encoding='utf-8')
    for ruta in ('index.html', 'es/index.html'):
        print(ruta, round(len(ROOT.joinpath(ruta).read_text(encoding='utf-8')) / 1024, 1), 'KB')


if __name__ == '__main__':
    main()
