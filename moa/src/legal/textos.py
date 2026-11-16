# Textos legales de MOA en castellano, catalán e inglés.
# Los datos entre {{...}} se rellenan en DATOS (abajo) y se regeneran con:
#     python3 build_legal.py
# Mientras un dato esté vacío, sale marcado en amarillo en la página.
#
# Son una plantilla razonable para una actividad como esta (entrenadora
# personal autónoma con web informativa y formulario de contacto). Conviene
# que los revise una asesoría antes de darlos por definitivos.

DATOS = {
    "titular": "",          # Nombre y apellidos, o razón social
    "nif": "",              # NIF / DNI
    "direccion": "",        # Dirección fiscal completa
    "email": "patriciadoradotrainer@gmail.com",
    "registro": "",         # Colegio o registro profesional y número (vacío si no aplica)
    "dominio": "",          # p. ej. moasalut.com
    "fecha": "noviembre de 2026",
}

PAGINAS = {
# ───────────────────────────── AVISO LEGAL ─────────────────────────────
"aviso-legal": {
 "es": {"titulo": "Aviso legal", "html": """
<h2>1. Datos identificativos</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
<ul>
<li><strong>Titular:</strong> {{titular}}</li>
<li><strong>NIF:</strong> {{nif}}</li>
<li><strong>Domicilio:</strong> {{direccion}}</li>
<li><strong>Correo electrónico:</strong> {{email}}</li>
<li><strong>Sitio web:</strong> {{dominio}}</li>
<li><strong>Registro o colegio profesional:</strong> {{registro}}</li>
</ul>
<p>MOA · Moviment i Salut es un proyecto de Patricia Dorado Trainer.</p>
<h2>2. Objeto</h2>
<p>Este sitio web ofrece información sobre los servicios de entrenamiento personal, entrenamiento en grupo, entrenamiento a domicilio, online y por app, y quiromasaje, y permite contactar con el titular.</p>
<h2>3. Condiciones de uso</h2>
<p>El acceso al sitio web es gratuito y atribuye la condición de usuario, que se compromete a hacer un uso adecuado de los contenidos, de acuerdo con la ley, la buena fe y el orden público. El usuario se compromete a no utilizar el sitio para actividades ilícitas ni para introducir virus o cualquier otro sistema que pueda causar daños.</p>
<h2>4. Información sobre salud</h2>
<p>Los contenidos de esta web son informativos y no sustituyen el consejo de un profesional sanitario. Antes de iniciar un programa de ejercicio, especialmente si tienes una lesión o un problema de salud, se recomienda consultar con tu médico.</p>
<h2>5. Propiedad intelectual e industrial</h2>
<p>Los textos, fotografías, logotipos, diseño y demás contenidos de este sitio son propiedad del titular o se usan con autorización de sus autores. Queda prohibida su reproducción, distribución o transformación sin autorización expresa.</p>
<h2>6. Enlaces y contenidos de terceros</h2>
<p>El sitio incluye enlaces y contenidos de terceros (por ejemplo, vídeos de Instagram, Google Maps o WhatsApp). El titular no se responsabiliza de los contenidos ni de las políticas de esos sitios.</p>
<h2>7. Responsabilidad</h2>
<p>El titular no garantiza la ausencia de errores en los contenidos ni la disponibilidad continua del sitio, y no se hace responsable de los daños derivados de su uso, salvo en los casos previstos por la ley. Las tarifas y horarios publicados son orientativos y pueden cambiar.</p>
<h2>8. Legislación aplicable</h2>
<p>Este aviso legal se rige por la legislación española. Para cualquier controversia, las partes se someten a los juzgados y tribunales que correspondan según la normativa aplicable.</p>
"""},
 "ca": {"titulo": "Avís legal", "html": """
<h2>1. Dades identificatives</h2>
<p>En compliment de l’article 10 de la Llei 34/2002, de serveis de la societat de la informació i de comerç electrònic (LSSI-CE), s’informa de les dades del titular d’aquest lloc web:</p>
<ul>
<li><strong>Titular:</strong> {{titular}}</li>
<li><strong>NIF:</strong> {{nif}}</li>
<li><strong>Domicili:</strong> {{direccion}}</li>
<li><strong>Correu electrònic:</strong> {{email}}</li>
<li><strong>Lloc web:</strong> {{dominio}}</li>
<li><strong>Registre o col·legi professional:</strong> {{registro}}</li>
</ul>
<p>MOA · Moviment i Salut és un projecte de Patricia Dorado Trainer.</p>
<h2>2. Objecte</h2>
<p>Aquest lloc web ofereix informació sobre els serveis d’entrenament personal, entrenament en grup, entrenament a domicili, en línia i amb app, i quiromassatge, i permet contactar amb el titular.</p>
<h2>3. Condicions d’ús</h2>
<p>L’accés al lloc web és gratuït i atribueix la condició d’usuari, que es compromet a fer un ús adequat dels continguts, d’acord amb la llei, la bona fe i l’ordre públic. L’usuari es compromet a no utilitzar el lloc per a activitats il·lícites ni per introduir virus o qualsevol altre sistema que pugui causar danys.</p>
<h2>4. Informació sobre salut</h2>
<p>Els continguts d’aquest web són informatius i no substitueixen el consell d’un professional sanitari. Abans de començar un programa d’exercici, especialment si tens una lesió o un problema de salut, es recomana consultar el teu metge.</p>
<h2>5. Propietat intel·lectual i industrial</h2>
<p>Els textos, fotografies, logotips, disseny i la resta de continguts d’aquest lloc són propietat del titular o s’utilitzen amb autorització dels seus autors. Se’n prohibeix la reproducció, distribució o transformació sense autorització expressa.</p>
<h2>6. Enllaços i continguts de tercers</h2>
<p>El lloc inclou enllaços i continguts de tercers (per exemple, vídeos d’Instagram, Google Maps o WhatsApp). El titular no es fa responsable dels continguts ni de les polítiques d’aquests llocs.</p>
<h2>7. Responsabilitat</h2>
<p>El titular no garanteix l’absència d’errors en els continguts ni la disponibilitat contínua del lloc, i no es fa responsable dels danys derivats del seu ús, excepte en els casos previstos per la llei. Les tarifes i horaris publicats són orientatius i poden canviar.</p>
<h2>8. Legislació aplicable</h2>
<p>Aquest avís legal es regeix per la legislació espanyola. Per a qualsevol controvèrsia, les parts se sotmeten als jutjats i tribunals que corresponguin segons la normativa aplicable.</p>
"""},
 "en": {"titulo": "Legal notice", "html": """
<h2>1. Website owner</h2>
<p>In accordance with Article 10 of Spanish Law 34/2002 on Information Society Services and Electronic Commerce (LSSI-CE), the details of the owner of this website are:</p>
<ul>
<li><strong>Owner:</strong> {{titular}}</li>
<li><strong>Tax ID (NIF):</strong> {{nif}}</li>
<li><strong>Address:</strong> {{direccion}}</li>
<li><strong>Email:</strong> {{email}}</li>
<li><strong>Website:</strong> {{dominio}}</li>
<li><strong>Professional register or association:</strong> {{registro}}</li>
</ul>
<p>MOA · Moviment i Salut is a project by Patricia Dorado Trainer.</p>
<h2>2. Purpose</h2>
<p>This website provides information about personal training, group training, home, online and app-based training, and chiromassage services, and allows visitors to get in touch with the owner.</p>
<h2>3. Terms of use</h2>
<p>Access to this website is free and makes you a user, who agrees to use its content appropriately and in accordance with the law, good faith and public order. Users agree not to use the site for unlawful purposes or to introduce viruses or any other harmful systems.</p>
<h2>4. Health information</h2>
<p>The content of this website is for information only and does not replace the advice of a healthcare professional. Before starting an exercise programme, especially if you have an injury or a health condition, please consult your doctor.</p>
<h2>5. Intellectual and industrial property</h2>
<p>The texts, photographs, logos, design and other content of this site belong to the owner or are used with the authors’ permission. Reproduction, distribution or modification without express permission is prohibited.</p>
<h2>6. Third-party links and content</h2>
<p>This site includes links and content from third parties (for example, Instagram videos, Google Maps or WhatsApp). The owner is not responsible for the content or policies of those sites.</p>
<h2>7. Liability</h2>
<p>The owner does not guarantee that the content is error-free or that the site will always be available, and is not liable for damage arising from its use, except where required by law. Published prices and timetables are indicative and may change.</p>
<h2>8. Applicable law</h2>
<p>This legal notice is governed by Spanish law. Any dispute shall be submitted to the courts that have jurisdiction under the applicable regulations.</p>
"""},
},
# ─────────────────────────── PRIVACIDAD ───────────────────────────
"politica-de-privacidad": {
 "es": {"titulo": "Política de privacidad", "html": """
<p>Última actualización: {{fecha}}.</p>
<h2>1. Responsable del tratamiento</h2>
<ul>
<li><strong>Responsable:</strong> {{titular}}</li>
<li><strong>NIF:</strong> {{nif}}</li>
<li><strong>Domicilio:</strong> {{direccion}}</li>
<li><strong>Correo electrónico:</strong> {{email}}</li>
</ul>
<h2>2. Qué datos tratamos</h2>
<p>Los que nos facilitas en el formulario de contacto o al escribirnos por WhatsApp o correo: nombre, correo electrónico, teléfono (opcional), el servicio que te interesa y el mensaje que nos envías. Si en el mensaje nos cuentas información sobre tu salud (por ejemplo, una lesión), la tratamos solo para responder a tu consulta y adaptar la propuesta, con tu consentimiento explícito.</p>
<h2>3. Para qué los usamos</h2>
<ul>
<li>Responder a tus consultas y solicitudes de información.</li>
<li>Si te conviertes en cliente, gestionar el servicio contratado, los horarios y los cobros.</li>
</ul>
<p>No usamos tus datos para enviarte publicidad sin tu permiso ni tomamos decisiones automatizadas con ellos.</p>
<h2>4. Base legal</h2>
<ul>
<li>Tu <strong>consentimiento</strong>, al marcar la casilla del formulario o escribirnos (art. 6.1.a RGPD y, para datos de salud, art. 9.2.a).</li>
<li>La <strong>ejecución de un contrato</strong> o de medidas precontractuales, si contratas un servicio (art. 6.1.b).</li>
<li>El <strong>cumplimiento de obligaciones legales</strong>, por ejemplo fiscales (art. 6.1.c).</li>
</ul>
<h2>5. Cuánto tiempo los guardamos</h2>
<p>Los datos de las consultas, el tiempo necesario para responderlas y, como máximo, un año si no llegas a contratar ningún servicio. Los de clientes, mientras dure la relación y, después, durante los plazos que exige la ley (por ejemplo, fiscales).</p>
<h2>6. Con quién los compartimos</h2>
<p>No cedemos tus datos a terceros, salvo obligación legal. Para que la web funcione usamos estos proveedores, que pueden tratar datos por cuenta nuestra:</p>
<ul>
<li><strong>FormSubmit</strong>: envía al correo del responsable los mensajes del formulario. Puede implicar una transferencia internacional de datos.</li>
<li><strong>Google (Gmail)</strong>: correo electrónico donde se reciben las consultas.</li>
<li><strong>WhatsApp (Meta)</strong>: si eliges escribirnos por WhatsApp.</li>
<li>El <strong>proveedor de alojamiento</strong> de la web.</li>
</ul>
<p>Cuando hay transferencias fuera del Espacio Económico Europeo, se realizan con las garantías previstas en el RGPD (por ejemplo, cláusulas contractuales tipo o decisiones de adecuación).</p>
<h2>7. Tus derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad, y retirar tu consentimiento en cualquier momento, escribiendo a {{email}}. Si consideras que no hemos atendido bien tu solicitud, puedes reclamar ante la Agencia Española de Protección de Datos (www.aepd.es).</p>
<h2>8. Menores</h2>
<p>Si eres menor de 14 años, necesitamos el consentimiento de tu padre, madre o tutor para tratar tus datos.</p>
"""},
 "ca": {"titulo": "Política de privacitat", "html": """
<p>Darrera actualització: {{fecha}}.</p>
<h2>1. Responsable del tractament</h2>
<ul>
<li><strong>Responsable:</strong> {{titular}}</li>
<li><strong>NIF:</strong> {{nif}}</li>
<li><strong>Domicili:</strong> {{direccion}}</li>
<li><strong>Correu electrònic:</strong> {{email}}</li>
</ul>
<h2>2. Quines dades tractem</h2>
<p>Les que ens facilites al formulari de contacte o en escriure’ns per WhatsApp o correu: nom, correu electrònic, telèfon (opcional), el servei que t’interessa i el missatge que ens envies. Si al missatge ens expliques informació sobre la teva salut (per exemple, una lesió), la tractem només per respondre la teva consulta i adaptar la proposta, amb el teu consentiment explícit.</p>
<h2>3. Per a què les fem servir</h2>
<ul>
<li>Respondre les teves consultes i sol·licituds d’informació.</li>
<li>Si et fas client, gestionar el servei contractat, els horaris i els cobraments.</li>
</ul>
<p>No fem servir les teves dades per enviar-te publicitat sense el teu permís ni prenem decisions automatitzades amb elles.</p>
<h2>4. Base legal</h2>
<ul>
<li>El teu <strong>consentiment</strong>, en marcar la casella del formulari o escriure’ns (art. 6.1.a RGPD i, per a dades de salut, art. 9.2.a).</li>
<li>L’<strong>execució d’un contracte</strong> o de mesures precontractuals, si contractes un servei (art. 6.1.b).</li>
<li>El <strong>compliment d’obligacions legals</strong>, per exemple fiscals (art. 6.1.c).</li>
</ul>
<h2>5. Quant de temps les guardem</h2>
<p>Les dades de les consultes, el temps necessari per respondre-les i, com a màxim, un any si no arribes a contractar cap servei. Les de clients, mentre duri la relació i, després, durant els terminis que exigeix la llei (per exemple, fiscals).</p>
<h2>6. Amb qui les compartim</h2>
<p>No cedim les teves dades a tercers, excepte per obligació legal. Perquè el web funcioni fem servir aquests proveïdors, que poden tractar dades per compte nostre:</p>
<ul>
<li><strong>FormSubmit</strong>: envia al correu del responsable els missatges del formulari. Pot implicar una transferència internacional de dades.</li>
<li><strong>Google (Gmail)</strong>: correu electrònic on es reben les consultes.</li>
<li><strong>WhatsApp (Meta)</strong>: si tries escriure’ns per WhatsApp.</li>
<li>El <strong>proveïdor d’allotjament</strong> del web.</li>
</ul>
<p>Quan hi ha transferències fora de l’Espai Econòmic Europeu, es fan amb les garanties previstes al RGPD (per exemple, clàusules contractuals tipus o decisions d’adequació).</p>
<h2>7. Els teus drets</h2>
<p>Pots exercir els drets d’accés, rectificació, supressió, oposició, limitació i portabilitat, i retirar el consentiment en qualsevol moment, escrivint a {{email}}. Si consideres que no hem atès bé la teva sol·licitud, pots reclamar davant l’Agència Espanyola de Protecció de Dades (www.aepd.es) o l’Autoritat Catalana de Protecció de Dades (apdcat.gencat.cat).</p>
<h2>8. Menors</h2>
<p>Si tens menys de 14 anys, necessitem el consentiment del teu pare, mare o tutor per tractar les teves dades.</p>
"""},
 "en": {"titulo": "Privacy policy", "html": """
<p>Last updated: {{fecha}}.</p>
<h2>1. Data controller</h2>
<ul>
<li><strong>Controller:</strong> {{titular}}</li>
<li><strong>Tax ID (NIF):</strong> {{nif}}</li>
<li><strong>Address:</strong> {{direccion}}</li>
<li><strong>Email:</strong> {{email}}</li>
</ul>
<h2>2. What data we process</h2>
<p>The data you give us through the contact form or when you write to us on WhatsApp or by email: name, email address, phone number (optional), the service you are interested in and your message. If you tell us about your health in your message (for example, an injury), we process it only to answer your enquiry and tailor our proposal, with your explicit consent.</p>
<h2>3. Why we use it</h2>
<ul>
<li>To answer your enquiries and requests for information.</li>
<li>If you become a client, to manage the service, schedules and payments.</li>
</ul>
<p>We do not use your data to send you advertising without your permission, and we do not make automated decisions with it.</p>
<h2>4. Legal basis</h2>
<ul>
<li>Your <strong>consent</strong>, when you tick the box on the form or write to us (Art. 6(1)(a) GDPR and, for health data, Art. 9(2)(a)).</li>
<li>The <strong>performance of a contract</strong> or pre-contractual steps, if you book a service (Art. 6(1)(b)).</li>
<li><strong>Compliance with legal obligations</strong>, such as tax obligations (Art. 6(1)(c)).</li>
</ul>
<h2>5. How long we keep it</h2>
<p>Enquiry data is kept for as long as needed to answer it and for a maximum of one year if you do not book any service. Client data is kept for the duration of the relationship and then for the periods required by law (for example, for tax purposes).</p>
<h2>6. Who we share it with</h2>
<p>We do not share your data with third parties unless legally required. To run the website we use the following providers, which may process data on our behalf:</p>
<ul>
<li><strong>FormSubmit</strong>: forwards contact form messages to the controller’s email. This may involve an international data transfer.</li>
<li><strong>Google (Gmail)</strong>: the email service where enquiries are received.</li>
<li><strong>WhatsApp (Meta)</strong>: if you choose to write to us on WhatsApp.</li>
<li>The website’s <strong>hosting provider</strong>.</li>
</ul>
<p>Any transfers outside the European Economic Area are made with the safeguards provided for in the GDPR (for example, standard contractual clauses or adequacy decisions).</p>
<h2>7. Your rights</h2>
<p>You can exercise your rights of access, rectification, erasure, objection, restriction and portability, and withdraw your consent at any time, by writing to {{email}}. If you feel your request has not been handled properly, you can lodge a complaint with the Spanish Data Protection Agency (www.aepd.es).</p>
<h2>8. Minors</h2>
<p>If you are under 14, we need the consent of your parent or guardian to process your data.</p>
"""},
},
# ───────────────────────────── COOKIES ─────────────────────────────
"politica-de-cookies": {
 "es": {"titulo": "Política de cookies", "html": """
<p>Última actualización: {{fecha}}.</p>
<h2>1. Qué son las cookies</h2>
<p>Las cookies son pequeños archivos que una web guarda en tu navegador para recordar información sobre tu visita. Tecnologías parecidas, como el almacenamiento local del navegador, se rigen por las mismas normas.</p>
<h2>2. Qué usa esta web</h2>
<ul>
<li><strong>Técnicas y de preferencias (propias):</strong> el sitio guarda en tu navegador el idioma que eliges (catalán, castellano o inglés) para mostrártelo en tu próxima visita. Son necesarias y no requieren consentimiento.</li>
<li><strong>Las del propio WordPress y del alojamiento:</strong> pueden instalar cookies técnicas para el funcionamiento y la seguridad del sitio.</li>
<li><strong>De terceros (Instagram / Meta):</strong> la web muestra vídeos de Instagram. Al cargarlos, Instagram puede instalar cookies propias, incluidas de análisis o publicidad, que se rigen por su política: privacycenter.instagram.com.</li>
<li><strong>Google Fonts:</strong> las tipografías se cargan desde servidores de Google, que recibe tu dirección IP. No instala cookies.</li>
</ul>
<h2>3. Cómo gestionarlas</h2>
<p>Las cookies que no son técnicas solo se instalan con tu consentimiento, que puedes dar o retirar en cualquier momento desde el aviso de cookies de la web. También puedes bloquearlas o borrarlas desde la configuración de tu navegador (Chrome, Safari, Firefox, Edge…), aunque alguna parte de la web podría dejar de funcionar.</p>
<h2>4. Más información</h2>
<p>Si tienes dudas, escríbenos a {{email}}. Para saber cómo tratamos tus datos, consulta la <a href="/politica-de-privacidad/">política de privacidad</a>.</p>
"""},
 "ca": {"titulo": "Política de cookies", "html": """
<p>Darrera actualització: {{fecha}}.</p>
<h2>1. Què són les galetes</h2>
<p>Les galetes (cookies) són petits fitxers que un web desa al teu navegador per recordar informació sobre la teva visita. Tecnologies semblants, com l’emmagatzematge local del navegador, es regeixen per les mateixes normes.</p>
<h2>2. Què fa servir aquest web</h2>
<ul>
<li><strong>Tècniques i de preferències (pròpies):</strong> el lloc desa al teu navegador l’idioma que tries (català, castellà o anglès) per mostrar-te’l a la propera visita. Són necessàries i no requereixen consentiment.</li>
<li><strong>Les del mateix WordPress i de l’allotjament:</strong> poden instal·lar galetes tècniques per al funcionament i la seguretat del lloc.</li>
<li><strong>De tercers (Instagram / Meta):</strong> el web mostra vídeos d’Instagram. En carregar-los, Instagram pot instal·lar galetes pròpies, incloses d’anàlisi o publicitat, que es regeixen per la seva política: privacycenter.instagram.com.</li>
<li><strong>Google Fonts:</strong> les tipografies es carreguen des de servidors de Google, que rep la teva adreça IP. No instal·la galetes.</li>
</ul>
<h2>3. Com gestionar-les</h2>
<p>Les galetes que no són tècniques només s’instal·len amb el teu consentiment, que pots donar o retirar en qualsevol moment des de l’avís de galetes del web. També les pots bloquejar o esborrar des de la configuració del navegador (Chrome, Safari, Firefox, Edge…), tot i que alguna part del web podria deixar de funcionar.</p>
<h2>4. Més informació</h2>
<p>Si tens dubtes, escriu-nos a {{email}}. Per saber com tractem les teves dades, consulta la <a href="/politica-de-privacidad/">política de privacitat</a>.</p>
"""},
 "en": {"titulo": "Cookie policy", "html": """
<p>Last updated: {{fecha}}.</p>
<h2>1. What cookies are</h2>
<p>Cookies are small files that a website stores in your browser to remember information about your visit. Similar technologies, such as the browser’s local storage, follow the same rules.</p>
<h2>2. What this website uses</h2>
<ul>
<li><strong>Technical and preference cookies (our own):</strong> the site stores the language you choose (Catalan, Spanish or English) in your browser to show it on your next visit. They are necessary and do not require consent.</li>
<li><strong>WordPress and hosting cookies:</strong> may set technical cookies for the site to work and stay secure.</li>
<li><strong>Third-party cookies (Instagram / Meta):</strong> the website shows Instagram videos. When they load, Instagram may set its own cookies, including analytics or advertising cookies, governed by its policy: privacycenter.instagram.com.</li>
<li><strong>Google Fonts:</strong> fonts are loaded from Google’s servers, which receive your IP address. No cookies are set.</li>
</ul>
<h2>3. How to manage them</h2>
<p>Non-technical cookies are only set with your consent, which you can give or withdraw at any time from the website’s cookie banner. You can also block or delete them in your browser settings (Chrome, Safari, Firefox, Edge…), although some parts of the website may stop working.</p>
<h2>4. More information</h2>
<p>If you have any questions, write to us at {{email}}. To learn how we handle your data, see our <a href="/politica-de-privacidad/">privacy policy</a>.</p>
"""},
},
}
