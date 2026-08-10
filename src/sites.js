/* The nine mock sites that ride the conveyor.
 *
 * These are the ad's actual argument — the claim is "we build sites like
 * these" — so the brief for each one is: a different industry, a different
 * brand colour, a different layout skeleton, and a picture you can name at a
 * glance. An earlier pass gave them all the same shape and the same soft
 * abstract fills, and at card size they blurred into one site. Everything here
 * is pushed harder on purpose: bigger headlines, saturated colour blocks,
 * full-bleed imagery.
 *
 * Each site is authored at 1440x900 (a real desktop viewport) and scaled down
 * bodily by the card, so the proportions stay honest at any card size. */

const SITES = (() => {
  const bg = (scene, seed, w, h, opts) => ART.bg(scene, seed, w, h, opts);

  /* ---------------------------------------------------------------- 1 */
  const bruma = () => ({
    id: 'bruma',
    css: `
    .bruma{background:#0f0a14;color:#fff;font-family:'Work Sans',sans-serif}
    .bruma .hero{position:absolute;inset:0;background-size:cover;background-position:center}
    .bruma .sc{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,10,20,.62),rgba(15,10,20,.05) 38%,rgba(15,10,20,.88))}
    .bruma .nav{position:absolute;inset:0 0 auto 0;display:flex;align-items:center;
      justify-content:space-between;padding:34px 56px;z-index:3}
    .bruma .mark{font-family:'Instrument Serif',serif;font-size:30px}
    .bruma .menu{display:flex;gap:32px;font-size:13px;letter-spacing:.14em;text-transform:uppercase;opacity:.88}
    .bruma .btn{border:1px solid rgba(255,255,255,.55);padding:11px 24px;border-radius:999px;
      font-size:12px;letter-spacing:.14em;text-transform:uppercase}
    .bruma .mid{position:absolute;left:56px;right:56px;top:206px;z-index:2}
    .bruma .kick{font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:#e8b98a;margin-bottom:26px}
    .bruma h1{font-family:'Instrument Serif',serif;font-size:132px;line-height:.9;font-weight:400;max-width:11ch}
    .bruma h1 em{font-style:italic;color:#f0c79a}
    .bruma .book{position:absolute;left:56px;right:56px;bottom:52px;z-index:3;background:rgba(255,255,255,.96);
      color:#211a24;border-radius:8px;display:grid;grid-template-columns:1fr 1fr 1fr auto;align-items:center;
      padding:22px 24px;gap:26px;box-shadow:0 24px 60px rgba(0,0,0,.5)}
    .bruma .fld{border-left:1px solid #ded5e0;padding-left:22px}
    .bruma .fld:first-child{border-left:0;padding-left:0}
    .bruma .fld b{display:block;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#8d8194;font-weight:700}
    .bruma .fld span{font-size:21px;font-family:'Instrument Serif',serif}
    .bruma .go{background:#7a2f52;color:#fff;padding:17px 34px;border-radius:6px;font-size:14px;
      letter-spacing:.1em;text-transform:uppercase;font-weight:700}`,
    html: `
    <div class="hero" style="background-image:${bg('hills', 11, 960, 640, { sky: ['#160e33', '#5f2f57', '#c86a4e', '#f2b982'], ridge: '#1a1029' })}"></div>
    <div class="sc"></div>
    <div class="nav"><div class="mark">Casa Bruma</div>
      <div class="menu"><span>La casa</span><span>Estancias</span><span>Mesa</span></div>
      <div class="btn">Reservar</div></div>
    <div class="mid"><div class="kick">Sierra de Gredos · Ávila</div>
      <h1>Dormir <em>despacio</em></h1></div>
    <div class="book">
      <div class="fld"><b>Entrada</b><span>14 marzo</span></div>
      <div class="fld"><b>Salida</b><span>17 marzo</span></div>
      <div class="fld"><b>Huéspedes</b><span>2 adultos</span></div>
      <div class="go">Ver disponibilidad</div></div>`,
  });

  /* ---------------------------------------------------------------- 2 */
  const nudo = () => ({
    id: 'nudo',
    css: `
    .nudo{background:#0b0b0c;color:#f2f1ee;font-family:'Work Sans',sans-serif}
    .nudo .top{display:flex;justify-content:space-between;align-items:center;padding:34px 50px}
    .nudo .mark{font-size:19px;font-weight:700;letter-spacing:.4em}
    .nudo .menu{display:flex;gap:28px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#87867f}
    .nudo .split{display:grid;grid-template-columns:1fr 1fr;height:806px}
    .nudo .left{padding:44px 50px 0;display:flex;flex-direction:column;justify-content:space-between}
    .nudo h1{font-size:104px;line-height:.94;font-weight:400;letter-spacing:-.045em}
    .nudo h1 b{font-weight:700;display:block}
    .nudo .meta{font-size:15px;line-height:1.75;color:#96958e;max-width:32ch;padding-bottom:56px}
    .nudo .pic{position:relative;background-size:cover;background-position:center}
    .nudo .pic .cap{position:absolute;left:0;bottom:0;right:0;padding:22px 26px;display:flex;
      justify-content:space-between;font-size:12px;letter-spacing:.14em;text-transform:uppercase;
      background:linear-gradient(0deg,rgba(6,6,7,.92),transparent)}
    .nudo .left .thumbs{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding-bottom:44px}
    .nudo .left .thumbs div{height:168px;background-size:cover;background-position:center}`,
    html: `
    <div class="top"><div class="mark">NUDO</div>
      <div class="menu"><span>Obra</span><span>Estudio</span><span>Premios</span><span>Contacto</span></div></div>
    <div class="split">
      <div class="left"><h1>Arquitectura<br>que <b>envejece bien</b></h1>
        <div class="meta">Estudio en Valencia. Piedra, cal y madera maciza sobre estructuras
          que ya existen.<br><br>Rehabilitación · Vivienda · Equipamiento público</div>
        <div class="thumbs">
          <div style="background-image:${bg('room', 23, 480, 340, { wall: '#d8d0c2', floor: '#7d5a3a', object: '#2f3a35' })}"></div>
          <div style="background-image:${bg('room', 67, 480, 340, { wall: '#b8bcc0', floor: '#4a4d52', object: '#8a6a44', light: '#e8f0ff' })}"></div>
        </div></div>
      <div class="pic" style="background-image:${bg('facade', 41, 700, 820, { sky: '#6f7f8d', wall: '#c3b49b', lit: '#ffd98a', glass: '#2f3940' })}">
        <div class="cap"><span>Mercado de Ruzafa</span><span>2023</span></div></div>
    </div>
`,
  });

  /* ---------------------------------------------------------------- 3 */
  const tinta = () => ({
    id: 'tinta',
    css: `
    .tinta{background:#fbf6ec;color:#231a10;font-family:'Work Sans',sans-serif}
    .tinta .top{display:flex;justify-content:space-between;align-items:center;padding:26px 52px;
      background:#8a3a12;color:#fbf6ec}
    .tinta .mark{font-family:'Lora',serif;font-size:25px;font-weight:700}
    .tinta .menu{display:flex;gap:26px;font-size:14px}
    .tinta .bag{background:#fbf6ec;color:#8a3a12;border-radius:999px;padding:9px 20px;font-size:13px;font-weight:700}
    .tinta .hero{display:grid;grid-template-columns:1.05fr .95fr;height:520px}
    .tinta .copy{padding:0 52px;display:flex;flex-direction:column;justify-content:center;gap:22px}
    .tinta .badge{align-self:flex-start;background:#231a10;color:#f4c95d;font-size:11px;font-weight:700;
      letter-spacing:.2em;text-transform:uppercase;padding:9px 16px;border-radius:999px}
    .tinta h1{font-family:'Lora',serif;font-size:88px;line-height:1;font-weight:700;letter-spacing:-.03em}
    .tinta h1 span{color:#8a3a12}
    .tinta .sub{font-size:18px;line-height:1.6;color:#6b5946;max-width:32ch}
    .tinta .buy{display:flex;align-items:center;gap:20px;margin-top:8px}
    .tinta .btn{background:#8a3a12;color:#fff;padding:19px 38px;border-radius:999px;font-size:16px;font-weight:700}
    .tinta .price{font-family:'Lora',serif;font-size:34px;font-weight:700}
    .tinta .shot{background-size:cover;background-position:center}
    .tinta .row{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid #e6d9c4}
    .tinta .c{padding:30px 34px;border-left:1px solid #e6d9c4;display:flex;gap:18px;align-items:center}
    .tinta .c:first-child{border-left:0}
    .tinta .c .im{width:92px;height:92px;border-radius:8px;background-size:cover;background-position:center;flex:none}
    .tinta .c b{display:block;font-family:'Lora',serif;font-size:19px}
    .tinta .c span{font-size:13px;color:#8a7a63}
    .tinta .c i{font-style:normal;font-size:17px;font-weight:700;display:block;margin-top:6px}`,
    html: `
    <div class="top"><div class="mark">Tinta &amp; Grano</div>
      <div class="menu"><span>Café</span><span>Suscripción</span><span>Cursos</span><span>Tostadero</span></div>
      <div class="bag">Cesta · 2</div></div>
    <div class="hero">
      <div class="copy"><div class="badge">Tueste de la semana</div>
        <h1>Etiopía<br><span>Guji Natural</span></h1>
        <div class="sub">Melocotón, jazmín y un final largo a té negro. Tostado el martes, en tu casa el jueves.</div>
        <div class="buy"><div class="btn">Añadir a la cesta</div><div class="price">14,50 €</div></div></div>
      <div class="shot" style="background-image:${bg('coffee', 7, 700, 560, { table: '#4a2b17', crema: '#b06a30', saucer: '#f3ece0' })}"></div></div>
    <div class="row">
      <div class="c"><div class="im" style="background-image:${bg('coffee', 13, 200, 200, { table: '#2f1d12', crema: '#8e5326' })}"></div>
        <div><b>Colombia Huila</b><span>Lavado · 250 g</span><i>11,00 €</i></div></div>
      <div class="c"><div class="im" style="background-image:${bg('coffee', 19, 200, 200, { table: '#5a3a1e', crema: '#c98b46' })}"></div>
        <div><b>Kenia Nyeri</b><span>Lavado · 250 g</span><i>13,20 €</i></div></div>
      <div class="c"><div class="im" style="background-image:${bg('shop', 29, 200, 200, { wall: '#e8dcc6', clothes: ['#6b4423', '#8a5a2b', '#3d2a18'] })}"></div>
        <div><b>Molinillo cónico</b><span>Acero y nogal</span><i>89,00 €</i></div></div>
    </div>`,
  });

  /* ---------------------------------------------------------------- 4 */
  const volta = () => ({
    id: 'volta',
    css: `
    .volta{background:#0d1110;color:#f2f5f3;font-family:'Outfit',sans-serif}
    .volta .top{display:flex;justify-content:space-between;align-items:center;padding:26px 48px}
    .volta .mark{font-size:29px;font-weight:700;letter-spacing:-.03em}
    .volta .mark span{color:#c8fa4b}
    .volta .menu{display:flex;gap:26px;font-size:14px;color:#98a29c}
    .volta .join{background:#c8fa4b;color:#0d1110;padding:13px 26px;border-radius:999px;font-size:15px;font-weight:700}
    .volta .hero{position:relative;height:460px;background-size:cover;background-position:center;
      display:flex;align-items:center}
    .volta .sc{position:absolute;inset:0;background:linear-gradient(78deg,rgba(8,12,10,.94) 26%,rgba(8,12,10,.1))}
    .volta .in{position:relative;padding:0 48px}
    .volta h1{font-size:108px;line-height:.92;font-weight:700;letter-spacing:-.05em}
    .volta h1 span{color:#c8fa4b}
    .volta .kick{font-size:14px;letter-spacing:.24em;text-transform:uppercase;color:#c8fa4b;
      margin-bottom:20px;font-weight:700}
    .volta .grid{display:grid;grid-template-columns:1.6fr 1fr;gap:20px;padding:26px 48px}
    .volta .sched{border:1px solid #1f2724;border-radius:14px;overflow:hidden}
    .volta .hd,.volta .sr{display:grid;grid-template-columns:92px 1fr 108px 108px;align-items:center}
    .volta .hd{padding:13px 22px;font-size:11px;letter-spacing:.18em;text-transform:uppercase;
      color:#7d8781;background:#141a18}
    .volta .sr{padding:17px 22px;border-top:1px solid #1a201e;font-size:16px}
    .volta .sr b{font-weight:700;font-variant-numeric:tabular-nums}
    .volta .sr .c{color:#98a29c;font-size:13px}
    .volta .pill{justify-self:start;font-size:12px;font-weight:700;padding:6px 13px;border-radius:999px;
      background:#22331a;color:#c8fa4b}
    .volta .pill.full{background:#33201e;color:#ff8a6b}
    .volta .aside{background:#c8fa4b;color:#0d1110;border-radius:14px;padding:30px;
      display:flex;flex-direction:column;justify-content:space-between}
    .volta .aside h3{font-size:24px;font-weight:700;margin-bottom:10px}
    .volta .aside p{font-size:14px;line-height:1.55;opacity:.78}
    .volta .big{font-size:76px;font-weight:700;letter-spacing:-.045em;line-height:1}
    .volta .big small{font-size:17px;font-weight:500;opacity:.7}`,
    html: `
    <div class="top"><div class="mark">VOLTA<span>.</span></div>
      <div class="menu"><span>Pistas</span><span>Clases</span><span>Liga</span><span>Tarifas</span></div>
      <div class="join">Reservar pista</div></div>
    <div class="hero" style="background-image:${bg('court', 53, 960, 520, { floor: '#1e6b4f', sky: '#0c1512' })}">
      <div class="sc"></div>
      <div class="in"><div class="kick">Pádel · Valencia centro</div>
        <h1>Ocho pistas.<br>Abiertas<br><span>hasta la 1</span></h1></div></div>
    <div class="grid">
      <div class="sched"><div class="hd"><span>Hora</span><span>Pista</span><span>Nivel</span><span>Plazas</span></div>
        <div class="sr"><b>18:00</b><span>Central — cristal<div class="c">Con Marta Ferrer</div></span><span class="c">Intermedio</span><span class="pill">2 libres</span></div>
        <div class="sr"><b>19:30</b><span>Pista 3 — muro<div class="c">Clase dirigida</div></span><span class="c">Iniciación</span><span class="pill">4 libres</span></div>
        <div class="sr"><b>21:00</b><span>Central — cristal<div class="c">Liga interna</div></span><span class="c">Avanzado</span><span class="pill full">Completa</span></div></div>
      <div class="aside"><div><h3>Cuota mensual</h3>
        <p>Pistas ilimitadas de lunes a viernes y dos clases al mes.</p></div>
        <div class="big">39 €<small> / mes</small></div></div></div>`,
  });

  /* ---------------------------------------------------------------- 5 */
  const meridiana = () => ({
    id: 'meridiana',
    css: `
    .meridiana{background:#fff;color:#0d2331;font-family:'Work Sans',sans-serif}
    .meridiana .top{display:flex;justify-content:space-between;align-items:center;padding:24px 54px;
      border-bottom:1px solid #e6eef3}
    .meridiana .mark{font-size:22px;font-weight:700;display:flex;align-items:center;gap:11px}
    .meridiana .dot{width:24px;height:24px;border-radius:50%;background:#0b8fc4;
      box-shadow:inset 0 0 0 6px #fff,0 0 0 2px #0b8fc4}
    .meridiana .menu{display:flex;gap:26px;font-size:14px;color:#587284}
    .meridiana .tel{background:#0b8fc4;color:#fff;padding:12px 24px;border-radius:999px;font-weight:700;font-size:15px}
    .meridiana .hero{display:grid;grid-template-columns:1fr 1fr;height:472px}
    .meridiana .copy{padding:0 54px;display:flex;flex-direction:column;justify-content:center}
    .meridiana h1{font-size:82px;line-height:1;font-weight:700;letter-spacing:-.042em}
    .meridiana h1 span{color:#0b8fc4}
    .meridiana .sub{font-size:18px;line-height:1.62;color:#587284;margin:24px 0 32px;max-width:32ch}
    .meridiana .acts{display:flex;gap:14px;align-items:center}
    .meridiana .b1{background:#0d2331;color:#fff;padding:19px 34px;border-radius:10px;font-size:16px;font-weight:700}
    .meridiana .b2{border:2px solid #d6e4ec;padding:17px 28px;border-radius:10px;font-size:16px;font-weight:600}
    .meridiana .shot{background-size:cover;background-position:center}
    .meridiana .band{display:grid;grid-template-columns:repeat(4,1fr);background:#0d2331;color:#fff}
    .meridiana .stat{padding:34px 30px;border-left:1px solid rgba(255,255,255,.12)}
    .meridiana .stat:first-child{border-left:0}
    .meridiana .stat b{display:block;font-size:46px;font-weight:700;letter-spacing:-.04em;color:#5cc8f0;
      font-variant-numeric:tabular-nums;line-height:1}
    .meridiana .stat span{font-size:14px;color:#9fbdd0;line-height:1.45;display:block;margin-top:10px}`,
    html: `
    <div class="top"><div class="mark"><span class="dot"></span>Clínica Meridiana</div>
      <div class="menu"><span>Tratamientos</span><span>Equipo</span><span>Financiación</span><span>Blog</span></div>
      <div class="tel">960 22 14 08</div></div>
    <div class="hero"><div class="copy"><h1>Tu primera cita, <span>sin coste</span></h1>
      <div class="sub">Radiografía panorámica, diagnóstico y presupuesto cerrado por escrito. Sin sorpresas.</div>
      <div class="acts"><div class="b1">Pedir cita online</div><div class="b2">Ver tratamientos</div></div></div>
      <div class="shot" style="background-image:${bg('clinic', 71, 700, 500, { wall: '#e9f2f7', accent: '#0b8fc4' })}"></div></div>
    <div class="band">
      <div class="stat"><b>18</b><span>años en Russafa</span></div>
      <div class="stat"><b>4,9</b><span>en 612 reseñas</span></div>
      <div class="stat"><b>24 h</b><span>urgencias a diario</span></div>
      <div class="stat"><b>0 %</b><span>hasta 12 meses</span></div></div>`,
  });

  /* ---------------------------------------------------------------- 6 */
  const ferra = () => ({
    id: 'ferra',
    css: `
    .ferra{background:#100d09;color:#f2e8d6;font-family:'Work Sans',sans-serif}
    .ferra .top{display:flex;justify-content:space-between;align-items:center;padding:28px 54px;
      position:absolute;inset:0 0 auto 0;z-index:3}
    .ferra .mark{font-family:'Instrument Serif',serif;font-size:34px}
    .ferra .menu{display:flex;gap:30px;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#c7b393}
    .ferra .res{background:#d4a340;color:#100d09;padding:13px 28px;font-size:13px;font-weight:700;
      letter-spacing:.12em;text-transform:uppercase;border-radius:999px}
    .ferra .pic{position:relative;height:470px;background-size:cover;background-position:center}
    .ferra .sc{position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,13,9,.8),rgba(16,13,9,.15) 45%,rgba(16,13,9,.95))}
    .ferra .htxt{position:absolute;left:54px;bottom:44px;z-index:2}
    .ferra .kick{font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:#d4a340;margin-bottom:18px}
    .ferra h1{font-family:'Instrument Serif',serif;font-size:96px;line-height:.94;font-weight:400}
    .ferra h1 em{font-style:italic;color:#d4a340}
    .ferra .menuwrap{display:grid;grid-template-columns:1fr 1fr;gap:0 60px;padding:34px 54px 0}
    .ferra .dish{display:flex;align-items:baseline;gap:14px;padding:16px 0;border-top:1px solid #251e14}
    .ferra .dish .n{font-family:'Instrument Serif',serif;font-size:25px;white-space:nowrap}
    .ferra .dish .d{flex:1;border-bottom:1px dotted #4a3d28;transform:translateY(-6px)}
    .ferra .dish .p{font-size:19px;font-variant-numeric:tabular-nums;color:#d4a340;font-weight:600}
    .ferra .dish .sub{font-size:13px;color:#8d8069;margin-top:4px}`,
    html: `
    <div class="top"><div class="mark">Ferra</div>
      <div class="menu"><span>Carta</span><span>Bodega</span><span>La casa</span></div>
      <div class="res">Reservar mesa</div></div>
    <div class="pic" style="background-image:${bg('dish', 89, 960, 520, { table: '#1d140c', plate: '#3a2f24', food: ['#e0761f', '#a8461a', '#f0b94a'] })}">
      <div class="sc"></div>
      <div class="htxt"><div class="kick">Menú de temporada · marzo</div>
        <h1>Brasa, <em>sal</em><br>y poco más</h1></div></div>
    <div class="menuwrap">
      <div><div class="dish"><div><div class="n">Anchoa curada en casa</div>
          <div class="sub">Pan de cristal, mantequilla ahumada</div></div><div class="d"></div><div class="p">9 €</div></div>
        <div class="dish"><div><div class="n">Alcachofa a la brasa</div>
          <div class="sub">Yema curada y avellana</div></div><div class="d"></div><div class="p">14 €</div></div></div>
      <div><div class="dish"><div><div class="n">Sepia y su tinta</div>
          <div class="sub">Guisantes del Maresme</div></div><div class="d"></div><div class="p">18 €</div></div>
        <div class="dish"><div><div class="n">Costilla de vaca vieja</div>
          <div class="sub">Cuarenta días de maduración</div></div><div class="d"></div><div class="p">26 €</div></div></div>
    </div>`,
  });

  /* ---------------------------------------------------------------- 7 */
  const lumen = () => ({
    id: 'lumen',
    css: `
    .lumen{background:#000;color:#fff;font-family:'Work Sans',sans-serif;position:relative}
    .lumen .full{position:absolute;inset:0;background-size:cover;background-position:center}
    .lumen .sc{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,0) 38%,rgba(0,0,0,.82))}
    .lumen .top{position:absolute;inset:0 0 auto 0;display:flex;justify-content:space-between;
      align-items:center;padding:36px 52px;z-index:2}
    .lumen .mark{font-size:16px;font-weight:700;letter-spacing:.52em}
    .lumen .menu{display:flex;gap:32px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#c9c9c9}
    .lumen .center{position:absolute;left:52px;right:52px;top:50%;transform:translateY(-50%);z-index:2}
    .lumen h1{font-family:'Instrument Serif',serif;font-size:150px;line-height:.86;font-weight:400}
    .lumen h1 em{font-style:italic}
    .lumen .cap{font-size:13px;letter-spacing:.26em;text-transform:uppercase;color:#b9b9b9;margin-bottom:24px}
    .lumen .thumbs{position:absolute;left:52px;right:52px;bottom:44px;z-index:2;display:grid;
      grid-template-columns:repeat(5,1fr);gap:12px}
    .lumen .th{height:118px;background-size:cover;background-position:center;opacity:.58}
    .lumen .th.on{opacity:1;box-shadow:0 0 0 2px #fff}
    .lumen .idx{position:absolute;right:52px;bottom:190px;z-index:2;font-size:13px;letter-spacing:.2em;
      color:#c9c9c9;font-variant-numeric:tabular-nums}`,
    html: `
    <div class="full" style="background-image:${bg('hills', 97, 980, 640, { sky: ['#080a1c', '#3a1f4a', '#8e3f4e', '#e0855e'], ridge: '#0a0a14' })}"></div>
    <div class="sc"></div>
    <div class="top"><div class="mark">LUMEN</div>
      <div class="menu"><span>Series</span><span>Editorial</span><span>Copias</span><span>Estudio</span></div></div>
    <div class="center"><div class="cap">Serie 04 — Costa Brava, invierno</div>
      <h1>La luz <em>que queda</em></h1></div>
    <div class="idx">04 / 12</div>
    <div class="thumbs">
      <div class="th on" style="background-image:${bg('hills', 97, 280, 200, { sky: ['#080a1c', '#3a1f4a', '#8e3f4e', '#e0855e'], ridge: '#0a0a14' })}"></div>
      <div class="th" style="background-image:${bg('hills', 101, 280, 200, { sky: ['#0d1f2c', '#1f4a5c', '#5f9aa8', '#cfe4e6'], ridge: '#101c24' })}"></div>
      <div class="th" style="background-image:${bg('facade', 103, 280, 200, { sky: '#4a5560', wall: '#8d8578', lit: '#ffe0a0', glass: '#242c33' })}"></div>
      <div class="th" style="background-image:${bg('room', 107, 280, 200, { wall: '#3a3a3e', floor: '#26262a', object: '#151518', light: '#fff2d8' })}"></div>
      <div class="th" style="background-image:${bg('hills', 109, 280, 200, { sky: ['#241033', '#6b2f45', '#d4703f', '#f7cf95'], ridge: '#1b1024' })}"></div></div>`,
  });

  /* ---------------------------------------------------------------- 8 */
  const ovillo = () => ({
    id: 'ovillo',
    css: `
    .ovillo{background:#fdfaf5;color:#2a1f18;font-family:'Outfit',sans-serif}
    .ovillo .bar{background:#a8412a;color:#fff;text-align:center;padding:12px;font-size:14px;font-weight:600}
    .ovillo .top{display:flex;justify-content:space-between;align-items:center;padding:22px 50px}
    .ovillo .mark{font-size:32px;font-weight:700;letter-spacing:-.03em}
    .ovillo .menu{display:flex;gap:26px;font-size:15px;color:#6b5748}
    .ovillo .icons{display:flex;gap:16px;font-size:14px;color:#6b5748}
    .ovillo .promo{display:grid;grid-template-columns:1fr 1fr;height:330px}
    .ovillo .pcopy{background:#a8412a;color:#fff;padding:46px 50px;display:flex;flex-direction:column;justify-content:center}
    .ovillo .pcopy h1{font-size:66px;line-height:.98;font-weight:700;letter-spacing:-.04em}
    .ovillo .pcopy p{font-size:17px;margin-top:16px;opacity:.86}
    .ovillo .pcopy .b{align-self:flex-start;margin-top:26px;background:#fff;color:#a8412a;
      padding:16px 32px;border-radius:999px;font-weight:700;font-size:16px}
    .ovillo .pshot{background-size:cover;background-position:center}
    .ovillo .hd{padding:30px 50px 16px;display:flex;justify-content:space-between;align-items:flex-end}
    .ovillo .hd h2{font-size:34px;font-weight:700;letter-spacing:-.03em}
    .ovillo .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding:0 50px}
    .ovillo .p .im{position:relative;height:212px;border-radius:10px;background-size:cover;background-position:center}
    .ovillo .p .im .tag{position:absolute;top:12px;left:12px;background:#2a1f18;color:#fff;font-size:11px;
      font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:6px 11px;border-radius:999px}
    .ovillo .p .n{font-size:18px;font-weight:600;margin:13px 0 3px}
    .ovillo .p .m{font-size:13px;color:#8b7768}
    .ovillo .p .pr{display:flex;align-items:baseline;gap:9px;margin-top:8px}
    .ovillo .p .pr b{font-size:20px;font-weight:700;font-variant-numeric:tabular-nums}
    .ovillo .p .pr s{font-size:14px;color:#a99383}`,
    html: `
    <div class="bar">Envío gratis a partir de 60 € · Devoluciones en 30 días</div>
    <div class="top"><div class="mark">ovillo</div>
      <div class="menu"><span>Punto</span><span>Lanas</span><span>Patrones</span><span>Talleres</span></div>
      <div class="icons"><span>Buscar</span><span>Cuenta</span><span>Cesta (3)</span></div></div>
    <div class="promo">
      <div class="pcopy"><h1>Rebajas de<br>invierno</h1>
        <p>Hasta un 40 % en lana merina y alpaca.</p><div class="b">Ver rebajas</div></div>
      <div class="pshot" style="background-image:${bg('knit', 127, 700, 360, { yarn: '#b8452f' })}"></div></div>
    <div class="hd"><h2>Jerséis de invierno</h2><div style="font-size:15px;color:#8b7768">42 artículos</div></div>
    <div class="grid">
      <div class="p"><div class="im" style="background-image:${bg('knit', 131, 340, 280, { yarn: '#c2955c' })}">
        <div class="tag">−20 %</div></div><div class="n">Jersey Duna</div><div class="m">Merina · trenzado</div>
        <div class="pr"><b>79,00 €</b><s>99,00 €</s></div></div>
      <div class="p"><div class="im" style="background-image:${bg('knit', 137, 340, 280, { yarn: '#3f5b46' })}"></div>
        <div class="n">Cárdigan Ría</div><div class="m">Lana y alpaca</div>
        <div class="pr"><b>118,00 €</b></div></div>
      <div class="p"><div class="im" style="background-image:${bg('knit', 139, 340, 280, { yarn: '#2c3d5c' })}">
        <div class="tag">Nuevo</div></div><div class="n">Chaleco Sella</div><div class="m">Algodón orgánico</div>
        <div class="pr"><b>64,00 €</b></div></div>
      <div class="p"><div class="im" style="background-image:${bg('shop', 149, 340, 280, { wall: '#efe6d8' })}"></div>
        <div class="n">Toda la colección</div><div class="m">42 prendas</div>
        <div class="pr"><b>Ver más</b></div></div>
    </div>`,
  });

  /* ---------------------------------------------------------------- 9 */
  const cadencia = () => ({
    id: 'cadencia',
    css: `
    .cadencia{background:#0c0714;color:#f5ecff;font-family:'Outfit',sans-serif}
    .cadencia .hero{position:relative;height:520px;background-size:cover;background-position:center}
    .cadencia .sc{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,7,20,.72),rgba(12,7,20,.1) 40%,rgba(12,7,20,.96))}
    .cadencia .top{position:absolute;inset:0 0 auto 0;display:flex;justify-content:space-between;
      align-items:center;padding:26px 50px;z-index:3}
    .cadencia .mark{font-size:23px;font-weight:700;letter-spacing:.26em}
    .cadencia .menu{display:flex;gap:26px;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#a892b8}
    .cadencia .buy{background:#ff4d2e;color:#fff;padding:13px 26px;border-radius:999px;font-size:14px;
      font-weight:700;letter-spacing:.06em;text-transform:uppercase}
    .cadencia .hin{position:absolute;left:50px;bottom:46px;z-index:2}
    .cadencia .kick{font-size:13px;letter-spacing:.26em;text-transform:uppercase;color:#ff7a5e;
      font-weight:700;margin-bottom:16px}
    .cadencia h1{font-size:118px;line-height:.9;font-weight:700;letter-spacing:-.05em}
    .cadencia h1 span{color:#ff4d2e}
    .cadencia .list{padding:26px 50px 0}
    .cadencia .ev{display:grid;grid-template-columns:104px 1fr 170px 130px;align-items:center;gap:24px;
      padding:19px 0;border-top:1px solid #241634}
    .cadencia .dt{text-align:center;border-right:1px solid #241634;padding-right:16px}
    .cadencia .dt b{display:block;font-size:38px;font-weight:700;line-height:1;font-variant-numeric:tabular-nums}
    .cadencia .dt span{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#a892b8}
    .cadencia .ev .nm{font-size:27px;font-weight:600;letter-spacing:-.025em}
    .cadencia .ev .gn{font-size:13px;color:#a892b8;margin-top:3px}
    .cadencia .ev .hr{font-size:14px;color:#a892b8;font-variant-numeric:tabular-nums}
    .cadencia .ev .tk{justify-self:end;background:#ff4d2e;color:#fff;border-radius:999px;
      padding:11px 22px;font-size:14px;font-weight:700}
    .cadencia .ev .tk.out{background:transparent;border:1px solid #3a2a4a;color:#6c5a7a;font-weight:500}`,
    html: `
    <div class="hero" style="background-image:${bg('stage', 149, 960, 560, { top: '#1c0b33', beams: ['#ff4d2e', '#a24dff', '#2ec5ff'] })}">
      <div class="sc"></div>
      <div class="top"><div class="mark">CADENCIA</div>
        <div class="menu"><span>Agenda</span><span>Sala</span><span>Abonos</span><span>Alquiler</span></div>
        <div class="buy">Entradas</div></div>
      <div class="hin"><div class="kick">Temporada 25/26 · Zaragoza</div>
        <h1>Directos<br>cada <span>jueves</span></h1></div></div>
    <div class="list">
      <div class="ev"><div class="dt"><b>14</b><span>Mar</span></div>
        <div><div class="nm">Marina Herlop</div><div class="gn">Piano y electrónica</div></div>
        <div class="hr">21:00 · Sala grande</div><div class="tk">Últimas</div></div>
      <div class="ev"><div class="dt"><b>21</b><span>Mar</span></div>
        <div><div class="nm">Trío Balcánico</div><div class="gn">Folk de los Balcanes</div></div>
        <div class="hr">20:30 · Sótano</div><div class="tk">18 €</div></div>
      <div class="ev"><div class="dt"><b>28</b><span>Mar</span></div>
        <div><div class="nm">Rodrigo Cuevas</div><div class="gn">Folclore y cabaré</div></div>
        <div class="hr">21:30 · Sala grande</div><div class="tk out">Agotado</div></div>
    </div>`,
  });

  const list = [volta, bruma, tinta, cadencia, meridiana, ferra, ovillo, nudo, lumen];

  /* Built lazily on first call so the canvas work happens once, at init. */
  let built = null;
  function all() {
    if (!built) built = list.map((f) => f());
    return built;
  }
  return { all };
})();
