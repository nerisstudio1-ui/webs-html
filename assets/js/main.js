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

  /* --- Fila de tratamientos: se arrastra con el ratón --------------------
     En táctil el navegador ya lo hace solo; esto es para el escritorio, más
     la barra de abajo que dice por dónde vas. */
  document.querySelectorAll('[data-rail]').forEach(function (rail) {
    var barra = rail.parentNode.querySelector('.rail-bar span');

    var pintarBarra = function () {
      if (!barra) return;
      var recorrido = rail.scrollWidth - rail.clientWidth;
      var visible = rail.clientWidth / rail.scrollWidth;
      barra.style.width = (visible * 100).toFixed(1) + '%';
      var avance = recorrido > 0 ? rail.scrollLeft / recorrido : 0;
      barra.style.transform = 'translateX(' + (avance * (1 / visible - 1) * 100).toFixed(1) + '%)';
    };
    rail.addEventListener('scroll', pintarBarra, { passive: true });
    window.addEventListener('resize', pintarBarra);
    pintarBarra();

    var arrastrando = false, desdeX = 0, desdeScroll = 0, movido = 0;
    rail.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'touch') return;
      arrastrando = true; movido = 0;
      desdeX = e.clientX; desdeScroll = rail.scrollLeft;
      rail.setPointerCapture(e.pointerId);
    });
    rail.addEventListener('pointermove', function (e) {
      if (!arrastrando) return;
      var dx = e.clientX - desdeX;
      movido = Math.max(movido, Math.abs(dx));
      if (movido > 4) rail.classList.add('is-dragging');
      rail.scrollLeft = desdeScroll - dx;
    });
    var soltar = function () {
      arrastrando = false;
      /* el clic se rehabilita después, para que arrastrar no abra el enlace */
      setTimeout(function () { rail.classList.remove('is-dragging'); }, 0);
    };
    rail.addEventListener('pointerup', soltar);
    rail.addEventListener('pointercancel', soltar);
  });

  /* --- El método: se enciende el paso que estás leyendo ------------------- */
  var pin = document.querySelector('[data-pin]');
  if (pin) {
    var pasos = [].slice.call(pin.querySelectorAll('.pin__step'));
    if (pasos.length) {
      if (reduced || !('IntersectionObserver' in window)) {
        pasos.forEach(function (el) { el.classList.add('is-on'); });
      } else {
        var ioPasos = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            entry.target.classList.toggle('is-on', entry.isIntersecting);
          });
        }, { rootMargin: '-35% 0px -35% 0px' });
        pasos.forEach(function (el) { ioPasos.observe(el); });
      }
    }
  }

  /* --- La franja de marca sigue al desplazamiento -------------------------
     Al bajar acelera y va hacia la izquierda; al subir, al revés. Parada, se
     queda a su velocidad de crucero. */
  var franja = document.querySelector('.marquee__track');
  if (franja && !reduced) {
    var ultimaY = window.scrollY, empuje = 0, velocidad = 0, x = 0, previo = 0;
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      empuje = Math.max(-28, Math.min(28, (y - ultimaY) * .55));
      ultimaY = y;
    }, { passive: true });

    var mitad = 0;
    var medir = function () { mitad = franja.scrollWidth / 2; };
    medir();
    window.addEventListener('resize', medir);

    var animar = function (ahora) {
      var dt = previo ? Math.min(64, ahora - previo) : 16;
      previo = ahora;
      velocidad += (empuje - velocidad) * .08;
      empuje *= .9;
      x -= (1.1 + velocidad) * (dt / 16);
      if (mitad) {
        if (x <= -mitad) x += mitad;
        if (x > 0) x -= mitad;
      }
      franja.style.transform = 'translate3d(' + x.toFixed(1) + 'px,0,0)';
      requestAnimationFrame(animar);
    };
    franja.style.animation = 'none';
    requestAnimationFrame(animar);
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
