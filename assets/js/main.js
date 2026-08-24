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
    var toggleNav = function (open) {
      nav.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      document.body.classList.toggle('calma-menu-abierto', open);
    };
    burger.addEventListener('click', function () {
      toggleNav(burger.getAttribute('aria-expanded') !== 'true');
    });

    /* El menú se cuelga del final de la página al abrirse. Así ningún
       contenedor del tema puede recortarlo ni desplazarlo fuera de la
       pantalla, que es lo que pasaba dentro de Elementor. */
    var ancla = document.createComment('menu'), refugio = null;
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
      } else if (!movil && refugio && nav.parentNode === refugio) {
        ancla.parentNode.insertBefore(nav, ancla);
        toggleNav(false);
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
