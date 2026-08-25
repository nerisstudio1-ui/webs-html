/* ArTnia — interacciones básicas */
(function () {
  'use strict';

  /* --- Menú móvil --- */
  var btn = document.getElementById('menuBtn');
  var nav = document.getElementById('nav');

  if (btn && nav) {
    btn.addEventListener('click', function () {
      var abierto = nav.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', String(abierto));
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* --- Aparición al hacer scroll --- */
  var elementos = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window)) {
    elementos.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var observer = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (entrada.isIntersecting) {
          entrada.target.classList.add('is-visible');
          observer.unobserve(entrada.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });

    elementos.forEach(function (el) { observer.observe(el); });
  }

  /* --- Año en el pie --- */
  var year = document.getElementById('year');
  if (year) { year.textContent = new Date().getFullYear(); }
})();
