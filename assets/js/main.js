/* ==========================================================================
   main.js — comportamiento de la web
   ========================================================================== */
(function () {
  "use strict";

  var CONFIG = window.CONFIG || {};
  var I18N = window.I18N || {};
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ------------------------------------------------------------------
     1. Idioma
     ------------------------------------------------------------------ */
  var idiomaActual = CONFIG.idiomaPorDefecto || "es";

  function idiomaInicial() {
    var url = new URLSearchParams(location.search).get("lang");
    if (url && I18N[url]) return url;
    try {
      var guardado = localStorage.getItem("idioma");
      if (guardado && I18N[guardado]) return guardado;
    } catch (e) { /* navegación privada */ }
    var nav = (navigator.language || "es").slice(0, 2);
    return I18N[nav] ? nav : (CONFIG.idiomaPorDefecto || "es");
  }

  function traducir(lang) {
    var dic = I18N[lang];
    if (!dic) return;
    idiomaActual = lang;

    document.documentElement.lang = lang;

    $$("[data-i18n]").forEach(function (el) {
      var t = dic[el.dataset.i18n];
      if (t != null) el.textContent = t;
    });

    $$("[data-i18n-html]").forEach(function (el) {
      var t = dic[el.dataset.i18nHtml];
      if (t != null) el.innerHTML = t;
    });

    /* data-i18n-attr="alt:clave" o varios separados por coma */
    $$("[data-i18n-attr]").forEach(function (el) {
      el.dataset.i18nAttr.split(",").forEach(function (par) {
        var trozos = par.split(":");
        var attr = trozos[0].trim();
        var clave = (trozos[1] || "").trim();
        if (dic[clave] != null) el.setAttribute(attr, dic[clave]);
      });
    });

    $$(".lang__btn").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang));
    });

    pintarMarquesina();
    actualizarWhatsApp();

    try { localStorage.setItem("idioma", lang); } catch (e) { /* ignorar */ }
  }

  $$(".lang__btn").forEach(function (btn) {
    btn.addEventListener("click", function () { traducir(btn.dataset.lang); });
  });

  /* ------------------------------------------------------------------
     2. WhatsApp
     ------------------------------------------------------------------ */
  function actualizarWhatsApp() {
    var dic = I18N[idiomaActual] || {};
    var texto = encodeURIComponent(dic["wa.mensaje"] || "");
    var url = "https://wa.me/" + CONFIG.whatsapp + (texto ? "?text=" + texto : "");
    var flotante = $("#wa-float");
    var enlace = $("#wa-link-inline");
    if (flotante) flotante.href = url;
    if (enlace) enlace.href = url;
  }

  /* ------------------------------------------------------------------
     3. Cabecera y menú móvil
     ------------------------------------------------------------------ */
  var header = $("#header");
  var burger = $("#burger");

  function alScroll() {
    if (header) header.classList.toggle("is-stuck", window.scrollY > 40);
  }
  window.addEventListener("scroll", alScroll, { passive: true });
  alScroll();

  function cerrarMenu() {
    document.body.classList.remove("nav-open");
    if (burger) {
      burger.setAttribute("aria-expanded", "false");
      burger.setAttribute("aria-label", (I18N[idiomaActual] || {})["nav.abrir"] || "Abrir menú");
    }
  }

  if (burger) {
    burger.addEventListener("click", function () {
      var abierto = document.body.classList.toggle("nav-open");
      burger.setAttribute("aria-expanded", String(abierto));
      var dic = I18N[idiomaActual] || {};
      burger.setAttribute("aria-label", abierto ? (dic["nav.cerrar"] || "Cerrar menú") : (dic["nav.abrir"] || "Abrir menú"));
    });
  }

  $$(".nav__link").forEach(function (a) {
    a.addEventListener("click", cerrarMenu);
  });

  /* ------------------------------------------------------------------
     4. Enlace activo según la sección visible
     ------------------------------------------------------------------ */
  var secciones = $$("main section[id]");
  var enlaces = {};
  $$(".nav__link").forEach(function (a) {
    enlaces[a.getAttribute("href").slice(1)] = a;
  });

  if ("IntersectionObserver" in window && secciones.length) {
    var obsNav = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        var a = enlaces[e.target.id];
        if (a) a.setAttribute("aria-current", e.isIntersecting ? "true" : "false");
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    secciones.forEach(function (s) { obsNav.observe(s); });
  }

  /* ------------------------------------------------------------------
     5. Animaciones de entrada
     ------------------------------------------------------------------ */
  var reveals = $$(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var obsReveal = new IntersectionObserver(function (entradas, obs) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("is-visible");
          obs.unobserve(e.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { obsReveal.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ------------------------------------------------------------------
     6. Marquesina
     ------------------------------------------------------------------ */
  function pintarMarquesina() {
    var pista = $("#marquee");
    if (!pista) return;
    var dic = I18N[idiomaActual] || {};
    var palabras = [dic["marquee.1"] || "Poesía", dic["marquee.2"] || "Literatura infantil"];
    var html = "";
    /* Se duplica el contenido para que el bucle sea continuo (-50%) */
    for (var i = 0; i < 8; i++) {
      html += '<span class="marquee__item">' + palabras[i % 2] + "</span>";
    }
    pista.innerHTML = html;
  }

  /* ------------------------------------------------------------------
     7. Pestañas de obra publicada
     ------------------------------------------------------------------ */
  var tabs = $$(".tab");
  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      tabs.forEach(function (t) {
        var activo = t === tab;
        t.setAttribute("aria-selected", String(activo));
        var panel = document.getElementById(t.getAttribute("aria-controls"));
        if (panel) {
          panel.hidden = !activo;
          if (activo) {
            $$(".reveal", panel).forEach(function (el) { el.classList.add("is-visible"); });
          }
        }
      });
    });

    tab.addEventListener("keydown", function (e) {
      if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
      var i = tabs.indexOf(tab);
      var siguiente = tabs[(i + (e.key === "ArrowRight" ? 1 : tabs.length - 1)) % tabs.length];
      siguiente.focus();
      siguiente.click();
    });
  });

  /* ------------------------------------------------------------------
     8. Galería con lightbox
     ------------------------------------------------------------------ */
  var items = $$(".galeria__item");
  var lb = $("#lightbox");
  var lbImg = $("#lb-img");
  var indice = 0;
  var ultimoFoco = null;

  function abrirLB(i) {
    if (!lb || !items.length) return;
    indice = (i + items.length) % items.length;
    var img = items[indice].querySelector("img");
    lbImg.src = img.currentSrc || img.src;
    lbImg.alt = img.alt || (I18N[idiomaActual] || {})["galeria.alt"] || "";
    lb.classList.add("is-open");
    lb.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    $("#lb-close").focus();
  }

  function cerrarLB() {
    if (!lb) return;
    lb.classList.remove("is-open");
    lb.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (ultimoFoco) ultimoFoco.focus();
  }

  items.forEach(function (item, i) {
    item.addEventListener("click", function () {
      ultimoFoco = item;
      abrirLB(i);
    });
  });

  if (lb) {
    $("#lb-close").addEventListener("click", cerrarLB);
    $("#lb-prev").addEventListener("click", function (e) { e.stopPropagation(); abrirLB(indice - 1); });
    $("#lb-next").addEventListener("click", function (e) { e.stopPropagation(); abrirLB(indice + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) cerrarLB(); });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      if (lb && lb.classList.contains("is-open")) cerrarLB();
      if (document.body.classList.contains("nav-open")) cerrarMenu();
    }
    if (lb && lb.classList.contains("is-open")) {
      if (e.key === "ArrowLeft")  abrirLB(indice - 1);
      if (e.key === "ArrowRight") abrirLB(indice + 1);
    }
  });

  /* ------------------------------------------------------------------
     9. Vídeos — la miniatura carga el iframe solo al pulsar
         (así la web no arrastra el peso de YouTube en cada visita)
     ------------------------------------------------------------------ */
  $$(".video__frame").forEach(function (frame) {
    frame.addEventListener("click", function () {
      var id = frame.dataset.yt;
      if (!id || id.indexOf("VIDEO_ID") === 0) return;
      var iframe = document.createElement("iframe");
      iframe.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      iframe.title = frame.getAttribute("aria-label") || "";
      iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      iframe.allowFullscreen = true;
      frame.innerHTML = "";
      frame.appendChild(iframe);
    });
  });

  /* ------------------------------------------------------------------
     10. Formulario de contacto
     ------------------------------------------------------------------ */
  var form = $("#form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var dic = I18N[idiomaActual] || {};
      var estado = $("#form-status");
      var boton = $("#form-submit");

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      boton.disabled = true;
      boton.textContent = dic["form.enviando"] || "Enviando…";
      estado.className = "form__status";

      var datos = {};
      new FormData(form).forEach(function (v, k) { datos[k] = v; });
      datos._subject = "Nuevo mensaje desde la web — " + (datos.Asunto || datos.Nombre || "");
      datos._captcha = "false";

      fetch(CONFIG.formEndpoint + CONFIG.email, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(datos)
      })
        .then(function (r) {
          if (!r.ok) throw new Error("HTTP " + r.status);
          return r.json();
        })
        .then(function () {
          estado.className = "form__status is-visible is-ok";
          estado.textContent = dic["form.ok"] || "Mensaje enviado.";
          form.reset();
        })
        .catch(function () {
          estado.className = "form__status is-visible is-err";
          estado.textContent = dic["form.error"] || "No se ha podido enviar.";
        })
        .then(function () {
          boton.disabled = false;
          boton.textContent = dic["form.enviar"] || "Enviar mensaje";
        });
    });
  }

  /* ------------------------------------------------------------------
     11. Año del pie
     ------------------------------------------------------------------ */
  var year = $("#year");
  if (year) year.textContent = String(new Date().getFullYear());

  /* ------------------------------------------------------------------
     12. Arranque
     ------------------------------------------------------------------ */
  traducir(idiomaInicial());

})();
