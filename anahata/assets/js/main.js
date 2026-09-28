/* =========================================================
   ANAHATA · Interacciones
   Sin dependencias externas.
   ========================================================= */
(function () {
  'use strict';

  /* ---- Aviso superior (recordar cierre) ---- */
  var aviso = document.querySelector('[data-aviso]');
  if (aviso) {
    try {
      if (localStorage.getItem('anahata-aviso') === 'cerrado') aviso.hidden = true;
    } catch (e) { /* almacenamiento no disponible */ }
    var cerrar = aviso.querySelector('[data-cerrar-aviso]');
    if (cerrar) {
      cerrar.addEventListener('click', function () {
        aviso.hidden = true;
        try { localStorage.setItem('anahata-aviso', 'cerrado'); } catch (e) {}
      });
    }
  }

  /* ---- Cabecera: fondo sólido al hacer scroll ---- */
  var cabecera = document.querySelector('[data-cabecera]');
  if (cabecera) {
    var alFijar = function () {
      cabecera.classList.toggle('is-fija', window.scrollY > 40);
    };
    alFijar();
    window.addEventListener('scroll', alFijar, { passive: true });
  }

  /* ---- Altura real de la cabecera (para encajar el hero) ---- */
  if (cabecera) {
    var medirCabecera = function () {
      document.documentElement.style.setProperty('--header-h', cabecera.offsetHeight + 'px');
    };
    medirCabecera();
    window.addEventListener('resize', medirCabecera);
    window.addEventListener('load', medirCabecera);
  }

  /* ---- Menú móvil ---- */
  var boton = document.querySelector('[data-menu-boton]');
  var menu = document.querySelector('[data-menu]');
  if (boton && menu) {
    var alternarMenu = function (abrir) {
      var visible = abrir !== undefined ? abrir : !menu.classList.contains('is-abierto');
      menu.classList.toggle('is-abierto', visible);
      document.body.classList.toggle('menu-abierto', visible);
      document.body.style.overflow = visible ? 'hidden' : '';
      boton.setAttribute('aria-expanded', String(visible));
    };
    boton.addEventListener('click', function () { alternarMenu(); });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { alternarMenu(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-abierto')) alternarMenu(false);
    });
  }

  /* ---- Revelado al hacer scroll ---- */
  var revelables = document.querySelectorAll('.revelar');
  if (revelables.length) {
    if ('IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (entrada) {
          if (!entrada.isIntersecting) return;
          var el = entrada.target;
          var retardo = parseInt(el.getAttribute('data-retardo') || '0', 10);
          setTimeout(function () { el.classList.add('is-visible'); }, retardo);
          obs.unobserve(el);
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
      revelables.forEach(function (el) { obs.observe(el); });
    } else {
      revelables.forEach(function (el) { el.classList.add('is-visible'); });
    }
  }

  /* ---- Acordeón ---- */
  document.querySelectorAll('[data-acordeon] .acordeon__boton').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.acordeon__item');
      var abierto = item.classList.contains('is-abierto');
      var grupo = btn.closest('[data-acordeon]');
      grupo.querySelectorAll('.acordeon__item').forEach(function (otro) {
        otro.classList.remove('is-abierto');
        otro.querySelector('.acordeon__boton').setAttribute('aria-expanded', 'false');
      });
      if (!abierto) {
        item.classList.add('is-abierto');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---- Carrusel de testimonios ---- */
  document.querySelectorAll('[data-carrusel]').forEach(function (carrusel) {
    var pista = carrusel.querySelector('.testimonios');
    var anterior = carrusel.querySelector('[data-carrusel-anterior]');
    var siguiente = carrusel.querySelector('[data-carrusel-siguiente]');
    if (!pista) return;
    var paso = function () {
      var primera = pista.querySelector('.testimonio');
      return primera ? primera.getBoundingClientRect().width + 26 : 320;
    };
    if (anterior) anterior.addEventListener('click', function () {
      pista.scrollBy({ left: -paso(), behavior: 'smooth' });
    });
    if (siguiente) siguiente.addEventListener('click', function () {
      pista.scrollBy({ left: paso(), behavior: 'smooth' });
    });
  });

  /* ---- Formularios ---- */
  document.querySelectorAll('form[data-formulario]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      var aviso = form.querySelector('[data-aviso-form]');
      // Sin destino configurado no se envía a ninguna parte: mejor avisar
      // que dejar creer al visitante que su mensaje ha salido.
      if (!form.getAttribute('action')) {
        e.preventDefault();
        if (aviso) {
          aviso.textContent = 'El formulario todavía no está conectado. Escríbenos a saravgyoga@gmail.com o por WhatsApp.';
          aviso.hidden = false;
        }
        return;
      }
      // El navegador ya valida los campos obligatorios; si falla, no bloqueamos
      // el botón, porque el formulario no llega a enviarse.
      if (form.checkValidity && !form.checkValidity()) return;
      var boton = form.querySelector('button[type="submit"]');
      if (boton) { boton.disabled = true; boton.textContent = 'Enviando…'; }
    });
  });

  /* ---- Vídeo de portada ----
     Se carga también en móvil. Se respeta el ahorro de datos, las conexiones
     lentas y la preferencia de movimiento reducido: en esos casos se queda
     la fotografía, que pesa mucho menos. */
  var video = document.querySelector('[data-video]');
  if (video) {
    var conexion = navigator.connection || {};
    var puede = !window.matchMedia('(prefers-reduced-motion: reduce)').matches &&
                !conexion.saveData &&
                !/^(slow-2g|2g)$/.test(conexion.effectiveType || '');
    if (puede) {
      video.addEventListener('canplay', function () { video.classList.add('is-visible'); });
      video.addEventListener('error', function () { video.remove(); });
      video.src = video.getAttribute('data-video');
      video.load();
      var intento = video.play();
      if (intento && intento.catch) intento.catch(function () { video.remove(); });
    }
  }

  /* ---- Resultado del envío ----
     enviar.php devuelve a la web con ?envio=ok o ?envio=error */
  var resultado = new URLSearchParams(window.location.search).get('envio');
  if (resultado === 'ok' || resultado === 'error') {
    var cartel = document.querySelector('[data-envio="' + resultado + '"]');
    if (cartel) {
      cartel.hidden = false;
      cartel.setAttribute('role', 'status');
      cartel.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    // Limpiamos la dirección: al recargar no debe reaparecer el aviso
    if (window.history.replaceState) {
      window.history.replaceState({}, '', window.location.pathname + window.location.hash);
    }
  }

  /* ---- Año actual en el pie ---- */
  document.querySelectorAll('[data-anio]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
