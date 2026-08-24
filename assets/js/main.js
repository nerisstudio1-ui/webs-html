/* ═══════════════════════════════════════════════════
   CALMA · barre studio — interacciones
   Sin dependencias. Todo respeta prefers-reduced-motion.
   ═══════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ──────────────────────────────────────────────────
     👉 WHATSAPP DE RESERVAS
     Escribe aquí el número con prefijo del país y sin espacios,
     signos ni el +. España es 34, así que un móvil 600 12 34 56
     se escribe: '34600123456'

     Todos los botones de "Primera clase gratis" de la web abrirán
     WhatsApp con el mensaje ya escrito.
     ────────────────────────────────────────────────── */
  var WHATSAPP = '34646206292';   /* 646 20 62 92 · Rocío */

  /* El mensaje con el que se abre la conversación */
  var WHATSAPP_MSG = '¡Hola, Rocío! Me gustaría reservar mi primera clase gratis en CALMA \uD83E\uDD0D';

  /* Si algún día hay plataforma de reservas online, se pega aquí
     y manda sobre el WhatsApp */
  var RESERVAS_URL = '';

  var VERSION = 'v5 · 2026-08-24';

  /* Si esto se ejecuta, el aviso sobra */
  var aviso = document.getElementById('aviso-js');
  if (aviso) aviso.style.display = 'none';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ── Botones de reserva ──────────────────────────── */
  var reservaUrl = RESERVAS_URL ||
    (WHATSAPP ? 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(WHATSAPP_MSG) : '');

  if (reservaUrl) {
    $$('[data-book]').forEach(function (a) {
      a.href = reservaUrl;
      a.target = '_blank';
      a.rel = 'noopener';
    });
  } else {
    /* Sin número todavía: los botones llevan al bloque de contacto */
    document.documentElement.classList.add('sin-reservas');
  }

  /* ── Header pegajoso ─────────────────────────────── */
  var header = $('#header');
  var sticky = $('.sticky-book');
  var onScroll = function () {
    header.classList.toggle('is-stuck', window.scrollY > 24);
    if (sticky) sticky.classList.toggle('is-visible', window.scrollY > window.innerHeight * 0.8);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Menú móvil ──────────────────────────────────────
     El menú NO se estiliza con la hoja de estilos: al pulsar el
     icono se construye un panel nuevo, sin clases, con todos los
     estilos escritos en el propio elemento y marcados !important.
     Los enlaces se copian del menú de escritorio. Así da igual lo
     que haga el tema de WordPress: no hay nada suyo de por medio. */
  var burger = $('#burger');
  var nav = $('#nav');

  var CREMA = '#F7F1EA', TINTA = '#3F3936', TOPO = '#8E7C70';
  var LETRA = '"Montserrat",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif';

  var vestir = function (el, reglas) {
    for (var k in reglas) el.style.setProperty(k, reglas[k], 'important');
  };

  /* ¿Funciona aquí position:fixed? Muchos temas y plugins ponen un
     transform por encima, y entonces lo fijo deja de serlo. */
  var rompeFijo = function (el) {
    var n = el && el.parentElement;
    while (n) {
      var cs = getComputedStyle(n);
      if (cs.transform !== 'none' || cs.perspective !== 'none' ||
          cs.filter !== 'none' ||
          (cs.backdropFilter && cs.backdropFilter !== 'none') ||
          /transform|perspective|filter/.test(cs.willChange || '') ||
          /paint|layout|strict|content/.test(cs.contain || ''))
        return true;
      n = n.parentElement;
    }
    return false;
  };
  var fijoVa = function (el) {
    if (rompeFijo(el)) return false;
    var t = document.createElement('div');
    t.style.cssText = 'position:fixed;top:0;left:0;width:1px;height:1px;opacity:0;' +
                      'pointer-events:none;margin:0;padding:0;border:0';
    document.body.appendChild(t);
    var r = t.getBoundingClientRect();
    document.body.removeChild(t);
    return Math.abs(r.top) < 2 && Math.abs(r.left) < 2;
  };
  /* Deja el elemento en el punto (x, y) de la pantalla sin usar fixed:
     lo pone en 0,0, mide dónde ha caído de verdad y corrige. */
  var anclarEn = function (el, x, y) {
    vestir(el, { 'position':'absolute', 'right':'auto', 'bottom':'auto',
                 'transform':'none', 'top':'0', 'left':'0' });
    var r = el.getBoundingClientRect();
    vestir(el, { 'top': Math.round(y - r.top) + 'px',
                 'left': Math.round(x - r.left) + 'px' });
  };

  var APARTADOS = [
    { texto: 'CALMA',      href: '#calma'    },
    { texto: 'Barre',      href: '#barre'    },
    { texto: 'Clases',     href: '#clases'   },
    { texto: 'Tarifas',    href: '#tarifas'  },
    { texto: 'Sobre mí',   href: '#sobre-mi' },
    { texto: 'El estudio', href: '#estudio'  },
    { texto: 'Contacto',   href: '#contacto' },
    { texto: 'Primera clase gratis', href: '#contacto', cta: true }
  ];

  var panel = null;

  var cerrarMenu = function () {
    if (panel && panel.parentNode) panel.parentNode.removeChild(panel);
    panel = null;
    document.body.style.removeProperty('overflow');
    if (burger) {
      burger.setAttribute('aria-expanded', 'false');
      burger.setAttribute('aria-label', 'Abrir menú');
    }
  };

  var abrirMenu = function () {
    cerrarMenu();
    panel = document.createElement('div');
    panel.setAttribute('data-calma-menu', '');
    vestir(panel, {
      'position':'fixed', 'top':'0', 'left':'0', 'right':'0', 'bottom':'0',
      'width':window.innerWidth + 'px', 'height':window.innerHeight + 'px',
      'max-width':'none', 'min-width':'0', 'margin':'0', 'border':'0',
      'box-sizing':'border-box', 'display':'flex', 'flex-direction':'column',
      'align-items':'center', 'justify-content':'center', 'gap':'0',
      'padding':'70px 20px 40px', 'background':CREMA, 'color':TINTA,
      'font-family':LETRA, 'text-align':'center', 'transform':'none',
      'visibility':'visible', 'opacity':'1', 'z-index':'2147483000',
      'overflow-y':'auto', 'overflow-x':'hidden'
    });

    /* Botón de cerrar, dibujado a mano */
    var x = document.createElement('button');
    x.type = 'button';
    x.setAttribute('aria-label', 'Cerrar menú');
    vestir(x, { 'position':'absolute', 'top':'12px', 'right':'12px',
                'width':'48px', 'height':'48px', 'padding':'0', 'margin':'0',
                'border':'0', 'background':'none', 'cursor':'pointer',
                'display':'block', 'opacity':'1', 'visibility':'visible',
                'z-index':'1' });
    [45, -45].forEach(function (giro) {
      var raya = document.createElement('span');
      vestir(raya, { 'position':'absolute', 'left':'14px', 'top':'23px',
                     'width':'20px', 'height':'2px', 'background':TINTA,
                     'border-radius':'2px', 'display':'block',
                     'transform':'rotate(' + giro + 'deg)', 'opacity':'1' });
      x.appendChild(raya);
    });
    x.addEventListener('click', function (e) { e.preventDefault(); cerrarMenu(); });
    panel.appendChild(x);

    /* Los enlaces van escritos aquí, no se leen de la página: si el
       menú de la cabecera no apareciese por lo que sea, el panel se
       construye igual y nunca sale vacío. */
    APARTADOS.forEach(function (item) {
      var esCta = !!item.cta;
      var nuevo = document.createElement('a');
      nuevo.href = esCta ? (reservaUrl || '#contacto') : item.href;
      nuevo.textContent = item.texto;
      if (esCta && reservaUrl) { nuevo.target = '_blank'; nuevo.rel = 'noopener'; }
      vestir(nuevo, {
        'display':'block', 'width':'100%', 'max-width':'320px',
        'box-sizing':'border-box', 'text-align':'center',
        'text-decoration':'none', 'font-family':LETRA,
        'opacity':'1', 'visibility':'visible', 'border':'0',
        'text-transform':'uppercase', 'line-height':'1.2'
      });
      if (esCta) {
        vestir(nuevo, { 'margin':'26px 0 0', 'padding':'17px 24px',
                        'background':TOPO, 'color':CREMA,
                        'border-radius':'999px', 'font-size':'12px',
                        'font-weight':'500', 'letter-spacing':'.18em' });
      } else {
        vestir(nuevo, { 'margin':'0', 'padding':'15px 0', 'background':'none',
                        'color':TINTA, 'font-size':'15px', 'font-weight':'300',
                        'letter-spacing':'.22em' });
      }
      nuevo.addEventListener('click', function () { cerrarMenu(); });
      panel.appendChild(nuevo);
    });

    document.body.appendChild(panel);
    document.body.style.setProperty('overflow', 'hidden', 'important');
    if (!fijoVa(panel)) anclarEn(panel, 0, 0);   /* plan B si fixed no vale */
    if (burger) {
      burger.setAttribute('aria-expanded', 'true');
      burger.setAttribute('aria-label', 'Cerrar menú');
    }
  };

  document.addEventListener('click', function (e) {
    var boton = e.target && e.target.closest && e.target.closest('.burger, #burger');
    if (!boton) return;
    e.preventDefault();
    burger = boton;
    if (panel) cerrarMenu(); else abrirMenu();
  }, true);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') cerrarMenu();
  });
  window.addEventListener('resize', function () {
    if (panel && !window.matchMedia('(max-width:860px)').matches) cerrarMenu();
  });

  /* ── Botón flotante de WhatsApp ───────────────────────
     Se cuelga del final de la página, fuera del contenedor de
     Elementor, y si position:fixed no funciona se coloca a mano. */
  if (sticky) {
    var anclaBoton = document.createComment('boton');
    var refugio = null;
    var SITIO = { 'position':'', 'top':'', 'left':'', 'right':'', 'bottom':'', 'transform':'' };

    var colocarBoton = function () {
      if (!refugio || sticky.parentNode !== refugio) return;
      if (fijoVa(sticky)) { for (var k in SITIO) sticky.style.removeProperty(k); return; }
      anclarEn(sticky, Math.round((window.innerWidth - sticky.offsetWidth) / 2),
                       window.innerHeight - sticky.offsetHeight - 16);
    };
    var moverBoton = function () {
      var movil = window.matchMedia('(max-width:860px)').matches;
      if (movil && sticky.parentNode !== refugio) {
        if (!refugio) {
          refugio = document.createElement('div');
          refugio.setAttribute('data-calma-boton', '');
          refugio.style.cssText = 'margin:0;padding:0;border:0;background:none;width:auto';
          document.body.appendChild(refugio);
        }
        sticky.parentNode.insertBefore(anclaBoton, sticky);
        refugio.appendChild(sticky);
        colocarBoton();
      } else if (!movil && refugio && sticky.parentNode === refugio) {
        anclaBoton.parentNode.insertBefore(sticky, anclaBoton);
        for (var k in SITIO) sticky.style.removeProperty(k);
      }
    };
    moverBoton();
    window.addEventListener('resize', function () { moverBoton(); colocarBoton(); });
    var pendiente = false;
    window.addEventListener('scroll', function () {
      if (pendiente) return;
      pendiente = true;
      requestAnimationFrame(function () { pendiente = false; colocarBoton(); });
    }, { passive: true });
  }

  /* ── Diagnóstico ─────────────────────────────────────
     Tres maneras de abrirlo, por si una falla:
       · dirección terminada en  ?calma-debug  o  #calma-debug
       · añadir  #calma-debug  y recargar
       · tocar cinco veces seguidas el logotipo de arriba
     Sale un recuadro con lo que de verdad pasa en ese móvil. */
  var fallos = [];
  window.addEventListener('error', function (e) { fallos.push(e.message); });

  var diagnostico = function () {
    if (document.getElementById('calma-diag')) return;
    var probeta = document.createElement('div');
    probeta.style.cssText = 'position:fixed;top:0;left:0;width:1px;height:1px;opacity:0';
    document.body.appendChild(probeta);
    var pr = probeta.getBoundingClientRect();
    document.body.removeChild(probeta);

    var menu = document.querySelector('[data-calma-menu]') || document.querySelector('.nav');
    var estorba = function (n) {
      while (n) {
        var cs = getComputedStyle(n);
        if (cs.transform !== 'none' || cs.perspective !== 'none' || cs.filter !== 'none' ||
            /transform|perspective|filter/.test(cs.willChange || '') ||
            /paint|layout|strict|content/.test(cs.contain || '')) return true;
        n = n.parentElement;
      }
      return false;
    };
    var fijo = Math.abs(pr.top) < 2 && Math.abs(pr.left) < 2 &&
               !(menu && estorba(menu.parentElement));
    var c = menu ? menu.getBoundingClientRect() : null;
    var culpables = [], el = menu && menu.parentElement;
    while (el) {
      var cs = getComputedStyle(el);
      if (cs.transform !== 'none' || cs.filter !== 'none' ||
          cs.perspective !== 'none' || cs.contain !== 'none')
        culpables.push((el.tagName + '.' + (el.className || '')).slice(0, 34));
      el = el.parentElement;
    }

    var caja = document.createElement('div');
    caja.id = 'calma-diag';
    caja.style.cssText = 'position:absolute;top:0;left:0;width:100%;z-index:2147483600;' +
      'background:#111;color:#7CFF7C;font:12px/1.6 monospace;padding:14px;' +
      'white-space:pre-wrap;word-break:break-all;box-sizing:border-box';
    caja.textContent = [
      'CALMA · diagnostico ' + VERSION,
      'pantalla   ' + window.innerWidth + ' x ' + window.innerHeight,
      'fixed va   ' + (fijo ? 'SI' : 'NO  <-- aqui esta el problema'),
      'copias     ' + document.querySelectorAll('.calma-web[id]').length,
      'menu       ' + (document.querySelector('[data-calma-menu]') ? 'panel abierto' : (menu ? 'cerrado' : 'NO HAY MENU')),
      'menu en    ' + (menu ? (menu.parentElement.className || '?').slice(0, 34) : '-'),
      'menu caja  ' + (c ? [Math.round(c.x), Math.round(c.y),
                            Math.round(c.width), Math.round(c.height)].join(' / ') : '-'),
      'enlaces    ' + (menu ? menu.querySelectorAll('a').length : 0) + ' (cabecera: ' +
        (document.querySelector('.nav') ? document.querySelector('.nav').querySelectorAll('a').length : 0) + ')',
      'boton wa   ' + (document.querySelector('.sticky-book') ? 'si' : 'no'),
      'culpables  ' + (culpables.join(' | ') || 'ninguno'),
      'errores    ' + (fallos.join(' | ') || 'ninguno')
    ].join('\n');

    var x = document.createElement('button');
    x.textContent = 'CERRAR';
    x.style.cssText = 'display:block;margin:12px 0 0;padding:10px 18px;background:#7CFF7C;' +
      'color:#111;border:0;border-radius:4px;font:600 12px monospace';
    x.onclick = function () { caja.parentNode.removeChild(caja); };
    caja.appendChild(x);
    document.body.appendChild(caja);
    /* Que caiga donde se está mirando, aunque fixed no funcione */
    caja.style.top = Math.round(window.scrollY) + 'px';
  };

  if (/calma-debug/.test(location.hash) || /calma-debug/.test(location.search))
    setTimeout(diagnostico, 900);
  window.addEventListener('hashchange', function () {
    if (/calma-debug/.test(location.hash)) diagnostico();
  });
  /* Cinco toques seguidos en el logotipo */
  var marca = $('.logo'), toques = 0, reloj = 0;
  if (marca) marca.addEventListener('click', function (e) {
    clearTimeout(reloj);
    toques++;
    reloj = setTimeout(function () { toques = 0; }, 900);
    if (toques >= 5) { e.preventDefault(); toques = 0; diagnostico(); }
  });

  /* ── Apariciones al hacer scroll ─────────────────── */
  var revealables = $$('.reveal').concat($$('.hero__slogan'));
  if (!('IntersectionObserver' in window) || reduced) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-in'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -6% 0px' });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ── Frase que se ilumina palabra a palabra ──────── */
  var statement = $('[data-words]');
  if (statement) {
    var words = statement.textContent.trim().split(/\s+/);
    statement.textContent = '';
    words.forEach(function (word, i) {
      var span = document.createElement('span');
      span.className = 'w';
      span.textContent = word;
      span.style.transitionDelay = (i * 0.04) + 's';
      statement.appendChild(span);
      statement.appendChild(document.createTextNode(' '));
    });
    var lightUp = function () { $$('.w', statement).forEach(function (w) { w.classList.add('is-lit'); }); };
    if (reduced || !('IntersectionObserver' in window)) {
      lightUp();
    } else {
      var wordsIO = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) { if (entry.isIntersecting) { lightUp(); wordsIO.disconnect(); } });
      }, { threshold: 0.35 });
      wordsIO.observe(statement);
    }
  }

  /* ── Parallax suave en imágenes ──────────────────── */
  var parallaxEls = $$('[data-parallax]');
  if (parallaxEls.length && !reduced) {
    var ticking = false;
    var runParallax = function () {
      var vh = window.innerHeight;
      parallaxEls.forEach(function (el) {
        var rect = el.getBoundingClientRect();
        if (rect.bottom < -200 || rect.top > vh + 200) return;
        var speed = parseFloat(el.getAttribute('data-parallax')) || 0.06;
        var offset = (rect.top + rect.height / 2 - vh / 2) * -speed;
        var img = el.querySelector('img');
        if (img) img.style.transform = 'translate3d(0,' + offset.toFixed(1) + 'px,0) scale(1.08)';
      });
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(runParallax); ticking = true; }
    }, { passive: true });
    window.addEventListener('resize', runParallax);
    runParallax();
  }

  /* ── Acordeón: solo uno abierto a la vez ─────────── */
  var accs = $$('.acc');
  accs.forEach(function (acc) {
    acc.addEventListener('toggle', function () {
      if (!acc.open) return;
      accs.forEach(function (other) { if (other !== acc) other.open = false; });
    });
  });

  /* ── Año en el pie ───────────────────────────────── */
  var year = $('#year');
  if (year) year.textContent = new Date().getFullYear();
})();
