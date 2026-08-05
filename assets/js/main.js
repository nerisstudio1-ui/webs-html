/* Laconic Studio — interacciones básicas (sin dependencias) */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Header: fondo al hacer scroll + auto-ocultar ---- */
  var header = document.querySelector(".header");
  if (header) {
    var lastY = window.scrollY;
    var onScroll = function () {
      var y = window.scrollY;
      header.classList.toggle("is-stuck", y > 40);
      var goingDown = y > lastY && y > 320;
      if (!document.body.classList.contains("menu-open")) {
        header.classList.toggle("is-hidden", goingDown);
      }
      lastY = y;
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---- Menú móvil ---- */
  var burger = document.querySelector(".burger");
  var menu = document.querySelector(".mobile-menu");
  if (burger && menu) {
    var setMenu = function (open) {
      document.body.classList.toggle("menu-open", open);
      burger.setAttribute("aria-expanded", String(open));
      menu.setAttribute("aria-hidden", String(!open));
      document.documentElement.style.overflow = open ? "hidden" : "";
    };
    burger.addEventListener("click", function () {
      setMenu(!document.body.classList.contains("menu-open"));
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("menu-open")) {
        setMenu(false);
        burger.focus();
      }
    });
    setMenu(false);
  }

  /* ---- Reveal al entrar en viewport ---- */
  var revealables = document.querySelectorAll(".reveal");
  if (revealables.length) {
    if (reduced || !("IntersectionObserver" in window)) {
      revealables.forEach(function (el) {
        el.classList.add("is-in");
      });
    } else {
      var io = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-in");
              io.unobserve(entry.target);
            }
          });
        },
        { rootMargin: "0px 0px -10% 0px", threshold: 0 }
      );
      revealables.forEach(function (el) {
        io.observe(el);
      });
    }
  }

  /* ---- Hero: collage que sube con el scroll ----
     Escribe --p (0 → 1) en la sección; el CSS decide cuánto sube cada pieza. */
  var collage = document.querySelector("[data-collage]");
  if (collage && !reduced) {
    var ticking = false;
    var setProgress = function () {
      var travel = collage.offsetHeight - window.innerHeight;
      var scrolled = window.scrollY - collage.offsetTop;
      var p = travel > 0 ? scrolled / travel : 1;
      collage.style.setProperty("--p", Math.min(1, Math.max(0, p)).toFixed(4));
      ticking = false;
    };
    var request = function () {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(setProgress);
      }
    };
    window.addEventListener("scroll", request, { passive: true });
    window.addEventListener("resize", request);
    setProgress();
  } else if (collage) {
    collage.style.setProperty("--p", "1");
  }

  /* ---- Marquee: duplicar contenido para bucle continuo ---- */
  document.querySelectorAll(".marquee__track").forEach(function (track) {
    track.innerHTML += track.innerHTML;
  });

  /* ---- Año en el footer ---- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---- Formulario de contacto: sin backend, abre el correo ---- */
  var form = document.querySelector("[data-mailto]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var servicios = data.getAll("servicio").join(", ") || "Sin especificar";
      var body = [
        "Nombre: " + (data.get("nombre") || ""),
        "Marca: " + (data.get("marca") || ""),
        "Email: " + (data.get("email") || ""),
        "Servicios: " + servicios,
        "Presupuesto: " + (data.get("presupuesto") || ""),
        "",
        "Cuéntanos:",
        data.get("mensaje") || ""
      ].join("\n");

      var href =
        "mailto:" +
        form.getAttribute("data-mailto") +
        "?subject=" +
        encodeURIComponent("Nuevo proyecto — " + (data.get("marca") || data.get("nombre") || "Laconic")) +
        "&body=" +
        encodeURIComponent(body);

      window.location.href = href;

      var status = form.querySelector("[data-form-status]");
      if (status) {
        status.textContent =
          "Abrimos tu cliente de correo con el mensaje listo. Si no se abre, escríbenos a " +
          form.getAttribute("data-mailto") + ".";
      }
    });
  }
})();
