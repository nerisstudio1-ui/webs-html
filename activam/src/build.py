#!/usr/bin/env python3
"""Genera activam/index.html (ES), activam/ca/index.html y activam/en/index.html
a partir de template.html y los textos de este archivo.

Uso:  python3 activam/src/build.py
"""
import html
import json
from pathlib import Path
from urllib.parse import quote

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent
WA = "https://wa.me/34626660770?text="

STAR = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.2 8.1L21 3l-4.6 7L24 12l-7.6 2 '
        '4.6 7-6.8-5.1L12 24l-2.2-8.1L3 21l4.6-7L0 12l7.6-2L3 3l6.8 5.1z"/></svg>')

LANGS = {
    # ------------------------------------------------------------------ ES
    "es": dict(
        path="", url="https://activam.es/", og_locale="es_ES", label="ES",
        meta_title="Activa'M · Entrenamiento personal y rehabilitación en Sant Andreu (Barcelona)",
        meta_desc="Centro de entrenamiento personal, rehabilitación, fisioterapia y nutrición en Sant Andreu, Barcelona. "
                  "Fisios especializados en ejercicio y entrenadores en readaptación desde 2013. Cita previa por WhatsApp, de 7 a 22 h.",
        nav_label="Principal", menu_open="Abrir menú",
        id_about="nosotros", id_services="servicios", id_pt="entrenamiento-personal", id_rehab="rehabilitacion",
        id_nutri="nutricion", id_faq="preguntas", id_contact="contacto",
        nav_about="Nosotros", nav_services="Servicios", nav_groups="Grupos", nav_faq="FAQ", nav_contact="Contacto",
        cta_short="Pide cita", cta_long="Pide tu cita por WhatsApp", cta_wa="Escríbenos por WhatsApp",
        wa_general="Hola Activa'M, me gustaría pedir cita",
        wa_pt="Hola, quiero información sobre entrenamiento personal",
        wa_rh="Hola, quiero información sobre rehabilitación",
        wa_nu="Hola, quiero información sobre nutrición",
        hero_h1_a="Entrenamiento", hero_h1_b="personal y<br>rehabilitación",
        hero_p="Fisioterapeutas especializados en ejercicio, entrenadores especializados en readaptación y nutricionistas, en el corazón de Sant Andreu.",
        hero_meta="C/ Malats, 22 · Sant Andreu · De 7 a 22 h con cita previa",
        marquee_words=["Actívate", "Muévete", "Recupérate"],
        alt_hero="Recepción de Activa'M en el Carrer de Malats, Sant Andreu",
        alt_intro1="Profesional de Activa'M con la camiseta del centro",
        alt_intro2="Zona de mancuernas y sala de entrenamiento",
        intro_eyebrow="Desde 2013 en Sant Andreu", intro_h2="Activando la salud del barrio",
        intro_p="En Activa'M encontrarás un equipo multidisciplinar de entrenadores, fisioterapeutas y nutricionistas que te ayudarán, "
                "cada uno en su especialidad, según lo que necesites. Tanto si quieres ponerte en forma como si vienes a recuperarte "
                "de una lesión, diseñamos un plan pensado solo para ti.",
        intro_cta="Descubre los servicios",
        stats_label="Activa'M en cifras",
        stat_1="Desde este año en el barrio", stat_2="Especialidades bajo un mismo techo",
        stat_3="Atención individualizada", stat_4="Con cita previa",
        svc_eyebrow="Qué hacemos", svc_h2="Nuestros servicios",
        svc_p="Entrenamiento, rehabilitación y nutrición bajo un mismo techo, con un seguimiento cercano y personalizado.",
        more="Saber más", gr_more="Ir a Activa'M Pilates", ask_info="Pedir información", ideal_for="Ideal si buscas",
        pt_title="Entrenamiento personal",
        pt_short="Un plan individualizado según tus objetivos, tu nivel y tu salud, y un entrenador a tu lado en cada sesión.",
        pt_long="Tu entrenador personal diseña un plan a medida a partir de tu punto de partida y de lo que quieres conseguir. "
                "Te acompaña en cada sesión para que entrenes con buena técnica y de forma segura, va ajustando el plan según tu evolución "
                "y te prepara una rutina personalizada para que también puedas entrenar fuera del centro.",
        pt_list=["Ganar fuerza y tono muscular", "Perder peso de forma saludable", "Mejorar la postura",
                 "Cuidar la salud a largo plazo", "Preparar un reto deportivo", "Volver a entrenar después de un parón"],
        alt_pt="Sala de entrenamiento personal con rack, banco y material de fuerza",
        rh_title="Rehabilitación",
        rh_short="¿Lesión o dolor? Te recuperas a través del trabajo muscular, con fisios especializados en ejercicio y entrenadores en readaptación.",
        rh_long="No hacemos una rehabilitación convencional: estamos especializados en un proceso mucho más eficaz, a través del trabajo muscular "
                "y el ejercicio guiado. Fisioterapeutas especializados en ejercicio y entrenadores especializados en readaptación te acompañan "
                "desde la valoración hasta que vuelves a tu actividad con seguridad, y te ayudan a no volver a lesionarte.",
        rh_sub="Te acompañamos en",
        rh_list=["Dolor de espalda y cuello", "Lesiones deportivas", "Readaptación tras una lesión",
                 "Recuperación después de una operación", "Molestias articulares", "Vuelta segura a tu deporte"],
        alt_rh="Zona funcional con césped, esterilla y material de readaptación",
        nu_title="Nutrición",
        nu_short="Planes de alimentación personalizados: nutrición deportiva, educación nutricional, pérdida de peso y masa muscular.",
        nu_long="Nuestros dietistas-nutricionistas elaboran un plan de alimentación adaptado a ti, a tus objetivos y a tu día a día, "
                "y lo coordinan con tu entrenamiento para que los resultados lleguen antes y se mantengan.",
        nu_sub="Especialidades",
        nu_list=["Nutrición deportiva", "Educación nutricional", "Pérdida de peso", "Aumento de masa muscular"],
        alt_nu="Material de entrenamiento de fuerza en Activa'M",
        gr_title="Entrenamientos en grupo",
        gr_short="Pilates, tonificación y fuerza en grupos reducidos en nuestro centro Activa'M Pilates.",
        fw_eyebrow="Para quién", fw_h2="Activa'M es para ti si…",
        fw_p="No hace falta estar en forma para empezar: adaptamos cada plan a tu punto de partida.",
        fw_cards=[("Tienes dolor o una lesión", "Quieres recuperarte bien, entender qué te pasa y no volver a recaer."),
                  ("Quieres ponerte en forma", "Buscas fuerza, energía y resultados con un plan hecho para ti."),
                  ("Haces deporte", "Quieres rendir más, prevenir lesiones o preparar un reto."),
                  ("Quieres cuidarte a largo plazo", "Buscas moverte mejor y ganar salud a cualquier edad.")],
        steps_h2="Cómo funciona",
        steps=[("Paso 1", "Escríbenos", "Mándanos un WhatsApp, cuéntanos qué necesitas y concertamos tu primera cita. Atendemos de 7 a 22 h."),
               ("Paso 2", "Valoración", "Conocemos tu historial, tus objetivos y tu punto de partida para saber qué profesional y qué plan encajan contigo."),
               ("Paso 3", "Plan y seguimiento", "Entrenas, te recuperas o mejoras tu alimentación con un plan a medida y ajustes continuos según tu evolución.")],
        alt_about="Pared de la recepción con el logo de Activa'M",
        why_eyebrow="Por qué Activa'M", why_h2="Una forma diferente de recuperarte",
        why_p="Combinamos fisioterapia, entrenamiento y nutrición en un mismo centro, con profesionales que trabajan en equipo sobre tu caso. "
              "Así cada paso, desde la valoración hasta el alta, tiene sentido y continuidad.",
        why_list=["Atención individualizada", "Equipo multidisciplinar", "Fisios especializados en ejercicio",
                  "Entrenadores en readaptación", "Dietistas-nutricionistas", "Rutina para entrenar también fuera",
                  "Seguimiento de tu evolución", "Más de 10 años en Sant Andreu"],
        video_eyebrow="Así trabajamos", video_h2="Conoce el centro",
        more_eyebrow="Más Activa'M", more_h2="Sigue activándote",
        pilates_p="Nuestro centro de grupos reducidos en Carrer Gran de Sant Andreu, 346: Pilates Reformer, Pilates MAT, tonificación y fuerza, "
                  "y grupos para embarazadas.",
        mtb_p="Rutas en bicicleta de montaña por Barcelona y Beseit, con la misma filosofía: moverse, disfrutar y cuidarse.",
        visit="Visitar web",
        insta_h2="Síguenos en Instagram", insta_cta="Ver perfil", insta_alt="Instalaciones de Activa'M en Sant Andreu",
        faq_eyebrow="Preguntas frecuentes", faq_h2="Resolvemos tus dudas",
        faq=[("¿Dónde está Activa'M?", "Estamos en el Carrer de Malats, 22, en el barrio de Sant Andreu (Barcelona)."),
             ("¿Cuál es el horario?", "Atendemos de 7:00 a 22:00 h, siempre con cita concertada previamente por WhatsApp."),
             ("¿Cómo pido cita?", "Escríbenos por WhatsApp al +34 626 660 770. Te preguntaremos qué necesitas y te propondremos día y hora."),
             ("¿En qué se diferencia vuestra rehabilitación de la fisioterapia convencional?",
              "Trabajamos la recuperación a través del ejercicio y el trabajo muscular. Fisioterapeutas especializados en ejercicio y entrenadores "
              "especializados en readaptación te acompañan hasta que vuelves a tu actividad con seguridad."),
             ("¿Necesito estar en forma para empezar?",
              "No. Cada plan se adapta a tu punto de partida, tu edad, tus lesiones y tus objetivos, tanto si vienes a entrenar como a recuperarte."),
             ("¿Qué tengo que traer a la primera sesión?",
              "Ropa cómoda para moverte y, si tienes una lesión, los informes médicos o pruebas que tengas. Nos ayudan a valorar mejor tu caso."),
             ("¿Puedo combinar entrenamiento, rehabilitación y nutrición?",
              "Sí. Es una de las ventajas de Activa'M: los profesionales trabajan en equipo y coordinan tu plan."),
             ("¿Hacéis clases en grupo?",
              "Sí. Pilates, tonificación y fuerza en grupos reducidos en Activa'M Pilates. Toda la información está en activampilates.cat.")],
        contact_h2="Ven a vernos", lbl_address="Dirección", lbl_hours="Horario",
        hours="De 7:00 a 22:00 h · Solo con cita previa",
        map_title="Mapa: Activa'M, Carrer de Malats 22, Barcelona",
        foot_p="Entrenamiento personal, rehabilitación y nutrición en Sant Andreu desde 2013.",
        legal=[("aviso-legal.html", "Aviso legal"), ("privacidad.html", "Privacidad"), ("cookies.html", "Cookies")],
        svc_names=["Entrenamiento personal", "Rehabilitación y readaptación de lesiones", "Nutrición", "Entrenamientos en grupo"],
    ),
    # ------------------------------------------------------------------ CA
    "ca": dict(
        path="ca/", url="https://activam.es/ca/", og_locale="ca_ES", label="CA",
        meta_title="Activa'M · Entrenament personal i rehabilitació a Sant Andreu (Barcelona)",
        meta_desc="Centre d'entrenament personal, rehabilitació, fisioteràpia i nutrició a Sant Andreu, Barcelona. "
                  "Fisios especialitzats en exercici i entrenadors en readaptació des del 2013. Cita prèvia per WhatsApp, de 7 a 22 h.",
        nav_label="Principal", menu_open="Obrir menú",
        id_about="nosaltres", id_services="serveis", id_pt="entrenament-personal", id_rehab="rehabilitacio",
        id_nutri="nutricio", id_faq="preguntes", id_contact="contacte",
        nav_about="Nosaltres", nav_services="Serveis", nav_groups="Grups", nav_faq="FAQ", nav_contact="Contacte",
        cta_short="Demana cita", cta_long="Demana cita per WhatsApp", cta_wa="Escriu-nos per WhatsApp",
        wa_general="Hola Activa'M, m'agradaria demanar cita",
        wa_pt="Hola, vull informació sobre entrenament personal",
        wa_rh="Hola, vull informació sobre rehabilitació",
        wa_nu="Hola, vull informació sobre nutrició",
        hero_h1_a="Entrenament", hero_h1_b="personal i<br>rehabilitació",
        hero_p="Fisioterapeutes especialitzats en exercici, entrenadors especialitzats en readaptació i nutricionistes, al cor de Sant Andreu.",
        hero_meta="C/ Malats, 22 · Sant Andreu · De 7 a 22 h amb cita prèvia",
        marquee_words=["Activa't", "Mou-te", "Recupera't"],
        alt_hero="Recepció d'Activa'M al carrer de Malats, Sant Andreu",
        alt_intro1="Professional d'Activa'M amb la samarreta del centre",
        alt_intro2="Zona de manuelles i sala d'entrenament",
        intro_eyebrow="Des del 2013 a Sant Andreu", intro_h2="Activant la salut del barri",
        intro_p="A Activa'M hi trobaràs un equip multidisciplinari d'entrenadors, fisioterapeutes i nutricionistes que t'ajudaran, "
                "cadascú en la seva especialitat, segons el que necessitis. Tant si vols posar-te en forma com si véns a recuperar-te "
                "d'una lesió, dissenyem un pla pensat només per a tu.",
        intro_cta="Descobreix els serveis",
        stats_label="Activa'M en xifres",
        stat_1="Des d'aquest any al barri", stat_2="Especialitats sota un mateix sostre",
        stat_3="Atenció individualitzada", stat_4="Amb cita prèvia",
        svc_eyebrow="Què fem", svc_h2="Els nostres serveis",
        svc_p="Entrenament, rehabilitació i nutrició sota un mateix sostre, amb un seguiment proper i personalitzat.",
        more="Saber-ne més", gr_more="Anar a Activa'M Pilates", ask_info="Demanar informació", ideal_for="Ideal si busques",
        pt_title="Entrenament personal",
        pt_short="Un pla individualitzat segons els teus objectius, el teu nivell i la teva salut, i un entrenador al teu costat a cada sessió.",
        pt_long="El teu entrenador personal dissenya un pla a mida a partir del teu punt de partida i del que vols aconseguir. "
                "T'acompanya a cada sessió perquè entrenis amb bona tècnica i de manera segura, ajusta el pla segons la teva evolució "
                "i et prepara una rutina personalitzada perquè també puguis entrenar fora del centre.",
        pt_list=["Guanyar força i to muscular", "Perdre pes de manera saludable", "Millorar la postura",
                 "Cuidar la salut a llarg termini", "Preparar un repte esportiu", "Tornar a entrenar després d'una aturada"],
        alt_pt="Sala d'entrenament personal amb rack, banc i material de força",
        rh_title="Rehabilitació",
        rh_short="Lesió o dolor? Et recuperes a través del treball muscular, amb fisios especialitzats en exercici i entrenadors en readaptació.",
        rh_long="No fem una rehabilitació convencional: estem especialitzats en un procés molt més eficaç, a través del treball muscular "
                "i l'exercici guiat. Fisioterapeutes especialitzats en exercici i entrenadors especialitzats en readaptació t'acompanyen "
                "des de la valoració fins que tornes a la teva activitat amb seguretat, i t'ajuden a no tornar-te a lesionar.",
        rh_sub="T'acompanyem en",
        rh_list=["Mal d'esquena i de coll", "Lesions esportives", "Readaptació després d'una lesió",
                 "Recuperació després d'una operació", "Molèsties articulars", "Tornada segura al teu esport"],
        alt_rh="Zona funcional amb gespa, estora i material de readaptació",
        nu_title="Nutrició",
        nu_short="Plans d'alimentació personalitzats: nutrició esportiva, educació nutricional, pèrdua de pes i massa muscular.",
        nu_long="Els nostres dietistes-nutricionistes elaboren un pla d'alimentació adaptat a tu, als teus objectius i al teu dia a dia, "
                "i el coordinen amb el teu entrenament perquè els resultats arribin abans i es mantinguin.",
        nu_sub="Especialitats",
        nu_list=["Nutrició esportiva", "Educació nutricional", "Pèrdua de pes", "Augment de massa muscular"],
        alt_nu="Material d'entrenament de força a Activa'M",
        gr_title="Entrenaments en grup",
        gr_short="Pilates, tonificació i força en grups reduïts al nostre centre Activa'M Pilates.",
        fw_eyebrow="Per a qui", fw_h2="Activa'M és per a tu si…",
        fw_p="No cal estar en forma per començar: adaptem cada pla al teu punt de partida.",
        fw_cards=[("Tens dolor o una lesió", "Vols recuperar-te bé, entendre què et passa i no tornar a recaure."),
                  ("Vols posar-te en forma", "Busques força, energia i resultats amb un pla fet per a tu."),
                  ("Fas esport", "Vols rendir més, prevenir lesions o preparar un repte."),
                  ("Vols cuidar-te a llarg termini", "Busques moure't millor i guanyar salut a qualsevol edat.")],
        steps_h2="Com funciona",
        steps=[("Pas 1", "Escriu-nos", "Envia'ns un WhatsApp, explica'ns què necessites i concertem la primera cita. Atenem de 7 a 22 h."),
               ("Pas 2", "Valoració", "Coneixem el teu historial, els teus objectius i el teu punt de partida per saber quin professional i quin pla encaixen amb tu."),
               ("Pas 3", "Pla i seguiment", "Entrenes, et recuperes o millores la teva alimentació amb un pla a mida i ajustos continus segons la teva evolució.")],
        alt_about="Paret de la recepció amb el logo d'Activa'M",
        why_eyebrow="Per què Activa'M", why_h2="Una manera diferent de recuperar-te",
        why_p="Combinem fisioteràpia, entrenament i nutrició en un mateix centre, amb professionals que treballen en equip sobre el teu cas. "
              "Així cada pas, des de la valoració fins a l'alta, té sentit i continuïtat.",
        why_list=["Atenció individualitzada", "Equip multidisciplinari", "Fisios especialitzats en exercici",
                  "Entrenadors en readaptació", "Dietistes-nutricionistes", "Rutina per entrenar també fora",
                  "Seguiment de la teva evolució", "Més de 10 anys a Sant Andreu"],
        video_eyebrow="Així treballem", video_h2="Coneix el centre",
        more_eyebrow="Més Activa'M", more_h2="Continua activant-te",
        pilates_p="El nostre centre de grups reduïts al carrer Gran de Sant Andreu, 346: Pilates Reformer, Pilates MAT, tonificació i força, "
                  "i grups per a embarassades.",
        mtb_p="Rutes en bicicleta de muntanya per Barcelona i Beseit, amb la mateixa filosofia: moure's, gaudir i cuidar-se.",
        visit="Visitar web",
        insta_h2="Segueix-nos a Instagram", insta_cta="Veure perfil", insta_alt="Instal·lacions d'Activa'M a Sant Andreu",
        faq_eyebrow="Preguntes freqüents", faq_h2="Resolem els teus dubtes",
        faq=[("On és Activa'M?", "Som al carrer de Malats, 22, al barri de Sant Andreu (Barcelona)."),
             ("Quin és l'horari?", "Atenem de 7:00 a 22:00 h, sempre amb cita concertada prèviament per WhatsApp."),
             ("Com demano cita?", "Escriu-nos per WhatsApp al +34 626 660 770. Et preguntarem què necessites i et proposarem dia i hora."),
             ("En què es diferencia la vostra rehabilitació de la fisioteràpia convencional?",
              "Treballem la recuperació a través de l'exercici i el treball muscular. Fisioterapeutes especialitzats en exercici i entrenadors "
              "especialitzats en readaptació t'acompanyen fins que tornes a la teva activitat amb seguretat."),
             ("Cal estar en forma per començar?",
              "No. Cada pla s'adapta al teu punt de partida, la teva edat, les teves lesions i els teus objectius, tant si véns a entrenar com a recuperar-te."),
             ("Què he de portar a la primera sessió?",
              "Roba còmoda per moure't i, si tens una lesió, els informes mèdics o proves que tinguis. Ens ajuden a valorar millor el teu cas."),
             ("Puc combinar entrenament, rehabilitació i nutrició?",
              "Sí. És un dels avantatges d'Activa'M: els professionals treballen en equip i coordinen el teu pla."),
             ("Feu classes en grup?",
              "Sí. Pilates, tonificació i força en grups reduïts a Activa'M Pilates. Tota la informació és a activampilates.cat.")],
        contact_h2="Vine a veure'ns", lbl_address="Adreça", lbl_hours="Horari",
        hours="De 7:00 a 22:00 h · Només amb cita prèvia",
        map_title="Mapa: Activa'M, carrer de Malats 22, Barcelona",
        foot_p="Entrenament personal, rehabilitació i nutrició a Sant Andreu des del 2013.",
        legal=[("../aviso-legal.html", "Avís legal"), ("../privacidad.html", "Privacitat"), ("../cookies.html", "Galetes")],
        svc_names=["Entrenament personal", "Rehabilitació i readaptació de lesions", "Nutrició", "Entrenaments en grup"],
    ),
    # ------------------------------------------------------------------ EN
    "en": dict(
        path="en/", url="https://activam.es/en/", og_locale="en_GB", label="EN",
        meta_title="Activa'M · Personal training and rehabilitation in Sant Andreu (Barcelona)",
        meta_desc="Personal training, rehabilitation, physiotherapy and nutrition centre in Sant Andreu, Barcelona. "
                  "Exercise-based physios and return-to-sport trainers since 2013. Book on WhatsApp, 7 am to 10 pm.",
        nav_label="Main", menu_open="Open menu",
        id_about="about", id_services="services", id_pt="personal-training", id_rehab="rehabilitation",
        id_nutri="nutrition", id_faq="faq", id_contact="contact",
        nav_about="About", nav_services="Services", nav_groups="Classes", nav_faq="FAQ", nav_contact="Contact",
        cta_short="Book now", cta_long="Book on WhatsApp", cta_wa="Message us on WhatsApp",
        wa_general="Hi Activa'M, I'd like to book an appointment",
        wa_pt="Hi, I'd like information about personal training",
        wa_rh="Hi, I'd like information about rehabilitation",
        wa_nu="Hi, I'd like information about nutrition",
        hero_h1_a="Personal", hero_h1_b="training &amp;<br>rehabilitation",
        hero_p="Exercise-based physiotherapists, return-to-sport trainers and nutritionists, in the heart of Sant Andreu, Barcelona.",
        hero_meta="C/ Malats, 22 · Sant Andreu · 7 am to 10 pm, by appointment",
        marquee_words=["Get active", "Move", "Recover"],
        alt_hero="Activa'M reception on Carrer de Malats, Sant Andreu",
        alt_intro1="Activa'M professional wearing the centre's T-shirt",
        alt_intro2="Dumbbell area and training room",
        intro_eyebrow="In Sant Andreu since 2013", intro_h2="Keeping the neighbourhood healthy",
        intro_p="At Activa'M you'll find a multidisciplinary team of trainers, physiotherapists and nutritionists, each helping you "
                "in their own speciality, depending on what you need. Whether you want to get fit or recover from an injury, "
                "we design a plan just for you.",
        intro_cta="See our services",
        stats_label="Activa'M in numbers",
        stat_1="In the neighbourhood since", stat_2="Specialities under one roof",
        stat_3="One-to-one attention", stat_4="By appointment",
        svc_eyebrow="What we do", svc_h2="Our services",
        svc_p="Training, rehabilitation and nutrition under one roof, with close, personal follow-up.",
        more="Learn more", gr_more="Go to Activa'M Pilates", ask_info="Ask for information", ideal_for="Ideal if you want to",
        pt_title="Personal training",
        pt_short="A plan built around your goals, your level and your health, with a trainer by your side every session.",
        pt_long="Your personal trainer designs a tailored plan based on where you're starting from and what you want to achieve. "
                "They're with you every session so you train with good technique and safely, adjust the plan as you progress "
                "and give you a personalised routine so you can also train outside the centre.",
        pt_list=["Build strength and muscle tone", "Lose weight healthily", "Improve your posture",
                 "Look after your long-term health", "Prepare for a sports challenge", "Get back into training after a break"],
        alt_pt="Personal training room with rack, bench and strength equipment",
        rh_title="Rehabilitation",
        rh_short="Injury or pain? Recover through muscle work, with exercise-based physios and return-to-sport trainers.",
        rh_long="We don't do conventional rehab: we specialise in a much more effective process, based on muscle work and guided exercise. "
                "Exercise-based physiotherapists and return-to-sport trainers stay with you from the first assessment until you're "
                "safely back to your activity, and help you avoid getting injured again.",
        rh_sub="We can help with",
        rh_list=["Back and neck pain", "Sports injuries", "Return to sport after injury",
                 "Post-surgery recovery", "Joint discomfort", "Getting back to your sport safely"],
        alt_rh="Functional area with turf, mat and rehabilitation equipment",
        nu_title="Nutrition",
        nu_short="Personalised eating plans: sports nutrition, nutrition education, weight loss and muscle gain.",
        nu_long="Our dietitian-nutritionists create an eating plan that fits you, your goals and your daily life, "
                "and coordinate it with your training so you see results sooner and keep them.",
        nu_sub="Specialities",
        nu_list=["Sports nutrition", "Nutrition education", "Weight loss", "Muscle gain"],
        alt_nu="Strength training equipment at Activa'M",
        gr_title="Group classes",
        gr_short="Pilates, toning and strength in small groups at our Activa'M Pilates studio.",
        fw_eyebrow="Who it's for", fw_h2="Activa'M is for you if…",
        fw_p="You don't need to be fit to start: we adapt every plan to your starting point.",
        fw_cards=[("You're in pain or injured", "You want to recover properly, understand what's going on and avoid relapses."),
                  ("You want to get fit", "You're after strength, energy and results with a plan made for you."),
                  ("You play sport", "You want to perform better, prevent injuries or prepare for a challenge."),
                  ("You want to stay healthy", "You want to move better and gain health at any age.")],
        steps_h2="How it works",
        steps=[("Step 1", "Message us", "Send us a WhatsApp, tell us what you need and we'll book your first appointment. We're open 7 am to 10 pm."),
               ("Step 2", "Assessment", "We get to know your history, goals and starting point to match you with the right professional and plan."),
               ("Step 3", "Plan &amp; follow-up", "Train, recover or improve your diet with a tailored plan, adjusted as you progress.")],
        alt_about="Reception wall with the Activa'M logo",
        why_eyebrow="Why Activa'M", why_h2="A different way to recover",
        why_p="We combine physiotherapy, training and nutrition in one centre, with professionals who work on your case as a team. "
              "That way every step, from assessment to discharge, makes sense and connects.",
        why_list=["One-to-one attention", "Multidisciplinary team", "Exercise-based physios",
                  "Return-to-sport trainers", "Dietitian-nutritionists", "A routine to train outside too",
                  "Progress tracking", "Over 10 years in Sant Andreu"],
        video_eyebrow="How we work", video_h2="See the centre",
        more_eyebrow="More Activa'M", more_h2="Keep moving",
        pilates_p="Our small-group studio at Carrer Gran de Sant Andreu, 346: Reformer Pilates, Mat Pilates, toning and strength, "
                  "plus pregnancy groups.",
        mtb_p="Mountain bike routes around Barcelona and Beseit, with the same philosophy: move, enjoy and look after yourself.",
        visit="Visit website",
        insta_h2="Follow us on Instagram", insta_cta="See profile", insta_alt="Activa'M facilities in Sant Andreu",
        faq_eyebrow="FAQ", faq_h2="Your questions answered",
        faq=[("Where is Activa'M?", "We're at Carrer de Malats, 22, in the Sant Andreu neighbourhood of Barcelona."),
             ("What are your opening hours?", "We're open from 7 am to 10 pm, always by appointment booked in advance on WhatsApp."),
             ("How do I book?", "Message us on WhatsApp at +34 626 660 770. We'll ask what you need and suggest a day and time."),
             ("How is your rehabilitation different from conventional physiotherapy?",
              "We work on recovery through exercise and muscle work. Exercise-based physiotherapists and return-to-sport trainers "
              "stay with you until you're safely back to your activity."),
             ("Do I need to be fit to start?",
              "No. Every plan is adapted to your starting point, age, injuries and goals, whether you come to train or to recover."),
             ("What should I bring to my first session?",
              "Comfortable clothes to move in and, if you have an injury, any medical reports or scans. They help us assess your case."),
             ("Can I combine training, rehabilitation and nutrition?",
              "Yes. That's one of the advantages of Activa'M: our professionals work as a team and coordinate your plan."),
             ("Do you run group classes?",
              "Yes. Pilates, toning and strength in small groups at Activa'M Pilates. All the details are at activampilates.cat."),
             ("Do you speak English?", "Yes, just message us on WhatsApp in English and we'll take it from there.")],
        contact_h2="Come and see us", lbl_address="Address", lbl_hours="Opening hours",
        hours="7 am to 10 pm · By appointment only",
        map_title="Map: Activa'M, Carrer de Malats 22, Barcelona",
        foot_p="Personal training, rehabilitation and nutrition in Sant Andreu since 2013.",
        legal=[("../aviso-legal.html", "Legal notice"), ("../privacidad.html", "Privacy"), ("../cookies.html", "Cookies")],
        svc_names=["Personal training", "Injury rehabilitation", "Nutrition", "Group classes"],
    ),
}


