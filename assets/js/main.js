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

  /* ---- Servicios: la foto sigue al servicio activo ---- */
  var svcList = document.querySelector("[data-svc-list]");
  if (svcList) {
    var items = svcList.querySelectorAll(".svc__item");
    var imgs = document.querySelectorAll("[data-svc-img]");
    var activar = function (clave) {
      imgs.forEach(function (im) {
        im.classList.toggle("is-on", im.dataset.svcImg === clave);
      });
      items.forEach(function (it) {
        it.classList.toggle("is-active", it.dataset.svc === clave);
      });
    };
    activar(items[0] ? items[0].dataset.svc : null);

    items.forEach(function (item) {
      item.addEventListener("mouseenter", function () {
        activar(item.dataset.svc);
      });
    });

    if ("IntersectionObserver" in window) {
      var ioSvc = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) activar(entry.target.dataset.svc);
          });
        },
        { rootMargin: "-45% 0px -45% 0px", threshold: 0 }
      );
      items.forEach(function (it) {
        ioSvc.observe(it);
      });
    }
  }

  /* ---- Reels: se reproducen solos al entrar en pantalla y se paran al salir.
         El botón activa el audio de uno y silencia el resto. ---- */
  var reels = document.querySelectorAll("[data-reel]");
  if (reels.length) {
    var videos = [];
    reels.forEach(function (reel) {
      var v = reel.querySelector("video");
      if (!v) return;
      videos.push(v);
      v.muted = true;

      var boton = reel.querySelector("[data-sound]");
      if (boton) {
        boton.addEventListener("click", function () {
          var encender = v.muted;
          // Solo puede sonar uno a la vez
          videos.forEach(function (otro) {
            otro.muted = true;
            var suyo = otro.closest("[data-reel]");
            if (suyo) suyo.classList.remove("is-audible");
            var b = suyo && suyo.querySelector("[data-sound]");
            if (b) b.setAttribute("aria-label", b.getAttribute("data-on") || "");
          });
          v.muted = !encender;
          reel.classList.toggle("is-audible", encender);
          boton.setAttribute(
            "aria-label",
            boton.getAttribute(encender ? "data-off" : "data-on") || ""
          );
          if (encender) v.play().catch(function () {});
        });
      }

      // Al hacer clic en el vídeo, pausa o sigue
      v.addEventListener("click", function () {
        if (v.paused) {
          v.play().catch(function () {});
        } else {
          v.pause();
        }
      });
    });

    if ("IntersectionObserver" in window) {
      var ioReel = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            var v = entry.target.querySelector("video");
            if (!v) return;
            if (entry.isIntersecting) {
              if (!reduced) v.play().catch(function () {});
            } else {
              v.pause();
              v.muted = true;
              entry.target.classList.remove("is-audible");
            }
          });
        },
        { threshold: 0.35 }
      );
      reels.forEach(function (reel) {
        ioReel.observe(reel);
      });
    }
  }

  /* ---- Bucle de scroll: tira, paralaje, raíl del proceso, giro del cero ---- */
  var collage = document.querySelector("[data-collage]");
  var parallax = document.querySelectorAll("[data-parallax]");
  var rail = document.querySelector("[data-rail]");
  var spin = document.querySelector("[data-spin]");
  var pasos = rail ? rail.querySelectorAll(".step") : [];

  var clamp01 = function (v) {
    return v < 0 ? 0 : v > 1 ? 1 : v;
  };

  // Las piezas del inicio no siguen el scroll uno a uno: el valor que las mueve
  // persigue al del scroll acercándose un 9 % cada fotograma. Con la rueda del
  // ratón, que llega a saltos de decenas de píxeles, la diferencia entre las dos
  // cosas es lo que se nota: sin esto el movimiento va a tirones.
  var pSuave = null;
  var SEGUIMIENTO = 0.09;

  var frame = function () {
    var vh = window.innerHeight;
    var sigue = false;

    if (collage) {
      var travel = collage.offsetHeight - vh;
      var objetivo = clamp01(travel > 0 ? (window.scrollY - collage.offsetTop) / travel : 1);
      if (pSuave === null) pSuave = objetivo;   // el primer fotograma, sin arrastre
      var salto = objetivo - pSuave;
      if (Math.abs(salto) < 0.0004) {
        pSuave = objetivo;
      } else {
        pSuave += salto * SEGUIMIENTO;
        sigue = true;                            // aún no ha llegado: otro fotograma
      }
      collage.style.setProperty("--p", pSuave.toFixed(4));
    }

    parallax.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      // -1 al entrar por abajo, +1 al salir por arriba
      var centro = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2);
      el.style.setProperty("--py", (-clamp01((centro + 1) / 2) * 2 + 1).toFixed(3));
    });

    if (rail) {
      var rr = rail.getBoundingClientRect();
      var avance = clamp01((vh * 0.62 - rr.top) / rr.height);
      rail.style.setProperty("--fill", avance.toFixed(3));
      pasos.forEach(function (paso, i) {
        var pr = paso.getBoundingClientRect();
        paso.classList.toggle("is-on", pr.top < vh * 0.66);
      });
    }

    if (spin) {
      var sr = spin.getBoundingClientRect();
      if (sr.bottom > 0 && sr.top < vh) {
        var giro = ((vh - sr.top) / (vh + sr.height)) * 40 - 12;
        spin.style.setProperty("--spin", giro.toFixed(2) + "deg");
      }
    }

    ticking = false;
    if (sigue) pedir();   // sigue habiendo movimiento pendiente
  };

  var ticking = false;
  var pedir = function () {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(frame);
    }
  };

  if (reduced) {
    if (collage) collage.style.setProperty("--p", "1");
    pasos.forEach(function (p) {
      p.classList.add("is-on");
    });
  } else {
    window.addEventListener("scroll", pedir, { passive: true });
    window.addEventListener("resize", pedir);
    frame();
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
        "",
        "Cuéntanos:",
        data.get("mensaje") || ""
      ].join("\n");

      window.location.href =
        "mailto:" + form.getAttribute("data-mailto") +
        "?subject=" + encodeURIComponent("Nuevo proyecto — " + (data.get("marca") || data.get("nombre") || "Laconic")) +
        "&body=" + encodeURIComponent(body);

      var status = form.querySelector("[data-form-status]");
      if (status) {
        status.textContent =
          (form.getAttribute("data-ok") || "") + form.getAttribute("data-mailto") + ".";
      }
    });
  }
})();
