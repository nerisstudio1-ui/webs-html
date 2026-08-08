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
        nav=[('#estudi', 'Estudi'), ('#serveis', 'Serveis'),
             ('#treball', 'Treball'), ('#faq', 'FAQ'), ('#contacte', 'Contacte')],
        nav_movil=[('#estudi', 'Estudi', 'qui som'), ('#serveis', 'Serveis', 'què fem'),
                   ('#treball', 'Treball', 'projectes'),
                   ('#faq', 'FAQ', 'dubtes'),
                   ('#contacte', 'Contacte', 'escriu-nos')],
        cta='Parlem', menu_abrir='Obre el menú',
        hero_nota='Estudi creatiu · Barcelona i remot',
        hero_izq='Estudi creatiu', hero_der='Barcelona i remot',
        reclamo="L'agència de RRSS que connecta, crea i converteix",
        k_sobre='Sobre Laconic',
        # La manuscrita va dentro de la frase, como la cursiva de la referencia
        declaracion='Ajudem marques a <span class="hand">travessar el soroll</span> '
                    'i a deixar una <span class="hand">empremta que duri</span>.',
        btn_saber='Saber-ne més',
        tira_fantasma='laconic studio',
        id_estudio='estudi', id_servicios='serveis', id_trabajo='treball',
        id_proceso='proces', id_faq='faq', id_contacto='contacte',
        k_estudio='L\'estudi',
        h_estudio='Cada marca comunica, <span class="hand">però no totes connecten</span>.',
        lead_estudio='Una bona comunicació no consisteix a publicar més, sinó a explicar millor.',
        cuerpo_estudio=[
            'Som un estudi creatiu especialitzat en xarxes socials, creació de contingut i '
            'estratègia digital. Treballem amb marques que volen construir una presència '
            'coherent, autèntica i amb criteri, creant contingut que connecti amb les '
            'persones i tingui un objectiu darrere.',
            'Ens impliquem en cada projecte com si fos nostre: analitzem, planifiquem, '
            'gravem, editem i pensem cada detall perquè cada publicació sumi i tingui '
            'sentit dins d\'una estratègia.'],
        nota_estudio='No busquem omplir un calendari. Busquem marques que deixin empremta.',
        equipo=[('Núria', 'Creative &amp; Founder'), ('Júlia', 'Strategist &amp; Founder')],
        equipo_nota='Som dues. Això vol dir que parles sempre amb qui fa la feina, i que '
                    'diem no a allò que no podem fer bé.',
        k_clientes='Marques amb qui hem treballat',
        k_servicios='Serveis',
        h_servicios='Això és el que fem <span class="hand">i què te\'n queda</span>.',
        # Los cinco del flyer del estudio, con su subtítulo tal cual
        servicios=[
            ('01', 'Content creation', 'Contingut amb aquell no-sé-què',
             ['Concepte i guió', 'Foto i vídeo', 'Reels i verticals', 'Edició i subtítols']),
            ('02', 'Social media', 'Scroll i pausa, això busquem',
             ['Línia editorial', 'Calendari', 'Community management', 'Informe mensual']),
            ('03', 'Graphic design', 'Intenció i actitud',
             ['Identitat visual', 'Sistema de plantilles', 'Peces per a xarxes', 'Presentacions']),
            ('04', 'Ads &amp; campaigns', 'Ni soroll ni sort, impacte',
             ['Meta i TikTok Ads', 'Segmentació i públics', 'Creativitats per provar', 'Informe de resultats']),
            ('05', 'UGC', 'Real i amb propòsit',
             ['Selecció de creadors', 'Briefing', 'Producció', 'Drets d\'ús']),
        ],
        btn_presupuesto='Demana pressupost',
        k_trabajo='Treball · Set marques',
        h_trabajo='Get people <span class="hand">talking</span> about your brand.',
        pieza='Peça', reel_sonido='Activa el so', reel_silencio='Silencia el so',
        ver_instagram='Mira-ho a Instagram',
        cita='Menys soroll. <span class="hand">Més sentit</span>.',
        k_proceso='Com treballem',
        h_proceso='Sense misteri, <span class="hand">amb mètode</span>.',
        pasos=[('Escoltem', 'Una trucada de vint minuts per entendre el negoci, no només el '
                            'feed. Què venes, a qui i què t\'està frenant.'),
               ('Definim', 'Una proposta curta: objectiu, entregables, terminis i preu. Si '
                           'alguna cosa no aporta, la traiem abans de començar.'),
               ('Creem', 'Producció en cicles curts amb revisions acotades. Veus el material '
                         'en un tauler compartit, no en cadenes de correu.'),
               ('Mesurem', 'Publiquem, llegim les dades i ajustem. Cada mes t\'expliquem què '
                           'ha funcionat, què no i què provarem.')],
        k_faq='Preguntes freqüents',
        h_faq='El que ens pregunten <span class="hand">abans de començar</span>.',
        faq=[
            ('Amb quines marques treballeu?',
             'Amb marques petites i mitjanes que volen una presència amb criteri: '
             'formació esportiva, alimentació, licors artesans, distribució i marca '
             'personal. A la secció de treball hi són totes les que hem acompanyat.'),
            ('Què inclou exactament cada servei?',
             'A la secció de serveis hi ha els entregables d\'un en un. Si el que '
             'necessites no hi és o va a mig camí entre dos, ens ho expliques i ho '
             'muntem a mida: no venem paquets tancats.'),
            ('Cal que us contractem tots els serveis?',
             'No. Hi ha marques amb qui fem només contingut i altres amb qui portem '
             'social media, direcció creativa i campanyes. Es pot començar per un i '
             'ampliar quan tingui sentit.'),
            ('Com és treballar amb vosaltres?',
             'Som dues, així que parles sempre amb qui fa la feina. El procés està '
             'explicat a la secció de com treballem: escoltem, definim, creem i '
             'mesurem, amb revisions acotades i el material en un tauler compartit.'),
            ('Veniu a gravar o ho feu tot en remot?',
             'Som de Barcelona i ens movem per gravar quan el projecte ho demana. La '
             'resta —estratègia, edició, calendari, informes— la portem en remot.'),
            ('En quins idiomes treballeu?',
             'Català, castellà i anglès. El contingut es pensa en l\'idioma en què '
             'parla la marca als seus clients, no en el nostre.'),
        ],
        k_resenas='El que diuen',
        h_resenas='Marques que <span class="hand">ho han provat</span>.',
        k_contacto='Contacte',
        h_contacto='Això comença <span class="hand">amb un missatge</span>.',
        lead_contacto='Explica\'ns quina marca ets i què t\'està frenant. Responem en menys '
                      'de 48 hores laborables, sempre una persona.',
        dm='DM a @laconicstudio_',
        nota_contacto_hand='Fes match amb allò que vibri amb tu',
        f_nombre='El teu nom', f_marca='Marca o projecte', f_email='Email',
        f_necesitas='Què necessites', f_cuentanos='Explica\'ns',
        f_placeholder='Què venes, a qui i què t\'agradaria canviar.',
        f_enviar='Envia el missatge',
        f_nota='En enviar s\'obre el teu client de correu amb el missatge ja redactat.',
        f_ok='Obrim el teu client de correu amb el missatge llest. Si no s\'obre, escriu-nos a ',
        pie_ubicacion='Barcelona, treballem en remot.',
        pie_nav=[('#estudi', 'Estudi'), ('#serveis', 'Serveis'), ('#treball', 'Treball'),
                 ('#faq', 'FAQ'), ('#contacte', 'Contacte')],
    ),
    'es': dict(
        lang='es', otra='ca', otra_nombre='CA', propia_nombre='ES',
        titulo='Laconic Studio | Estudio creativo de contenido, social media y estrategia',
        descripcion='Laconic Studio: creación de contenido, social media y estrategia digital. '
                    'Less noise. More meaning.',
        saltar='Saltar al contenido',
        nav=[('#estudio', 'Estudio'), ('#servicios', 'Servicios'),
             ('#trabajo', 'Trabajo'), ('#faq', 'FAQ'), ('#contacto', 'Contacto')],
        nav_movil=[('#estudio', 'Estudio', 'quiénes somos'), ('#servicios', 'Servicios', 'qué hacemos'),
                   ('#trabajo', 'Trabajo', 'proyectos'),
                   ('#faq', 'FAQ', 'dudas'),
                   ('#contacto', 'Contacto', 'escríbenos')],
        cta='Hablemos', menu_abrir='Abrir el menú',
        hero_nota='Estudio creativo · Barcelona y remoto',
        hero_izq='Estudio creativo', hero_der='Barcelona y remoto',
        reclamo='La agencia de RRSS que conecta, crea y convierte',
        k_sobre='Sobre Laconic',
        declaracion='Ayudamos a marcas a <span class="hand">atravesar el ruido</span> '
                    'y a dejar una <span class="hand">huella que dure</span>.',
        btn_saber='Saber más',
        tira_fantasma='laconic studio',
        id_estudio='estudio', id_servicios='servicios', id_trabajo='trabajo',
        id_proceso='proceso', id_faq='faq', id_contacto='contacto',
        k_estudio='El estudio',
        h_estudio='Cada marca comunica, <span class="hand">pero no todas conectan</span>.',
        lead_estudio='Una buena comunicación no consiste en publicar más, sino en explicar mejor.',
        cuerpo_estudio=[
            'Somos un estudio creativo especializado en redes sociales, creación de contenido '
            'y estrategia digital. Trabajamos con marcas que quieren construir una presencia '
            'coherente, auténtica y con criterio, creando contenido que conecte con las '
            'personas y tenga un objetivo detrás.',
            'Nos implicamos en cada proyecto como si fuera nuestro: analizamos, planificamos, '
            'grabamos, editamos y pensamos cada detalle para que cada publicación sume y '
            'tenga sentido dentro de una estrategia.'],
        nota_estudio='No buscamos llenar un calendario. Buscamos marcas que dejen huella.',
        equipo=[('Núria', 'Creative &amp; Founder'), ('Júlia', 'Strategist &amp; Founder')],
        equipo_nota='Somos dos. Eso significa que hablas siempre con quien hace el trabajo, y '
                    'que decimos no a lo que no podemos hacer bien.',
        k_clientes='Marcas con las que hemos trabajado',
        k_servicios='Servicios',
        h_servicios='Esto es lo que hacemos <span class="hand">y qué te llevas</span>.',
        # Los cinco del flyer del estudio, con su subtítulo tal cual
        servicios=[
            ('01', 'Content creation', 'Contenido con ese no-sé-qué',
             ['Concepto y guion', 'Foto y vídeo', 'Reels y verticales', 'Edición y subtítulos']),
            ('02', 'Social media', 'Scroll y pausa, eso buscamos',
             ['Línea editorial', 'Calendario', 'Community management', 'Informe mensual']),
            ('03', 'Graphic design', 'Intención y actitud',
             ['Identidad visual', 'Sistema de plantillas', 'Piezas para redes', 'Presentaciones']),
            ('04', 'Ads &amp; campaigns', 'Ni ruido ni suerte, impacto',
             ['Meta y TikTok Ads', 'Segmentación y públicos', 'Creatividades para testar', 'Informe de resultados']),
            ('05', 'UGC', 'Real y con propósito',
             ['Selección de creadores', 'Briefing', 'Producción', 'Derechos de uso']),
        ],
        btn_presupuesto='Pedir presupuesto',
        k_trabajo='Trabajo · Siete marcas',
        h_trabajo='Get people <span class="hand">talking</span> about your brand.',
        pieza='Pieza', reel_sonido='Activar el sonido', reel_silencio='Silenciar',
        ver_instagram='Verlo en Instagram',
        cita='Menos ruido. <span class="hand">Más sentido</span>.',
        k_proceso='Cómo trabajamos',
        h_proceso='Sin misterio, <span class="hand">con método</span>.',
        pasos=[('Escuchamos', 'Una llamada de veinte minutos para entender el negocio, no solo '
                              'el feed. Qué vendes, a quién y qué te está frenando.'),
               ('Definimos', 'Una propuesta corta: objetivo, entregables, plazos y precio. Si '
                             'algo no aporta, lo quitamos antes de empezar.'),
               ('Creamos', 'Producción en ciclos cortos con revisiones acotadas. Ves el '
                           'material en un tablero compartido, no en cadenas de correo.'),
               ('Medimos', 'Publicamos, leemos los datos y ajustamos. Cada mes te contamos qué '
                           'funcionó, qué no y qué vamos a probar.')],
        k_faq='Preguntas frecuentes',
        h_faq='Lo que nos preguntan <span class="hand">antes de empezar</span>.',
        faq=[
            ('¿Con qué marcas trabajáis?',
             'Con marcas pequeñas y medianas que quieren una presencia con criterio: '
             'formación deportiva, alimentación, licores artesanos, distribución y '
             'marca personal. En la sección de trabajo están todas las que hemos '
             'acompañado.'),
            ('¿Qué incluye exactamente cada servicio?',
             'En la sección de servicios están los entregables uno por uno. Si lo que '
             'necesitas no está o va a medio camino entre dos, nos lo cuentas y lo '
             'montamos a medida: no vendemos paquetes cerrados.'),
            ('¿Hay que contrataros todos los servicios?',
             'No. Hay marcas con las que hacemos solo contenido y otras con las que '
             'llevamos social media, dirección creativa y campañas. Se puede empezar '
             'por uno y ampliar cuando tenga sentido.'),
            ('¿Cómo es trabajar con vosotras?',
             'Somos dos, así que hablas siempre con quien hace el trabajo. El proceso '
             'está explicado en la sección de cómo trabajamos: escuchamos, definimos, '
             'creamos y medimos, con revisiones acotadas y el material en un tablero '
             'compartido.'),
            ('¿Vais a grabar o lo hacéis todo en remoto?',
             'Somos de Barcelona y nos movemos para grabar cuando el proyecto lo pide. '
             'El resto —estrategia, edición, calendario, informes— lo llevamos en '
             'remoto.'),
            ('¿En qué idiomas trabajáis?',
             'Catalán, castellano e inglés. El contenido se piensa en el idioma en que '
             'la marca habla a sus clientes, no en el nuestro.'),
        ],
        k_resenas='Lo que dicen',
        h_resenas='Marcas que <span class="hand">lo han probado</span>.',
        k_contacto='Contacto',
        h_contacto='Esto empieza <span class="hand">con un mensaje</span>.',
        lead_contacto='Cuéntanos qué marca eres y qué te está frenando. Respondemos en menos '
                      'de 48 horas laborables, siempre una persona.',
        dm='DM a @laconicstudio_',
        nota_contacto_hand='Haz match con lo que vibre contigo',
        f_nombre='Tu nombre', f_marca='Marca o proyecto', f_email='Email',
        f_necesitas='Qué necesitas', f_cuentanos='Cuéntanos',
        f_placeholder='Qué vendes, a quién y qué te gustaría cambiar.',
        f_enviar='Enviar mensaje',
        f_nota='Al enviar se abre tu cliente de correo con el mensaje ya redactado.',
        f_ok='Abrimos tu cliente de correo con el mensaje listo. Si no se abre, escríbenos a ',
        pie_ubicacion='Barcelona, trabajamos en remoto.',
        pie_nav=[('#estudio', 'Estudio'), ('#servicios', 'Servicios'), ('#trabajo', 'Trabajo'),
                 ('#faq', 'FAQ'), ('#contacto', 'Contacto')],
    ),
}

