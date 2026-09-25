/* =========================================================
   Chío Jiménez · Maquillaje profesional
   ========================================================= */
(function () {
  'use strict';

  /* ---------------------------------------------------------
     DATOS DE CONTACTO  ·  editar aquí si cambian
     --------------------------------------------------------- */
  var CONTACT = {
    phone: '34627232326',          // WhatsApp, sin + ni espacios
    email: 'chiojm@gmail.com'
  };

  /* ---------------------------------------------------------
     PORTFOLIO
     Para añadir una foto: sube el archivo a assets/img/ y añade
     una línea aquí. cat: novias | moda | audiovisual | creativo
     wide:true hace la pieza el doble de ancha.
     --------------------------------------------------------- */
  var PHOTOS = [
    { src: 'creativo-01.jpg',  cat: 'moda',        es: 'Trabajo creativo',            en: 'Creative work' },
    { src: 'creativo-03.jpg',  cat: 'moda',        es: 'Diseño de mirada',            en: 'Eye design' },
    { src: 'creativo-04.jpg',  cat: 'moda',        es: 'Color sobre la piel',         en: 'Colour on skin' },
    { src: 'creativo-02.jpg',  cat: 'moda',        es: 'Retrato de belleza',          en: 'Beauty portrait' },
    { src: 'pub-01.jpg',       cat: 'moda',        es: 'MOEVIR · Disco',              en: 'MOEVIR · Disco' },
    { src: 'nov-01.jpg',       cat: 'novias',      es: 'Recogido de novia',           en: 'Bridal updo' },
    { src: 'pub-05.jpg',       cat: 'moda',        es: 'StyleCruze · The Last Gheisa', en: 'StyleCruze · The Last Gheisa' },
    { src: 'nov-02.jpg',       cat: 'novias',      es: 'Maquillaje de novia',         en: 'Bridal make-up' },
    { src: 'pub-09.jpg',       cat: 'moda',        es: 'MOEVIR · Winter Brides',      en: 'MOEVIR · Winter Brides' },
    { src: 'nov-12.jpg',       cat: 'novias',      es: 'Preparativos',                en: 'Getting ready', wide: true },
    { src: 'pub-02.jpg',       cat: 'moda',        es: 'StyleCruze · The Black Orchid', en: 'StyleCruze · The Black Orchid' },
    { src: 'nov-04.jpg',       cat: 'novias',      es: 'Novia con flores',            en: 'Bride with flowers' },
    { src: 'pub-11.jpg',       cat: 'moda',        es: 'StyleCruze · Electric',       en: 'StyleCruze · Electric' },
    { src: 'nov-05.jpg',       cat: 'novias',      es: 'Antes de la ceremonia',       en: 'Before the ceremony' },
    { src: 'pub-10.jpg',       cat: 'moda',        es: 'StyleCruze · Flower Girl',    en: 'StyleCruze · Flower Girl' },
    { src: 'nov-03.jpg',       cat: 'novias',      es: 'Belleza natural',             en: 'Natural beauty' },
    { src: 'pub-06.jpg',       cat: 'moda',        es: 'StyleCruze · All Green',      en: 'StyleCruze · All Green' },
    { src: 'nov-06.jpg',       cat: 'novias',      es: 'Corona y velo',               en: 'Crown and veil' },
    { src: 'pub-04.jpg',       cat: 'moda',        es: 'Vigour · Sauvage Swan',       en: 'Vigour · Sauvage Swan' },
    { src: 'nov-07.jpg',       cat: 'novias',      es: 'Recogido pulido',             en: 'Sleek updo' },
    { src: 'pub-07.jpg',       cat: 'moda',        es: 'StyleCruze · Neon Vibes',     en: 'StyleCruze · Neon Vibes' },
    { src: 'nov-08.jpg',       cat: 'novias',      es: 'Tiara y trenza',              en: 'Tiara and braid' },
    { src: 'pub-03.jpg',       cat: 'moda',        es: 'Vigour · Belleza natural',    en: 'Vigour · Natural beauty' },
    { src: 'nov-09.jpg',       cat: 'novias',      es: 'Novia con corona',            en: 'Bride with crown' },
    { src: 'pub-08.jpg',       cat: 'moda',        es: 'StyleCruze · Young and Beauty', en: 'StyleCruze · Young and Beauty' },
    { src: 'nov-10.jpg',       cat: 'novias',      es: 'Semirecogido',                en: 'Half-up hair' },
    { src: 'moda-102.jpg',     cat: 'moda',        es: 'Maquillaje artístico',        en: 'Artistic make-up' },
    { src: 'moda-04.jpg',      cat: 'moda',        es: 'Editorial de moda',           en: 'Fashion editorial' },
    { src: 'nov-11.jpg',       cat: 'novias',      es: 'El proceso',                  en: 'The process' },
    { src: 'novia-02.jpg',     cat: 'novias',      es: 'Preparativos en el hotel',    en: 'Getting ready at the hotel', wide: true },
    { src: 'novia-01.jpg',     cat: 'novias',      es: 'Peinado de novia',            en: 'Bridal hair' },
    { src: 'novia-03.jpg',     cat: 'novias',      es: 'El día de la boda',           en: 'The wedding day' },
    { src: 'evento-01.jpg',    cat: 'novias',      es: 'Prueba de novia',             en: 'Bridal trial', wide: true },
    { src: 'av-01.jpg',        cat: 'audiovisual', es: 'Rodaje',                      en: 'On set' },
    { src: 'av-02.jpg',        cat: 'audiovisual', es: 'Maquillaje en set',           en: 'Make-up on set' },
    { src: 'av-03.jpg',        cat: 'audiovisual', es: 'Peinado en rodaje',           en: 'Hair on set' },
    { src: 'formacion-01.jpg', cat: 'formacion',   es: 'Escuma Granada',              en: 'Escuma Granada', wide: true },
    { src: 'guia-color.jpg',   cat: 'formacion',   es: 'Pequeña guía del color',      en: 'A Short Guide to Colour' }
  ];

  /* ---------------------------------------------------------
     MARQUEE
     --------------------------------------------------------- */
  var BRANDS = [
    'Paris Haute Couture Week 2026', 'Leandro Cano', 'Dellafuente', 'Saiko',
    'Carmen Avilés', 'Lori Meyers', 'Eskorzo', 'Adidas', 'Camin', 'Pepe & Vizio',
    'MOEVIR Magazine', 'StyleCruze Magazine', 'Vigour Magazine'
  ];

  /* ---------------------------------------------------------
     TRADUCCIONES
     --------------------------------------------------------- */
  var I18N = {
    en: {
      'skip': 'Skip to content',
      'nav.about': 'About', 'nav.services': 'Services', 'nav.portfolio': 'Portfolio',
      'nav.featured': 'Featured work', 'nav.contact': 'Contact', 'nav.menu': 'Menu',

      'hero.eyebrow': 'Professional make-up artist · Director of Escuma Granada',
      'hero.lead': 'Science, technique and art. Three inseparable pillars in the way I understand make-up.',
      'hero.meta': 'Granada · All of Spain · International',
      'cta.quote': 'Request a quote', 'cta.portfolio': 'View portfolio',

      'about.eyebrow': 'About me',
      'about.title': 'Observe, understand,<br><span class="italic">analyse and decide</span>',
      'about.body':
        '<p>I am a professional make-up artist, teacher and director of <strong>Escuma Granada</strong>. The way I understand make-up comes from the union of science, technique and art: three disciplines that, far from being separate, complement each other and shape the way I work.</p>' +
        '<p>I hold a <strong>degree in Biology</strong> from the University of Granada and postgraduate training in <strong>Cosmetics</strong>. Before devoting myself fully to make-up, I spent 19 years working in the pharmaceutical laboratory field. That experience gave me a rigorous, analytical training that is still essential to the way I work today: observing, understanding, analysing and making decisions with judgement.</p>' +
        '<p>My first contact with professional make-up training was with <strong>Noelia Fuentes</strong>, in Málaga. I then continued in Madrid, at the <strong>Bôgart Make Up</strong> school, with <strong>Baltasar González Pinel</strong>. There I built a solid technical foundation and discovered a way of understanding make-up that went far beyond execution: a deep knowledge of technique as the tool that makes creation possible.</p>' +
        '<p>Since <strong>2008</strong> I have worked professionally as a make-up artist across different fields, evolving continuously through training and experience. In <strong>2019</strong> I decided to devote myself exclusively to make-up and teaching, opening a new professional chapter in which Escuma Granada was born and continues to grow.</p>' +
        '<p>My work brings together the knowledge of skin and cosmetics, colour, make-up technique, painting techniques, fashion history and, increasingly, creative research and visual language.</p>' +
        '<p>My most recent training in fashion and creativity took place at <strong>Kabuki Make Up</strong>, in Buenos Aires, with <strong>Jazmín Calcarami</strong>. An experience that widened my view of make-up as an artistic language and of the relationship between make-up, image, fashion and creativity.</p>',
      'facts.start': 'Career begins', 'facts.lab': 'Years in pharmaceutical labs',
      'facts.escuma': 'Full dedication · Escuma is born',

      'quote.text': '“Learn the rules like a pro, so you can break them like an artist.”',
      'philo.1': 'A professional make-up artist is not defined solely by the number of techniques they know, but by their ability to <em>observe, analyse, decide and adapt</em>.',
      'philo.2': 'Learning make-up is not only about reproducing a technique, but about understanding why it works, when to use it and how to transform it to build a proposal of your own.',
      'philo.3': 'Before breaking the rules you have to know them. And technique does not limit creativity: <strong>once mastered, it becomes freedom</strong>.',

      'services.eyebrow': 'Services',
      'services.title': 'Make-up and <span class="italic">hair</span>',
      'services.sub': 'Based in Granada, travelling throughout Spain and abroad.',
      'service.bride.t': 'Bride',
      'service.bride.d': 'Bridal make-up and/or hair. Trial session, look design and support on the wedding day.',
      'service.madrina.t': 'Mother of the bride / groom',
      'service.madrina.d': 'Make-up and/or hair designed in harmony with the style of the event.',
      'service.home.t': 'At home or in studio',
      'service.home.d': 'Make-up and/or hair for events, guests and special occasions, at your home or in studio.',
      'service.shooting.t': 'Shooting, fashion and advertising',
      'service.shooting.d': 'Editorial, music video, campaign, catalogue and audiovisual production. Working closely with direction and the creative team.',
      'service.creative.t': 'Creative projects',
      'service.creative.d': 'Creative research and visual language: authorial proposals, artistic collaborations and concept development.',
      'service.school.t': 'Training · Escuma Granada',
      'service.school.d': 'Professional make-up school. Understanding why a technique works, when to use it and how to transform it.',
      'price.quote': 'Request a quote', 'price.from90': 'from €90', 'price.info': 'More information',
      'cta.ask': 'Request a quote', 'cta.book': 'Book', 'cta.project': "Let's talk about it",
      'cta.collab': 'Propose a collaboration', 'cta.info': 'Request information',

      'gaze.title': 'Eye design',
      'gaze.brows.t': 'Brow design and lamination',
      'gaze.brows.d': 'Shape study based on proportion and expression, plus lamination to set and order the hair.',
      'gaze.lash.t': 'Korean lash lift',
      'gaze.lash.d': 'A natural, long-lasting curl that opens the eye without extensions.',

      'portfolio.eyebrow': 'Portfolio',
      'portfolio.title': 'The work, <span class="italic">in images</span>',
      'portfolio.ig': 'More work on Instagram',
      'filter.all': 'All', 'filter.brides': 'Brides & events', 'filter.fashion': 'Fashion & press',
      'filter.av': 'Audiovisual', 'filter.training': 'Training', 'filter.creative': 'Creative',
      'portfolio.empty': 'New images coming soon.',

      'featured.eyebrow': 'Featured work',
      'featured.title': 'Clients and <span class="italic">projects</span>',
      'featured.couture': 'Haute couture',
      'featured.paris.t': 'Key Make Up Artist · Paris Haute Couture Week 2026',
      'featured.paris.d': 'Make-up direction for <strong>Leandro Cano</strong> at Paris Haute Couture Week.',
      'cat.video': 'Music video', 'cat.brand': 'Advertising · Brand',
      'work.toyota': 'YouTube reviews · From 2021 to today',
      'work.toyota.enlace': 'Watch an example', 'cat.adv': 'Advertising · Music', 'cat.campaign': 'Campaign',
      'work.sayko': 'Intro for <em>Sakura</em>',
      'work.della': '<em>Adidas</em> promo · Launch material for the album <em>Brigado</em>',
      'work.camin': 'Advertising campaign',

      'libro.eyebrow': 'Publication',
      'libro.titulo': 'A Short Guide to Colour for Make-up Artists',
      'libro.desc': 'A guide to colour for those who work with it. It gathers the way Chío has come to understand it, bringing together her scientific training \u2014a degree in Biology and a master\u2019s in cosmetology\u2014 with the practice of professional make-up.',
      'libro.cta': 'Buy via WhatsApp',
      'trio.moda': 'Fashion & press', 'trio.novias': 'Brides & events', 'trio.av': 'Audiovisual',
      'press.title': 'Featured in', 'press.beauty': 'Beauty editorial',

      'contact.eyebrow': 'Contact',
      'contact.title': 'Tell me about your <span class="italic">project</span>',
      'contact.lead': 'Weddings, events, audiovisual productions, advertising and creative projects. Write to me with the date and the details and I will prepare a tailored quote.',
      'contact.whatsapp': 'WhatsApp', 'contact.email': 'Email',
      'contact.area': 'Working area', 'contact.areaval': 'Granada · All of Spain · International',
      'contact.reviews': 'Reviews', 'contact.reviewsval': 'Read reviews on Google',
      'contact.social': 'Social',

      'form.name': 'Full name', 'form.email': 'Email', 'form.phone': 'Phone',
      'form.service': 'Service', 'form.choose': 'Choose a service',
      'form.date': 'Date', 'form.place': 'Location', 'form.message': 'Tell me more',
      'form.optional': '(optional)',
      'form.send': 'Send via WhatsApp', 'form.sendmail': 'Send by email',
      'form.error': 'Please fill in the required fields.',
      'form.okwa': 'Opening WhatsApp with your message…',
      'form.okmail': 'Opening your email app…',
      'form.subject': 'Enquiry from the website',

      'footer.role': 'Professional make-up artist · Granada',
      'footer.rights': 'All rights reserved.'
    }
  };

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var state = { lang: 'es', filter: 'moda' };   // se entra por moda y publicaciones
  var originals = null;

  /* =========================================================
     IDIOMA
     ========================================================= */
  function cacheOriginals() {
    originals = [];
    $$('[data-i18n]').forEach(function (el) {
      originals.push({ el: el, html: el.innerHTML });
    });
  }

  function t(key) {
    var dict = I18N[state.lang];
    return dict ? dict[key] : null;
  }

  function applyLang(lang) {
    state.lang = lang;
    document.documentElement.lang = lang;

    originals.forEach(function (o) {
      if (lang === 'es') {
        o.el.innerHTML = o.html;
        return;
      }
      var val = t(o.el.getAttribute('data-i18n'));
      if (val != null) o.el.innerHTML = val;
    });

    $$('.lang__btn').forEach(function (b) {
      var on = b.getAttribute('data-lang') === lang;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });

    try { localStorage.setItem('cj-lang', lang); } catch (e) { /* modo privado */ }

    renderGrid();
  }

  function initLang() {
    cacheOriginals();

    var saved = null;
    try { saved = localStorage.getItem('cj-lang'); } catch (e) { /* modo privado */ }

    var lang;
    if (saved === 'es' || saved === 'en') {
      lang = saved;                                  // preferencia guardada
    } else {
      var browser = (navigator.language || 'es').toLowerCase();
      lang = browser.indexOf('es') === 0 ? 'es' : 'en';
    }
    $$('.lang__btn').forEach(function (b) {
      b.addEventListener('click', function () { applyLang(b.getAttribute('data-lang')); });
    });
    applyLang(lang);
  }

  /* =========================================================
     NAV
     ========================================================= */
  function initNav() {
    var nav = $('#nav');
    var toggle = $('#navToggle');
    var menu = $('#navMenu');

    var hero = $('#top');
    var wa = $('.wa');

    var onScroll = function () {
      // La cabecera va en blanco mientras queda sobre la portada en negro,
      // y pasa a fondo claro en cuanto la portada deja de estar detrás.
      var limite = hero ? hero.offsetHeight - nav.offsetHeight : 40;
      var sobreLaPortada = window.scrollY < limite;

      nav.classList.toggle('is-on-dark', sobreLaPortada);
      nav.classList.toggle('is-stuck', !sobreLaPortada);
      if (wa) wa.classList.toggle('is-visible', window.scrollY > 400);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      onScroll();
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });

    $$('a', menu).forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    // Sección activa
    var links = $$('a[href^="#"]', menu);
    var sections = links.map(function (a) { return $(a.getAttribute('href')); }).filter(Boolean);
    if ('IntersectionObserver' in window && sections.length) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          links.forEach(function (a) {
            a.classList.toggle('is-current', a.getAttribute('href') === '#' + e.target.id);
          });
        });
      }, { rootMargin: '-45% 0px -50% 0px' });
      sections.forEach(function (s) { spy.observe(s); });
    }
  }

  /* =========================================================
     MARQUEE
     ========================================================= */
  function initMarquee() {
    var track = $('#marqueeTrack');
    if (!track) return;
    var half = BRANDS.map(function (b) {
      return '<span>' + b + '</span><b>·</b>';
    }).join('');
    track.innerHTML = half + half; // duplicado para bucle continuo
  }

  /* =========================================================
     PORTFOLIO
     ========================================================= */
  function renderGrid() {
    var grid = $('#grid');
    if (!grid) return;

    var items = PHOTOS.filter(function (p) {
      return p.cat === state.filter;
    });

    grid.innerHTML = items.map(function (p, i) {
      var title = state.lang === 'en' ? (p.en || p.es) : p.es;
      return '' +
        '<button class="tile' + (p.wide ? ' tile--wide' : '') + ' ph reveal" ' +
              'type="button" data-index="' + i + '" data-ph="' + p.src + '">' +
          '<img src="assets/img/' + p.src + '" alt="' + title + '" loading="lazy" decoding="async">' +
          '<span class="tile__meta">' +
            '<span class="tile__cat">' + catLabel(p.cat) + '</span>' +
            '<span class="tile__title">' + title + '</span>' +
          '</span>' +
        '</button>';
    }).join('');

    // Marca como vacía toda pieza cuya imagen aún no exista
    $$('img', grid).forEach(function (img) {
      img.addEventListener('error', function () {
        var tile = img.closest('.tile');
        if (tile) tile.classList.add('is-empty');
        img.remove();
      });
    });

    $$('.tile', grid).forEach(function (tile) {
      tile.addEventListener('click', function () {
        if (tile.classList.contains('is-empty')) return;
        openLightbox(items, parseInt(tile.getAttribute('data-index'), 10));
      });
    });

    observeReveals(grid);
  }

  function catLabel(cat) {
    var map = {
      novias:      { es: 'Novias y eventos',  en: 'Brides & events' },
      moda:        { es: 'Moda y publicaciones', en: 'Fashion & press' },
      audiovisual: { es: 'Audiovisuales',     en: 'Audiovisual' },
      formacion:   { es: 'Formación',         en: 'Training' },
      creativo:    { es: 'Creativo',          en: 'Creative' }
    };
    var m = map[cat];
    return m ? m[state.lang] || m.es : cat;
  }

  function initFilters() {
    $$('.filter').forEach(function (btn) {
      btn.addEventListener('click', function () {
        $$('.filter').forEach(function (b) { b.classList.remove('is-active'); });
        btn.classList.add('is-active');
        state.filter = btn.getAttribute('data-filter');
        renderGrid();
      });
    });
  }

  /* =========================================================
     LIGHTBOX
     ========================================================= */
  var lb = { el: null, items: [], i: 0, lastFocus: null };

  function buildLightbox() {
    var el = document.createElement('div');
    el.className = 'lb';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-modal', 'true');
    el.innerHTML =
      '<button class="lb__close" type="button" aria-label="Cerrar">&#10005;</button>' +
      '<button class="lb__nav lb__nav--prev" type="button" aria-label="Anterior">&#8249;</button>' +
      '<button class="lb__nav lb__nav--next" type="button" aria-label="Siguiente">&#8250;</button>' +
      '<div><img alt=""><p class="lb__cap"></p></div>';
    document.body.appendChild(el);

    $('.lb__close', el).addEventListener('click', closeLightbox);
    $('.lb__nav--prev', el).addEventListener('click', function () { step(-1); });
    $('.lb__nav--next', el).addEventListener('click', function () { step(1); });
    el.addEventListener('click', function (e) { if (e.target === el) closeLightbox(); });

    document.addEventListener('keydown', function (e) {
      if (!el.classList.contains('is-open')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') step(-1);
      if (e.key === 'ArrowRight') step(1);
    });

    lb.el = el;
  }

  function openLightbox(items, i) {
    if (!lb.el) buildLightbox();
    lb.items = items;
    lb.i = i;
    lb.lastFocus = document.activeElement;
    paint();
    lb.el.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    $('.lb__close', lb.el).focus();
  }

  function closeLightbox() {
    lb.el.classList.remove('is-open');
    document.body.style.overflow = '';
    if (lb.lastFocus) lb.lastFocus.focus();
  }

  function step(dir) {
    lb.i = (lb.i + dir + lb.items.length) % lb.items.length;
    paint();
  }

  function paint() {
    var p = lb.items[lb.i];
    var title = state.lang === 'en' ? (p.en || p.es) : p.es;
    $('img', lb.el).src = 'assets/img/' + p.src;
    $('img', lb.el).alt = title;
    $('.lb__cap', lb.el).textContent = title + ' · ' + catLabel(p.cat);
  }

  /* =========================================================
     FORMULARIO  →  WhatsApp / Email
     ========================================================= */
  function initForm() {
    var form = $('#contactForm');
    if (!form) return;
    var note = $('#formNote');

    var read = function () {
      return {
        nombre:   form.nombre.value.trim(),
        email:    form.email.value.trim(),
        telefono: form.telefono.value.trim(),
        servicio: form.servicio.value,
        fecha:    form.fecha.value,
        lugar:    form.lugar.value.trim(),
        mensaje:  form.mensaje.value.trim()
      };
    };

    var validate = function () {
      var ok = true;
      ['nombre', 'email', 'servicio', 'mensaje'].forEach(function (name) {
        var field = form[name];
        var empty = !field.value.trim();
        var bad = name === 'email' && field.value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(field.value);
        field.classList.toggle('is-error', empty || bad);
        if (empty || bad) ok = false;
      });
      if (!ok) {
        note.textContent = state.lang === 'en'
          ? I18N.en['form.error']
          : 'Por favor, completa los campos obligatorios.';
        note.classList.add('is-error');
      } else {
        note.classList.remove('is-error');
      }
      return ok;
    };

    var compose = function (d) {
      var en = state.lang === 'en';
      var L = en
        ? { hi: 'Hello Chío, I am writing from your website.', name: 'Name', email: 'Email',
            phone: 'Phone', service: 'Service', date: 'Date', place: 'Location', msg: 'Message' }
        : { hi: 'Hola Chío, te escribo desde tu web.', name: 'Nombre', email: 'Email',
            phone: 'Teléfono', service: 'Servicio', date: 'Fecha', place: 'Lugar', msg: 'Mensaje' };

      var lines = [L.hi, '', L.name + ': ' + d.nombre, L.email + ': ' + d.email];
      if (d.telefono) lines.push(L.phone + ': ' + d.telefono);
      lines.push(L.service + ': ' + d.servicio);
      if (d.fecha) lines.push(L.date + ': ' + d.fecha);
      if (d.lugar) lines.push(L.place + ': ' + d.lugar);
      lines.push('', L.msg + ': ' + d.mensaje);
      return lines.join('\n');
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate()) return;
      var body = compose(read());
      note.textContent = state.lang === 'en'
        ? I18N.en['form.okwa']
        : 'Abriendo WhatsApp con tu mensaje…';
      window.open('https://wa.me/' + CONTACT.phone + '?text=' + encodeURIComponent(body), '_blank', 'noopener');
    });

    $('#sendMail').addEventListener('click', function () {
      if (!validate()) return;
      var d = read();
      var subject = (state.lang === 'en' ? I18N.en['form.subject'] : 'Consulta desde la web') + ' · ' + d.servicio;
      note.textContent = state.lang === 'en'
        ? I18N.en['form.okmail']
        : 'Abriendo tu aplicación de correo…';
      window.location.href = 'mailto:' + CONTACT.email +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(compose(d));
    });

    $$('input, select, textarea', form).forEach(function (f) {
      f.addEventListener('input', function () { f.classList.remove('is-error'); });
    });
  }

  /* =========================================================
     REVEAL AL HACER SCROLL
     ========================================================= */
  var revealObserver = null;

  function observeReveals(scope) {
    if (!('IntersectionObserver' in window)) {
      $$('.reveal', scope || document).forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    if (!revealObserver) {
      revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-in');
          revealObserver.unobserve(e.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    }
    $$('.reveal', scope || document).forEach(function (el) {
      if (!el.classList.contains('is-in')) revealObserver.observe(el);
    });
  }

  /* =========================================================
     INIT
     ========================================================= */
  function init() {
    var y = $('#year');
    if (y) y.textContent = String(new Date().getFullYear());

    initNav();
    initMarquee();
    initFilters();
    initLang();      // llama a renderGrid()
    initForm();
    observeReveals();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
