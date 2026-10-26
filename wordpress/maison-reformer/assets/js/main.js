/* Maison Reformer — comportamiento del tema */
(function () {
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

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
  if (document.body.classList.contains("home") && header) {
    var onScroll = function () { header.classList.toggle("solid", window.scrollY > 40); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* Aparición suave de bloques al hacer scroll */
  var reveals = $$(".reveal");
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

  /* Dispara "change" también para los oyentes de jQuery que usa WooCommerce */
  function fireChange(el) {
    if (window.jQuery) window.jQuery(el).trigger("change");
    else el.dispatchEvent(new Event("change", { bubbles: true }));
  }

  /* Botones − / + en los campos de cantidad */
  function enhanceQty(root) {
    $$(".quantity", root).forEach(function (wrap) {
      var input = $("input.qty", wrap);
      if (!input || input.type === "hidden" || wrap.dataset.enhanced) return;
      wrap.dataset.enhanced = "1";
      var minus = document.createElement("button");
      var plus = document.createElement("button");
      minus.type = plus.type = "button";
      minus.className = "qty-btn"; plus.className = "qty-btn";
      minus.textContent = "−"; plus.textContent = "+";
      minus.setAttribute("aria-label", "Restar");
      plus.setAttribute("aria-label", "Sumar");
      wrap.insertBefore(minus, input);
      wrap.appendChild(plus);
      function step(d) {
        var min = parseFloat(input.min) || 0;
        var max = parseFloat(input.max) || Infinity;
        var v = (parseFloat(input.value) || 0) + d * (parseFloat(input.step) || 1);
        input.value = Math.min(max, Math.max(min, v));
        fireChange(input);
      }
      minus.addEventListener("click", function () { step(-1); });
      plus.addEventListener("click", function () { step(1); });
    });
  }
  enhanceQty(document);
  if (window.jQuery) window.jQuery(document.body).on("updated_cart_totals", function () { enhanceQty(document); });

  /* Selectores de variación como muestras de color */
  var colors = window.MAISON_SWATCHES || {};
  function slug(s) {
    return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }
  $$("table.variations select").forEach(function (select) {
    var box = document.createElement("div");
    box.className = "swatches";
    box.setAttribute("role", "group");
    function build() {
      box.innerHTML = "";
      $$("option", select).forEach(function (opt) {
        if (!opt.value) return;
        var b = document.createElement("button");
        b.type = "button";
        b.className = "swatch";
        b.setAttribute("aria-pressed", select.value === opt.value ? "true" : "false");
        if (opt.disabled) b.disabled = true;
        var c = colors[slug(opt.value)] || colors[slug(opt.textContent)];
        b.innerHTML = (c ? '<i style="background:' + c + '"></i>' : "") + opt.textContent;
        b.addEventListener("click", function () {
          select.value = select.value === opt.value ? "" : opt.value;
          fireChange(select);
        });
        box.appendChild(b);
      });
    }
    select.classList.add("is-swatched");
    select.parentNode.insertBefore(box, select);
    build();
    select.addEventListener("change", build);
    if (window.jQuery) {
      window.jQuery(select).closest("form").on("woocommerce_update_variation_values reset_data", function () { setTimeout(build, 0); });
      window.jQuery(select).on("change", build);
    }
  });
})();
