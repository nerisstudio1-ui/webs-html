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

  /* ── Menú móvil ──────────────────────────────────── */
  var burger = $('#burger');
  var nav = $('#nav');
  if (burger && nav) {
    /* El menú se pinta con estilos en línea marcados !important.
       Así se ve igual aunque el CSS llegue tocado: ni el tema de
       WordPress, ni un plugin que comprima el código, ni un widget
       antiguo que siga en la página pueden dejarlo a medias. */
    var ABIERTO = {
      'position':'fixed', 'top':'0', 'right':'0', 'bottom':'0', 'left':'0',
      'width':'100%', 'height':'100%', 'max-width':'none', 'min-width':'0',
      'margin':'0', 'border':'0', 'box-sizing':'border-box',
      'display':'flex', 'flex-direction':'column',
      'align-items':'center', 'justify-content':'center', 'gap':'.4rem',
      'padding':'5.5rem 1.4rem 3rem', 'text-align':'center',
      'background':'#F7F1EA', 'transform':'none',
      'visibility':'visible', 'opacity':'1',
      'z-index':'2147483000', 'overflow-y':'auto'
    };
    var ENLACE = {
      'display':'block', 'width':'100%', 'max-width':'320px',
      'color':'#3F3936', 'background':'none', 'opacity':'1',
      'visibility':'visible', 'text-decoration':'none',
      'font-size':'1rem', 'letter-spacing':'.22em', 'padding':'.95rem 0'
    };
    var CTA = {
      'display':'block', 'width':'100%', 'max-width':'320px',
      'margin-top':'1.8rem', 'color':'#F7F1EA', 'background':'#8E7C70',
      'border-radius':'999px', 'padding':'1.05rem 1.5rem',
      'opacity':'1', 'visibility':'visible', 'text-decoration':'none',
      'font-size':'.78rem', 'letter-spacing':'.18em'
    };
    var forzar  = function (el, p) { for (var k in p) el.style.setProperty(k, p[k], 'important'); };
    var soltar  = function (el, p) { for (var k in p) el.style.removeProperty(k); };
    var esMovil = function () { return window.matchMedia('(max-width:860px)').matches; };
    var enlaces = function () { return $$('a', nav); };

    /* ¿Funciona aquí position:fixed? Muchos temas y plugins de WordPress
       ponen un transform en el body o en un contenedor, y entonces lo
       "fijo" deja de serlo: el menú aparece donde no toca y el botón de
       WhatsApp se queda clavado al final de la página. Lo comprobamos
       midiendo, en vez de darlo por hecho. */
    var fijoVa = function () {
      var t = document.createElement('div');
      t.style.cssText = 'position:fixed;top:0;left:0;width:1px;height:1px;' +
                        'opacity:0;pointer-events:none;margin:0;padding:0;border:0';
      document.body.appendChild(t);
      var r = t.getBoundingClientRect();
      document.body.removeChild(t);
      return Math.abs(r.top) < 2 && Math.abs(r.left) < 2;
    };

    /* Deja el elemento en el punto (x, y) de la PANTALLA sin usar fixed:
       lo pone en 0,0, mide dónde ha caído de verdad y corrige la
       diferencia. Así da igual lo que haya hecho el tema por encima. */
    var anclarEn = function (el, x, y) {
      forzar(el, { 'position':'absolute', 'right':'auto', 'bottom':'auto',
                   'transform':'none', 'top':'0', 'left':'0' });
      var r = el.getBoundingClientRect();
      forzar(el, { 'top': Math.round(y - r.top) + 'px',
                   'left': Math.round(x - r.left) + 'px' });
    };

    var pintar = function () {
      forzar(nav, ABIERTO);
      if (!fijoVa()) {
        /* Plan B: el menú tapa la pantalla igual, pero colocado a mano.
           Como al abrirlo se bloquea el scroll, se queda quieto. */
        forzar(nav, { 'width': window.innerWidth + 'px',
                      'height': window.innerHeight + 'px' });
        anclarEn(nav, 0, 0);
      }
      enlaces().forEach(function (a) {
        forzar(a, a.classList.contains('nav__cta') ? CTA : ENLACE);
      });
      document.body.style.setProperty('overflow', 'hidden', 'important');
    };
    var despintar = function (ocultar) {
      soltar(nav, ABIERTO);
      enlaces().forEach(function (a) { soltar(a, CTA); soltar(a, ENLACE); });
      document.body.style.removeProperty('overflow');
      if (ocultar) nav.style.setProperty('display', 'none', 'important');
    };

    var toggleNav = function (open) {
      nav.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      document.body.classList.toggle('calma-menu-abierto', open);
      if (!esMovil()) { despintar(false); return; }
      if (open) { pintar(); } else { despintar(true); }
    };
    burger.addEventListener('click', function () {
      toggleNav(burger.getAttribute('aria-expanded') !== 'true');
    });

    /* El menú se cuelga del final de la página al abrirse. Así ningún
       contenedor del tema puede recortarlo ni desplazarlo fuera de la
       pantalla, que es lo que pasaba dentro de Elementor. */
    var ancla = document.createComment('menu');
    var anclaBoton = document.createComment('boton');
    var refugio = null;
    var SITIO_BOTON = { 'position':'', 'top':'', 'left':'', 'right':'', 'bottom':'', 'transform':'' };

    /* Si fixed va bien, el botón se queda como está (lo manda el CSS).
       Si no, lo colocamos nosotros y lo recolocamos al hacer scroll. */
    var colocarBoton = function () {
      if (!sticky || !esMovil() || sticky.parentNode !== refugio) return;
      if (fijoVa()) { soltar(sticky, SITIO_BOTON); return; }
      var ancho = sticky.offsetWidth, alto = sticky.offsetHeight;
      anclarEn(sticky, Math.round((window.innerWidth - ancho) / 2),
                       window.innerHeight - alto - 16);
    };
    var pendiente = false;
    window.addEventListener('scroll', function () {
      if (pendiente) return;
      pendiente = true;
      requestAnimationFrame(function () { pendiente = false; colocarBoton(); });
    }, { passive: true });
    window.addEventListener('resize', colocarBoton);
    var moverMenu = function () {
      var movil = window.matchMedia('(max-width:860px)').matches;
      if (movil && nav.parentNode !== refugio) {
        if (!refugio) {
          refugio = document.createElement('div');
          refugio.className = 'calma-web calma-refugio-menu';
          document.body.appendChild(refugio);
        }
        nav.parentNode.insertBefore(ancla, nav);
        refugio.appendChild(nav);
        if (!nav.classList.contains('is-open')) despintar(true);
        if (sticky && sticky.parentNode !== refugio) {
          sticky.parentNode.insertBefore(anclaBoton, sticky);
          refugio.appendChild(sticky);
        }
        colocarBoton();
      } else if (!movil && refugio) {
        if (nav.parentNode === refugio) {
          ancla.parentNode.insertBefore(nav, ancla);
          toggleNav(false);
          despintar(false);
        }
        if (sticky && sticky.parentNode === refugio) {
          anclaBoton.parentNode.insertBefore(sticky, anclaBoton);
          soltar(sticky, SITIO_BOTON);
        }
      }
    };
    moverMenu();
    window.addEventListener('resize', moverMenu);

    /* Se busca dentro del propio menú: para entonces ya se ha mudado
       fuera del contenedor y una búsqueda desde arriba no lo encontraría */
    var cerrar = nav.querySelector('#nav-cerrar, .nav__cerrar');
    if (cerrar) cerrar.addEventListener('click', function (e) {
      e.preventDefault(); toggleNav(false);
    });
    nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') toggleNav(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggleNav(false); });
  }

  /* ── Diagnóstico ─────────────────────────────────────
     Abriendo la web con  #calma-debug  al final de la dirección
     aparece un recuadro con lo que de verdad está pasando en ese
     móvil. Sirve para mandar una captura cuando algo no se ve. */
  if (/calma-debug/.test(location.hash)) {
    var fallos = [];
    window.addEventListener('error', function (e) { fallos.push(e.message); });
    setTimeout(function () {
      var probeta = document.createElement('div');
      probeta.style.cssText = 'position:fixed;top:0;left:0;width:1px;height:1px;opacity:0';
      document.body.appendChild(probeta);
      var pr = probeta.getBoundingClientRect();
      document.body.removeChild(probeta);
      var menu = document.querySelector('.nav');
      var caja = menu ? menu.getBoundingClientRect() : null;
      var culpables = [], el = menu && menu.parentElement;
      while (el) {
        var cs = getComputedStyle(el);
        if (cs.transform !== 'none' || cs.filter !== 'none' ||
            cs.perspective !== 'none' || cs.contain !== 'none')
          culpables.push((el.tagName + '.' + (el.className || '')).slice(0, 40));
        el = el.parentElement;
      }
      var caj = document.querySelectorAll('.calma-web[id]').length;
      var p = document.createElement('pre');
      p.style.cssText = 'position:absolute;top:0;left:0;right:0;z-index:2147483001;' +
        'margin:0;padding:12px;background:#111;color:#0f0;font:11px/1.5 monospace;' +
        'white-space:pre-wrap;word-break:break-all';
      p.textContent = [
        'pantalla   ' + window.innerWidth + 'x' + window.innerHeight,
        'fixed va   ' + (Math.abs(pr.top) < 2 && Math.abs(pr.left) < 2),
        'copias     ' + caj,
        'menu en    ' + (menu ? menu.parentElement.className.slice(0, 40) : 'NO HAY MENU'),
        'menu caja  ' + (caja ? [Math.round(caja.x), Math.round(caja.y),
                                 Math.round(caja.width), Math.round(caja.height)].join(' / ') : '-'),
        'enlaces    ' + (menu ? menu.querySelectorAll('a').length : 0),
        'boton      ' + (document.querySelector('.sticky-book') ? 'si' : 'no'),
        'culpables  ' + (culpables.join(' | ') || 'ninguno'),
        'errores    ' + (fallos.join(' | ') || 'ninguno')
      ].join('\n');
      document.body.appendChild(p);
    }, 900);
  }

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
