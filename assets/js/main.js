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
        { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
      );
      revealables.forEach(function (el) {
        io.observe(el);
      });
    }
  }

  /* ---- Acordeón de servicios ---- */
  var services = document.querySelectorAll(".service");
  services.forEach(function (service) {
    var head = service.querySelector(".service__head");
    var panel = service.querySelector(".service__panel");
    if (!head || !panel) return;

    var close = function () {
      service.classList.remove("is-open");
      head.setAttribute("aria-expanded", "false");
      panel.style.height = "0px";
    };
    var open = function () {
      service.classList.add("is-open");
      head.setAttribute("aria-expanded", "true");
      panel.style.height = panel.scrollHeight + "px";
    };

    close();

    head.addEventListener("click", function () {
      var isOpen = service.classList.contains("is-open");
      services.forEach(function (other) {
        if (other !== service && other.classList.contains("is-open")) {
          other.classList.remove("is-open");
          other.querySelector(".service__head").setAttribute("aria-expanded", "false");
          other.querySelector(".service__panel").style.height = "0px";
        }
      });
      if (isOpen) close();
      else open();
    });

    window.addEventListener("resize", function () {
      if (service.classList.contains("is-open")) {
        panel.style.height = panel.scrollHeight + "px";
      }
    });
  });

  /* Abre el primer servicio en escritorio para que la sección no parezca vacía */
  if (services.length && window.innerWidth > 860) {
    var first = services[0].querySelector(".service__head");
    if (first) first.click();
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
