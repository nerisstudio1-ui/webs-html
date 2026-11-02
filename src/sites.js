/* The mock sites that ride the conveyor.
 *
 * Built to the references the studio sent: the current "creative studio"
 * house style. Its grammar, and what every site below is made of:
 *
 *   · cream grounds, with pastel blocks — sage, lavender, blush, chartreuse,
 *     deep olive — rather than saturated brand colours
 *   · a display serif and its italic mixed inside the same sentence, which is
 *     the single most characteristic move of the look
 *   · scrolling marquee strips of repeated text
 *   · pill buttons with an arrow
 *   · photographs in arches, rounded cards, or tilted with a white border
 *   · handwritten annotations with a curved arrow
 *   · rotated sticker badges
 *   · testimonial cards, star ratings, stat rows
 *
 * Plus the furniture any real site drags along — footer columns, legal line,
 * cookie notice — because its absence was reading as "mockup".
 *
 * Each site is authored at 1440x1240 and scaled down bodily by the card. The
 * card shows 760 of those pixels and scrolls the rest as it crosses frame. */

const SITES = (() => {
  const bg = (scene, seed, w, h, opts) => ART.bg(scene, seed, w, h, opts);

  /* A generated photograph if one exists for this slot, otherwise the painted
     scene. Keeps every site renderable while the photo set is still being
     filled in, and makes adding a photo a one-file change. */
  const photo = (name, scene, seed, w, h, opts) =>
    (typeof PHOTOS !== 'undefined' && PHOTOS[name])
      ? `url(${PHOTOS[name]})`
      : bg(scene, seed, w, h, opts);

  /* Shared grammar. Every site gets these, so the eight read as one studio's
     work rather than eight unrelated pages. */
  const base = `
    .st{display:flex;flex-direction:column;font-family:'Work Sans',sans-serif}
    .st .bar{display:flex;align-items:center;justify-content:space-between;
      padding:24px 52px;flex:none}
    .st .wm{font-family:'Gloock',serif;font-size:27px;letter-spacing:-.01em}
    .st .nv{display:flex;gap:26px;font-size:13.5px;opacity:.68}
    .st .btnp{display:inline-flex;align-items:center;gap:10px;border-radius:999px;
      padding:13px 26px;font-size:14px;font-weight:600;white-space:nowrap}
    .st .btnp::after{content:'→';font-size:15px}
    .st .ghost{border:1px solid currentColor;border-radius:999px;padding:11px 22px;
      font-size:13px;font-weight:600}
    /* Marquee: a band of repeated text, the way these sites separate sections. */
    .st .mq{overflow:hidden;white-space:nowrap;padding:13px 0;flex:none;text-align:center}
    .st .mq span{font-size:15px;letter-spacing:.02em;font-style:italic;font-family:'Lora',serif}
    .st .mq b{font-weight:400;opacity:.45;margin:0 16px}
    /* Sticker: a rotated pill, as if slapped on the page. */
    .st .stick{display:inline-block;background:#141414;color:#fff;border-radius:999px;
      padding:9px 20px;font-size:12px;font-weight:700;letter-spacing:.1em;
      text-transform:uppercase;transform:rotate(-2.2deg)}
    /* Handwritten aside plus its curved arrow. */
    .st .hand{font-family:'Hand',cursive;font-size:26px;line-height:1.25;opacity:.8}
    .st .arrow{font-family:'Hand',cursive;font-size:40px;opacity:.6;display:block}
    .st .arch{border-radius:999px 999px 14px 14px;background-size:cover;background-position:center}
    .st .stats{display:flex;gap:56px;justify-content:center;padding:26px 0;flex:none}
    .st .stats b{display:block;font-family:'Gloock',serif;font-size:44px;font-style:italic;font-weight:400}
    .st .stats span{font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.55}
    .st .stars{display:inline-flex;align-items:center;gap:7px;font-size:13px}
    .st .stars b{letter-spacing:.1em;color:#c58a2e}
    .st .ft{margin-top:auto;flex:none;border-top:1px solid rgba(0,0,0,.1);
      padding:32px 52px 0;display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:32px}
    .st .ft h5{font-size:11px;letter-spacing:.18em;text-transform:uppercase;
      opacity:.5;margin:0 0 13px;font-weight:600}
    .st .ft a{display:block;font-size:13.5px;opacity:.72;margin-bottom:8px;text-decoration:none;color:inherit}
    .st .ft .about{font-size:13.5px;line-height:1.65;opacity:.68;max-width:30ch}
    .st .ft .soc{display:flex;gap:9px;margin-top:15px}
    .st .ft .soc i{width:27px;height:27px;border-radius:50%;border:1px solid currentColor;opacity:.4;display:block}
    .st .legal{display:flex;justify-content:space-between;padding:20px 52px 24px;font-size:12px;opacity:.45}
    .st .cookie{position:absolute;left:26px;right:26px;top:1086px;z-index:6;background:#fff;
      color:#1a1a1a;border-radius:12px;padding:15px 19px;display:flex;align-items:center;gap:16px;
      box-shadow:0 10px 30px rgba(0,0,0,.16);font-size:13px}
    .st .cookie p{flex:1;line-height:1.5;opacity:.75}
    .st .cookie .b1{background:#141414;color:#fff;padding:10px 17px;border-radius:999px;font-weight:600;white-space:nowrap}
    .st .cookie .b2{padding:10px 13px;opacity:.6;white-space:nowrap}`;

  const marquee = (text, times) =>
    `<div class="mq"><span>${Array(times || 5).fill(text).join('<b>✦</b>')}</span></div>`;

  const foot = (cols, legal) => `
    <div class="ft">
      <div><h5>${cols.brand}</h5><div class="about">${cols.about}</div>
        <div class="soc"><i></i><i></i><i></i></div></div>
      ${cols.groups.map((g) => `<div><h5>${g.h}</h5>${g.items.map((i) => `<a>${i}</a>`).join('')}</div>`).join('')}
    </div>
    <div class="legal"><span>${legal}</span><span>Aviso legal · Privacidad · Cookies</span></div>`;

  const cookie = `
    <div class="cookie"><p>Usamos cookies propias y de terceros para medir el tráfico.</p>
      <span class="b2">Configurar</span><span class="b1">Aceptar todas</span></div>`;

  /* ---------------------------------------------------------------- 1
     Knockout wordmark across a photograph, as in the yoga reference. */
  const flow = () => ({
    id: 'flow',
    css: `${base.replace(/\.st(?![\w-])/g, '.flow')}
    .flow{background:#f3f0e8;color:#1d1c18}
    .flow .wm{font-size:24px}
    .flow .hero{position:relative;height:396px;margin:0 52px;overflow:hidden;flex:none;border-radius:14px}
    .flow .hero .im{position:absolute;inset:0;background-size:cover;background-position:center}
    .flow .hero::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,16,12,.42),rgba(18,16,12,.66))}
    .flow .ko{z-index:2}
    .flow .ko{position:absolute;left:0;right:0;bottom:-26px;text-align:center;
      font-family:'Gloock',serif;font-size:250px;line-height:.8;color:#f3f0e8;letter-spacing:-.045em}
    .flow .tag{text-align:center;font-size:17px;opacity:.62;padding:22px 0 0;flex:none}
    .flow .mid{text-align:center;padding:30px 52px 0;flex:none}
    .flow .mid h2{font-family:'Gloock',serif;font-size:62px;line-height:1.08;font-weight:400;max-width:17ch;margin:14px auto 0}
    .flow .mid h2 em{font-style:italic}
    .flow .mid p{font-size:16px;line-height:1.6;opacity:.66;max-width:52ch;margin:18px auto 0}
    .flow .tabs{display:flex;gap:12px;justify-content:center;padding:26px 0 0;flex:none}
    .flow .tabs span{border-radius:999px;padding:11px 24px;font-size:14px;opacity:.6}
    .flow .tabs .on{background:#e3e0d6;opacity:1;font-weight:600}
    .flow .low{display:grid;grid-template-columns:1fr 1fr;gap:38px;padding:30px 52px 0;align-items:center;flex:none}
    .flow .low h3{font-family:'Gloock',serif;font-size:34px;font-weight:400;margin-bottom:12px}
    .flow .low h3 em{font-style:italic}
    .flow .low p{font-size:15px;line-height:1.65;opacity:.68}
    .flow .low .btnp{background:#1d1c18;color:#f3f0e8;margin-top:18px}
    .flow .low .arch{height:260px}
    .flow .mq{background:#1d1c18;color:#f3f0e8;margin-top:28px}`,
    html: `
    <div class="bar"><div class="wm">flow</div>
      <div class="nv"><span>Clases</span><span>Horarios</span><span>Bonos</span><span>Estudio</span></div>
      <div class="ghost">Primera clase gratis</div></div>
    <div class="hero">
      <div class="im" style="background-image:${photo('yoga', 'mat', 3, 980, 460, { wall: '#9a9183', floor: '#8a6a44' })}"></div>
      <div class="ko">flow</div></div>
    <div class="tag">Encuentra tu centro. Respira, muévete, transforma.</div>
    <div class="mid">
      <span class="stars"><b>★★★★★</b>4,97 sobre 5 · 212 reseñas</span>
      <h2>Tres formas de moverte, <em>una misma</em> manera de cuidarte</h2>
      <p>Reformer, pilates máquina y yoga en grupos de seis. Toca una para ver cuál te encaja.</p></div>
    <div class="tabs"><span>Hot mat</span><span class="on">Flow yoga</span><span>Reformer</span></div>
    <div class="low">
      <div><h3>Flow <em>yoga</em></h3>
        <p>Prácticas con atención a la respiración y al movimiento, pensadas para asentarte. Todos los niveles.</p>
        <div class="btnp">Reservar plaza</div></div>
      <div class="arch" style="background-image:${photo('pool', 'water', 9, 520, 420, { shallow: '#8fc6c0', deep: '#2e6e74' })}"></div></div>
    ${marquee('estudio en Ruzafa', 4)}
    ${foot({ brand: 'Flow Estudio', about: 'Pilates reformer, mat y yoga en grupos de seis personas. Calle Cuba 34, Valencia.',
      groups: [{ h: 'Clases', items: ['Reformer', 'Mat', 'Yoga', 'Embarazo'] },
               { h: 'Estudio', items: ['Horarios', 'Precios', 'Equipo'] },
               { h: 'Contacto', items: ['960 41 22 08', 'hola@flowestudio.es'] }] },
      '© 2026 Flow Estudio SL')}
    ${cookie}`,
  });

  /* ---------------------------------------------------------------- 2
     Split colour block and serif/italic headline, as in the first reference. */
  const olmo = () => ({
    id: 'olmo',
    css: `${base.replace(/\.st(?![\w-])/g, '.olmo')}
    .olmo{background:#f8f4ea;color:#23251c}
    .olmo .split{display:grid;grid-template-columns:1.08fr 1fr;height:392px;flex:none}
    .olmo .split .im{background-size:cover;background-position:center;border-right:3px solid #23251c}
    .olmo .blk{background:#dff07f;padding:46px 46px;display:flex;flex-direction:column;justify-content:center;gap:16px}
    .olmo .blk .kick{font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;font-weight:700}
    .olmo .blk h1{font-family:'Gloock',serif;font-size:50px;line-height:1.1;font-weight:400}
    .olmo .blk h1 em{font-style:italic}
    .olmo .blk h1 b{font-weight:400;text-transform:uppercase;font-family:'Work Sans',sans-serif;
      font-size:.82em;letter-spacing:-.02em}
    .olmo .blk p{font-size:14.5px;line-height:1.62;opacity:.8;max-width:34ch}
    .olmo .blk .btnp{background:#c3c9f5;color:#23251c;align-self:flex-start;margin-top:4px}
    .olmo .mid{text-align:center;padding:34px 52px 0;flex:none;position:relative}
    .olmo .mid h2{font-family:'Gloock',serif;font-size:58px;line-height:1.05;font-weight:400;margin-top:18px}
    .olmo .mid h2 em{font-style:italic}
    .olmo .mid p{font-size:15px;line-height:1.65;opacity:.68;max-width:50ch;margin:16px auto 0}
    .olmo .mid .hand{position:absolute;right:76px;top:84px;transform:rotate(-7deg);width:172px;text-align:left}
    .olmo .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:28px 52px 0;flex:none}
    .olmo .cards > div{border-radius:14px;overflow:hidden;background:#eef0e2;padding:0 0 18px}
    .olmo .cards .ph{height:160px;background-size:cover;background-position:center}
    .olmo .cards h4{font-family:'Gloock',serif;font-size:21px;font-weight:400;margin:14px 18px 6px}
    .olmo .cards p{font-size:13px;line-height:1.5;opacity:.66;margin:0 18px}
    .olmo .mq{background:#23251c;color:#f8f4ea;margin-top:28px}`,
    html: `
    <div class="bar"><div class="wm">Casa Olmo</div>
      <div class="nv"><span>La casa</span><span>Estancias</span><span>Mesa</span><span>Termas</span></div>
      <div class="ghost">Reservar</div></div>
    <div class="split">
      <div class="im" style="background-image:${photo('hills', 'tuscan', 5, 760, 440)}"></div>
      <div class="blk"><div class="kick">¿Prisa? Nunca oímos hablar de ella.</div>
        <h1>Siete habitaciones que <b>PIDEN</b> <em>quedarse</em>.</h1>
        <p>Chimenea en cada una, vistas al valle y absolutamente nada que hacer. A dos horas de Madrid.</p>
        <div class="btnp">Ver disponibilidad</div></div></div>
    <div class="mid"><span class="stick">Sierra de Gredos · Ávila</span>
      <h2>Échale un <em>vistazo</em><br>a la casa</h2>
      <p>Una casa de piedra rehabilitada en 2019, con siete estancias, termas al aire libre y mesa compartida a las nueve.</p>
      <div class="hand">lo de la mesa<br>compartida engancha<span class="arrow">↙</span></div></div>
    <div class="cards">
      <div><div class="ph" style="background-image:${photo('bedroom', 'chair', 21, 440, 260, { wall: '#e6ddc9', velvet: '#5c6b47', cloth: '#9a7c5e', skin: '#c99064' })}"></div>
        <h4>Las estancias</h4><p>Siete, todas distintas, todas con chimenea.</p></div>
      <div><div class="ph" style="background-image:${photo('table', 'dish', 23, 440, 220, { table: '#241a10', plate: '#3f3528' })}"></div>
        <h4>La mesa</h4><p>Menú corto con lo que llega de la huerta.</p></div>
      <div><div class="ph" style="background-image:${photo('bath', 'water', 27, 440, 220, { shallow: '#9ec4bd', deep: '#2f5b56' })}"></div>
        <h4>Las termas</h4><p>Agua caliente al aire libre, de sol a sol.</p></div></div>
    ${marquee('despacio, que hay prisa', 4)}
    ${foot({ brand: 'Casa Olmo', about: 'Casa rural de siete habitaciones en la Sierra de Gredos. Registro turístico AV-0412.',
      groups: [{ h: 'La casa', items: ['Estancias', 'Termas', 'Mesa', 'Galería'] },
               { h: 'Reservas', items: ['Disponibilidad', 'Condiciones', 'Bonos regalo'] },
               { h: 'Cómo llegar', items: ['Navarredonda', 'A 2 h de Madrid'] }] },
      '© 2026 Casa Olmo')}`,
  });

  /* ---------------------------------------------------------------- 3
     Blush wellness page: arch photo, stats in italic serif. */
  const piel = () => ({
    id: 'piel',
    css: `${base.replace(/\.st(?![\w-])/g, '.piel')}
    .piel{background:#f6efe9;color:#2e211d}
    .piel .hero{position:relative;height:374px;margin:0 52px;border-radius:18px;overflow:hidden;flex:none}
    .piel .hero .im{position:absolute;inset:0;background-size:cover;background-position:center}
    .piel .hero .tint{position:absolute;inset:0;background:linear-gradient(90deg,rgba(60,36,30,.42),rgba(60,36,30,.04))}
    .piel .hero .tx{position:absolute;left:46px;top:50%;transform:translateY(-50%);color:#fff7f2;width:52%}
    .piel .hero h1{font-family:'Gloock',serif;font-size:50px;line-height:1.08;font-weight:400}
    .piel .hero h1 em{font-style:italic}
    .piel .hero .btnp{background:#fff7f2;color:#2e211d;margin-top:22px}
    .piel .mid{text-align:center;padding:34px 52px 0;flex:none}
    .piel .mid h2{font-family:'Gloock',serif;font-size:52px;line-height:1.14;font-weight:400;max-width:21ch;margin:0 auto}
    .piel .mid h2 em{font-style:italic}
    .piel .mid h2 i{font-style:normal;background:#e8cfc4;border-radius:999px;padding:0 14px}
    .piel .stats b{color:#8c4a3a}
    .piel .row{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding:12px 52px 0;flex:none}
    .piel .row > div{background:#efe2da;border-radius:16px;padding:22px;text-align:center}
    .piel .row .ph{height:150px;border-radius:12px;background-size:cover;background-position:center;margin-bottom:14px}
    .piel .row h4{font-family:'Gloock',serif;font-size:20px;font-weight:400}
    .piel .row span{font-size:13px;opacity:.6;display:block;margin-top:4px}
    .piel .mq{background:#8c4a3a;color:#f6efe9;margin-top:30px}`,
    html: `
    <div class="bar"><div class="wm">Piel</div>
      <div class="nv"><span>Rutina</span><span>Productos</span><span>Ingredientes</span><span>Diario</span></div>
      <div class="ghost">Cesta · 2</div></div>
    <div class="hero">
      <div class="im" style="background-image:${photo('skin', 'macro', 11, 980, 440)}"></div>
      <div class="tint"></div>
      <div class="tx"><h1>Encuentra tu <em>equilibrio</em> con Piel</h1>
        <div class="btnp">Ver la rutina</div></div></div>
    <div class="mid"><h2>No necesitas <i>más</i> cremas. <em>Solo mejores.</em></h2></div>
    <div class="stats">
      <div><b>6</b><span>fórmulas</span></div>
      <div><b>0</b><span>perfume</span></div>
      <div><b>4,8</b><span>sobre 5</span></div></div>
    <div class="row">
      <div><div class="ph" style="background-image:${photo('bottles', 'bottles', 7, 420, 300)}"></div>
        <h4>Limpieza</h4><span>Gel suave · 150 ml</span></div>
      <div><div class="ph" style="background-image:${photo('cream', 'bottles', 13, 420, 300, { tones: ['#a9674a', '#c08a63', '#8d5339', '#d0a07a'] })}"></div>
        <h4>Hidratación</h4><span>Crema ligera · 50 ml</span></div>
      <div><div class="ph" style="background-image:${photo('linen', 'linen', 17, 420, 300, { cloth: '#e3cdc0' })}"></div>
        <h4>Protección</h4><span>SPF 50 · 50 ml</span></div></div>
    ${marquee('fabricado en Alicante', 4)}
    ${foot({ brand: 'Piel', about: 'Cosmética corta, sin perfume y fabricada en Alicante. Cruelty free.',
      groups: [{ h: 'Tienda', items: ['Rutina', 'Limpieza', 'Hidratación', 'Packs'] },
               { h: 'Ayuda', items: ['Envíos', 'Devoluciones', 'Contacto'] },
               { h: 'Nosotras', items: ['Fórmulas', 'Ingredientes', 'Diario'] }] },
      '© 2026 Piel Laboratorios SL · CIF B-54xxxxxx')}
    ${cookie}`,
  });

  /* ---------------------------------------------------------------- 4
     Deep olive restaurant, serif display over a dark photograph. */
  const brasa = () => ({
    id: 'brasa',
    css: `${base.replace(/\.st(?![\w-])/g, '.brasa')}
    .brasa{background:#f4efe3;color:#22220f}
    .brasa .hero{position:relative;height:402px;margin:0 52px;border-radius:16px;overflow:hidden;flex:none}
    .brasa .hero .im{position:absolute;inset:0;background-size:cover;background-position:center}
    .brasa .hero .tint{position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,18,8,.5),rgba(18,18,8,.08) 46%,rgba(18,18,8,.72))}
    .brasa .hero h1{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);
      text-align:center;font-family:'Gloock',serif;font-size:84px;line-height:1;color:#f4efe3;font-weight:400}
    .brasa .hero h1 em{font-style:italic;color:#dfe08a}
    .brasa .hero .stick{position:absolute;left:36px;top:30px;background:#dfe08a;color:#22220f}
    .brasa .mid{display:grid;grid-template-columns:1fr 1.1fr;gap:42px;padding:34px 52px 0;align-items:center;flex:none}
    .brasa .mid h2{font-family:'Gloock',serif;font-size:42px;line-height:1.12;font-weight:400}
    .brasa .mid h2 em{font-style:italic}
    .brasa .mid p{font-size:15px;line-height:1.68;opacity:.7;margin-top:14px}
    .brasa .mid .btnp{background:#3c4a1e;color:#f4efe3;margin-top:18px}
    .brasa .menu{background:#3c4a1e;color:#eef0dd;border-radius:16px;padding:26px 30px}
    .brasa .d{display:flex;align-items:baseline;gap:12px;padding:12px 0;border-top:1px solid rgba(238,240,221,.16)}
    .brasa .d:first-child{border-top:0}
    .brasa .d .n{font-family:'Gloock',serif;font-size:20px;white-space:nowrap}
    .brasa .d .dot{flex:1;border-bottom:1px dotted rgba(238,240,221,.3);transform:translateY(-5px)}
    .brasa .d .p{font-size:17px;color:#dfe08a;font-variant-numeric:tabular-nums}
    .brasa .d .s{font-size:12.5px;opacity:.62;margin-top:3px}
    .brasa .mq{background:#22220f;color:#f4efe3;margin-top:30px}`,
    html: `
    <div class="bar"><div class="wm">Brasa</div>
      <div class="nv"><span>Carta</span><span>Bodega</span><span>La casa</span></div>
      <div class="ghost">Reservar mesa</div></div>
    <div class="hero">
      <div class="im" style="background-image:${photo('food', 'dish', 29, 980, 460, { table: '#1b120b', plate: '#3a2f24', food: ['#e0761f', '#a8461a', '#f0b94a'] })}"></div>
      <div class="tint"></div>
      <span class="stick">Menú de marzo</span>
      <h1>Brasa, <em>sal</em><br>y poco más</h1></div>
    <div class="mid">
      <div><h2>Cinco pases que <em>cambian</em> cada semana</h2>
        <p>Según lo que llega de la lonja y de la huerta de El Palmar. Servicio de martes a sábado.</p>
        <div class="btnp">Ver el menú completo</div></div>
      <div class="menu">
        <div class="d"><div><div class="n">Anchoa curada en casa</div><div class="s">Pan de cristal, mantequilla ahumada</div></div><div class="dot"></div><div class="p">9 €</div></div>
        <div class="d"><div><div class="n">Alcachofa a la brasa</div><div class="s">Yema curada y avellana</div></div><div class="dot"></div><div class="p">14 €</div></div>
        <div class="d"><div><div class="n">Sepia y su tinta</div><div class="s">Guisantes del Maresme</div></div><div class="dot"></div><div class="p">18 €</div></div>
        <div class="d"><div><div class="n">Costilla de vaca vieja</div><div class="s">Cuarenta días de maduración</div></div><div class="dot"></div><div class="p">26 €</div></div></div></div>
    ${marquee('menú completo 58 € · maridaje 24 €', 3)}
    ${foot({ brand: 'Brasa', about: 'Cocina de fuego en el Carmen. Servicio de martes a sábado, comidas y cenas.',
      groups: [{ h: 'Carta', items: ['Menú degustación', 'A la carta', 'Bodega'] },
               { h: 'Reservas', items: ['Mesa', 'Grupos', 'Eventos'] },
               { h: 'Dónde', items: ['Calle Roteros 9', '963 92 14 70'] }] },
      '© 2026 Brasa · Valencia')}`,
  });

  /* ---------------------------------------------------------------- 5
     Shop page with lavender block and testimonials. */
  const ovillo = () => ({
    id: 'ovillo',
    css: `${base.replace(/\.st(?![\w-])/g, '.ovillo')}
    .ovillo{background:#f7f3ec;color:#2a2118}
    .ovillo .mq.top{background:#141414;color:#f7f3ec}
    .ovillo .promo{display:grid;grid-template-columns:1fr 1fr;gap:0;height:340px;margin:0 52px;flex:none}
    .ovillo .pc{background:#d3cbf2;padding:40px 42px;display:flex;flex-direction:column;
      justify-content:center;gap:15px;border-radius:16px 0 0 16px}
    .ovillo .pc h1{font-family:'Gloock',serif;font-size:50px;line-height:1.08;font-weight:400}
    .ovillo .pc h1 em{font-style:italic}
    .ovillo .pc p{font-size:14.5px;line-height:1.6;opacity:.78;max-width:30ch}
    .ovillo .pc .btnp{background:#2a2118;color:#f7f3ec;align-self:flex-start}
    .ovillo .ps{background-size:cover;background-position:center;border-radius:0 16px 16px 0}
    .ovillo .shelf{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;padding:28px 52px 0;flex:none}
    .ovillo .p .im{height:190px;border-radius:12px;background-size:cover;background-position:center}
    .ovillo .p .n{font-size:16px;font-weight:600;margin:11px 0 2px}
    .ovillo .p .m{font-size:12.5px;opacity:.6}
    .ovillo .p .pr{margin-top:6px;font-size:17px;font-weight:700;font-variant-numeric:tabular-nums}
    .ovillo .tst{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:30px 52px 0;flex:none}
    .ovillo .tst > div{background:#edf0e0;border-radius:16px;padding:22px}
    .ovillo .tst p{font-family:'Lora',serif;font-size:15px;line-height:1.6;font-style:italic}
    .ovillo .tst .who{display:flex;align-items:center;gap:10px;margin-top:14px;font-size:12.5px;opacity:.65}
    .ovillo .tst .av{width:30px;height:30px;border-radius:50%;background-size:cover;background-position:center;flex:none}`,
    html: `
    ${marquee('rebajas de invierno · hasta −40 %', 4).replace('class="mq"', 'class="mq top"')}
    <div class="bar"><div class="wm">Ovillo</div>
      <div class="nv"><span>Punto</span><span>Lanas</span><span>Patrones</span><span>Talleres</span></div>
      <div class="ghost">Cesta · 3</div></div>
    <div class="promo">
      <div class="pc"><h1>Rebajas de <em>invierno</em></h1>
        <p>Hasta un 40 % en lana merina y alpaca hilada en Asturias. Hasta fin de existencias.</p>
        <div class="btnp">Ver rebajas</div></div>
      <div class="ps" style="background-image:${photo('knit', 'knit', 47, 700, 400, { yarn: '#9c5a44' })}"></div></div>
    <div class="shelf">
      <div class="p"><div class="im" style="background-image:${photo('sweater', 'knit', 53, 380, 280, { yarn: '#c2955c' })}"></div>
        <div class="n">Jersey Duna</div><div class="m">Merina · trenzado</div><div class="pr">79,00 €</div></div>
      <div class="p"><div class="im" style="background-image:${bg('knit', 59, 380, 280, { yarn: '#3f5b46' })}"></div>
        <div class="n">Cárdigan Ría</div><div class="m">Lana y alpaca</div><div class="pr">118,00 €</div></div>
      <div class="p"><div class="im" style="background-image:${bg('knit', 61, 380, 280, { yarn: '#2c3d5c' })}"></div>
        <div class="n">Chaleco Sella</div><div class="m">Algodón orgánico</div><div class="pr">64,00 €</div></div>
      <div class="p"><div class="im" style="background-image:${photo('linen', 'linen', 67, 380, 280, { cloth: '#cdd3c4' })}"></div>
        <div class="n">La colección</div><div class="m">42 prendas</div><div class="pr">Ver todo</div></div></div>
    <div class="tst">
      <div><p>“Llegó en dos días y la lana es exactamente la del catálogo.”</p>
        <div class="who"><span class="av" style="background-image:${bg('macro', 71, 90, 90, { skin: '#d9a98b' })}"></span>Marta R. · Gijón</div></div>
      <div><p>“El cárdigan tiene tres inviernos y está igual que el primer día.”</p>
        <div class="who"><span class="av" style="background-image:${bg('macro', 73, 90, 90, { skin: '#c08f6e' })}"></span>Lucía P. · Bilbao</div></div>
      <div><p>“Cambié la talla sin preguntas y sin pagar el envío.”</p>
        <div class="who"><span class="av" style="background-image:${bg('macro', 79, 90, 90, { skin: '#e0b391' })}"></span>Nuria S. · Madrid</div></div></div>
    ${foot({ brand: 'Ovillo', about: 'Punto hecho en Asturias con lana merina y alpaca. Tienda en Gijón y online.',
      groups: [{ h: 'Tienda', items: ['Jerséis', 'Cárdigans', 'Lanas', 'Rebajas'] },
               { h: 'Ayuda', items: ['Guía de tallas', 'Envíos', 'Cambios'] },
               { h: 'Taller', items: ['Cursos', 'Patrones', 'Reparaciones'] }] },
      '© 2026 Ovillo · Hecho en Asturias')}`,
  });

  /* ---------------------------------------------------------------- 6
     Coffee shop: sage block, product row, handwritten aside. */
  const tinta = () => ({
    id: 'tinta',
    css: `${base.replace(/\.st(?![\w-])/g, '.tinta')}
    .tinta{background:#f7f3e8;color:#241c12}
    .tinta .hero{display:grid;grid-template-columns:1fr 1fr;height:386px;margin:0 52px;flex:none}
    .tinta .cp{background:#c9d4ac;border-radius:16px 0 0 16px;padding:42px 40px;
      display:flex;flex-direction:column;justify-content:center;gap:15px;position:relative}
    .tinta .cp h1{font-family:'Gloock',serif;font-size:54px;line-height:1.04;font-weight:400}
    .tinta .cp h1 em{font-style:italic}
    .tinta .cp p{font-size:14.5px;line-height:1.62;opacity:.78;max-width:30ch}
    .tinta .cp .btnp{background:#241c12;color:#f7f3e8;align-self:flex-start}
    .tinta .cp .stick{position:absolute;right:28px;top:26px;transform:rotate(3deg)}
    .tinta .sh{background-size:cover;background-position:center;border-radius:0 16px 16px 0}
    .tinta .mid{text-align:center;padding:32px 52px 0;flex:none;position:relative}
    .tinta .mid h2{font-family:'Gloock',serif;font-size:46px;font-weight:400;line-height:1.1}
    .tinta .mid h2 em{font-style:italic}
    .tinta .mid .hand{position:absolute;left:80px;top:40px;transform:rotate(-6deg);width:164px;text-align:left}
    .tinta .row{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding:24px 52px 0;flex:none}
    .tinta .c{display:flex;gap:15px;align-items:center;background:#efe9da;border-radius:14px;padding:16px}
    .tinta .c .im{width:84px;height:84px;flex:none;border-radius:10px;background-size:cover;background-position:center}
    .tinta .c b{display:block;font-family:'Gloock',serif;font-size:18px;font-weight:400}
    .tinta .c span{font-size:12.5px;opacity:.6}
    .tinta .c i{font-style:normal;font-size:15px;font-weight:700;display:block;margin-top:5px}
    .tinta .mq{background:#241c12;color:#f7f3e8;margin-top:30px}`,
    html: `
    <div class="bar"><div class="wm">Tinta &amp; Grano</div>
      <div class="nv"><span>Café</span><span>Suscripción</span><span>Cursos</span><span>Tostadero</span></div>
      <div class="ghost">Cesta · 2</div></div>
    <div class="hero">
      <div class="cp"><span class="stick">Tueste de la semana</span>
        <h1>Etiopía<br><em>Guji Natural</em></h1>
        <p>Melocotón, jazmín y un final largo a té negro. Tostado el martes, en tu casa el jueves.</p>
        <div class="btnp">Añadir a la cesta · 14,50 €</div></div>
      <div class="sh" style="background-image:${photo('coffee', 'coffee', 71, 700, 440, { table: '#4a2b17', crema: '#b06a30', saucer: '#f3ece0' })}"></div></div>
    <div class="mid"><h2>También te <em>gustará</em></h2>
      <div class="hand">este es el que<br>más repetimos<span class="arrow">↘</span></div></div>
    <div class="row">
      <div class="c"><div class="im" style="background-image:${bg('coffee', 73, 200, 200, { table: '#2f1d12', crema: '#8e5326' })}"></div>
        <div><b>Colombia Huila</b><span>Lavado · 250 g</span><i>11,00 €</i></div></div>
      <div class="c"><div class="im" style="background-image:${bg('coffee', 79, 200, 200, { table: '#5a3a1e', crema: '#c98b46' })}"></div>
        <div><b>Kenia Nyeri</b><span>Lavado · 250 g</span><i>13,20 €</i></div></div>
      <div class="c"><div class="im" style="background-image:${bg('bottles', 83, 200, 200, { wall: '#e4d8c6', tones: ['#6b4423', '#8a5a2b', '#3d2a18', '#a07440'] })}"></div>
        <div><b>Molinillo cónico</b><span>Acero y nogal</span><i>89,00 €</i></div></div></div>
    ${marquee('tostamos los martes', 4)}
    ${foot({ brand: 'Tinta &amp; Grano', about: 'Tostadero propio en Benimaclet. Café de especialidad y cursos de cata.',
      groups: [{ h: 'Café', items: ['Orígenes', 'Suscripción', 'Molido', 'Cápsulas'] },
               { h: 'Aprender', items: ['Cursos', 'Métodos', 'Blog'] },
               { h: 'Pedidos', items: ['Envíos', 'Devoluciones', 'Mayorista'] }] },
      '© 2026 Tinta &amp; Grano SL')}
    ${cookie}`,
  });

  /* ---------------------------------------------------------------- 7
     Photographer: big display over a full-bleed photograph. */
  const lumen = () => ({
    id: 'lumen',
    css: `${base.replace(/\.st(?![\w-])/g, '.lumen')}
    .lumen{background:#efece4;color:#1b1a18}
    .lumen .hero{position:relative;height:408px;margin:0 52px;border-radius:16px;overflow:hidden;flex:none}
    .lumen .hero .im{position:absolute;inset:0;background-size:cover;background-position:center}
    .lumen .hero .tint{position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,12,18,.42),rgba(14,12,18,.6))}
    .lumen .hero .tx{position:absolute;inset:0;display:flex;flex-direction:column;
      align-items:center;justify-content:center;color:#f3f0e8;text-align:center}
    .lumen .hero .kick{font-size:11.5px;letter-spacing:.3em;text-transform:uppercase;opacity:.8;margin-bottom:16px}
    .lumen .hero h1{font-family:'Gloock',serif;font-size:76px;line-height:1.02;font-weight:400;max-width:15ch}
    .lumen .hero h1 em{font-style:italic}
    .lumen .big{text-align:center;font-family:'Gloock',serif;font-size:96px;line-height:1;
      font-weight:400;padding:28px 0 0;flex:none;letter-spacing:-.02em}
    .lumen .big em{font-style:italic;color:#8d9ab4}
    .lumen .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:24px 52px 0;flex:none}
    .lumen .grid > div{height:184px;border-radius:12px;background-size:cover;background-position:center}
    .lumen .grid > div:nth-child(2){border-radius:999px 999px 12px 12px}
    .lumen .say{display:grid;grid-template-columns:1fr 1fr;gap:38px;padding:30px 52px 0;align-items:center;flex:none}
    .lumen .say p{font-family:'Lora',serif;font-style:italic;font-size:21px;line-height:1.6}
    .lumen .say .btnp{background:#1b1a18;color:#efece4;margin-top:16px}
    .lumen .mq{background:#1b1a18;color:#efece4;margin-top:28px}`,
    html: `
    <div class="bar"><div class="wm">Lumen</div>
      <div class="nv"><span>Series</span><span>Bodas</span><span>Editorial</span><span>Copias</span></div>
      <div class="ghost">Disponibilidad</div></div>
    <div class="hero">
      <div class="im" style="background-image:${photo('coast', 'hills', 31, 980, 470, { sky: ['#101430', '#44274f', '#a3524a', '#e8a470'], ridge: '#0d0c14' })}"></div>
      <div class="tint"></div>
      <div class="tx"><div class="kick">Serie 04 — Costa Brava, invierno</div>
        <h1>La luz <em>que queda</em></h1></div></div>
    <div class="big">Mira <em>el</em> trabajo</div>
    <div class="grid">
      <div style="background-image:${photo('hills', 'tuscan', 37, 400, 260)}"></div>
      <div style="background-image:${photo('pool', 'water', 41, 400, 300, { shallow: '#5f9fb0', deep: '#113d52' })}"></div>
      <div style="background-image:${photo('bedroom', 'chair', 43, 400, 260, { wall: '#d8cfc0', velvet: '#43523f', cloth: '#8d94a8', skin: '#bf8a62' })}"></div>
      <div style="background-image:${photo('coast', 'hills', 47, 400, 260, { sky: ['#1b2340', '#4e3a5e', '#b06a52', '#f0bd86'], ridge: '#141726' })}"></div></div>
    <div class="say">
      <div><p>“Nos devolvió fotos que no sabíamos que queríamos hasta que las vimos.”</p>
        <div class="btnp">Ver disponibilidad 2026</div></div>
      <span class="stars"><b>★★★★★</b>5,0 · 48 bodas fotografiadas</span></div>
    ${marquee('disponible en toda la península', 4)}
    ${foot({ brand: 'Lumen', about: 'Fotografía de paisaje, bodas y editorial. Trabajo en toda la península.',
      groups: [{ h: 'Trabajo', items: ['Series', 'Bodas', 'Editorial'] },
               { h: 'Tienda', items: ['Copias', 'Ediciones', 'Libros'] },
               { h: 'Contacto', items: ['hola@lumen.photo', 'Disponibilidad'] }] },
      '© 2026 Lumen')}`,
  });

  /* ---------------------------------------------------------------- 8
     Clinic, kept soft: sage block, arch photo, testimonial row. */
  const meridiana = () => ({
    id: 'meridiana',
    css: `${base.replace(/\.st(?![\w-])/g, '.meridiana')}
    .meridiana{background:#f4f3ed;color:#1f2a24}
    .meridiana .top{display:grid;grid-template-columns:1.05fr 1fr;gap:38px;padding:14px 52px 0;align-items:center;flex:none}
    .meridiana .top h1{font-family:'Gloock',serif;font-size:58px;line-height:1.06;font-weight:400;margin-top:16px}
    .meridiana .top h1 em{font-style:italic;color:#5c7a5e}
    .meridiana .top p{font-size:15.5px;line-height:1.68;opacity:.7;margin-top:16px;max-width:36ch}
    .meridiana .top .btnp{background:#1f2a24;color:#f4f3ed;margin-top:20px}
    .meridiana .top .arch{height:328px}
    .meridiana .band{background:#cfdcc6;margin:30px 52px 0;border-radius:18px;padding:28px 36px;
      display:flex;justify-content:space-between;align-items:center;flex:none}
    .meridiana .band h3{font-family:'Gloock',serif;font-size:32px;font-weight:400;max-width:16ch}
    .meridiana .band h3 em{font-style:italic}
    .meridiana .band .btnp{background:#1f2a24;color:#f4f3ed}
    .meridiana .stats b{color:#5c7a5e}
    .meridiana .tst{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:8px 52px 0;flex:none}
    .meridiana .tst > div{background:#eaeade;border-radius:16px;padding:20px}
    .meridiana .tst p{font-family:'Lora',serif;font-style:italic;font-size:14.5px;line-height:1.6}
    .meridiana .tst .who{display:flex;align-items:center;gap:10px;margin-top:12px;font-size:12.5px;opacity:.65}
    .meridiana .tst .av{width:28px;height:28px;border-radius:50%;background-size:cover;flex:none}
    .meridiana .mq{background:#1f2a24;color:#f4f3ed;margin-top:28px}`,
    html: `
    <div class="bar"><div class="wm">Meridiana</div>
      <div class="nv"><span>Tratamientos</span><span>Equipo</span><span>Precios</span><span>Blog</span></div>
      <div class="ghost">Pedir cita</div></div>
    <div class="top">
      <div><span class="stick">Primera cita sin coste</span>
        <h1>Cuidarte los dientes <em>sin sustos</em> en la factura</h1>
        <p>Diagnóstico completo con radiografía y presupuesto cerrado por escrito antes de empezar.</p>
        <div class="btnp">Pedir cita online</div></div>
      <div class="arch" style="background-image:${photo('clinic', 'studio', 89, 560, 440, { wall: '#dfe4d6', pouf: '#b6ab8c', cloth: '#6d8268', skin: '#c08a63' })}"></div></div>
    <div class="band"><h3>Dieciocho años <em>en el mismo barrio</em></h3>
      <div class="btnp">Conocer al equipo</div></div>
    <div class="stats">
      <div><b>4,9</b><span>612 reseñas</span></div>
      <div><b>24 h</b><span>urgencias</span></div>
      <div><b>0 %</b><span>financiación</span></div></div>
    <div class="tst">
      <div><p>“Me dijeron el precio antes de tocarme nada. Eso ya es raro.”</p>
        <div class="who"><span class="av" style="background-image:${bg('macro', 91, 90, 90, { skin: '#d9a98b' })}"></span>Javier M.</div></div>
      <div><p>“Fui de urgencias un domingo y me atendieron en media hora.”</p>
        <div class="who"><span class="av" style="background-image:${bg('macro', 97, 90, 90, { skin: '#c08f6e' })}"></span>Pilar A.</div></div>
      <div><p>“Llevo con ellos desde que abrieron. Nunca me han vendido de más.”</p>
        <div class="who"><span class="av" style="background-image:${bg('macro', 101, 90, 90, { skin: '#e0b391' })}"></span>Rosa T.</div></div></div>
    ${marquee('Ruzafa · Valencia', 5)}
    ${foot({ brand: 'Clínica Meridiana', about: 'Odontología y estética dental en Ruzafa desde 2008. Dir. médica Dra. E. Soler, col. 46-xxxx.',
      groups: [{ h: 'Tratamientos', items: ['Implantes', 'Ortodoncia', 'Estética', 'Infantil'] },
               { h: 'Clínica', items: ['Equipo', 'Instalaciones', 'Precios'] },
               { h: 'Cita', items: ['960 22 14 08', 'Calle Cádiz 48'] }] },
      '© 2026 Clínica Meridiana · Registro sanitario 46-C-xxxx')}
    ${cookie}`,
  });

  const list = [flow, olmo, piel, brasa, tinta, ovillo, lumen, meridiana];

  /* Built lazily on first call so the canvas work happens once, at init. */
  let built = null;
  function all() {
    if (!built) built = list.map((f) => f());
    return built;
  }
  return { all };
})();