# Reseñas de clientes. Vacío a propósito: son palabras de otra persona y no se
# inventan. En cuanto lleguen, se añaden aquí y la sección aparece sola.
#   ('Nom Cognom', 'Marca', {'ca': 'La cita…', 'es': 'La cita…'})
RESENAS = []

EMAIL = 'itslaconicstudio@gmail.com'
INSTAGRAM = 'https://www.instagram.com/laconicstudio_/'
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
HERO_TILES = [('malhivern', 2), ('quality', 1), ('maitasuna', 1), ('puig', 3), ('jordi-coll', 3)]
TIRA = [('quality', 1), ('f45', 1), ('maitasuna', 1), ('f4s', 1), ('malhivern', 2)]

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


def foto(prefix, slug, n, sizes, lang, loading='lazy', clases=''):
    alt = ALT.get(f'{slug}-{n}', {}).get(lang, '')
    cls = f' class="{clases}"' if clases else ''
    return (f'<img{cls} src="{prefix}assets/img/proyectos/{slug}-{n}-1100.jpg" '
            f'srcset="{prefix}assets/img/proyectos/{slug}-{n}-700.jpg 700w, '
            f'{prefix}assets/img/proyectos/{slug}-{n}-1100.jpg 1100w" sizes="{sizes}" '
            f'width="1080" height="1350" alt="{alt}" loading="{loading}" decoding="async">')


