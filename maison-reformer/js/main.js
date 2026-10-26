/* Maison Reformer — comportamiento de la web */
(function () {
  var CONTACT_EMAIL = "maisonreformer@gmail.com";
  // Número de WhatsApp en formato internacional sin "+" ni espacios (p. ej. "34600000000").
  // Mientras esté vacío, "Chatea con nosotros" lleva a la página de contacto.
  var WHATSAPP = "";

  var products = window.MAISON_PRODUCTS || [];
  var categories = window.MAISON_CATEGORIES || [];
  var params = new URLSearchParams(location.search);

  function $(sel) { return document.querySelector(sel); }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function catName(id) {
    for (var i = 0; i < categories.length; i++) if (categories[i].id === id) return categories[i].name;
    return "";
  }
  function priceText(p) { return p.price ? p.price : "Precio por confirmar"; }

  /* Cabecera: menú móvil y fondo sólido al hacer scroll en la portada */
  var header = $(".header");
  var toggle = $(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = $(".nav").classList.toggle("open");
      header.classList.toggle("menu-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  if (document.body.classList.contains("home")) {
    var onScroll = function () { header.classList.toggle("solid", window.scrollY > 40); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* Año del pie */
  var year = $("[data-year]");
  if (year) year.textContent = new Date().getFullYear();

  function card(p) {
    return '<a class="card" href="producto.html?p=' + p.id + '">' +
      "<figure>" + (p.badge ? '<span class="badge">' + esc(p.badge) + "</span>" : "") +
      '<img src="' + p.image + '" alt="' + esc(p.fullName) + '" loading="lazy"></figure>' +
      '<div class="meta"><div class="name">' + esc(p.fullName) + "</div>" +
      "<div>" + esc(catName(p.category)) + "</div>" +
      "<div>" + priceText(p) + "</div></div></a>";
  }

  /* Colección en la página de inicio */
  var home = $("[data-home-grid]");
  if (home) home.innerHTML = products.map(card).join("");

  /* Catálogo */
  var catalog = $("[data-catalog]");
  if (catalog) {
    var cat = params.get("cat");
    if (cat && !catName(cat)) cat = null;
    var filters = '<a href="productos.html"' + (cat ? "" : ' class="active"') + ">Todo</a>";
    categories.forEach(function (c) {
      filters += '<a href="productos.html?cat=' + c.id + '"' + (c.id === cat ? ' class="active"' : "") + ">" + esc(c.name) + "</a>";
    });
    $("[data-filters]").innerHTML = filters;
    var list = products.filter(function (p) { return !cat || p.category === cat; });
    catalog.innerHTML = list.length ? list.map(card).join("") : '<p class="empty">Próximamente.</p>';
    if (cat) {
      $("[data-cat-title]").textContent = catName(cat);
      document.title = catName(cat) + " · Maison Reformer";
    }
  }

  /* Ficha de producto */
  var view = $("[data-product]");
  if (view) {
    var p = products.filter(function (x) { return x.id === params.get("p"); })[0] || products[0];
    document.title = p.fullName + " · Maison Reformer";
    var color = p.defaultColor || "";
    var swatchColors = { Negro: "#1d1b1a", Gris: "#9a9894", Mocca: "#8a6e5c" };
    var images = [p.image].concat(p.gallery || []);

    var html = '<div class="product"><div class="gallery"><div class="slides">' +
      images.map(function (src, i) {
        return '<figure class="slide' + (i === 0 ? " on" : "") + (p.portrait ? " contain" : "") + '"><img src="' + src + '" alt="' + esc(p.fullName) + '"></figure>';
      }).join("") + "</div>";
    if (images.length > 1) {
      html += '<button class="arrow prev" type="button" aria-label="Anterior" data-slide="-1">‹</button>' +
        '<button class="arrow next" type="button" aria-label="Siguiente" data-slide="1">›</button>' +
        '<div class="count"><span data-slide-n>1</span> / ' + images.length + "</div>";
    }
    html += '</div><div class="buy"><div class="buy-inner">' +
      '<nav class="crumbs center" aria-label="Ruta"><a href="productos.html">Equipamiento</a> / <a href="productos.html?cat=' + p.category + '">' + esc(catName(p.category)) + "</a></nav>" +
      "<h1>" + esc(p.fullName) + "</h1>" +
      '<div class="price">' + priceText(p) + '</div><div class="vat">+ IVA · Envío gratuito a península</div><hr>' +
      '<div class="buy-row"><div class="qty"><button type="button" data-qty="-1" aria-label="Restar">−</button>' +
      '<input type="number" value="1" min="1" aria-label="Cantidad" data-qty-input><button type="button" data-qty="1" aria-label="Sumar">+</button></div>' +
      '<button type="button" class="btn" data-add>Añadir al carrito</button></div>';

    if (p.colors.length) {
      html += '<div class="label">Color: <span data-color>' + esc(color) + "</span></div>" +
        '<div class="swatches" role="group" aria-label="Color de tapizado">' +
        p.colors.map(function (c) {
          return '<button type="button" class="swatch" data-swatch="' + c + '" aria-pressed="' + (c === color) + '">' +
            '<i style="background:' + swatchColors[c] + '"></i>' + c + "</button>";
        }).join("") + "</div>";
    }

    html += '<p class="ship">Fecha prevista de envío: por confirmar</p>' +
      '<a class="btn btn-line btn-block chat" data-chat href="#">Chatea con nosotros</a>' +
      '<div class="toast" data-toast role="status"></div>';

    html += '<div class="acc">' +
      '<details open><summary>Descripción</summary><div class="body">' +
      p.description.map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("") + "</div></details>";
    if (p.accessories) {
      html += '<details><summary>Accesorios incluidos</summary><div class="body"><ul class="chips">' +
        p.accessories.map(function (a) { return "<li>" + esc(a) + "</li>"; }).join("") + "</ul></div></details>";
    }
    html += '<details><summary>Ficha técnica · Medidas y características</summary><div class="body">' +
      "<p>La ficha técnica completa estará disponible próximamente. Si necesitas las medidas o características del equipo, escríbenos y te la enviamos.</p>" +
      '<p><a href="contacto.html?asunto=' + encodeURIComponent("Ficha técnica · " + p.fullName) + '">Solicitar ficha técnica →</a></p></div></details>' +
      '<details><summary>Cuidados y mantenimiento</summary><div class="body">' +
      "<p>Mantén tu equipo en un espacio interior, protegido de la humedad. Limpia guías y raíles semanalmente, la tapicería después de cada uso con un paño de microfibra ligeramente humedecido y revisa periódicamente muelles, mosquetones y enganches.</p>" +
      '<p><a href="maison-care.html">Ver la guía Maison Care →</a></p></div></details>' +
      '<details><summary>Envíos y entregas</summary><div class="body">' +
      "<p>Envío estándar gratuito a España peninsular, con entrega a pie de calle en 24-48 horas laborables para productos en stock. Entrega interior y montaje disponibles bajo presupuesto.</p>" +
      '<p><a href="envios.html">Política de envíos y entregas →</a></p></div></details></div>';
    html += "</div></div></div>";

    view.innerHTML = html;

    var related = $("[data-related]");
    if (related) {
      related.innerHTML = products.filter(function (x) { return x.id !== p.id; }).slice(0, 4).map(card).join("");
    }

    var slide = 0;
    view.addEventListener("click", function (e) {
      var arrow = e.target.closest("[data-slide]");
      if (arrow) {
        var slides = view.querySelectorAll(".slide");
        slides[slide].classList.remove("on");
        slide = (slide + parseInt(arrow.getAttribute("data-slide"), 10) + slides.length) % slides.length;
        slides[slide].classList.add("on");
        $("[data-slide-n]").textContent = slide + 1;
      }
      var sw = e.target.closest("[data-swatch]");
      if (sw) {
        color = sw.getAttribute("data-swatch");
        view.querySelectorAll("[data-swatch]").forEach(function (b) { b.setAttribute("aria-pressed", b === sw); });
        $("[data-color]").textContent = color;
      }
      var q = e.target.closest("[data-qty]");
      if (q) {
        var input = $("[data-qty-input]");
        input.value = Math.max(1, (parseInt(input.value, 10) || 1) + parseInt(q.getAttribute("data-qty"), 10));
      }
      if (e.target.closest("[data-add]")) {
        var qty = Math.max(1, parseInt($("[data-qty-input]").value, 10) || 1);
        var subject = "Pedido · " + p.fullName + (color ? " (" + color + ")" : "") + " × " + qty;
        var toast = $("[data-toast]");
        toast.innerHTML = "Estamos ultimando los precios de nuestro equipamiento. " +
          '<a href="contacto.html?asunto=' + encodeURIComponent(subject) + '">Escríbenos</a> y te enviamos tu presupuesto personalizado.';
        toast.classList.add("show");
      }
    });

    var chat = $("[data-chat]");
    chat.href = WHATSAPP
      ? "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent("Hola, me interesa " + p.fullName + ".")
      : "contacto.html?asunto=" + encodeURIComponent("Consulta · " + p.fullName);
    if (WHATSAPP) { chat.target = "_blank"; chat.rel = "noopener"; }
  }

  /* Aparición suave de bloques al hacer scroll */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.15 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* Carrusel de la colección */
  var carousel = $("[data-carousel]");
  if (carousel) {
    var slideBy = function (dir) {
      var item = carousel.querySelector(".card");
      var step = item ? item.getBoundingClientRect().width + 16 : carousel.clientWidth * 0.8;
      carousel.scrollBy({ left: dir * step, behavior: "smooth" });
    };
    $("[data-carousel-prev]").addEventListener("click", function () { slideBy(-1); });
    $("[data-carousel-next]").addEventListener("click", function () { slideBy(1); });
  }

  /* Cifras que cuentan al aparecer */
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        co.unobserve(en.target);
        var el = en.target, end = parseInt(el.getAttribute("data-count"), 10), t0 = null;
        var tick = function (t) {
          if (!t0) t0 = t;
          var k = Math.min(1, (t - t0) / 1400);
          el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3)));
          if (k < 1) requestAnimationFrame(tick);
        };
        el.textContent = "0";
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { co.observe(el); });
  }

  /* Parallax suave en las bandas de imagen */
  var plx = document.querySelectorAll("[data-parallax]");
  if (plx.length && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var onPlx = function () {
      plx.forEach(function (img) {
        var r = img.parentNode.getBoundingClientRect();
        if (r.bottom < 0 || r.top > innerHeight) return;
        var p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
        img.style.transform = "translateY(" + (p * -12) + "%)";
      });
    };
    window.addEventListener("scroll", onPlx, { passive: true });
    onPlx();
  }

  /* Formulario de contacto: abre el correo del cliente con el mensaje preparado */
  var form = $("[data-contact-form]");
  if (form) {
    if (params.get("asunto")) form.asunto.value = params.get("asunto");
    if (params.get("email")) form.email.value = params.get("email");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = $("[data-form-msg]");
      if (!form.checkValidity()) {
        msg.textContent = "Revisa los campos obligatorios y acepta la política de privacidad.";
        form.reportValidity();
        return;
      }
      var body = "Nombre: " + form.nombre.value + " " + form.apellidos.value +
        "\nEmail: " + form.email.value +
        (form.telefono.value ? "\nTeléfono: " + form.telefono.value : "") +
        "\n\n" + form.mensaje.value;
      location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(form.asunto.value) +
        "&body=" + encodeURIComponent(body);
      msg.textContent = "Gracias. Se abrirá tu aplicación de correo para enviar el mensaje.";
    });
  }
})();
