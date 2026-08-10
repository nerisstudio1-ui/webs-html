/* The nine mock sites that ride the conveyor.
 *
 * These are the ad's actual argument: the claim is "we build sites like
 * these", so each one gets its own palette, typeface pairing and layout
 * rather than being a recolour of one template. Every site is authored at
 * 1440x900 (a real desktop viewport) and scaled down by the card, so the
 * proportions stay honest at any card size. */

const SITES = (() => {
  const bg = (kind, pal, seed, w, h) => ART.bg(kind, pal, seed, w, h);

  /* ---------------------------------------------------------------- 1 */
  const bruma = () => ({
    id: 'bruma',
    css: `
    .bruma{background:#f4efe6;color:#2a241c;font-family:'Work Sans',sans-serif}
    .bruma .nav{position:absolute;inset:0 0 auto 0;display:flex;align-items:center;
      justify-content:space-between;padding:34px 56px;z-index:3;color:#fff}
    .bruma .mark{font-family:'Instrument Serif',serif;font-size:27px;letter-spacing:.01em}
    .bruma .menu{display:flex;gap:34px;font-size:14px;letter-spacing:.06em;text-transform:uppercase;opacity:.9}
    .bruma .hero{position:relative;height:612px;background-size:cover;background-position:center}
    .bruma .scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,14,8,.5),rgba(20,14,8,.08) 42%,rgba(20,14,8,.55))}
    .bruma .htxt{position:absolute;left:56px;bottom:150px;color:#fff;z-index:2}
    .bruma .eyebrow{font-size:13px;letter-spacing:.24em;text-transform:uppercase;opacity:.82;margin-bottom:20px}
    .bruma h1{font-family:'Instrument Serif',serif;font-size:92px;line-height:.95;font-weight:400;max-width:9ch}
    .bruma h1 em{font-style:italic}
    .bruma .book{position:absolute;left:56px;right:56px;bottom:44px;z-index:3;background:#fffdf8;
      border-radius:6px;display:grid;grid-template-columns:1fr 1fr 1fr auto;align-items:center;
      padding:20px 22px;gap:26px;box-shadow:0 18px 40px rgba(30,20,10,.28)}
    .bruma .fld{border-left:1px solid #e2d9c8;padding-left:20px}
    .bruma .fld:first-child{border-left:0;padding-left:0}
    .bruma .fld b{display:block;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#a2937a;font-weight:600}
    .bruma .fld span{font-size:19px;font-family:'Instrument Serif',serif}
    .bruma .cta{background:#2a241c;color:#f4efe6;padding:15px 32px;border-radius:4px;font-size:14px;
      letter-spacing:.1em;text-transform:uppercase;font-weight:600}
    .bruma .strip{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;height:288px;background:#e5dccb}
    .bruma .cell{padding:38px 34px;background:#f4efe6;display:flex;flex-direction:column;justify-content:space-between}
    .bruma .cell h3{font-family:'Instrument Serif',serif;font-size:32px;font-weight:400}
    .bruma .cell p{font-size:15px;line-height:1.55;color:#6f6455;max-width:30ch}
    .bruma .num{font-size:12px;letter-spacing:.2em;color:#b0a086}`,
    html: `
    <div class="nav"><div class="mark">Casa Bruma</div>
      <div class="menu"><span>La casa</span><span>Estancias</span><span>Mesa</span><span>Reservar</span></div></div>
    <div class="hero" style="background-image:${bg('landscape', 'dusk', 11, 900, 620)}">
      <div class="scrim"></div>
      <div class="htxt"><div class="eyebrow">Sierra de Gredos · Ávila</div>
        <h1>Dormir <em>despacio</em></h1></div>
      <div class="book">
        <div class="fld"><b>Entrada</b><span>14 marzo</span></div>
        <div class="fld"><b>Salida</b><span>17 marzo</span></div>
        <div class="fld"><b>Huéspedes</b><span>2 adultos</span></div>
        <div class="cta">Ver disponibilidad</div>
      </div></div>
    <div class="strip">
      <div class="cell"><div class="num">01</div><div><h3>Siete estancias</h3>
        <p>Cada una con chimenea, vistas al valle y nada que hacer.</p></div></div>
      <div class="cell"><div class="num">02</div><div><h3>Cocina de campo</h3>
        <p>Menú corto, producto de la comarca, mesa compartida a las nueve.</p></div></div>
      <div class="cell"><div class="num">03</div><div><h3>Termas</h3>
        <p>Agua caliente al aire libre, abierta de sol a sol.</p></div></div>
    </div>`,
  });

  /* ---------------------------------------------------------------- 2 */
  const nudo = () => ({
    id: 'nudo',
    css: `
    .nudo{background:#0c0c0d;color:#ededea;font-family:'Work Sans',sans-serif}
    .nudo .top{display:flex;justify-content:space-between;align-items:baseline;padding:38px 52px 0}
    .nudo .mark{font-size:18px;font-weight:700;letter-spacing:.32em}
    .nudo .menu{display:flex;gap:30px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#8d8d88}
    .nudo .menu span:first-child{color:#ededea}
    .nudo .lead{padding:76px 52px 60px;display:grid;grid-template-columns:1.35fr 1fr;gap:60px;align-items:end}
    .nudo h1{font-size:76px;line-height:1.0;font-weight:400;letter-spacing:-.03em;max-width:16ch}
    .nudo h1 b{font-weight:700}
    .nudo .meta{font-size:14px;line-height:1.7;color:#9a9a94;max-width:34ch}
    .nudo .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 52px}
    .nudo .proj{position:relative;height:330px;background-size:cover;background-position:center;overflow:hidden}
    .nudo .proj .tag{position:absolute;left:0;bottom:0;right:0;padding:18px 20px;display:flex;
      justify-content:space-between;align-items:center;font-size:12px;letter-spacing:.1em;
      text-transform:uppercase;background:linear-gradient(0deg,rgba(8,8,9,.88),transparent);color:#fff}
    .nudo .proj .yr{color:#a09a90}`,
    html: `
    <div class="top"><div class="mark">NUDO</div>
      <div class="menu"><span>Obra</span><span>Estudio</span><span>Premios</span><span>Contacto</span></div></div>
    <div class="lead"><h1>Arquitectura que <b>envejece bien</b></h1>
      <div class="meta">Estudio en Valencia. Trabajamos con piedra, cal y madera maciza sobre
        estructuras que ya existen. Rehabilitación, vivienda y equipamiento público.</div></div>
    <div class="grid">
      <div class="proj" style="background-image:${bg('interior', 'linen', 23, 520, 480)}">
        <div class="tag"><span>Casa Poniente</span><span class="yr">2024</span></div></div>
      <div class="proj" style="background-image:${bg('interior', 'steel', 41, 520, 480)}">
        <div class="tag"><span>Mercado de Ruzafa</span><span class="yr">2023</span></div></div>
      <div class="proj" style="background-image:${bg('interior', 'ink', 67, 520, 480)}">
        <div class="tag"><span>Nave Trinitat</span><span class="yr">2023</span></div></div>
    </div>`,
  });

  /* ---------------------------------------------------------------- 3 */
  const tinta = () => ({
    id: 'tinta',
    css: `
    .tinta{background:#fbf7f0;color:#241c14;font-family:'Work Sans',sans-serif}
    .tinta .top{display:flex;justify-content:space-between;align-items:center;padding:28px 54px;
      border-bottom:1px solid #e6dccb}
    .tinta .mark{font-family:'Lora',serif;font-size:24px;font-weight:700}
    .tinta .menu{display:flex;gap:28px;font-size:14px;color:#6d5f4d}
    .tinta .bag{background:#241c14;color:#fbf7f0;border-radius:999px;padding:9px 20px;font-size:13px}
    .tinta .hero{display:grid;grid-template-columns:1fr 1fr;min-height:410px}
    .tinta .copy{padding:70px 54px;display:flex;flex-direction:column;justify-content:center;gap:24px}
    .tinta .badge{align-self:flex-start;background:#e8dcc4;color:#7a5c27;font-size:11px;font-weight:700;
      letter-spacing:.18em;text-transform:uppercase;padding:8px 14px;border-radius:3px}
    .tinta h1{font-family:'Lora',serif;font-size:62px;line-height:1.06;font-weight:700;letter-spacing:-.02em}
    .tinta .sub{font-size:17px;line-height:1.65;color:#6d5f4d;max-width:34ch}
    .tinta .buy{display:flex;align-items:center;gap:18px;margin-top:6px}
    .tinta .btn{background:#8a4b1e;color:#fff;padding:16px 30px;border-radius:4px;font-size:15px;font-weight:600}
    .tinta .price{font-family:'Lora',serif;font-size:26px;font-weight:700}
    .tinta .shot{background-size:cover;background-position:center}
    .tinta .rowhd{display:flex;justify-content:space-between;align-items:baseline;padding:36px 54px 18px}
    .tinta .rowhd h2{font-family:'Lora',serif;font-size:26px;font-weight:700}
    .tinta .rowhd a{font-size:13px;color:#8a4b1e;text-decoration:underline}
    .tinta .row{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding:0 54px}
    .tinta .card .im{height:150px;border-radius:5px;background-size:cover;background-position:center}
    .tinta .card b{display:block;font-family:'Lora',serif;font-size:17px;margin:14px 0 4px;font-weight:700}
    .tinta .card span{font-size:13px;color:#8a7a63}
    .tinta .card i{display:block;font-style:normal;font-size:15px;font-weight:600;margin-top:8px}`,
    html: `
    <div class="top"><div class="mark">Tinta &amp; Grano</div>
      <div class="menu"><span>Café</span><span>Suscripción</span><span>Cursos</span><span>Tostadero</span></div>
      <div class="bag">Cesta · 2</div></div>
    <div class="hero">
      <div class="copy"><div class="badge">Tueste de la semana</div>
        <h1>Etiopía<br>Guji Natural</h1>
        <div class="sub">Melocotón, jazmín y un final largo a té negro. Tostado el martes,
          en tu casa el jueves.</div>
        <div class="buy"><div class="btn">Añadir a la cesta</div><div class="price">14,50 €</div></div></div>
      <div class="shot" style="background-image:${bg('deep', 'ember', 7, 620, 520)}"></div></div>
    <div class="rowhd"><h2>También te gustará</h2><a>Ver los 24 orígenes</a></div>
    <div class="row">
      <div class="card"><div class="im" style="background-image:${bg('soft', 'ember', 13, 320, 220)}"></div>
        <b>Colombia Huila</b><span>Lavado · 250 g</span><i>11,00 €</i></div>
      <div class="card"><div class="im" style="background-image:${bg('soft', 'moss', 19, 320, 220)}"></div>
        <b>Kenia Nyeri</b><span>Lavado · 250 g</span><i>13,20 €</i></div>
      <div class="card"><div class="im" style="background-image:${bg('soft', 'citrus', 29, 320, 220)}"></div>
        <b>Brasil Cerrado</b><span>Natural · 1 kg</span><i>29,90 €</i></div>
      <div class="card"><div class="im" style="background-image:${bg('soft', 'steel', 37, 320, 220)}"></div>
        <b>Prensa francesa</b><span>Vidrio y acero</span><i>34,00 €</i></div>
    </div>`,
  });

  /* ---------------------------------------------------------------- 4 */
  const volta = () => ({
    id: 'volta',
    css: `
    .volta{background:#111417;color:#f2f5f3;font-family:'Outfit',sans-serif}
    .volta .top{display:flex;justify-content:space-between;align-items:center;padding:26px 50px}
    .volta .mark{font-size:26px;font-weight:700;letter-spacing:-.02em}
    .volta .mark span{color:#c8fa4b}
    .volta .menu{display:flex;gap:26px;font-size:14px;color:#9aa39d}
    .volta .join{background:#c8fa4b;color:#111417;padding:11px 22px;border-radius:999px;font-size:14px;font-weight:700}
    .volta .hero{position:relative;margin:8px 50px 0;border-radius:14px;overflow:hidden;height:330px;
      background-size:cover;background-position:center;display:flex;align-items:flex-end}
    .volta .hero .sc{position:absolute;inset:0;background:linear-gradient(70deg,rgba(10,14,12,.9) 22%,rgba(10,14,12,.15))}
    .volta .hero .in{position:relative;padding:40px 44px}
    .volta h1{font-size:66px;line-height:.98;font-weight:700;letter-spacing:-.035em;max-width:13ch}
    .volta h1 span{color:#c8fa4b}
    .volta .kick{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#c8fa4b;margin-bottom:16px;font-weight:700}
    .volta .grid{display:grid;grid-template-columns:1.5fr 1fr;gap:24px;padding:30px 50px}
    .volta .sched{border:1px solid #222a2c;border-radius:12px;overflow:hidden}
    .volta .sched .hd{display:grid;grid-template-columns:88px 1fr 110px 96px;padding:14px 20px;
      font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#7f8a84;background:#171b1e}
    .volta .sr{display:grid;grid-template-columns:88px 1fr 110px 96px;padding:16px 20px;
      border-top:1px solid #1c2225;align-items:center;font-size:15px}
    .volta .sr b{font-weight:700;font-variant-numeric:tabular-nums}
    .volta .sr .c{color:#9aa39d;font-size:13px}
    .volta .pill{justify-self:start;font-size:12px;font-weight:700;padding:5px 12px;border-radius:999px;
      background:#1e2b1a;color:#c8fa4b}
    .volta .pill.full{background:#2b1e1e;color:#ff8a6b}
    .volta .aside{border:1px solid #222a2c;border-radius:12px;padding:28px;display:flex;
      flex-direction:column;justify-content:space-between}
    .volta .aside h3{font-size:22px;font-weight:700;margin-bottom:10px}
    .volta .aside p{font-size:14px;line-height:1.6;color:#9aa39d}
    .volta .big{font-size:56px;font-weight:700;letter-spacing:-.03em;color:#c8fa4b}
    .volta .big small{font-size:16px;color:#9aa39d;font-weight:400}`,
    html: `
    <div class="top"><div class="mark">VOLTA<span>.</span></div>
      <div class="menu"><span>Pistas</span><span>Clases</span><span>Liga</span><span>Tarifas</span></div>
      <div class="join">Reservar pista</div></div>
    <div class="hero" style="background-image:${bg('deep', 'moss', 53, 900, 420)}"><div class="sc"></div>
      <div class="in"><div class="kick">Pádel · Valencia centro</div>
        <h1>Ocho pistas.<br>Abiertas <span>hasta la 1</span></h1></div></div>
    <div class="grid">
      <div class="sched"><div class="hd"><span>Hora</span><span>Pista</span><span>Nivel</span><span>Plazas</span></div>
        <div class="sr"><b>18:00</b><span>Central — cristal<div class="c">Con Marta Ferrer</div></span><span class="c">Intermedio</span><span class="pill">2 libres</span></div>
        <div class="sr"><b>19:30</b><span>Pista 3 — muro<div class="c">Clase dirigida</div></span><span class="c">Iniciación</span><span class="pill">4 libres</span></div>
        <div class="sr"><b>21:00</b><span>Central — cristal<div class="c">Liga interna</div></span><span class="c">Avanzado</span><span class="pill full">Completa</span></div>
        <div class="sr"><b>22:30</b><span>Pista 6 — exterior<div class="c">Partida abierta</div></span><span class="c">Todos</span><span class="pill">6 libres</span></div></div>
      <div class="aside"><div><h3>Cuota mensual</h3>
        <p>Pistas ilimitadas de lunes a viernes, dos clases al mes y bolsa de partidas.</p></div>
        <div class="big">39 €<small> / mes</small></div></div></div>`,
  });

  /* ---------------------------------------------------------------- 5 */
  const meridiana = () => ({
    id: 'meridiana',
    css: `
    .meridiana{background:#fff;color:#0f2230;font-family:'Work Sans',sans-serif}
    .meridiana .top{display:flex;justify-content:space-between;align-items:center;padding:26px 56px;
      border-bottom:1px solid #e8eef2}
    .meridiana .mark{font-size:21px;font-weight:700;letter-spacing:-.01em;display:flex;align-items:center;gap:10px}
    .meridiana .dot{width:22px;height:22px;border-radius:50%;background:#1a7fa8;
      box-shadow:inset 0 0 0 5px #fff,0 0 0 1px #1a7fa8}
    .meridiana .menu{display:flex;gap:28px;font-size:14px;color:#5b7280}
    .meridiana .tel{color:#1a7fa8;font-weight:700;font-size:15px}
    .meridiana .hero{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;padding:64px 56px 46px;align-items:center}
    .meridiana h1{font-size:60px;line-height:1.04;font-weight:700;letter-spacing:-.032em}
    .meridiana h1 span{color:#1a7fa8}
    .meridiana .sub{font-size:17px;line-height:1.68;color:#5b7280;margin:22px 0 30px;max-width:36ch}
    .meridiana .acts{display:flex;gap:14px;align-items:center}
    .meridiana .b1{background:#1a7fa8;color:#fff;padding:16px 30px;border-radius:8px;font-size:15px;font-weight:600}
    .meridiana .b2{border:1px solid #cfdde5;padding:16px 26px;border-radius:8px;font-size:15px;color:#0f2230}
    .meridiana .shot{height:330px;border-radius:14px;background-size:cover;background-position:center}
    .meridiana .band{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:0 56px 34px}
    .meridiana .stat{background:#f4f9fb;border-radius:12px;padding:24px}
    .meridiana .stat b{display:block;font-size:34px;font-weight:700;letter-spacing:-.03em;color:#1a7fa8;
      font-variant-numeric:tabular-nums}
    .meridiana .stat span{font-size:13px;color:#5b7280;line-height:1.5;display:block;margin-top:6px}
    .meridiana .strip{background:#0f2230;color:#dcecf3;display:flex;justify-content:space-between;
      align-items:center;padding:26px 56px;font-size:14px}
    .meridiana .strip b{font-size:17px;color:#fff}`,
    html: `
    <div class="top"><div class="mark"><span class="dot"></span>Clínica Meridiana</div>
      <div class="menu"><span>Tratamientos</span><span>Equipo</span><span>Financiación</span><span>Blog</span></div>
      <div class="tel">960 22 14 08</div></div>
    <div class="hero"><div><h1>Tu primera cita, <span>sin coste</span></h1>
      <div class="sub">Diagnóstico completo con radiografía panorámica y plan de tratamiento
        cerrado por escrito. Sin sorpresas después.</div>
      <div class="acts"><div class="b1">Pedir cita online</div><div class="b2">Ver tratamientos</div></div></div>
      <div class="shot" style="background-image:${bg('interior', 'tide', 71, 620, 460)}"></div></div>
    <div class="band">
      <div class="stat"><b>18</b><span>años en el barrio de Russafa</span></div>
      <div class="stat"><b>4.9</b><span>sobre 5 en 612 reseñas</span></div>
      <div class="stat"><b>24 h</b><span>urgencias todos los días</span></div>
      <div class="stat"><b>0 %</b><span>financiación hasta 12 meses</span></div></div>
    <div class="strip"><span>Lunes a viernes · 9:00 – 20:30 · Sábados por la mañana</span>
      <b>Calle Cádiz 48, Valencia</b></div>`,
  });

  /* ---------------------------------------------------------------- 6 */
  const ferra = () => ({
    id: 'ferra',
    css: `
    .ferra{background:#14100c;color:#f0e7d8;font-family:'Work Sans',sans-serif}
    .ferra .top{display:flex;justify-content:space-between;align-items:center;padding:30px 56px}
    .ferra .mark{font-family:'Instrument Serif',serif;font-size:30px;letter-spacing:.02em}
    .ferra .menu{display:flex;gap:30px;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:#a2947e}
    .ferra .res{border:1px solid #6b5b45;padding:11px 24px;font-size:13px;letter-spacing:.1em;text-transform:uppercase}
    .ferra .split{display:grid;grid-template-columns:1fr 1.1fr;gap:0;height:730px}
    .ferra .pic{background-size:cover;background-position:center}
    .ferra .menuside{padding:56px 56px 0 52px}
    .ferra .kick{font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:#c9a25f;margin-bottom:22px}
    .ferra h1{font-family:'Instrument Serif',serif;font-size:64px;line-height:1;font-weight:400;margin-bottom:14px}
    .ferra h1 em{font-style:italic;color:#c9a25f}
    .ferra .note{font-size:15px;line-height:1.7;color:#a2947e;max-width:38ch;margin-bottom:38px}
    .ferra .dish{display:flex;align-items:baseline;gap:14px;padding:15px 0;border-top:1px solid #2a231a}
    .ferra .dish .n{font-family:'Instrument Serif',serif;font-size:23px;white-space:nowrap}
    .ferra .dish .d{flex:1;border-bottom:1px dotted #4a3f30;transform:translateY(-5px)}
    .ferra .dish .p{font-size:17px;font-variant-numeric:tabular-nums;color:#c9a25f}
    .ferra .dish .sub{font-size:13px;color:#8e806b;margin-top:4px}
    .ferra .foot{margin-top:34px;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#8e806b}`,
    html: `
    <div class="top"><div class="mark">Ferra</div>
      <div class="menu"><span>Carta</span><span>Bodega</span><span>La casa</span></div>
      <div class="res">Reservar mesa</div></div>
    <div class="split">
      <div class="pic" style="background-image:${bg('deep', 'ember', 89, 620, 800)}"></div>
      <div class="menuside"><div class="kick">Menú de temporada · marzo</div>
        <h1>Brasa, <em>sal</em><br>y poco más</h1>
        <div class="note">Cinco pases que cambian cada semana según lo que llega de la lonja
          y de la huerta de El Palmar.</div>
        <div class="dish"><div><div class="n">Anchoa curada en casa</div>
          <div class="sub">Pan de cristal, mantequilla ahumada</div></div><div class="d"></div><div class="p">9 €</div></div>
        <div class="dish"><div><div class="n">Alcachofa a la brasa</div>
          <div class="sub">Yema curada y avellana</div></div><div class="d"></div><div class="p">14 €</div></div>
        <div class="dish"><div><div class="n">Sepia y su tinta</div>
          <div class="sub">Guisantes del Maresme</div></div><div class="d"></div><div class="p">18 €</div></div>
        <div class="dish"><div><div class="n">Costilla de vaca vieja</div>
          <div class="sub">Cuarenta días de maduración</div></div><div class="d"></div><div class="p">26 €</div></div>
        <div class="foot">Menú completo 58 € · Maridaje 24 €</div></div></div>`,
  });

  /* ---------------------------------------------------------------- 7 */
  const lumen = () => ({
    id: 'lumen',
    css: `
    .lumen{background:#0a0a0a;color:#fff;font-family:'Work Sans',sans-serif;position:relative}
    .lumen .full{position:absolute;inset:0;background-size:cover;background-position:center}
    .lumen .sc{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,.1) 40%,rgba(0,0,0,.75))}
    .lumen .top{position:absolute;inset:0 0 auto 0;display:flex;justify-content:space-between;
      align-items:center;padding:36px 54px;z-index:2}
    .lumen .mark{font-size:15px;font-weight:700;letter-spacing:.42em}
    .lumen .menu{display:flex;gap:32px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#cfcfcf}
    .lumen .center{position:absolute;left:54px;bottom:210px;z-index:2}
    .lumen h1{font-family:'Instrument Serif',serif;font-size:104px;line-height:.9;font-weight:400;letter-spacing:-.01em}
    .lumen h1 em{font-style:italic}
    .lumen .cap{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:#bdbdbd;margin-bottom:22px}
    .lumen .thumbs{position:absolute;left:54px;right:54px;bottom:48px;z-index:2;display:grid;
      grid-template-columns:repeat(5,1fr);gap:12px}
    .lumen .th{height:104px;background-size:cover;background-position:center;border-radius:2px;opacity:.62}
    .lumen .th.on{opacity:1;box-shadow:0 0 0 2px #fff}
    .lumen .idx{position:absolute;right:54px;bottom:180px;z-index:2;font-size:13px;letter-spacing:.2em;
      color:#cfcfcf;font-variant-numeric:tabular-nums}`,
    html: `
    <div class="full" style="background-image:${bg('landscape', 'plum', 97, 940, 620)}"></div>
    <div class="sc"></div>
    <div class="top"><div class="mark">LUMEN</div>
      <div class="menu"><span>Series</span><span>Editorial</span><span>Copias</span><span>Estudio</span></div></div>
    <div class="center"><div class="cap">Serie 04 — Costa Brava, invierno</div>
      <h1>La luz <em>que queda</em></h1></div>
    <div class="idx">04 / 12</div>
    <div class="thumbs">
      <div class="th on" style="background-image:${bg('landscape', 'plum', 97, 260, 180)}"></div>
      <div class="th" style="background-image:${bg('landscape', 'tide', 101, 260, 180)}"></div>
      <div class="th" style="background-image:${bg('soft', 'stone', 103, 260, 180)}"></div>
      <div class="th" style="background-image:${bg('deep', 'ink', 107, 260, 180)}"></div>
      <div class="th" style="background-image:${bg('landscape', 'dusk', 109, 260, 180)}"></div></div>`,
  });

  /* ---------------------------------------------------------------- 8 */
  const ovillo = () => ({
    id: 'ovillo',
    css: `
    .ovillo{background:#fdfaf6;color:#2b2119;font-family:'Outfit',sans-serif}
    .ovillo .bar{background:#7d3b2e;color:#fdfaf6;text-align:center;padding:10px;font-size:13px;letter-spacing:.06em}
    .ovillo .top{display:flex;justify-content:space-between;align-items:center;padding:24px 52px}
    .ovillo .mark{font-size:27px;font-weight:700;letter-spacing:-.02em}
    .ovillo .menu{display:flex;gap:26px;font-size:14px;color:#6d5c4c}
    .ovillo .icons{display:flex;gap:16px;font-size:13px;color:#6d5c4c}
    .ovillo .hd{padding:26px 52px 20px;display:flex;justify-content:space-between;align-items:flex-end}
    .ovillo .hd h1{font-size:46px;font-weight:700;letter-spacing:-.035em}
    .ovillo .hd .c{font-size:14px;color:#8b7a68}
    .ovillo .filters{display:flex;gap:9px;padding:0 52px 22px}
    .ovillo .f{border:1px solid #e0d5c7;border-radius:999px;padding:8px 17px;font-size:13px;color:#6d5c4c}
    .ovillo .f.on{background:#2b2119;color:#fdfaf6;border-color:#2b2119}
    .ovillo .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;padding:0 52px}
    .ovillo .p .im{position:relative;height:250px;border-radius:8px;background-size:cover;background-position:center}
    .ovillo .p .im .tag{position:absolute;top:12px;left:12px;background:#fdfaf6;font-size:11px;
      font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:6px 10px;border-radius:4px}
    .ovillo .p .n{font-size:17px;font-weight:600;margin:14px 0 3px}
    .ovillo .p .m{font-size:13px;color:#8b7a68}
    .ovillo .p .pr{display:flex;align-items:baseline;gap:9px;margin-top:9px}
    .ovillo .p .pr b{font-size:18px;font-weight:700;font-variant-numeric:tabular-nums}
    .ovillo .p .pr s{font-size:14px;color:#a99783}
    .ovillo .sw{display:flex;gap:6px;margin-top:11px}
    .ovillo .sw i{width:15px;height:15px;border-radius:50%;display:block;box-shadow:0 0 0 1px rgba(0,0,0,.12)}`,
    html: `
    <div class="bar">Envío gratis a partir de 60 € · Devoluciones en 30 días</div>
    <div class="top"><div class="mark">ovillo</div>
      <div class="menu"><span>Punto</span><span>Lanas</span><span>Patrones</span><span>Talleres</span></div>
      <div class="icons"><span>Buscar</span><span>Cuenta</span><span>Cesta (3)</span></div></div>
    <div class="hd"><h1>Jerséis de invierno</h1><div class="c">42 artículos</div></div>
    <div class="filters"><div class="f on">Todo</div><div class="f">Lana merina</div>
      <div class="f">Algodón orgánico</div><div class="f">Hecho a mano</div><div class="f">Rebajas</div></div>
    <div class="grid">
      <div class="p"><div class="im" style="background-image:${bg('soft', 'ember', 127, 340, 320)}">
        <div class="tag">−20 %</div></div><div class="n">Jersey Duna</div><div class="m">Merina · trenzado</div>
        <div class="pr"><b>79,00 €</b><s>99,00 €</s></div>
        <div class="sw"><i style="background:#c9a27a"></i><i style="background:#3c4a3a"></i><i style="background:#8c3b2e"></i></div></div>
      <div class="p"><div class="im" style="background-image:${bg('soft', 'moss', 131, 340, 320)}"></div>
        <div class="n">Cárdigan Ría</div><div class="m">Lana y alpaca</div>
        <div class="pr"><b>118,00 €</b></div>
        <div class="sw"><i style="background:#4a5b47"></i><i style="background:#d8cdb8"></i></div></div>
      <div class="p"><div class="im" style="background-image:${bg('soft', 'linen', 137, 340, 320)}">
        <div class="tag">Nuevo</div></div><div class="n">Chaleco Sella</div><div class="m">Algodón orgánico</div>
        <div class="pr"><b>64,00 €</b></div>
        <div class="sw"><i style="background:#e6dcc9"></i><i style="background:#2b3542"></i><i style="background:#b08968"></i></div></div>
      <div class="p"><div class="im" style="background-image:${bg('soft', 'tide', 139, 340, 320)}"></div>
        <div class="n">Jersey Norte</div><div class="m">Merina gruesa</div>
        <div class="pr"><b>92,00 €</b></div>
        <div class="sw"><i style="background:#33506b"></i><i style="background:#9aa7ae"></i></div></div>
    </div>`,
  });

  /* ---------------------------------------------------------------- 9 */
  const cadencia = () => ({
    id: 'cadencia',
    css: `
    .cadencia{background:#120b18;color:#f6ecff;font-family:'Outfit',sans-serif}
    .cadencia .top{display:flex;justify-content:space-between;align-items:center;padding:28px 52px}
    .cadencia .mark{font-size:22px;font-weight:700;letter-spacing:.22em}
    .cadencia .menu{display:flex;gap:26px;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:#a892b8}
    .cadencia .buy{background:#ff5c39;color:#fff;padding:11px 22px;border-radius:4px;font-size:13px;
      font-weight:700;letter-spacing:.08em;text-transform:uppercase}
    .cadencia .hero{position:relative;margin:6px 52px 0;height:300px;border-radius:10px;overflow:hidden;
      background-size:cover;background-position:center;display:flex;align-items:center}
    .cadencia .sc{position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,7,20,.92) 30%,rgba(14,7,20,.2))}
    .cadencia .hin{position:relative;padding:0 46px}
    .cadencia .kick{font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#ff5c39;
      font-weight:700;margin-bottom:14px}
    .cadencia h1{font-size:72px;line-height:.94;font-weight:700;letter-spacing:-.04em}
    .cadencia .list{padding:34px 52px 0}
    .cadencia .ev{display:grid;grid-template-columns:104px 1fr 150px 120px;align-items:center;gap:24px;
      padding:20px 0;border-top:1px solid #261a30}
    .cadencia .dt{text-align:center;border-right:1px solid #261a30;padding-right:16px}
    .cadencia .dt b{display:block;font-size:32px;font-weight:700;line-height:1;font-variant-numeric:tabular-nums}
    .cadencia .dt span{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#a892b8}
    .cadencia .ev .nm{font-size:24px;font-weight:600;letter-spacing:-.02em}
    .cadencia .ev .gn{font-size:13px;color:#a892b8;margin-top:4px}
    .cadencia .ev .hr{font-size:14px;color:#a892b8;font-variant-numeric:tabular-nums}
    .cadencia .ev .tk{justify-self:end;border:1px solid #4a3358;border-radius:4px;padding:10px 18px;font-size:13px}
    .cadencia .ev .tk.out{border-color:#2a1e33;color:#6c5a7a}`,
    html: `
    <div class="top"><div class="mark">CADENCIA</div>
      <div class="menu"><span>Agenda</span><span>Sala</span><span>Abonos</span><span>Alquiler</span></div>
      <div class="buy">Entradas</div></div>
    <div class="hero" style="background-image:${bg('deep', 'plum', 149, 900, 380)}"><div class="sc"></div>
      <div class="hin"><div class="kick">Temporada 25/26 · Zaragoza</div>
        <h1>Música en<br>directo, cada<br>jueves</h1></div></div>
    <div class="list">
      <div class="ev"><div class="dt"><b>14</b><span>Mar</span></div>
        <div><div class="nm">Marina Herlop</div><div class="gn">Piano y electrónica</div></div>
        <div class="hr">21:00 · Sala grande</div><div class="tk">Últimas</div></div>
      <div class="ev"><div class="dt"><b>21</b><span>Mar</span></div>
        <div><div class="nm">Trio Balcánico</div><div class="gn">Folk de los Balcanes</div></div>
        <div class="hr">20:30 · Sótano</div><div class="tk">18 €</div></div>
      <div class="ev"><div class="dt"><b>28</b><span>Mar</span></div>
        <div><div class="nm">Rodrigo Cuevas</div><div class="gn">Folclore y cabaré</div></div>
        <div class="hr">21:30 · Sala grande</div><div class="tk out">Agotado</div></div>
    </div>`,
  });

  const list = [bruma, nudo, tinta, volta, meridiana, ferra, lumen, ovillo, cadencia];

  /* Built lazily on first call so the canvas work happens once, at init. */
  let built = null;
  function all() {
    if (!built) built = list.map((f) => f());
    return built;
  }
  return { all };
})();