ICONS = dict(
    arrow='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7l5 5-5 5M13 7l5 5-5 5"/></svg>',
    arrow_ne='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></svg>',
    wa_icon='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8 8 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4s-1 1-1 2.5 1.1 2.9 1.2 3.1 2.1 3.2 5.1 4.5c1.9.8 2.6.9 3.6.7.6-.1 1.8-.7 2-1.4s.3-1.3.2-1.4-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/></svg>',
    ico_pt='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6.5 6.5v11M17.5 6.5v11M3 9.5v5M21 9.5v5M6.5 12h11"/></svg>',
    ico_rh='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l2-5 4 10 2-5h6"/></svg>',
    ico_nu='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7c-2-2-6-1.5-6 3 0 5 3 10 6 10s6-5 6-10c0-4.5-4-5-6-3z"/><path d="M12 7c0-2 1-3.5 3-4"/></svg>',
    ico_gr='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 19c0-3.3 2.7-5 6-5s6 1.7 6 5M15 14.5c3 0 6 1.3 6 4.5"/></svg>',
)

EXTRA = {
    "es": dict(
        hero_h1="Entrenamiento personal y rehabilitación",
        trust="<strong>Desde 2013</strong> cuidando la salud de Sant Andreu con un equipo de entrenadores, fisios y nutricionistas.",
        svc_center_h="Un centro, cuatro especialidades",
        svc_center_p="Un equipo que trabaja junto sobre tu caso, en el corazón de Sant Andreu.",
        statement="Combinamos fisioterapia, entrenamiento y nutrición en un mismo centro para que te recuperes, ganes salud y no vuelvas a lesionarte.",
        id_how="como-funciona", how_h2="Tu plan, paso a paso",
        ask_h="¿Tienes más dudas?", ask_p="Escríbenos por WhatsApp y te respondemos lo antes posible.",
        cta_h2="¿Listo para activarte?", read_more="Pide información", fw_photos=["insta-3", "detalle-fuerza", "insta-5", "intro-2"],
    ),
    "ca": dict(
        hero_h1="Entrenament personal i rehabilitació",
        trust="<strong>Des del 2013</strong> cuidant la salut de Sant Andreu amb un equip d'entrenadors, fisios i nutricionistes.",
        svc_center_h="Un centre, quatre especialitats",
        svc_center_p="Un equip que treballa junt sobre el teu cas, al cor de Sant Andreu.",
        statement="Combinem fisioteràpia, entrenament i nutrició en un mateix centre perquè et recuperis, guanyis salut i no et tornis a lesionar.",
        id_how="com-funciona", how_h2="El teu pla, pas a pas",
        ask_h="Tens més dubtes?", ask_p="Escriu-nos per WhatsApp i et responem al més aviat possible.",
        cta_h2="A punt per activar-te?", read_more="Demana informació", fw_photos=["insta-3", "detalle-fuerza", "insta-5", "intro-2"],
    ),
    "en": dict(
        hero_h1="Personal training &amp; rehabilitation",
        trust="<strong>Since 2013</strong> looking after Sant Andreu's health with a team of trainers, physios and nutritionists.",
        svc_center_h="One centre, four specialities",
        svc_center_p="A team that works on your case together, in the heart of Sant Andreu.",
        statement="We combine physiotherapy, training and nutrition in one centre so you recover, get healthier and avoid getting injured again.",
        id_how="how-it-works", how_h2="Your plan, step by step",
        ask_h="Still have questions?", ask_p="Message us on WhatsApp and we'll get back to you as soon as we can.",
        cta_h2="Ready to get active?", read_more="Ask for information", fw_photos=["insta-3", "detalle-fuerza", "insta-5", "intro-2"],
    ),
}
for _code, _extra in EXTRA.items():
    LANGS[_code].update(_extra)


