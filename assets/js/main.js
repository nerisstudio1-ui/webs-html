/* BELA. Brow Design — interacciones */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Header sólido al hacer scroll ---------------------------------- */
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-solid', window.scrollY > 24);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* --- Menú móvil ------------------------------------------------------ */
  var burger = document.querySelector('[data-burger]');
  var mobileNav = document.querySelector('.mobile-nav');
  if (burger && mobileNav) {
    var toggleNav = function (open) {
      mobileNav.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', function () {
      toggleNav(!mobileNav.classList.contains('is-open'));
    });
    mobileNav.querySelectorAll('a, [data-close]').forEach(function (el) {
      el.addEventListener('click', function () { toggleNav(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') toggleNav(false);
    });
  }

  /* --- Barra de anuncios ---------------------------------------------- */
  var announce = document.querySelector('[data-announce]');
  if (announce) {
    var items = announce.querySelectorAll('.announce-item');
    var idx = 0;
    var show = function (n) {
      idx = (n + items.length) % items.length;
      items.forEach(function (it, i) { it.classList.toggle('is-active', i === idx); });
    };
    announce.querySelectorAll('[data-announce-step]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        show(idx + Number(btn.dataset.announceStep));
      });
    });
    show(0);
    if (!reduced && items.length > 1) setInterval(function () { show(idx + 1); }, 6000);
  }

  /* --- Hero: slideshow del panel derecho ------------------------------- */
  var hero = document.querySelector('[data-hero]');
  if (hero) {
    var slides = hero.querySelectorAll('.hero__slide');
    var dots = hero.querySelectorAll('.hero__dots button');
    var pauseBtn = hero.querySelector('.hero__pause');
    var current = 0;
    var timer = null;

    var go = function (n) {
      current = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle('is-active', i === current); });
      dots.forEach(function (d, i) { d.setAttribute('aria-selected', String(i === current)); });
    };
    var start = function () {
      if (reduced || timer) return;
      timer = setInterval(function () { go(current + 1); }, 6000);
      if (pauseBtn) pauseBtn.setAttribute('aria-pressed', 'false');
    };
    var stop = function () {
      clearInterval(timer); timer = null;
      if (pauseBtn) pauseBtn.setAttribute('aria-pressed', 'true');
    };

    dots.forEach(function (d, i) {
      d.addEventListener('click', function () { go(i); stop(); start(); });
    });
    if (pauseBtn) {
      pauseBtn.addEventListener('click', function () { timer ? stop() : start(); });
    }
    go(0);
    start();
  }

  /* --- Pestañas + carrusel de tratamientos ----------------------------- */
  var tabsRoot = document.querySelector('[data-tabs]');
  if (tabsRoot) {
    var tabButtons = tabsRoot.querySelectorAll('[role="tab"]');
    tabButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        tabButtons.forEach(function (b) {
          var on = b === btn;
          b.setAttribute('aria-selected', String(on));
          var panel = document.getElementById(b.getAttribute('aria-controls'));
          if (panel) panel.hidden = !on;
        });
        var active = document.getElementById(btn.getAttribute('aria-controls'));
        if (active) updateProgress(active);
      });
    });
  }

  function updateProgress(rail) {
    var bar = rail.parentElement && rail.parentElement.querySelector('.progress span');
    if (!bar) return;
    var max = rail.scrollWidth - rail.clientWidth;
    var ratio = rail.clientWidth / rail.scrollWidth;
    var width = Math.max(ratio, 0.15) * 100;
    var pos = max > 0 ? (rail.scrollLeft / max) * (100 - width) : 0;
    bar.style.width = width + '%';
    bar.style.transform = 'translateX(' + (pos / width) * 100 + '%)';
  }

  document.querySelectorAll('.rail').forEach(function (rail) {
    updateProgress(rail);
    rail.addEventListener('scroll', function () { updateProgress(rail); }, { passive: true });
    window.addEventListener('resize', function () { updateProgress(rail); });
  });

  /* --- FAQ (acordeón accesible) ---------------------------------------- */
  document.querySelectorAll('.faq__q').forEach(function (q) {
    var panel = document.getElementById(q.getAttribute('aria-controls'));
    if (!panel) return;
    q.addEventListener('click', function () {
      var open = q.getAttribute('aria-expanded') === 'true';
      q.setAttribute('aria-expanded', String(!open));
      panel.style.height = open ? '0px' : panel.scrollHeight + 'px';
    });
  });

  /* --- Reveal al entrar en viewport ------------------------------------ */
  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length) {
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
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* --- Newsletter (demostración, sin backend) --------------------------- */
  document.querySelectorAll('[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      if (status) status.textContent = 'Gracias, ya estás dentro ✦';
      form.reset();
    });
  });

  /* --- Formulario de cita ------------------------------------------------
     Sin servidor detrás: compone la solicitud y la abre en WhatsApp o en el
     gestor de correo con todo escrito. Al contratar hosting basta con
     sustituir este bloque por el envío real al backend.                    */
  var WHATSAPP = '34611599132';
  /* Cuando exista el correo profesional del estudio, ponerlo aquí: el botón
     «enviar por email» del formulario aparece solo si esta constante existe. */
  var EMAIL = '';

  document.querySelectorAll('[data-contact-form]').forEach(function (form) {
    var status = form.querySelector('.form-status');

    function collect() {
      var get = function (id) {
        var el = form.querySelector('#' + id);
        return el ? el.value.trim() : '';
      };
      var lines = [
        'Hola Bela, me gustaría pedir cita.',
        '',
        'Nombre: ' + get('nombre'),
        'Teléfono: ' + get('telefono')
      ];
      if (get('email')) lines.push('Email: ' + get('email'));
      lines.push('Tratamiento: ' + get('tratamiento'));
      lines.push('Disponibilidad: ' + get('franja'));
      if (get('mensaje')) lines.push('', get('mensaje'));
      return lines.join('\n');
    }

    function ready() {
      if (form.reportValidity && !form.reportValidity()) return false;
      return true;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      window.open('https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(collect()), '_blank', 'noopener');
      if (status) status.textContent = 'Abriendo WhatsApp con tu solicitud ✦';
    });

    var mailBtn = form.querySelector('[data-send-email]');
    if (mailBtn && !EMAIL) {
      mailBtn.hidden = true;
    } else if (mailBtn) {
      mailBtn.addEventListener('click', function () {
        if (!ready()) return;
        window.location.href = 'mailto:' + EMAIL +
          '?subject=' + encodeURIComponent('Solicitud de cita — web') +
          '&body=' + encodeURIComponent(collect());
        if (status) status.textContent = 'Abriendo tu gestor de correo ✦';
      });
    }
  });

  /* --- Año en el footer -------------------------------------------------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
