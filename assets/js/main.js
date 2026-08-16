/* BELA. Brow Design — interacciones */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Cabecera: sólida al bajar, oculta al alejarse, vuelve al subir --- */
  var header = document.querySelector('.header');
  if (header) {
    var lastY = window.scrollY;
    var onScroll = function () {
      var y = window.scrollY;
      header.classList.toggle('is-solid', y > 24);
      if (!reduced) {
        var bajando = y > lastY && y > 320;
        var menuAbierto = document.querySelector('.mobile-nav.is-open');
        header.classList.toggle('is-hidden', bajando && !menuAbierto);
      }
      lastY = y;
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

  /* --- Pestañas -------------------------------------------------------- */
  document.querySelectorAll('[data-tabs]').forEach(function (tabsRoot) {
    var tabButtons = tabsRoot.querySelectorAll('[role="tab"]');
    tabButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        tabButtons.forEach(function (b) {
          var on = b === btn;
          b.setAttribute('aria-selected', String(on));
          var panel = document.getElementById(b.getAttribute('aria-controls'));
          if (panel) panel.hidden = !on;
        });
      });
    });
  });

  /* --- Antes y después --------------------------------------------------
     El tirador es un input de rango invisible sobre la fotografía: así el
     arrastre, el táctil y el teclado funcionan sin escribir nada de eso. */
  document.querySelectorAll('[data-ba]').forEach(function (frame) {
    var range = frame.querySelector('.ba__range');
    if (!range) return;
    var pintar = function () { frame.style.setProperty('--pos', range.value + '%'); };
    range.addEventListener('input', pintar);
    pintar();
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

  /* --- Profundidad al desplazar ----------------------------------------
     Las imágenes marcadas se mueven algo más despacio que la página. Es un
     efecto sutil: como mucho unas decenas de píxeles. */
  var capas = [].slice.call(document.querySelectorAll('[data-parallax]'));
  if (capas.length && !reduced) {
    var pendiente = false;
    var pintar = function () {
      pendiente = false;
      var alto = window.innerHeight;
      capas.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > alto + 200) return;
        var avance = (r.top + r.height / 2 - alto / 2) / alto;   // -1 … 1
        var fuerza = parseFloat(el.dataset.parallax) || 18;
        el.style.transform = 'translate3d(0,' + (avance * -fuerza).toFixed(1) + 'px,0)';
      });
    };
    var pedir = function () {
      if (pendiente) return;
      pendiente = true;
      requestAnimationFrame(pintar);
    };
    window.addEventListener('scroll', pedir, { passive: true });
    window.addEventListener('resize', pedir);
    pintar();
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