EXTRA_RWC = {
    "es": dict(
        hero_h1_em="Entrenamiento personal y rehabilitación <em>en Sant Andreu</em>",
        intro_lead="Activa'M es un centro de entrenamiento personal, rehabilitación y nutrición en Sant Andreu (Barcelona). "
                   "Desde 2013 ayudamos al barrio a moverse mejor, recuperarse de lesiones y ganar salud.",
        feats=[("Atención individualizada", "Cada persona tiene su plan, su ritmo y un profesional pendiente de su evolución."),
               ("Equipo multidisciplinar", "Entrenadores, fisioterapeutas y nutricionistas que trabajan juntos sobre tu caso."),
               ("Rehabilitación activa", "Te recuperas a través del trabajo muscular y el ejercicio guiado, no solo con camilla.")],
        svc_q="¿Qué servicio es <em>para ti?</em>",
        lbl_start="Para empezar", lbl_how="Cómo trabajamos",
        method_h2="El método detrás <em>del movimiento</em>",
        method_photos=["insta-1", "detalle-rehabilitacion", "detalle-fuerza"],
        fw_h2_em="Activa'M es <em>para ti si…</em>",
        video_h2_em="Conoce <em>el centro</em>", insta_h2_em="Síguenos en <em>Instagram</em>",
        faq_h2_em="Preguntas <em>frecuentes</em>", cta_h2_em="¿Listo para <em>activarte?</em>",
        directions="Cómo llegar",
        marquee_words=["Entrenamiento personal", "Rehabilitación", "Nutrición", "Sant Andreu desde 2013"],
    ),
    "ca": dict(
        hero_h1_em="Entrenament personal i rehabilitació <em>a Sant Andreu</em>",
        intro_lead="Activa'M és un centre d'entrenament personal, rehabilitació i nutrició a Sant Andreu (Barcelona). "
                   "Des del 2013 ajudem el barri a moure's millor, recuperar-se de lesions i guanyar salut.",
        feats=[("Atenció individualitzada", "Cada persona té el seu pla, el seu ritme i un professional pendent de la seva evolució."),
               ("Equip multidisciplinari", "Entrenadors, fisioterapeutes i nutricionistes que treballen junts sobre el teu cas."),
               ("Rehabilitació activa", "Et recuperes a través del treball muscular i l'exercici guiat, no només amb llitera.")],
        svc_q="Quin servei és <em>per a tu?</em>",
        lbl_start="Per començar", lbl_how="Com treballem",
        method_h2="El mètode darrere <em>del moviment</em>",
        method_photos=["insta-1", "detalle-rehabilitacion", "detalle-fuerza"],
        fw_h2_em="Activa'M és <em>per a tu si…</em>",
        video_h2_em="Coneix <em>el centre</em>", insta_h2_em="Segueix-nos a <em>Instagram</em>",
        faq_h2_em="Preguntes <em>freqüents</em>", cta_h2_em="A punt per <em>activar-te?</em>",
        directions="Com arribar-hi",
        marquee_words=["Entrenament personal", "Rehabilitació", "Nutrició", "Sant Andreu des del 2013"],
    ),
    "en": dict(
        hero_h1_em="Personal training &amp; rehabilitation <em>in Sant Andreu</em>",
        intro_lead="Activa'M is a personal training, rehabilitation and nutrition centre in Sant Andreu, Barcelona. "
                   "Since 2013 we've been helping the neighbourhood move better, recover from injuries and get healthier.",
        feats=[("One-to-one attention", "Everyone gets their own plan, their own pace and a professional following their progress."),
               ("Multidisciplinary team", "Trainers, physiotherapists and nutritionists working on your case together."),
               ("Active rehabilitation", "You recover through muscle work and guided exercise, not just on the treatment table.")],
        svc_q="Which service is <em>right for you?</em>",
        lbl_start="Getting started", lbl_how="How we work",
        method_h2="The method behind <em>the movement</em>",
        method_photos=["insta-1", "detalle-rehabilitacion", "detalle-fuerza"],
        fw_h2_em="Activa'M is <em>for you if…</em>",
        video_h2_em="See <em>the centre</em>", insta_h2_em="Follow us on <em>Instagram</em>",
        faq_h2_em="Frequently asked <em>questions</em>", cta_h2_em="Ready to <em>get active?</em>",
        directions="Get directions",
        marquee_words=["Personal training", "Rehabilitation", "Nutrition", "Sant Andreu since 2013"],
    ),
}
for _code, _extra in EXTRA_RWC.items():
    LANGS[_code].update(_extra)
