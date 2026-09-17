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
    actualizarContacto();

    try { localStorage.setItem("idioma", lang); } catch (e) { /* ignorar */ }
  }

  $$(".lang__btn").forEach(function (btn) {
    btn.addEventListener("click", function () { traducir(btn.dataset.lang); });
  });

  /* ------------------------------------------------------------------
     2. WhatsApp
     ------------------------------------------------------------------ */
  /* Pone el número con espacios, como se escribe de toda la vida:
     34645764616 → +34 645 76 46 16 */
  function telefonoLegible(numero) {
    var m = String(numero).match(/^(\d{2})(\d{3})(\d{2})(\d{2})(\d{2})$/);
    return m ? "+" + m[1] + " " + m[2] + " " + m[3] + " " + m[4] + " " + m[5] : "+" + numero;
  }

  function actualizarContacto() {
    var dic = I18N[idiomaActual] || {};
    var texto = encodeURIComponent(dic["wa.mensaje"] || "");
    var url = "https://wa.me/" + CONFIG.whatsapp + (texto ? "?text=" + texto : "");

    var flotante = $("#wa-float");
    if (flotante) flotante.href = url;

    var enlaceWa = $("#wa-link-inline");
    if (enlaceWa) {
      enlaceWa.href = url;
      enlaceWa.textContent = telefonoLegible(CONFIG.whatsapp);
    }

    var enlaceEmail = $("#enlace-email");
    if (enlaceEmail) {
      enlaceEmail.href = "mailto:" + CONFIG.email;
      enlaceEmail.textContent = CONFIG.email;
    }
  }

  /* ------------------------------------------------------------------
     3. Cabecera y menú móvil
     ------------------------------------------------------------------ */
  var header = $("#header");
  var burger = $("#burger");

  var botonWa = $("#wa-float");

  function alScroll() {
    if (header) header.classList.toggle("is-stuck", window.scrollY > 40);
    /* El botón de WhatsApp espera a que se pase la portada */
    if (botonWa) botonWa.classList.toggle("is-visible", window.scrollY > window.innerHeight * 0.6);
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
     9. Vídeos
     ------------------------------------------------------------------
     Hasta que alguien pulsa, en la página solo hay una imagen. Así la
     visita no arrastra megas de vídeo que quizá nadie vea.

     Admite las dos formas: data-src para un archivo propio y data-yt
     para un vídeo de YouTube, por si algún día se enlaza alguno.
     ------------------------------------------------------------------ */
  function reproducir(frame) {
    var propio = frame.dataset.src;
    var yt = frame.dataset.yt;
    var etiqueta = frame.getAttribute("aria-label") || "";

    if (propio) {
      var video = document.createElement("video");
      video.src = propio;
      video.controls = true;
      video.autoplay = true;
      video.playsInline = true;
      video.preload = "auto";
      video.setAttribute("aria-label", etiqueta);
      frame.innerHTML = "";
      frame.appendChild(video);
      video.play().catch(function () { /* si el navegador lo bloquea, queda el control */ });
      return;
    }

    if (yt && yt.indexOf("VIDEO_ID") !== 0) {
      var iframe = document.createElement("iframe");
      iframe.src = "https://www.youtube-nocookie.com/embed/" + yt + "?autoplay=1&rel=0";
      iframe.title = etiqueta;
      iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      iframe.allowFullscreen = true;
      frame.innerHTML = "";
      frame.appendChild(iframe);
    }
  }

  $$(".video__frame").forEach(function (frame) {
    frame.addEventListener("click", function () { reproducir(frame); }, { once: true });
  });

  /* Fondo en movimiento de la portada.
     No se descarga hasta que hace falta, y no se reproduce si el sistema
     pide menos animación ni si el navegador dice que la conexión va justa
     o el usuario pidió ahorrar datos. En esos casos se queda el póster,
     que ya es una imagen del propio vídeo. */
  (function () {
    var fondo = $("#portada-fondo");
    if (!fondo) return;

    var menosMovimiento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var con = navigator.connection || {};
    var conexionJusta = con.saveData === true || /2g/.test(con.effectiveType || "");
    if (menosMovimiento || conexionJusta || !("IntersectionObserver" in window)) return;

    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) {
          fondo.preload = "auto";
          fondo.play().catch(function () { /* sin autoplay, se queda el póster */ });
        } else if (!fondo.paused) {
          fondo.pause();
        }
      });
    }, { rootMargin: "200px" });

    obs.observe(fondo);
  })();

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
     11. Ancho real de la ventana
     ------------------------------------------------------------------
     Solo hace falta cuando la web va incrustada en otra página, como en
     un bloque de WordPress: allí el CSS la saca a todo lo ancho y
     necesita saber cuánto mide la ventana sin la barra de
     desplazamiento. Suelto en su propia página no molesta.
     ------------------------------------------------------------------ */
  (function () {
    var raiz = document.getElementById("cfm-web");
    if (!raiz) return;

    function medir() {
      raiz.style.setProperty("--ancho-real", document.documentElement.clientWidth + "px");
    }
    medir();
    window.addEventListener("resize", medir, { passive: true });
    window.addEventListener("orientationchange", medir);
  })();

  /* ------------------------------------------------------------------
     12. Año del pie
     ------------------------------------------------------------------ */
  var year = $("#year");
  if (year) year.textContent = String(new Date().getFullYear());

  /* ------------------------------------------------------------------
     13. Arranque
     ------------------------------------------------------------------ */
  traducir(idiomaInicial());

})();
