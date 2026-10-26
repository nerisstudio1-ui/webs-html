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

  /* Menú móvil */
  var toggle = $(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var nav = $(".nav");
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* Año del pie */
  var year = $("[data-year]");
  if (year) year.textContent = new Date().getFullYear();

  function card(p) {
    return '<a class="card" href="producto.html?p=' + p.id + '">' +
      '<figure><img src="' + p.image + '" alt="' + esc(p.fullName) + '" loading="lazy"></figure>' +
      '<div class="eyebrow card-cat">' + esc(catName(p.category)) + "</div>" +
      "<h3>" + esc(p.fullName) + "</h3>" +
      '<div class="price">' + priceText(p) + "</div></a>";
  }

  function sidebar(active) {
    var html = "<h2>Equipamiento</h2><ul>" +
      '<li><a href="productos.html"' + (active ? "" : ' class="active"') + ">Todo el equipamiento</a></li>";
    categories.forEach(function (c) {
      html += '<li><a href="productos.html?cat=' + c.id + '"' + (c.id === active ? ' class="active"' : "") + ">" + esc(c.name) + "</a></li>";
    });
    return html + "</ul>";
  }

  /* Colección en la página de inicio */
  var home = $("[data-home-grid]");
  if (home) home.innerHTML = products.map(card).join("");

  /* Catálogo */
  var catalog = $("[data-catalog]");
  if (catalog) {
    var cat = params.get("cat");
    if (cat && !catName(cat)) cat = null;
    $("[data-side]").innerHTML = sidebar(cat);
    var list = products.filter(function (p) { return !cat || p.category === cat; });
    catalog.innerHTML = list.length ? list.map(card).join("") : '<p class="empty">Próximamente.</p>';
    var crumb = $("[data-crumb]");
    if (cat) {
      crumb.innerHTML = '<a href="index.html">Inicio</a> / <a href="productos.html">Equipamiento</a> / ' + esc(catName(cat));
      document.title = catName(cat) + " · Maison Reformer";
    }
  }

  /* Ficha de producto */
  var view = $("[data-product]");
  if (view) {
    var p = products.filter(function (x) { return x.id === params.get("p"); })[0] || products[0];
    document.title = p.fullName + " · Maison Reformer";
    $("[data-side]").innerHTML = sidebar(p.category);
    $("[data-crumb]").innerHTML = '<a href="index.html">Inicio</a> / <a href="productos.html">Equipamiento</a> / ' +
      '<a href="productos.html?cat=' + p.category + '">' + esc(catName(p.category)) + "</a> / " + esc(p.fullName);

    var icon = '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/></svg>';
    var color = p.defaultColor || "";
    var swatchColors = { Negro: "#1d1b1a", Gris: "#9a9894", Mocca: "#8a6e5c" };

    var html = '<div class="product">' +
      '<div class="gallery"><figure' + (p.portrait ? ' class="tall"' : "") + '><img src="' + p.image + '" alt="' + esc(p.fullName) + '"></figure></div>' +
      '<div class="buy"><div class="brandline">Maison Reformer</div>' +
      "<h1>" + esc(p.fullName) + "</h1>" +
      '<div class="price">' + priceText(p) + '</div><div class="vat">+ IVA</div><hr>';

    if (p.colors.length) {
      html += '<div class="label">Color: <span data-color>' + esc(color) + "</span></div>" +
        '<div class="swatches" role="group" aria-label="Color de tapizado">' +
        p.colors.map(function (c) {
          return '<button type="button" class="swatch" data-swatch="' + c + '" aria-pressed="' + (c === color) + '">' +
            '<i style="background:' + swatchColors[c] + '"></i>' + c + "</button>";
        }).join("") + "</div><hr>";
    }

    html += '<div class="buy-row"><div class="qty"><button type="button" data-qty="-1" aria-label="Restar">−</button>' +
      '<input type="number" value="1" min="1" aria-label="Cantidad" data-qty-input><button type="button" data-qty="1" aria-label="Sumar">+</button></div>' +
      '<button type="button" class="btn" data-add>Añadir al carrito</button></div>' +
      '<p class="ship">Fecha prevista de envío: por confirmar</p>' +
      '<a class="btn btn-outline chat" data-chat href="#"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>Chatea con nosotros</a>' +
      '<p class="chat-note">Te ayudamos a elegir tu equipo</p>' +
      '<div class="toast" data-toast role="status"></div></div></div>';

    html += '<div class="acc">' +
      "<details open><summary>" + icon + "Descripción</summary><div class=\"body\">" +
      p.description.map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("") + "</div></details>";

    if (p.accessories) {
      html += "<details open><summary>" + icon + "Accesorios incluidos</summary><div class=\"body\"><ul class=\"chips\">" +
        p.accessories.map(function (a) { return "<li>" + esc(a) + "</li>"; }).join("") + "</ul></div></details>";
    }

    html += "<details><summary>" + icon + 'Ficha técnica · Medidas y características</summary><div class="body">' +
      "<p>La ficha técnica completa estará disponible próximamente. Si necesitas las medidas o características del equipo, escríbenos y te la enviamos.</p>" +
      '<p><a class="dl" href="contacto.html?asunto=' + encodeURIComponent("Ficha técnica · " + p.fullName) + '">Solicitar ficha técnica →</a></p></div></details>' +
      "<details><summary>" + icon + 'Cuidados y mantenimiento</summary><div class="body">' +
      "<p>Mantén tu equipo en un espacio interior, protegido de la humedad. Limpia guías y raíles semanalmente, la tapicería después de cada uso con un paño de microfibra ligeramente humedecido y revisa periódicamente muelles, mosquetones y enganches.</p>" +
      '<p><a class="dl" href="maison-care.html">Ver la guía Maison Care →</a></p></div></details></div>';

    view.innerHTML = html;

    view.addEventListener("click", function (e) {
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
    var chatText = "Hola, me interesa " + p.fullName + (color ? " en " + color : "") + ".";
    chat.href = WHATSAPP
      ? "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(chatText)
      : "contacto.html?asunto=" + encodeURIComponent("Consulta · " + p.fullName);
    if (WHATSAPP) { chat.target = "_blank"; chat.rel = "noopener"; }
  }

  /* Formulario de contacto: abre el correo del cliente con el mensaje preparado */
  var form = $("[data-contact-form]");
  if (form) {
    var asunto = params.get("asunto");
    if (asunto) form.asunto.value = asunto;
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