ICONS["arrow"] = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
                  'stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')


EXTRA_BOOK = {
    "es": dict(
        id_book="cita", book_h2_em="Pide tu cita <em>en 30 segundos</em>",
        book_p="Elige qué necesitas y te abrimos WhatsApp con el mensaje listo. Te proponemos día y hora.",
        f_service="¿Qué necesitas?", f_when="¿Cuándo te va mejor?", f_name="Tu nombre", f_name_ph="Nombre",
        f_msg="Cuéntanos algo más (opcional)", f_msg_ph="Ej.: tengo una molestia en la rodilla…",
        f_submit="Enviar por WhatsApp", f_note="Atendemos de 7 a 22 h, siempre con cita previa.",
        f_tpl="Hola Activa'M, soy {name}. Me interesa: {service}. Me va mejor: {when}. {msg}", f_any="sin preferencia",
        whens=["Mañana (7–14 h)", "Tarde (14–22 h)", "Indiferente"], svc_chip_extra="Aún no lo sé",
        step1_cta="Da el primer paso", float_label="¿Hablamos?",
    ),
    "ca": dict(
        id_book="cita", book_h2_em="Demana cita <em>en 30 segons</em>",
        book_p="Tria què necessites i t'obrim WhatsApp amb el missatge a punt. Et proposem dia i hora.",
        f_service="Què necessites?", f_when="Quan et va millor?", f_name="El teu nom", f_name_ph="Nom",
        f_msg="Explica'ns alguna cosa més (opcional)", f_msg_ph="Ex.: tinc una molèstia al genoll…",
        f_submit="Enviar per WhatsApp", f_note="Atenem de 7 a 22 h, sempre amb cita prèvia.",
        f_tpl="Hola Activa'M, soc {name}. M'interessa: {service}. Em va millor: {when}. {msg}", f_any="sense preferència",
        whens=["Matí (7–14 h)", "Tarda (14–22 h)", "Indiferent"], svc_chip_extra="Encara no ho sé",
        step1_cta="Fes el primer pas", float_label="En parlem?",
    ),
    "en": dict(
        id_book="book", book_h2_em="Book in <em>30 seconds</em>",
        book_p="Choose what you need and we'll open WhatsApp with your message ready. We'll suggest a day and time.",
        f_service="What do you need?", f_when="When suits you best?", f_name="Your name", f_name_ph="Name",
        f_msg="Anything else? (optional)", f_msg_ph="E.g. I have some knee pain…",
        f_submit="Send on WhatsApp", f_note="Open 7 am to 10 pm, by appointment only.",
        f_tpl="Hi Activa'M, I'm {name}. I'm interested in: {service}. Best time: {when}. {msg}", f_any="no preference",
        whens=["Morning (7 am–2 pm)", "Afternoon (2–10 pm)", "Any time"], svc_chip_extra="Not sure yet",
        step1_cta="Take the first step", float_label="Let's talk",
    ),
}
for _code, _extra in EXTRA_BOOK.items():
    LANGS[_code].update(_extra)