def render(lang):
    t = T[lang]
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
      <svg class="brand__mark" viewBox="{VB_ZERO}" aria-hidden="true"><use href="#lg-zero"/></svg>
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

  <!-- Inici: fons beix, el logotip al mig i les peces que pugen fins a dalt -->
  <section class="hero" data-theme="cream" data-collage>
    <div class="hero__stage">
      <div class="hero__tiles" aria-hidden="true">
        <figure class="tile tile--1">{foto(prefix, HERO_TILES[0][0], HERO_TILES[0][1], '24vw', lang, 'eager')}</figure>
        <figure class="tile tile--2">{foto(prefix, HERO_TILES[1][0], HERO_TILES[1][1], '24vw', lang, 'eager')}</figure>
        <figure class="tile tile--3">{foto(prefix, HERO_TILES[2][0], HERO_TILES[2][1], '24vw', lang, 'lazy')}</figure>
        <figure class="tile tile--4">{foto(prefix, HERO_TILES[3][0], HERO_TILES[3][1], '24vw', lang, 'lazy')}</figure>
        <figure class="tile tile--5">{foto(prefix, HERO_TILES[4][0], HERO_TILES[4][1], '24vw', lang, 'lazy')}</figure>
      </div>

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
      <span class="hero__scroll" aria-hidden="true">scroll</span>
    </div>
  </section>

  <!-- Declaració: bloc de color, centrat, amb la manuscrita dins de la frase -->
  <section class="decl slab-top" data-theme="terra">
    <div class="wrap wrap--narrow center">
      <p class="kicker kicker--center fade">{t['k_sobre']}</p>
      <p class="decl__text display rl">{t['declaracion']}</p>
      <p class="fade" data-delay="1">
        <a class="btn btn--line" href="#{t['id_estudio']}"><span>{t['btn_saber']}</span></a>
      </p>
    </div>
  </section>

  <!-- Tira de fotos que passa en bucle, amb el rètol gran a sota -->
  <div class="strip" data-theme="terra">
    <div class="strip__band">
      <div class="strip__track">
        <figure class="strip__cell">{foto(prefix, TIRA[0][0], TIRA[0][1], '22vw', lang)}</figure>
        <figure class="strip__cell">{foto(prefix, TIRA[1][0], TIRA[1][1], '22vw', lang)}</figure>
        <figure class="strip__cell">{foto(prefix, TIRA[2][0], TIRA[2][1], '22vw', lang)}</figure>
        <figure class="strip__cell">{foto(prefix, TIRA[3][0], TIRA[3][1], '22vw', lang)}</figure>
        <figure class="strip__cell">{foto(prefix, TIRA[4][0], TIRA[4][1], '22vw', lang)}</figure>
      </div>
    </div>
    <span class="strip__ghost" aria-hidden="true">{t['tira_fantasma']}</span>
  </div>

  <!-- Estudi -->
  <section class="section slab-top" data-theme="cream" id="{t['id_estudio']}">
    <div class="wrap">
      <p class="kicker fade">{t['k_estudio']}</p>
      <h2 class="display rl">
        {t['h_estudio']}
      </h2>

      <div class="manifesto__grid">
        <div class="fade">
          <p class="lead">{t['lead_estudio']}</p>
          <p class="claim">Less noise. <em>More meaning.</em></p>
        </div>
        <div class="body-col fade" data-delay="1">''')
    for parrafo in t['cuerpo_estudio']:
        w(f'          <p>{parrafo}</p>')
    w(f'''          <p class="hand-note">{t['nota_estudio']}</p>
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

      <div class="clients fade" data-delay="2">
        <p class="clients__label">{t['k_clientes']}</p>
        <ul class="clients__list">
          <li>{PROYECTOS[0]["nombre"]}</li>
          <li>{PROYECTOS[1]["nombre"]}</li>
          <li>{PROYECTOS[2]["nombre"]}</li>
          <li>{PROYECTOS[3]["nombre"]}</li>
          <li>{PROYECTOS[4]["nombre"]}</li>
          <li>{PROYECTOS[5]["nombre"]}</li>
          <li>{PROYECTOS[6]["nombre"]}</li>
        </ul>
      </div>
    </div>
  </section>

  <div class="marquee" data-theme="ink" aria-hidden="true">
    <div class="marquee__track">''')
    for i, (_, nombre, _, _) in enumerate(t['servicios']):
        clase = ' class="hand"' if i % 2 == 0 else ''
        w(f'      <span{clase}>{nombre}</span>')
    w(f'''    </div>
  </div>

  <!-- Serveis: la foto segueix el servei actiu -->
  <section class="section slab-top" data-theme="terra" id="{t['id_servicios']}">
    <div class="wrap">
      <p class="kicker fade">{t['k_servicios']}</p>
      <h2 class="display rl">
        {t['h_servicios']}
      </h2>

      <div class="svc">
        <div class="svc__media fade" aria-hidden="true">''')
    for i, (slug, n) in enumerate(COLLAGE):
        clases = 'is-on' if i == 0 else ''
        img = foto(prefix, slug, n, '(min-width: 940px) 42vw, 100vw', lang, 'lazy', clases)
        w('          ' + img.replace('<img', f'<img data-svc-img="{slug}"', 1))
    w('''        </div>

        <ol class="svc__list" data-svc-list>''')
    for i, (num, nombre, tag, items) in enumerate(t['servicios']):
        slug = COLLAGE[i][0]
        w(f'''          <li class="svc__item" data-svc="{slug}">
            <div class="svc__head">
              <svg class="svc__icon" viewBox="0 0 24 24" aria-hidden="true"><use href="#{ICONO_SERVICIO[i]}"/></svg>
              <span class="svc__num">{num}</span>
              <span class="svc__name hand">{nombre}</span>
            </div>
            <p class="svc__tag">{tag}</p>
            <ul class="svc__items">''')
        for it in items:
            w(f'              <li>{it}</li>')
        w('''            </ul>
          </li>''')
    w(f'''        </ol>

        <p class="svc__cta fade">
          <a class="btn btn--cream btn--lg" href="#{t['id_contacto']}"><span>{t['btn_presupuesto']}</span><span class="arrow" aria-hidden="true">&rarr;</span></a>
        </p>
      </div>
    </div>
  </section>

  <!-- Treball -->
  <section class="section section--tight slab-top" data-theme="cream" id="{t['id_trabajo']}">
    <div class="wrap">
      <p class="kicker fade">{t['k_trabajo']}</p>
      <h2 class="display rl">
        {t['h_trabajo']}
      </h2>
    </div>
    <div class="wrap">''')
    for i, pr in enumerate(PROYECTOS):
        flip = ' slab--flip' if i % 2 else ''
        vids = videos_de(pr['slug'])
        if vids:
            # Reels: se reproducen solos y sin sonido al entrar en pantalla,
            # y el botón activa el audio. La foto hace de póster.
            w(f'''      <article class="slab{flip} fade">
        <div class="slab__media slab__media--reels">''')
            for j, nombre_video in enumerate(vids, 1):
                n_foto = pr['portada'] if j == 1 else min(j, pr['fotos'])
                poster = poster_de(nombre_video)
                ruta_poster = (f'{prefix}assets/video/{poster}' if poster else
                               f'{prefix}assets/img/proyectos/{pr["slug"]}-{n_foto}-700.jpg')
                w(f'''          <div class="reel" data-reel>
            <video src="{prefix}assets/video/{nombre_video}"
              poster="{ruta_poster}"
              muted loop playsinline preload="metadata"
              aria-label="{t['pieza']} {j:02d} &mdash; {pr['nombre']}"></video>
            <span class="reel__tag" aria-hidden="true">{t['pieza']} {j:02d}</span>
            <button class="reel__sound" type="button" data-sound
              data-on="{t['reel_sonido']}" data-off="{t['reel_silencio']}"
              aria-label="{t['reel_sonido']}">
              <span class="is-on" aria-hidden="true">&#9834;</span>
              <span class="is-off" aria-hidden="true">&times;</span>
            </button>
          </div>''')
            w('        </div>')
        else:
            w(f'''      <article class="slab{flip} fade">
        <div class="slab__media" data-parallax>
          {foto(prefix, pr['slug'], pr['portada'], '(min-width: 900px) 52vw, 100vw', lang)}
        </div>''')
        w(f'''        <div class="slab__text">
          <span class="slab__index">{i + 1:02d} / {len(PROYECTOS):02d} &middot; {pr['sector'][lang]}</span>
          <h3 class="slab__title">{pr['nombre']}</h3>
          <p>{pr['texto'][lang]}</p>''')
        if pr['piezas']:
            w('          <div class="slab__links">')
            if vids:
                # El vídeo ya se ve en la web: el enlace solo lleva al original.
                w(f'            <a href="{pr["piezas"][0]}" target="_blank" rel="noopener">'
                  f'{t["ver_instagram"]} <span aria-hidden="true">&#8599;</span></a>')
            else:
                for j, url in enumerate(pr['piezas'], 1):
                    w(f'            <a href="{url}" target="_blank" rel="noopener">'
                      f'{t["pieza"]} {j:02d} <span aria-hidden="true">&#8599;</span></a>')
            w('          </div>')
        w('          <div class="slab__meta">')
        for s in pr['servicios'][lang]:
            w(f'            <span>{s}</span>')
        w('          </div>')
        extras = extras_de(pr['slug'], pr['portada'])
        if extras:
            w('          <div class="slab__extra">')
            for n in extras:
                w('            <figure>'
                  + foto(prefix, pr['slug'], n, '(min-width: 900px) 22vw, 46vw', lang)
                  + '</figure>')
            w('          </div>')
        w('''        </div>
      </article>''')
    w(f'''    </div>
  </section>

  <!-- Cita -->
  <section class="section slab-top quote" data-theme="deep">
    <svg class="quote__mark" viewBox="{VB_ZERO}" aria-hidden="true" data-spin><use href="#lg-zero"/></svg>
    <div class="wrap">
      <blockquote class="quote__text rl">
        {t['cita']}
      </blockquote>
      <cite class="fade">Laconic Studio</cite>
    </div>
  </section>

  <!-- Procés -->
  <section class="section slab-top" data-theme="cream" id="{t['id_proceso']}">
    <div class="wrap">
      <div class="process">
        <div class="process__head">
          <p class="kicker fade">{t['k_proceso']}</p>
          <h2 class="display display--sm rl">
            {t['h_proceso']}
          </h2>
        </div>
        <div class="rail" data-rail>
          <span class="rail__fill" aria-hidden="true"></span>''')
    for i, (titulo, texto) in enumerate(t['pasos'], 1):
        w(f'''          <div class="step">
            <span class="step__n">{i:02d}</span>
            <h3>{titulo}</h3>
            <p>{texto}</p>
          </div>''')
    w(f'''        </div>
      </div>
    </div>
  </section>


  <!-- Preguntes freqüents -->
  <section class="section slab-top" data-theme="cream-2" id="{t['id_faq']}">
    <div class="wrap wrap--narrow">
      <p class="kicker fade">{t['k_faq']}</p>
      <h2 class="display display--sm rl">{t['h_faq']}</h2>
      <div class="faq">
        <details class="faq__item fade">
          <summary>
            <span>{t['faq'][0][0]}</span>
            <span class="faq__sign" aria-hidden="true"></span>
          </summary>
          <div class="faq__body"><p>{t['faq'][0][1]}</p></div>
        </details>
        <details class="faq__item fade" data-delay="1">
          <summary>
            <span>{t['faq'][1][0]}</span>
            <span class="faq__sign" aria-hidden="true"></span>
          </summary>
          <div class="faq__body"><p>{t['faq'][1][1]}</p></div>
        </details>
        <details class="faq__item fade" data-delay="1">
          <summary>
            <span>{t['faq'][2][0]}</span>
            <span class="faq__sign" aria-hidden="true"></span>
          </summary>
          <div class="faq__body"><p>{t['faq'][2][1]}</p></div>
        </details>
        <details class="faq__item fade" data-delay="1">
          <summary>
            <span>{t['faq'][3][0]}</span>
            <span class="faq__sign" aria-hidden="true"></span>
          </summary>
          <div class="faq__body"><p>{t['faq'][3][1]}</p></div>
        </details>
        <details class="faq__item fade" data-delay="1">
          <summary>
            <span>{t['faq'][4][0]}</span>
            <span class="faq__sign" aria-hidden="true"></span>
          </summary>
          <div class="faq__body"><p>{t['faq'][4][1]}</p></div>
        </details>
        <details class="faq__item fade" data-delay="1">
          <summary>
            <span>{t['faq'][5][0]}</span>
            <span class="faq__sign" aria-hidden="true"></span>
          </summary>
          <div class="faq__body"><p>{t['faq'][5][1]}</p></div>
        </details>
      </div>
    </div>
  </section>

  <!-- El que diuen. Només es dibuixa si hi ha cites a RESENAS -->''')
    if RESENAS:
        w(f'''  <section class="section" data-theme="cream" id="ressenyes">
    <div class="wrap">
      <p class="kicker fade">{t['k_resenas']}</p>
      <h2 class="display display--sm rl">{t['h_resenas']}</h2>
      <div class="quotes">''')
        for i, (nombre, marca_cli, cita) in enumerate(RESENAS):
            retardo = f' data-delay="{min(i, 3)}"' if i else ''
            w(f'''        <figure class="quotes__item fade"{retardo}>
          <blockquote><p>{cita[lang]}</p></blockquote>
          <figcaption><strong>{nombre}</strong><span>{marca_cli}</span></figcaption>
        </figure>''')
        w('''      </div>
    </div>
  </section>''')
    w(f'''
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
          <p class="hand-note">{t['nota_contacto_hand']}</p>
        </div>

        <div class="fade" data-delay="1">
          <!-- Sense backend: compon un correu amb les dades. Per rebre-ho en un
               servidor, canviar data-mailto per action + method. -->
          <form class="form" data-mailto="{EMAIL}" data-ok="{t['f_ok']}" novalidate>
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
    for _, nombre, _, _ in t['servicios']:
        w(f'                <label class="chip"><input type="checkbox" name="servicio" '
          f'value="{nombre}"><span>{nombre}</span></label>')
    w(f'''              </div>
            </div>
            <div class="field">
              <label for="mensaje">{t['f_cuentanos']}</label>
              <textarea id="mensaje" name="mensaje" rows="4" placeholder="{t['f_placeholder']}"></textarea>
            </div>
            <div>
              <button class="btn btn--cream btn--lg" type="submit"><span>{t['f_enviar']}</span><span class="arrow" aria-hidden="true">&rarr;</span></button>
            </div>
            <p class="note" data-form-status role="status">{t['f_nota']}</p>
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
    <p class="footer__copy">&copy; <span data-year>2026</span> Laconic Studio</p>
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
