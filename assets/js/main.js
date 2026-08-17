/* Laconic Studio — interacciones (sin dependencias) */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* ---- Marca de carga: dispara la entrada del logo ---- */
  var loaded = function () {
    document.documentElement.classList.add("is-loaded");
  };
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(loaded);
    window.setTimeout(loaded, 1200); // por si las tipografías tardan
  } else {
    loaded();
  }

  /* ---- Titulares: cada palabra en su propia caja para revelarla ---- */
  var splitWords = function (root) {
    var index = 0;
    var walk = function (node) {
      var kids = Array.prototype.slice.call(node.childNodes);
      kids.forEach(function (child) {
        if (child.nodeType === 3) {
          var text = child.textContent;
          if (!text.trim()) return;
          var frag = document.createDocumentFragment();
          text.split(/(\s+)/).forEach(function (chunk) {
            if (!chunk) return;
            if (!chunk.trim()) {
              frag.appendChild(document.createTextNode(chunk));
              return;
            }
            var wrap = document.createElement("span");
            wrap.className = "w";
            wrap.style.setProperty("--i", index++);
            var inner = document.createElement("i");
            inner.textContent = chunk;
            wrap.appendChild(inner);
            frag.appendChild(wrap);
          });
          node.replaceChild(frag, child);
        } else if (child.nodeType === 1) {
          walk(child);
        }
      });
    };
    walk(root);
  };

  var headlines = document.querySelectorAll(".rl");
  if (!reduced) {
    headlines.forEach(splitWords);
  }

  /* ---- Entradas al viewport (titulares y bloques) ---- */
  var animables = document.querySelectorAll(".rl, .fade");
  if (animables.length) {
    if (reduced || !("IntersectionObserver" in window)) {
      animables.forEach(function (el) {
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
        { rootMargin: "0px 0px -12% 0px", threshold: 0 }
      );
      animables.forEach(function (el) {
        io.observe(el);
      });
    }
  }

  /* ---- Cabecera: sombra al despegarse y auto-ocultar al bajar ----
         El color ya no depende de la sección: la barra es clara siempre. ---- */
  var header = document.querySelector(".header");
  if (header) {
    var lastY = window.scrollY;
    var onScroll = function () {
      var y = window.scrollY;
      header.classList.toggle("is-stuck", y > 60);
      if (!document.body.classList.contains("menu-open")) {
        header.classList.toggle("is-hidden", y > lastY && y > 400);
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

  /* ---- Navegación: marca el enlace de la sección visible ---- */
  var navLinks = document.querySelectorAll(".nav a[href^='#']");
  if (navLinks.length && "IntersectionObserver" in window) {
    var porId = {};
    navLinks.forEach(function (a) {
      porId[a.getAttribute("href").slice(1)] = a;
    });
    var ioNav = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var link = porId[entry.target.id];
          if (link && entry.isIntersecting) {
            navLinks.forEach(function (a) {
              a.classList.remove("is-active");
            });
            link.classList.add("is-active");
          }
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );
    Object.keys(porId).forEach(function (id) {
      var sec = document.getElementById(id);
      if (sec) ioNav.observe(sec);
    });
  }

  /* ---- Servicios: el nombre elegido enseña su definición ----
         Las cinco definiciones están en el HTML: sin JavaScript se ven todas,
         una detrás de otra, que es la manera de que se lean igual. ---- */
  var svc = document.querySelector("[data-svc-list]");
  if (svc) {
    var nombres = svc.querySelectorAll(".svc__nom");
    var defs = svc.querySelectorAll("[data-svc-def]");
    var activarSvc = function (clave) {
      nombres.forEach(function (n) {
        var suyo = n.dataset.svc === clave;
        n.classList.toggle("is-active", suyo);
        var b = n.querySelector("button");
        if (b) b.setAttribute("aria-expanded", String(suyo));
      });
      defs.forEach(function (d) {
        d.classList.toggle("is-on", d.dataset.svcDef === clave);
      });
    };
    activarSvc(nombres[0] ? nombres[0].dataset.svc : null);

    nombres.forEach(function (n) {
      var boton = n.querySelector("button");
      if (!boton) return;
      // Con el ratón basta pasar por encima; con el teclado, el foco; y el
      // clic vale para el móvil, que no tiene ninguna de las dos cosas.
      ["mouseenter", "focus", "click"].forEach(function (ev) {
        (ev === "mouseenter" ? n : boton).addEventListener(ev, function () {
          activarSvc(n.dataset.svc);
        });
      });
    });
  }

  /* ---- Los vídeos de las fichas de proyecto ----
         Arrancan por el atributo autoplay del HTML, sin depender de esto. Aquí
         solo se paran al salir de pantalla, para no gastar batería con cuatro
         vídeos en marcha a la vez, y se respeta a quien pide menos movimiento. */
  var videosFicha = document.querySelectorAll(".obra__video");
  if (videosFicha.length) {
    videosFicha.forEach(function (v) {
      v.muted = true;
      if (reduced) {
        v.autoplay = false;
        v.removeAttribute("autoplay");
        v.pause();
      }
    });

    if (!reduced && "IntersectionObserver" in window) {
      var ioVideo = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            var v = entry.target;
            if (entry.isIntersecting) {
              v.play().catch(function () {});
            } else {
              v.pause();
            }
          });
        },
        { threshold: 0.25 }
      );
      videosFicha.forEach(function (v) {
        ioVideo.observe(v);
      });
    }
  }

  /* ---- Las dos fotos del inicio, subiendo con el scroll ---- */
  var collage = document.querySelector("[data-collage]");
  if (collage) {
    var clamp01 = function (v) {
      return v < 0 ? 0 : v > 1 ? 1 : v;
    };

    // Las fotos no siguen el scroll uno a uno: el valor que las mueve persigue al
    // del scroll acercándose un 9 % cada fotograma. Con la rueda del ratón, que
    // llega a saltos de decenas de píxeles, la diferencia entre las dos cosas es
    // lo que se nota: sin esto el movimiento va a tirones.
    var pSuave = null;
    var SEGUIMIENTO = 0.09;
    var ticking = false;

    var frame = function () {
      var vh = window.innerHeight;
      var recorrido = collage.offsetHeight - vh;
      // Se mide con getBoundingClientRect, no con offsetTop y scrollY: dentro de
      // WordPress el contenedor del widget está posicionado, así que offsetTop
      // deja de contar desde el documento y el cálculo se descuadra.
      var avance = -collage.getBoundingClientRect().top;
      var objetivo = clamp01(recorrido > 0 ? avance / recorrido : 1);
      if (pSuave === null) pSuave = objetivo;   // el primer fotograma, sin arrastre
      var salto = objetivo - pSuave;
      var sigue = false;
      if (Math.abs(salto) < 0.0004) {
        pSuave = objetivo;
      } else {
        pSuave += salto * SEGUIMIENTO;
        sigue = true;                          // aún no ha llegado: otro fotograma
      }
      collage.style.setProperty("--p", pSuave.toFixed(4));
      ticking = false;
      if (sigue) pedir();
    };

    var pedir = function () {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(frame);
      }
    };

    if (reduced) {
      // Sin movimiento: las fotos ya colocadas arriba
      collage.style.setProperty("--p", "1");
    } else {
      window.addEventListener("scroll", pedir, { passive: true });
      window.addEventListener("resize", pedir);
      frame();
    }
  }

  /* ---- Carriles en bucle: duplicar para que no se vea la costura ---- */
  document.querySelectorAll(".marquee__track, .strip__track").forEach(function (track) {
    track.innerHTML += track.innerHTML;
  });

  /* ---- Cursor ---- */
  var cursor = document.querySelector(".cursor");
  if (cursor && fine && !reduced) {
    var cx = -100, cy = -100, tx = -100, ty = -100;
    document.addEventListener("mousemove", function (e) {
      tx = e.clientX;
      ty = e.clientY;
    });
    var seguir = function () {
      cx += (tx - cx) * 0.18;
      cy += (ty - cy) * 0.18;
      cursor.style.transform = "translate3d(" + (cx - 4.5) + "px," + (cy - 4.5) + "px,0)";
      window.requestAnimationFrame(seguir);
    };
    seguir();

    var interactivos = "a, button, .card, .svc__item, input, textarea, label";
    document.addEventListener("mouseover", function (e) {
      if (e.target.closest(interactivos)) document.body.classList.add("cursor-on");
    });
    document.addEventListener("mouseout", function (e) {
      if (e.target.closest(interactivos)) document.body.classList.remove("cursor-on");
    });
  }

  /* ---- Año del footer ---- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---- Formulario sin backend: compone el correo ---- */
  /* ---- Formulario de contacto ----
         Con data-envia el mensaje se manda al servicio de correo desde aquí, sin
         que la visita salga de la página. El action del <form> sigue puesto, así
         que si no hay JS (o si falla fetch) el envío ocurre igual, a la manera de
         siempre. Con data-mailto en su lugar, el formulario compone el correo y
         abre el cliente de email: es el modo de reserva. ---- */
  var form = document.querySelector(".form");
  if (form) {
    var status = form.querySelector("[data-form-status]");
    var boton = form.querySelector("button[type='submit']");
    var attr = function (nombre) {
      return form.getAttribute(nombre) || "";
    };
    var decir = function (texto) {
      if (status) status.textContent = texto;
    };
    var envia = form.getAttribute("data-envia");

    if (envia && window.fetch) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (form.classList.contains("is-sending")) return;

        // Un objeto plano: las casillas marcadas comparten nombre y se juntan.
        var datos = {};
        new FormData(form).forEach(function (valor, clave) {
          datos[clave] = clave in datos ? datos[clave] + ", " + valor : valor;
        });

        form.classList.remove("is-sent", "has-error");
        form.classList.add("is-sending");
        if (boton) boton.disabled = true;
        decir(attr("data-enviando"));

        window
          .fetch(envia, {
            method: "POST",
            headers: { "Content-Type": "application/json", Accept: "application/json" },
            body: JSON.stringify(datos)
          })
          .then(function (r) {
            if (!r.ok) throw new Error(String(r.status));
            form.classList.remove("is-sending");
            form.classList.add("is-sent");
            form.reset();
            if (boton) boton.disabled = false;
            decir(attr("data-hecho"));
          })
          .catch(function () {
            // Si el servicio no responde, no se pierde el mensaje: se dice a
            // dónde escribir, con el texto ya redactado a mano.
            form.classList.remove("is-sending");
            form.classList.add("has-error");
            if (boton) boton.disabled = false;
            decir(attr("data-error") + attr("data-correo") + ".");
          });
      });
    } else if (form.hasAttribute("data-mailto")) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var data = new FormData(form);
        var servicios = data.getAll("servicio").join(", ") || "Sin especificar";
        var body = [
          "Nombre: " + (data.get("nombre") || ""),
          "Marca: " + (data.get("marca") || ""),
          "Email: " + (data.get("email") || ""),
          "Servicios: " + servicios,
          "",
          "Cuéntanos:",
          data.get("mensaje") || ""
        ].join("\n");

        window.location.href =
          "mailto:" + form.getAttribute("data-mailto") +
          "?subject=" + encodeURIComponent("Nuevo proyecto — " + (data.get("marca") || data.get("nombre") || "Laconic")) +
          "&body=" + encodeURIComponent(body);

        decir(attr("data-ok") + form.getAttribute("data-mailto") + ".");
      });
    }
  }
})();