# Reseñas reales de Google: añadir aquí {"name": ..., "stars": 5, "text": ...} tal cual aparecen en Google.
# Mientras la lista esté vacía, la sección muestra solo los botones a la ficha de Google.
REVIEWS = []

MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Activa%27M%20Carrer%20de%20Malats%2022%20Barcelona"
GOOGLE_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.5 12.3c0-.8-.1-1.5-.2-2.2H12v4.2h5.9c-.3 1.4-1 2.5-2.2 3.3v2.7h3.6c2.1-1.9 3.2-4.7 3.2-8z"/>'
               '<path fill="#34A853" d="M12 23c3 0 5.5-1 7.3-2.7l-3.6-2.7c-1 .7-2.2 1.1-3.7 1.1-2.9 0-5.3-1.9-6.2-4.5H2.1v2.8C3.9 20.6 7.7 23 12 23z"/>'
               '<path fill="#FBBC05" d="M5.8 14.2c-.2-.7-.4-1.4-.4-2.2s.1-1.5.4-2.2V7H2.1C1.4 8.5 1 10.2 1 12s.4 3.5 1.1 5l3.7-2.8z"/>'
               '<path fill="#EA4335" d="M12 5.4c1.6 0 3.1.6 4.2 1.7l3.2-3.2C17.5 2.1 15 1 12 1 7.7 1 3.9 3.4 2.1 7l3.7 2.8C6.7 7.3 9.1 5.4 12 5.4z"/></svg>')

