/* ═══════════════════════════════════════════════
   CALMA · barre studio — interacciones
   Sin dependencias. Todo respeta prefers-reduced-motion.
   ═══════════════════════════════════════════════ */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ── Header pegajoso ─────────────────────────── */
  var header = $('#header');
  var onScroll = function () {
    header.classList.toggle('is-stuck', window.scrollY > 24);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Menú móvil ──────────────────────────────── */
  var burger = $('#burger');
  var nav = $('#nav');
  if (burger && nav) {
    var toggleNav = function (open) {
      nav.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      document.body.classList.toggle('nav-open', open);
    };
    burger.addEventListener('click', function () {
      toggleNav(burger.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') toggleNav(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') toggleNav(false);
    });
  }

  /* ── Apariciones al hacer scroll ─────────────── */
  var revealables = $$('.reveal').concat($$('.hero__title'));
  if (!('IntersectionObserver' in window) || reduced) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ── Frase que se ilumina palabra a palabra ──── */
  var statement = $('[data-words]');
  if (statement) {
    var words = statement.textContent.trim().split(/\s+/);
    statement.textContent = '';
    words.forEach(function (word, i) {
      var span = document.createElement('span');
      span.className = 'w';
      span.textContent = word;
      span.style.transitionDelay = (i * 0.035) + 's';
      statement.appendChild(span);
      statement.appendChild(document.createTextNode(' '));
    });
    if (reduced || !('IntersectionObserver' in window)) {
      $$('.w', statement).forEach(function (w) { w.classList.add('is-lit'); });
    } else {
      var wordsIO = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            $$('.w', statement).forEach(function (w) { w.classList.add('is-lit'); });
            wordsIO.disconnect();
          }
        });
      }, { threshold: 0.4 });
      wordsIO.observe(statement);
    }
  }

  /* ── Parallax suave en imágenes ──────────────── */
  var parallaxEls = $$('[data-parallax]');
  if (parallaxEls.length && !reduced) {
    var ticking = false;
    var runParallax = function () {
      var vh = window.innerHeight;
      parallaxEls.forEach(function (el) {
        var rect = el.getBoundingClientRect();
        if (rect.bottom < -200 || rect.top > vh + 200) return;
        var speed = parseFloat(el.getAttribute('data-parallax')) || 0.08;
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

  /* ── Horarios por día ────────────────────────── */
  var dayBtns = $$('.days .chip');
  var scheds = $$('#schedule .sched');
  dayBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var day = btn.getAttribute('data-day');
      dayBtns.forEach(function (b) {
        var active = b === btn;
        b.classList.toggle('is-active', active);
        b.setAttribute('aria-selected', String(active));
      });
      scheds.forEach(function (s) {
        var show = s.getAttribute('data-day') === day;
        s.hidden = !show;
        if (show) { s.style.animation = 'none'; void s.offsetWidth; s.style.animation = ''; }
      });
    });
  });

  /* Abre el día actual al cargar (lunes–sábado) */
  var todayKey = ['dom', 'lun', 'mar', 'mie', 'jue', 'vie', 'sab'][new Date().getDay()];
  var todayBtn = $('.days .chip[data-day="' + todayKey + '"]');
  if (todayBtn && !reduced) todayBtn.click();

  /* ── Acordeón: solo uno abierto a la vez ─────── */
  var accs = $$('.acc');
  accs.forEach(function (acc) {
    acc.addEventListener('toggle', function () {
      if (!acc.open) return;
      accs.forEach(function (other) { if (other !== acc) other.open = false; });
    });
  });

  /* ── Formulario → correo ─────────────────────── */
  var form = $('#booking-form');
  var status = $('#form-status');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var data = new FormData(form);
      var nombre = (data.get('Nombre') || '').toString().trim();
      var cuerpo = [
        'Nombre: ' + (data.get('Nombre') || ''),
        'Email: ' + (data.get('Email') || ''),
        'Teléfono: ' + (data.get('Telefono') || '—'),
        'Clase de interés: ' + (data.get('Clase') || ''),
        '',
        'Mensaje:',
        (data.get('Mensaje') || '—')
      ].join('\n');

      var href = 'mailto:Calma.barrestudio@gmail.com'
        + '?subject=' + encodeURIComponent('Reserva de clase — ' + (nombre || 'web CALMA'))
        + '&body=' + encodeURIComponent(cuerpo);

      window.location.href = href;
      if (status) {
        status.textContent = 'Abriendo tu gestor de correo… Si no se abre, escríbenos a Calma.barrestudio@gmail.com';
      }
    });
  }

  /* ── Año en el pie ───────────────────────────── */
  var year = $('#year');
  if (year) year.textContent = new Date().getFullYear();
})();
