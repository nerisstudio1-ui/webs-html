/* Timeline engine.
 *
 * Everything on screen is a pure function of `t` in seconds — there are no CSS
 * animations and no rAF-accumulated state. tools/render.mjs drives the exact
 * same `seek()` the live preview does, one frame at a time, so the captured
 * MP4 and the browser preview are the same piece. */

const AD = (() => {
  /* Facebook's placements, in the sizes Meta actually serves. */
  const FORMATS = {
    '4x5':  { w: 1080, h: 1350, name: 'Feed 4:5' },
    '3x4':  { w: 1080, h: 1440, name: 'Feed 3:4' },
    '9x16': { w: 1080, h: 1920, name: 'Reels / Stories 9:16' },
    '1x1':  { w: 1080, h: 1080, name: 'Feed 1:1' },
  };

  const DURATION = 12.0;

  /* Beat sheet, in seconds. */
  const T = {
    flowEnd: 7.0,     // conveyor stops running at cruising speed
    sweepEnd: 8.3,    // last site card has left the top of the frame
    plateIn: 7.0,     // the offer enters on the belt behind the last card
    plateSet: 8.9,    // offer has braked to centre and squared up to camera
    // The plate's contents fill in while it is still travelling, so it never
    // sits centred with an empty lower half waiting to be populated.
    ruleIn: 7.85,
    listIn: 8.00,
    ctaIn: 8.55,
  };

  /* Geometry. Cards are deliberately narrower than the frame: the tilt then
     leaves wedges of paper down both edges, which is where the display type
     shows through. Cover the whole width and the field behind disappears. */
  const CARD_W = 0.775;   // card width as a fraction of frame width
  const OVERLAP = 0.76;   // centre-to-centre gap as a fraction of card height
  const FIRST = 0.10;     // centre of card 0 at t=0, as a fraction of height
  const SWEEP_TOP = 1.40; // speed the belt accelerates to on the way out
  const MARQ = 0.100;     // display-type field px/s (deliberate parallax)

  /* Cruise speed is solved rather than fixed, so that the ninth card reaches
     the middle of the frame exactly as the flow ends — on every aspect ratio. */
  let cruise = 0;
  let slot = 0;

  /* What the pinned bottom-right label reads as each card passes. */
  const CAPTIONS = {
    bruma: 'Casa Bruma — hotel rural',
    nudo: 'Nudo — estudio de arquitectura',
    tinta: 'Tinta & Grano — tienda de café',
    volta: 'Volta — club de pádel',
    meridiana: 'Clínica Meridiana — reserva de citas',
    ferra: 'Ferra — restaurante',
    lumen: 'Lumen — porfolio de fotografía',
    ovillo: 'Ovillo — tienda online',
    cadencia: 'Cadencia — sala de conciertos',
  };

  const clamp01 = (x) => (x < 0 ? 0 : x > 1 ? 1 : x);
  const easeOutQuad = (u) => u * (2 - u);
  const easeOutCubic = (u) => 1 - Math.pow(1 - u, 3);
  const span = (t, a, b) => clamp01((t - a) / (b - a));

  let stage, marquee, conveyor, offer, capEl;
  let fmt, W, H;
  let cards = [];
  let marqueeLoop = 0;
  let plate = { start: 0, end: 0 };
  let staggered = [];
  let bound = false;   // resize listeners are attached on the first init only

  /* ---- display type field --------------------------------------------- */

  /* Both words are optically justified to the same over-width. Measuring the
     natural width and solving for letter-spacing keeps the two lines bleeding
     off the same edges even though "TU WEB" and "A 299 €" are different
     lengths — and it means the treatment survives a copy change. */
  function buildMarquee() {
    const type = W * 0.300;
    const lineH = type * 0.80;
    const target = W * 1.14;

    stage.style.setProperty('--type', type + 'px');

    const words = ['TU WEB', 'A 299 €'];
    const rows = Math.ceil(H / lineH) + 3;
    marquee.innerHTML = '';

    const probe = document.createElement('span');
    probe.className = 'line';
    probe.style.cssText = 'position:absolute;visibility:hidden;letter-spacing:0';
    marquee.appendChild(probe);

    const tracking = words.map((word) => {
      probe.textContent = word;
      const natural = probe.getBoundingClientRect().width;
      return (target - natural) / word.length;
    });
    probe.remove();

    for (let i = 0; i < rows; i++) {
      const k = i % 2;
      const el = document.createElement('span');
      el.className = 'line' + (k === 1 ? ' price' : '');
      el.textContent = words[k];
      el.style.letterSpacing = tracking[k].toFixed(2) + 'px';
      // Letter-spacing also trails the final glyph; pull it back so the line
      // stays optically centred.
      el.style.marginRight = (-tracking[k]).toFixed(2) + 'px';
      marquee.appendChild(el);
    }

    // The pattern repeats every two lines, so that is the scroll modulus.
    marqueeLoop = lineH * 2;
    marquee.style.top = -marqueeLoop + 'px';
  }

  /* ---- conveyor -------------------------------------------------------- */

  function buildCards() {
    const sites = SITES.all();
    conveyor.innerHTML = '';
    cards = sites.map((site, i) => {
      // A little variation in size and lateral placement, seeded off the index
      // so it is stable between runs, keeps the belt from looking mechanical.
      const wf = CARD_W + ((i * 37) % 5) * 0.016;
      const cw = W * wf;
      const scale = cw / 1440;
      const ch = 900 * scale;

      const el = document.createElement('div');
      el.className = 'ad-card';
      el.style.width = cw + 'px';
      el.style.height = ch + 'px';

      const inner = document.createElement('div');
      inner.className = 'ad-site ' + site.id;
      inner.style.transform = `scale(${scale})`;
      inner.innerHTML = site.html;
      el.appendChild(inner);
      conveyor.appendChild(el);

      return {
        el,
        h: ch,
        caption: CAPTIONS[site.id] || site.id,
        dx: (((i * 53) % 7) - 3) * W * 0.028,
        rz: -7.4 + (((i * 29) % 5) - 2) * 0.55,
        ry: -11 + (((i * 17) % 5) - 2) * 1.1,
        rx: 4.6 + (((i * 41) % 5) - 2) * 0.5,
      };
    });

    const cardH = cards[0].h;
    slot = cardH * OVERLAP;
    cruise = (FIRST * H + (cards.length - 1) * slot - H * 0.5) / T.flowEnd;

    // Style tags for the mock sites. init() can be called again to switch
    // format in place, so this is injected once rather than once per call.
    if (!document.getElementById('site-styles')) {
      const css = document.createElement('style');
      css.id = 'site-styles';
      css.textContent = sites.map((s) => s.css).join('\n');
      document.head.appendChild(css);
    }
  }

  /* Distance the belt has covered by time t: cruising, then accelerating away
     so the last card is gone before the offer squares up. */
  function beltDistance(t) {
    if (t <= T.flowEnd) return cruise * t;
    const dt = t - T.flowEnd;
    const a = (SWEEP_TOP * H - cruise) / (T.sweepEnd - T.flowEnd);
    return cruise * T.flowEnd + cruise * dt + 0.5 * a * dt * dt;
  }

  /* The type field runs slower than the belt and coasts to a standstill, so
     the composition is locked by the time the offer lands. */
  function marqueeDistance(t) {
    const v = MARQ * H;
    if (t <= T.flowEnd) return v * t;
    const stop = T.plateSet;
    const u = clamp01((t - T.flowEnd) / (stop - T.flowEnd));
    return v * T.flowEnd + v * (stop - T.flowEnd) * (u - (u * u) / 2);
  }

  /* ---- the offer ------------------------------------------------------- */

  function buildOffer() {
    offer.innerHTML = `
      <div class="eyebrow">Neris Studio · Diseño y desarrollo web</div>
      <h2><span>Una web así,</span><span>lista en 7 días</span></h2>
      <div class="rule"></div>
      <div class="lock">
        <div class="amount">299&thinsp;€</div>
        <div class="terms"><b>Pago único.</b><br>Sin cuotas ni permanencia.</div>
      </div>
      <ul>
        <li class="stagger"><i>—</i><span>Diseño a medida, no una plantilla</span></li>
        <li class="stagger"><i>—</i><span>Dominio y alojamiento del primer año</span></li>
        <li class="stagger"><i>—</i><span>Textos, formulario y visible en Google</span></li>
      </ul>
      <div class="cta stagger"><span>Pide la tuya en neris.studio</span><span class="arrow">→</span></div>`;

    staggered = Array.from(offer.querySelectorAll('.stagger'));
  }

  /* ---- the one function that draws a frame ----------------------------- */

  function seek(t) {
    t = Math.max(0, Math.min(DURATION, t));

    marquee.style.transform =
      `translate3d(0, ${(marqueeLoop - (marqueeDistance(t) % marqueeLoop)).toFixed(2)}px, 0)`;

    const belt = beltDistance(t);
    const first = FIRST * H;

    let nearest = null;
    let nearestDist = Infinity;

    for (let i = 0; i < cards.length; i++) {
      const c = cards[i];
      const centre = first + i * slot - belt;
      const top = centre - c.h / 2;

      // Cards well outside the frame are parked rather than transformed, which
      // keeps the compositor honest on the long 9:16 frame.
      const visible = top > -c.h - 200 && top < H + 200;
      c.el.style.visibility = visible ? 'visible' : 'hidden';
      if (!visible) continue;

      c.el.style.transform =
        `translate3d(calc(-50% + ${c.dx.toFixed(1)}px), ${top.toFixed(1)}px, 0)` +
        ` rotateZ(${c.rz}deg) rotateY(${c.ry}deg) rotateX(${c.rx}deg)`;

      const d = Math.abs(centre - H * 0.5);
      if (d < nearestDist) { nearestDist = d; nearest = c; }
    }

    /* The offer brakes from belt speed to a standstill, and untilts as it
       arrives — the last thing on the conveyor turns to face you. */
    const pu = span(t, T.plateIn, T.plateSet);
    const travel = easeOutQuad(pu);
    const top = plate.start + (plate.end - plate.start) * travel;
    const tilt = 1 - easeOutCubic(span(t, T.plateIn + 0.5, T.plateSet));
    const lift = 1 - 0.06 * (1 - travel);

    offer.style.visibility = t >= T.plateIn ? 'visible' : 'hidden';
    offer.style.transform =
      `translate3d(calc(-50% + ${(22 * tilt).toFixed(1)}px), ${top.toFixed(1)}px, 0)` +
      ` scale(${lift.toFixed(4)})` +
      ` rotateZ(${(-7.4 * tilt).toFixed(2)}deg)` +
      ` rotateY(${(-11 * tilt).toFixed(2)}deg)` +
      ` rotateX(${(4.6 * tilt).toFixed(2)}deg)`;

    const rule = offer.querySelector('.rule');
    if (rule) rule.style.transform = `scaleX(${easeOutCubic(span(t, T.ruleIn, T.ruleIn + 0.55)).toFixed(4)})`;

    staggered.forEach((el, i) => {
      const isCta = el.classList.contains('cta');
      const start = isCta ? T.ctaIn : T.listIn + i * 0.14;
      const u = easeOutCubic(span(t, start, start + 0.5));
      el.style.opacity = u.toFixed(3);
      el.style.transform = `translateY(${((1 - u) * W * 0.022).toFixed(2)}px)`;
    });

    if (capEl) {
      capEl.textContent = t >= T.plateSet - 0.6
        ? 'neris.studio'
        : (nearest ? nearest.caption : '');
    }
  }

  /* ---- boot ------------------------------------------------------------ */

  function layout(key) {
    fmt = FORMATS[key] || FORMATS['4x5'];
    W = fmt.w; H = fmt.h;
    // The offer plate scales off the smaller of the two axes so it stays
    // inside a square frame as comfortably as it does inside a 9:16 one.
    const u = Math.min(W, H * 0.75);
    for (const el of [stage, document.documentElement]) {
      el.style.setProperty('--W', W + 'px');
      el.style.setProperty('--H', H + 'px');
      el.style.setProperty('--u', u + 'px');
    }
  }

  /* Scale the frame to sit centred inside its host box. Measuring the host
     rather than the window is what lets the same component fill a browser
     window, sit inside a bordered player on a preview page, and land at scale
     1 in the renderer's exactly-sized viewport. */
  function fit() {
    const host = stage.parentElement;
    const hw = host.clientWidth || W;
    const hh = host.clientHeight || H;
    const k = Math.min(hw / W, hh / H);
    stage.style.transform =
      `translate(${((hw - W * k) / 2).toFixed(2)}px, ${((hh - H * k) / 2).toFixed(2)}px) scale(${k})`;
  }

  async function init(key) {
    stage = document.getElementById('stage');
    marquee = document.getElementById('marquee');
    conveyor = document.getElementById('conveyor');
    offer = document.getElementById('offer');

    layout(key);
    await document.fonts.ready;

    buildMarquee();
    buildCards();
    buildOffer();

    capEl = document.querySelector('.hud.br');

    // Measured after layout so the plate travels a real distance on any format.
    const ph = offer.getBoundingClientRect().height;
    plate.start = H + ph * 0.10;
    plate.end = (H - ph) / 2;

    fit();
    if (!bound) {
      bound = true;
      window.addEventListener('resize', fit);
      if (typeof ResizeObserver === 'function') {
        new ResizeObserver(fit).observe(stage.parentElement);
      }
    }
    seek(0);
    return { seek, duration: DURATION, format: fmt };
  }

  return { init, seek, FORMATS, DURATION };
})();