EXTRA_REV = {
    "es": dict(id_reviews="opiniones", rev_h2_em="Lo que dicen <em>de nosotros</em>",
               rev_p="Lee lo que opinan quienes ya entrenan y se recuperan con nosotros en Sant Andreu.",
               rev_all="Ver todas las reseñas en Google", rev_leave="Deja tu reseña"),
    "ca": dict(id_reviews="opinions", rev_h2_em="El que diuen <em>de nosaltres</em>",
               rev_p="Llegeix què en pensen els qui ja entrenen i es recuperen amb nosaltres a Sant Andreu.",
               rev_all="Veure totes les ressenyes a Google", rev_leave="Deixa la teva ressenya"),
    "en": dict(id_reviews="reviews", rev_h2_em="What people <em>say about us</em>",
               rev_p="Read what people who already train and recover with us in Sant Andreu have to say.",
               rev_all="Read all reviews on Google", rev_leave="Leave a review"),
}
for _code, _extra in EXTRA_REV.items():
    LANGS[_code].update(_extra)


def em_last(text):
    """Pone en cursiva la última palabra (o las dos últimas si la última es corta)."""
    words = text.split(" ")
    n = 2 if len(words) > 2 and len(words[-1]) <= 3 else 1
    return " ".join(words[:-n]) + " <em>" + " ".join(words[-n:]) + "</em>" if len(words) > 1 else text


