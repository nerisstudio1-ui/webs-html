/* The mock sites that ride the conveyor.
 *
 * These follow the house style of the work shown on nerisstudio.com: cream
 * grounds, a large photographic hero, display type set big and allowed to
 * overlap the image, one earthy accent block, and a small grid of supporting
 * photos. No dashboards, no stat bands, no listing tables — those read as
 * software screens, and the studio's portfolio is editorial.
 *
 * Two display registers, used deliberately: Instrument Serif for the places
 * that want elegance (villa, restaurant, photography) and Montserrat 900 caps
 * for the places that want volume (pilates, skincare). The italic serif stands
 * in for the script accent the real portfolio uses.
 *
 * Each site is authored at 1440x900 and scaled down bodily by the card, so
 * the proportions and type sizes stay truthful. The card shows 760 of those
 * 900 pixels and scrolls the rest as it crosses the frame. */

const SITES = (() => {
  const bg = (scene, seed, w, h, opts) => ART.bg(scene, seed, w, h, opts);

  /* Shared skeleton: every site gets the same quiet top bar, so the cards read
     as a set of sites by one studio rather than nine unrelated things. */
  const base = `
    .st{display:flex;flex-direction:column}
    .st .bar{display:flex;align-items:center;justify-content:space-between;
      padding:30px 54px;flex:none}
    .st .wm{font-size:21px;font-weight:700;letter-spacing:.22em;text-transform:uppercase}
    .st .nv{display:flex;gap:30px;font-size:13px;letter-spacing:.1em;text-transform:uppercase;opacity:.62}
    .st .pill{border:1px solid currentColor;border-radius:999px;padding:10px 22px;
      font-size:12px;letter-spacing:.12em;text-transform:uppercase;opacity:.85}`;

  /* ---------------------------------------------------------------- 1 */
  const flow = () => ({
    id: 'flow',
    css: `${base.replace(/\.st/g, '.flow')}
    .flow{background:#f2eee4;color:#1d2420;font-family:'Work Sans',sans-serif}
    .flow .hero{position:relative;height:452px;margin:0 54px;overflow:hidden;flex:none}
    .flow .hero .im{position:absolute;inset:0;background-size:cover;background-position:center}
    .flow .hero .tint{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,40,46,.3),rgba(8,40,46,.12))}
    .flow .big{position:absolute;left:0;right:0;top:92px;text-align:center;
      font-family:'Montserrat',sans-serif;font-weight:900;font-size:186px;line-height:.8;
      letter-spacing:.012em;color:#f6f3ea;text-transform:uppercase}
    .flow .scr{position:absolute;left:0;right:0;top:206px;text-align:center;
      font-family:'Instrument Serif',serif;font-style:italic;font-size:132px;color:#f2eee4}
    .flow .cap{position:absolute;left:34px;bottom:30px;right:34px;display:flex;
      justify-content:space-between;align-items:flex-end;color:#f6f3ea}
    .flow .cap p{font-size:19px;line-height:1.4;max-width:30ch;font-weight:500}
    .flow .cap .btn{background:#f6f3ea;color:#16302f;padding:16px 30px;border-radius:999px;
      font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
    .flow .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:26px 54px 0}
    .flow .grid div{height:206px;background-size:cover;background-position:center}
    .flow .meta{display:flex;justify-content:space-between;padding:20px 54px;
      font-size:13px;letter-spacing:.1em;text-transform:uppercase;opacity:.55}`,
    html: `
    <div class="bar"><div class="wm">Flow</div>
      <div class="nv"><span>Clases</span><span>Horarios</span><span>Bonos</span><span>Estudio</span></div>
      <div class="pill">Primera clase gratis</div></div>
    <div class="hero">
      <div class="im" style="background-image:${bg('water', 3, 980, 520)}"></div>
      <div class="tint"></div>
      <div class="big">Pilates</div>
      <div class="scr">&amp; yoga</div>
      <div class="cap"><p>Clases reducidas en pleno centro, de siete de la mañana a diez de la noche.</p>
        <div class="btn">Reservar plaza</div></div></div>
    <div class="grid">
      <div style="background-image:${bg('water', 9, 460, 300, { shallow: '#5fcfd2', deep: '#115f73' })}"></div>
      <div style="background-image:${bg('room', 13, 460, 300, { wall: '#ded6c6', floor: '#9b7b56', object: '#3f5450' })}"></div>
      <div style="background-image:${bg('macro', 17, 460, 300, { skin: '#d9a98b' })}"></div></div>
    <div class="meta"><span>Reformer · Mat · Yoga</span><span>Valencia — Ruzafa</span></div>`,
  });

  /* ---------------------------------------------------------------- 2 */
  const olmo = () => ({
    id: 'olmo',
    css: `${base.replace(/\.st/g, '.olmo')}
    .olmo{background:#f7f2e7;color:#2b2a20;font-family:'Work Sans',sans-serif}
    .olmo .wm{font-family:'Instrument Serif',serif;font-size:28px;letter-spacing:.06em;text-transform:none;font-weight:400}
    .olmo .head{text-align:center;padding:14px 54px 26px;flex:none}
    .olmo .head .kick{font-size:12px;letter-spacing:.34em;text-transform:uppercase;color:#8d8571}
    .olmo .head h1{font-family:'Instrument Serif',serif;font-size:82px;line-height:1.02;
      font-weight:400;letter-spacing:.06em;text-transform:uppercase;margin:16px 0 0}
    .olmo .head h1 em{font-style:italic;text-transform:none;letter-spacing:0}
    .olmo .shot{height:386px;margin:0 54px;background-size:cover;background-position:center;flex:none}
    .olmo .split{display:grid;grid-template-columns:1fr 1fr;margin:18px 54px 0;flex:none}
    .olmo .blk{background:#4e5b36;color:#f2efe2;padding:40px 44px;display:flex;
      flex-direction:column;justify-content:center;gap:16px}
    .olmo .blk h3{font-family:'Instrument Serif',serif;font-size:38px;font-weight:400}
    .olmo .blk p{font-size:16px;line-height:1.6;opacity:.82;max-width:34ch}
    .olmo .side{display:grid;grid-template-rows:1fr 1fr;gap:8px;padding-left:8px}
    .olmo .side div{background-size:cover;background-position:center}`,
    html: `
    <div class="bar"><div class="wm">Casa Olmo</div>
      <div class="nv"><span>La casa</span><span>Estancias</span><span>Mesa</span></div>
      <div class="pill">Reservar</div></div>
    <div class="head"><div class="kick">Sierra de Gredos · Ávila</div>
      <h1>Tu <em>refugio</em><br>en la sierra</h1></div>
    <div class="shot" style="background-image:${bg('tuscan', 5, 980, 480)}"></div>
    <div class="split">
      <div class="blk"><h3>Siete estancias</h3>
        <p>Chimenea en cada una, vistas al valle y absolutamente nada que hacer.</p></div>
      <div class="side">
        <div style="background-image:${bg('room', 21, 440, 190, { wall: '#e0d7c2', floor: '#8a6440', object: '#45503a' })}"></div>
        <div style="background-image:${bg('dish', 23, 440, 190, { table: '#241a10', plate: '#3f3528' })}"></div></div></div>`,
  });

  /* ---------------------------------------------------------------- 3 */
  const piel = () => ({
    id: 'piel',
    css: `${base.replace(/\.st/g, '.piel')}
    .piel{background:#efe4dd;color:#3a211c;font-family:'Work Sans',sans-serif}
    .piel .claim{padding:10px 54px 26px;flex:none}
    .piel .claim h1{font-family:'Montserrat',sans-serif;font-weight:900;font-size:76px;
      line-height:.96;letter-spacing:-.03em;text-transform:uppercase;max-width:19ch}
    .piel .claim h1 span{color:#8a3b2d}
    .piel .row{display:grid;grid-template-columns:1.25fr 1fr;gap:16px;margin:0 54px;flex:none}
    .piel .row .im{height:330px;background-size:cover;background-position:center}
    .piel .blk{background:#6d2b24;color:#f3e7e1;padding:36px 38px;display:flex;
      flex-direction:column;justify-content:space-between}
    .piel .blk p{font-size:17px;line-height:1.6;opacity:.86}
    .piel .blk .btn{align-self:flex-start;background:#f3e7e1;color:#6d2b24;padding:15px 28px;
      border-radius:999px;font-size:14px;font-weight:700}
    .piel .shelf{height:250px;margin:16px 54px 0;background-size:cover;background-position:center;flex:none}
    .piel .meta{display:flex;justify-content:space-between;padding:18px 54px;font-size:13px;
      letter-spacing:.1em;text-transform:uppercase;opacity:.55}`,
    html: `
    <div class="bar"><div class="wm">Piel</div>
      <div class="nv"><span>Rutina</span><span>Productos</span><span>Diario</span></div>
      <div class="pill">Cesta · 2</div></div>
    <div class="claim"><h1>No necesitas más cremas. <span>Solo mejores.</span></h1></div>
    <div class="row">
      <div class="im" style="background-image:${bg('macro', 11, 700, 420)}"></div>
      <div class="blk"><p>Seis fórmulas cortas, sin perfume y con lo que de verdad hace algo.
        Fabricadas en Alicante.</p><div class="btn">Ver la rutina</div></div></div>
    <div class="shelf" style="background-image:${bg('bottles', 7, 980, 330)}"></div>
    <div class="meta"><span>Envío en 24 h</span><span>Muestras gratis en cada pedido</span></div>`,
  });

  /* ---------------------------------------------------------------- 4 */
  const brasa = () => ({
    id: 'brasa',
    css: `${base.replace(/\.st/g, '.brasa')}
    .brasa{background:#15100b;color:#f0e6d4;font-family:'Work Sans',sans-serif}
    .brasa .wm{font-family:'Instrument Serif',serif;font-size:30px;letter-spacing:.04em;
      text-transform:none;font-weight:400}
    .brasa .pill{border-color:#c79a4a;color:#c79a4a}
    .brasa .hero{position:relative;height:430px;margin:0 54px;overflow:hidden;flex:none}
    .brasa .hero .im{position:absolute;inset:0;background-size:cover;background-position:center}
    .brasa .hero .tint{position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,10,7,.9) 28%,rgba(14,10,7,.1))}
    .brasa .hero .tx{position:absolute;left:44px;top:50%;transform:translateY(-50%)}
    .brasa .hero .kick{font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:#c79a4a;margin-bottom:18px}
    .brasa h1{font-family:'Instrument Serif',serif;font-size:92px;line-height:.96;font-weight:400}
    .brasa h1 em{font-style:italic;color:#c79a4a}
    .brasa .menu{display:grid;grid-template-columns:1fr 1fr;gap:0 56px;padding:28px 54px 0;flex:none}
    .brasa .d{display:flex;align-items:baseline;gap:14px;padding:15px 0;border-top:1px solid #2a2015}
    .brasa .d .n{font-family:'Instrument Serif',serif;font-size:25px;white-space:nowrap}
    .brasa .d .dot{flex:1;border-bottom:1px dotted #4b3c28;transform:translateY(-6px)}
    .brasa .d .p{font-size:19px;color:#c79a4a;font-variant-numeric:tabular-nums}
    .brasa .d .s{font-size:13px;color:#8e8069;margin-top:4px}`,
    html: `
    <div class="bar"><div class="wm">Brasa</div>
      <div class="nv"><span>Carta</span><span>Bodega</span><span>La casa</span></div>
      <div class="pill">Reservar mesa</div></div>
    <div class="hero">
      <div class="im" style="background-image:${bg('dish', 29, 980, 480, { table: '#1b120b', plate: '#3a2f24', food: ['#e0761f', '#a8461a', '#f0b94a'] })}"></div>
      <div class="tint"></div>
      <div class="tx"><div class="kick">Menú de temporada · marzo</div>
        <h1>Brasa, <em>sal</em><br>y poco más</h1></div></div>
    <div class="menu">
      <div><div class="d"><div><div class="n">Anchoa curada en casa</div>
        <div class="s">Pan de cristal, mantequilla ahumada</div></div><div class="dot"></div><div class="p">9 €</div></div>
        <div class="d"><div><div class="n">Alcachofa a la brasa</div>
        <div class="s">Yema curada y avellana</div></div><div class="dot"></div><div class="p">14 €</div></div></div>
      <div><div class="d"><div><div class="n">Sepia y su tinta</div>
        <div class="s">Guisantes del Maresme</div></div><div class="dot"></div><div class="p">18 €</div></div>
        <div class="d"><div><div class="n">Costilla de vaca vieja</div>
        <div class="s">Cuarenta días de maduración</div></div><div class="dot"></div><div class="p">26 €</div></div></div></div>`,
  });

  /* ---------------------------------------------------------------- 5 */
  const lumen = () => ({
    id: 'lumen',
    css: `${base.replace(/\.st/g, '.lumen')}
    .lumen{background:#0e0d0c;color:#fff;font-family:'Work Sans',sans-serif;position:relative}
    .lumen .full{position:absolute;inset:0;background-size:cover;background-position:center}
    .lumen .sc{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,6,8,.5),rgba(6,6,8,0) 36%,rgba(6,6,8,.78))}
    .lumen .bar,.lumen .mid,.lumen .thumbs{position:relative;z-index:2}
    .lumen .mid{flex:1;display:flex;flex-direction:column;justify-content:center;
      align-items:center;text-align:center;padding:0 54px}
    .lumen .kick{font-size:12px;letter-spacing:.32em;text-transform:uppercase;opacity:.74;margin-bottom:22px}
    .lumen h1{font-family:'Instrument Serif',serif;font-size:118px;line-height:.94;font-weight:400}
    .lumen h1 em{font-style:italic}
    .lumen .thumbs{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:0 54px 40px}
    .lumen .thumbs div{height:150px;background-size:cover;background-position:center;opacity:.72}
    .lumen .thumbs div:first-child{opacity:1;box-shadow:0 0 0 2px #fff}`,
    html: `
    <div class="full" style="background-image:${bg('hills', 31, 980, 620, { sky: ['#0a0c1e', '#3a2047', '#9a4a4a', '#e39a66'], ridge: '#0b0a12' })}"></div>
    <div class="sc"></div>
    <div class="bar"><div class="wm">Lumen</div>
      <div class="nv"><span>Series</span><span>Bodas</span><span>Editorial</span><span>Copias</span></div>
      <div class="pill">Disponibilidad</div></div>
    <div class="mid"><div class="kick">Serie 04 — Costa Brava, invierno</div>
      <h1>La luz <em>que queda</em></h1></div>
    <div class="thumbs">
      <div style="background-image:${bg('hills', 31, 400, 260, { sky: ['#0a0c1e', '#3a2047', '#9a4a4a', '#e39a66'], ridge: '#0b0a12' })}"></div>
      <div style="background-image:${bg('tuscan', 37, 400, 260)}"></div>
      <div style="background-image:${bg('water', 41, 400, 260, { shallow: '#3f93a8', deep: '#0b3d52' })}"></div>
      <div style="background-image:${bg('room', 43, 400, 260, { wall: '#3c3a38', floor: '#262320', object: '#15130f', light: '#fff0d4' })}"></div></div>`,
  });

  /* ---------------------------------------------------------------- 6 */
  const ovillo = () => ({
    id: 'ovillo',
    css: `${base.replace(/\.st/g, '.ovillo')}
    .ovillo{background:#f8f3eb;color:#2b2119;font-family:'Work Sans',sans-serif}
    .ovillo .promo{display:grid;grid-template-columns:1fr 1.15fr;margin:0 54px;flex:none;height:360px}
    .ovillo .pc{background:#a8412a;color:#fdf6ee;padding:44px 42px;display:flex;
      flex-direction:column;justify-content:center;gap:18px}
    .ovillo .pc h1{font-family:'Instrument Serif',serif;font-size:66px;line-height:1;font-weight:400}
    .ovillo .pc h1 em{font-style:italic}
    .ovillo .pc p{font-size:17px;opacity:.86;max-width:28ch}
    .ovillo .pc .btn{align-self:flex-start;background:#fdf6ee;color:#a8412a;padding:15px 30px;
      border-radius:999px;font-weight:700;font-size:15px}
    .ovillo .ps{background-size:cover;background-position:center}
    .ovillo .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;padding:24px 54px 0}
    .ovillo .p .im{height:224px;background-size:cover;background-position:center}
    .ovillo .p .n{font-size:17px;font-weight:600;margin:12px 0 2px}
    .ovillo .p .m{font-size:13px;color:#8b7768}
    .ovillo .p .pr{margin-top:7px;font-size:18px;font-weight:700;font-variant-numeric:tabular-nums}`,
    html: `
    <div class="bar"><div class="wm">Ovillo</div>
      <div class="nv"><span>Punto</span><span>Lanas</span><span>Patrones</span><span>Talleres</span></div>
      <div class="pill">Cesta · 3</div></div>
    <div class="promo">
      <div class="pc"><h1>Rebajas de <em>invierno</em></h1>
        <p>Hasta un 40 % en lana merina y alpaca hilada en Asturias.</p>
        <div class="btn">Ver rebajas</div></div>
      <div class="ps" style="background-image:${bg('knit', 47, 760, 400, { yarn: '#b8452f' })}"></div></div>
    <div class="grid">
      <div class="p"><div class="im" style="background-image:${bg('knit', 53, 380, 300, { yarn: '#c2955c' })}"></div>
        <div class="n">Jersey Duna</div><div class="m">Merina · trenzado</div><div class="pr">79,00 €</div></div>
      <div class="p"><div class="im" style="background-image:${bg('knit', 59, 380, 300, { yarn: '#3f5b46' })}"></div>
        <div class="n">Cárdigan Ría</div><div class="m">Lana y alpaca</div><div class="pr">118,00 €</div></div>
      <div class="p"><div class="im" style="background-image:${bg('knit', 61, 380, 300, { yarn: '#2c3d5c' })}"></div>
        <div class="n">Chaleco Sella</div><div class="m">Algodón orgánico</div><div class="pr">64,00 €</div></div>
      <div class="p"><div class="im" style="background-image:${bg('shop', 67, 380, 300, { wall: '#efe6d8' })}"></div>
        <div class="n">La colección</div><div class="m">42 prendas</div><div class="pr">Ver todo</div></div></div>`,
  });

  /* ---------------------------------------------------------------- 7 */
  const tinta = () => ({
    id: 'tinta',
    css: `${base.replace(/\.st/g, '.tinta')}
    .tinta{background:#f6f1e6;color:#241a10;font-family:'Work Sans',sans-serif}
    .tinta .wm{font-family:'Lora',serif;font-size:25px;letter-spacing:.02em;text-transform:none;font-weight:700}
    .tinta .hero{display:grid;grid-template-columns:1fr 1fr;height:432px;margin:0 54px;flex:none}
    .tinta .cp{display:flex;flex-direction:column;justify-content:center;gap:20px;padding-right:44px}
    .tinta .badge{align-self:flex-start;background:#241a10;color:#f0c45c;font-size:11px;font-weight:700;
      letter-spacing:.2em;text-transform:uppercase;padding:9px 16px;border-radius:999px}
    .tinta h1{font-family:'Lora',serif;font-size:74px;line-height:1.02;font-weight:700;letter-spacing:-.025em}
    .tinta h1 span{color:#8a3a12}
    .tinta .sub{font-size:17px;line-height:1.6;color:#6b5946;max-width:30ch}
    .tinta .buy{display:flex;align-items:center;gap:20px}
    .tinta .btn{background:#8a3a12;color:#fff;padding:17px 34px;border-radius:999px;font-size:15px;font-weight:700}
    .tinta .price{font-family:'Lora',serif;font-size:30px;font-weight:700}
    .tinta .shot{background-size:cover;background-position:center}
    .tinta .row{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding:24px 54px 0}
    .tinta .c{display:flex;gap:16px;align-items:center}
    .tinta .c .im{width:104px;height:104px;flex:none;background-size:cover;background-position:center}
    .tinta .c b{display:block;font-family:'Lora',serif;font-size:18px}
    .tinta .c span{font-size:13px;color:#8a7a63}
    .tinta .c i{font-style:normal;font-size:16px;font-weight:700;display:block;margin-top:5px}`,
    html: `
    <div class="bar"><div class="wm">Tinta &amp; Grano</div>
      <div class="nv"><span>Café</span><span>Suscripción</span><span>Cursos</span></div>
      <div class="pill">Cesta · 2</div></div>
    <div class="hero">
      <div class="cp"><div class="badge">Tueste de la semana</div>
        <h1>Etiopía<br><span>Guji Natural</span></h1>
        <div class="sub">Melocotón, jazmín y un final largo a té negro. Tostado el martes, en tu casa el jueves.</div>
        <div class="buy"><div class="btn">Añadir a la cesta</div><div class="price">14,50 €</div></div></div>
      <div class="shot" style="background-image:${bg('coffee', 71, 700, 460, { table: '#4a2b17', crema: '#b06a30', saucer: '#f3ece0' })}"></div></div>
    <div class="row">
      <div class="c"><div class="im" style="background-image:${bg('coffee', 73, 240, 240, { table: '#2f1d12', crema: '#8e5326' })}"></div>
        <div><b>Colombia Huila</b><span>Lavado · 250 g</span><i>11,00 €</i></div></div>
      <div class="c"><div class="im" style="background-image:${bg('coffee', 79, 240, 240, { table: '#5a3a1e', crema: '#c98b46' })}"></div>
        <div><b>Kenia Nyeri</b><span>Lavado · 250 g</span><i>13,20 €</i></div></div>
      <div class="c"><div class="im" style="background-image:${bg('bottles', 83, 240, 240, { wall: '#e4d8c6', tones: ['#6b4423', '#8a5a2b', '#3d2a18', '#a07440'] })}"></div>
        <div><b>Molinillo cónico</b><span>Acero y nogal</span><i>89,00 €</i></div></div></div>`,
  });

  /* ---------------------------------------------------------------- 8 */
  const meridiana = () => ({
    id: 'meridiana',
    css: `${base.replace(/\.st/g, '.meridiana')}
    .meridiana{background:#f4f1ec;color:#1d2a30;font-family:'Work Sans',sans-serif}
    .meridiana .pill{background:#2f6f73;color:#f4f1ec;border-color:#2f6f73;font-weight:700}
    .meridiana .head{padding:12px 54px 24px;flex:none}
    .meridiana h1{font-family:'Instrument Serif',serif;font-size:84px;line-height:1.0;font-weight:400;max-width:17ch}
    .meridiana h1 em{font-style:italic;color:#2f6f73}
    .meridiana .sub{font-size:18px;line-height:1.6;color:#5d6b70;max-width:44ch;margin-top:18px}
    .meridiana .row{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin:0 54px;flex:none}
    .meridiana .row .im{height:324px;background-size:cover;background-position:center}
    .meridiana .blk{background:#2f6f73;color:#eef5f4;padding:34px 36px;display:flex;
      flex-direction:column;justify-content:space-between}
    .meridiana .blk h3{font-family:'Instrument Serif',serif;font-size:34px;font-weight:400}
    .meridiana .blk p{font-size:15px;line-height:1.6;opacity:.86}
    .meridiana .blk .btn{align-self:flex-start;background:#eef5f4;color:#2f6f73;padding:14px 26px;
      border-radius:999px;font-weight:700;font-size:14px}
    .meridiana .strip{display:flex;justify-content:space-between;padding:22px 54px;
      font-size:14px;color:#5d6b70}
    .meridiana .strip b{color:#1d2a30}`,
    html: `
    <div class="bar"><div class="wm">Meridiana</div>
      <div class="nv"><span>Tratamientos</span><span>Equipo</span><span>Precios</span></div>
      <div class="pill">Pedir cita</div></div>
    <div class="head"><h1>Tu primera cita, <em>sin coste</em></h1>
      <div class="sub">Diagnóstico completo y presupuesto cerrado por escrito. Sin sorpresas después.</div></div>
    <div class="row">
      <div class="im" style="background-image:${bg('clinic', 89, 700, 420, { wall: '#eaf0f0', accent: '#2f6f73' })}"></div>
      <div class="blk"><div><h3>Dieciocho años<br>en el barrio</h3>
        <p>Urgencias todos los días y financiación sin intereses hasta doce meses.</p></div>
        <div class="btn">Ver tratamientos</div></div></div>
    <div class="strip"><span>Lunes a viernes · 9:00 – 20:30</span><b>Calle Cádiz 48, Valencia</b></div>`,
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