def lis(items):
    return "".join(f"<li>{i}</li>" for i in items)


def jsonld(t, lang):
    plain = lambda s: html.unescape(s)
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["HealthClub", "MedicalBusiness"],
                "@id": "https://activam.es/#centro",
                "name": "Activa'M",
                "alternateName": "Activa'M Sant Andreu",
                "description": plain(t["meta_desc"]),
                "url": t["url"],
                "image": "https://activam.es/img/og.jpg",
                "logo": "https://activam.es/img/logo-burdeos.png",
                "telephone": "+34626660770",
                "email": "info@activam.es",
                "foundingDate": "2013",
                "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Malats, 22", "addressLocality": "Barcelona",
                            "addressRegion": "Barcelona", "postalCode": "08030", "addressCountry": "ES"},
                "areaServed": ["Sant Andreu", "Barcelona"],
                "knowsLanguage": ["es", "ca", "en"],
                "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                               "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                               "opens": "07:00", "closes": "22:00"}],
                "sameAs": ["https://www.facebook.com/activamsantandreu/", "https://x.com/ActivamStAndreu",
                           "https://www.activampilates.cat/"],
                "hasOfferCatalog": {"@type": "OfferCatalog", "name": plain(t["svc_h2"]), "itemListElement": [
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "description": plain(d)}}
                    for n, d in zip(t["svc_names"], [t["pt_short"], t["rh_short"], t["nu_short"], t["gr_short"]])]},
            },
            {"@type": "WebPage", "url": t["url"], "name": plain(t["meta_title"]), "inLanguage": lang,
             "about": {"@id": "https://activam.es/#centro"}},
            {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
                {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                for q, a in t["faq"]]},
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def render(lang, t, template):
    base = "../" if t["path"] else ""
    v = {k: x for k, x in t.items() if isinstance(x, str)}
    v.update(lang=lang, base=base)
    for key in ("wa_general", "wa_pt", "wa_rh", "wa_nu"):
        v[key] = WA + quote(t[key])
    v["lang_links"] = "".join(
        f'<a href="{base}{o["path"]}" hreflang="{code}" lang="{code}"'
        + (' aria-current="page"' if code == lang else "") + f'>{o["label"]}</a>'
        for code, o in LANGS.items())
    v["marquee"] = "<span>" + "".join(f"{w} <i></i> " for w in t["marquee_words"]) + "</span>"
    for key in ("pt_title", "rh_title", "nu_title", "gr_title"):
        v[key + "_em"] = em_last(t[key])
    v["book_h2_em"] = t["book_h2_em"]
    chip = lambda name, val, checked=False: (f'<label><input type="radio" name="{name}" value="{val}"'
                                            + (' checked' if checked else '') + f'><span>{val}</span></label>')
    v["f_services"] = "".join(chip("service", x, i == 0) for i, x in
                              enumerate([t["pt_title"], t["rh_title"], t["nu_title"], t["gr_title"], t["svc_chip_extra"]]))
    v["f_whens"] = "".join(chip("when", x, i == 2) for i, x in enumerate(t["whens"]))
    v["maps_url"] = MAPS_URL
    v["google_icon"] = GOOGLE_ICON
    v["reviews_html"] = "".join(
        f'<article class="rev"><span class="stars" aria-label="{r["stars"]}/5">{"★" * r["stars"]}</span>'
        f'<blockquote>{html.escape(r["text"])}</blockquote>'
        f'<footer><span class="avatar">{html.escape(r["name"][0])}</span><span><strong>{html.escape(r["name"])}</strong>Google</span></footer></article>'
        for r in REVIEWS)
    v["feats"] = "".join(f"<li><div><strong>{h}</strong><p>{p}</p></div></li>" for h, p in t["feats"])
    v["fw_rows"] = "".join(f"<li><div><strong>{h}</strong><p>{p}</p></div></li>" for h, p in t["fw_cards"])
    v["method_cards"] = "".join(
        f'<article class="mcard"><span class="num">0{i}</span><h3>{h}</h3><p>{p}</p></article>'
        for i, (_, h, p) in enumerate(t["steps"], 1))
    for key in ("pt_list", "rh_list", "nu_list", "why_list"):
        v[key] = lis(t[key])
    v.update(ICONS)
    v["fw_cards"] = "".join(
        f'<article class="pcard"><div class="ph" style="--img:url({base}img/{img}.jpg)"></div>'
        f'<div class="body"><h3>{h}</h3><p>{p}</p>'
        f'<a href="{v["wa_general"]}" target="_blank" rel="noopener">{t["read_more"]}<i>{ICONS["arrow"]}</i></a></div></article>'
        for (h, p), img in zip(t["fw_cards"], t["fw_photos"]))
    v["steps"] = "".join(f'<div class="step"><h3>{i}. {h}</h3><p>{p}</p></div>'
                         for i, (_, h, p) in enumerate(t["steps"], 1))
    v["insta"] = "".join(
        f'<a href="https://www.instagram.com/activamstandreu/" target="_blank" rel="noopener">'
        f'<img src="{base}img/insta-{i}.jpg" alt="{t["insta_alt"]}" width="600" height="600" loading="lazy"></a>'
        for i in range(1, 7))
    v["faq_html"] = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(t["faq"]))
    v["legal_links"] = " · ".join(f'<a href="{h}">{l}</a>' for h, l in t["legal"])
    v["jsonld"] = jsonld(t, lang)

    out = template
    for key, val in v.items():
        out = out.replace("{{" + key + "}}", val)
    assert "{{" not in out, out[out.index("{{"):out.index("{{") + 40]
    return out


def main():
    template = (SRC / "template.html").read_text()
    for lang, t in LANGS.items():
        dest = ROOT / t["path"] / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(lang, t, template))
        print("ok", dest.relative_to(ROOT))


if __name__ == "__main__":
    main()
