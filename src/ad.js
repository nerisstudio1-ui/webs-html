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

  /* Beat sheet, in seconds.
   *
   * The first beat exists because feeds autoplay muted and most people are
   * gone inside two seconds: frame 0 already carries the price, full frame,
   * before a single mock site appears. */
  const T = {
    hookOut: 1.30,    // hook starts leaving upward
    hookGone: 2.10,   // hook fully clear of the frame
    beltStart: 0.90,  // belt starts under the hook, so the first card is already
                      // arriving as the hook clears — otherwise there is a beat
                      // of empty ground between the two
    flowEnd: 7.80,    // conveyor stops cruising
    sweepEnd: 8.90,   // last site card has left the top
    plateIn: 7.80,    // the offer enters on the belt behind the last card
    plateSet: 9.30,   // offer has braked to centre and squared up to camera
    // The plate's contents fill in while it is still travelling, so it never
    // sits centred with an empty lower half waiting to be populated.
    ruleIn: 8.50,
    listIn: 8.65,
    ctaIn: 9.10,
  };

  /* Geometry. */
  const CARD_W = 0.775;   // card width as a fraction of frame width
  const OVERLAP = 0.64;   // centre-to-centre gap as a fraction of card height
  const SWEEP_TOP = 1.55; // speed the belt accelerates to on the way out

  /* The card is a window onto a taller page. Showing 760 of the site's 900
     authored pixels leaves 140 to travel, so each card scrolls its own site as
     it crosses the frame: the mock sites read as live pages rather than
     screenshots, and the viewer sees more of each one. */
  const SITE_H = 900;
  const VIEW_H = 760;

  /* One card squares up to the camera as it passes the middle — a beat that
     says "look at this one" and breaks the metronome of the belt. */
  const HERO = 3;         // index into the site list (cadencia)
  const HERO_HOLD = 0.46; // seconds either side of centre
  let heroAt = 0;         // solved in buildCards once the speed is known

  /* Cruise speed is solved rather than fixed, so the ninth card reaches the
     middle of the frame exactly as the flow ends — on every aspect ratio. */
  let cruise = 0;
  let slot = 0;
  let first = 0;

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
  const easeInCubic = (u) => u * u * u;
  const easeInOut = (u) => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2);
  /* Overshoots its target and settles — what makes the offer land instead of
     arrive. Kept mild on purpose; a big bounce reads as a template. */
  const easeOutBack = (u, s) => {
    const c1 = s == null ? 1.10 : s;
    const c3 = c1 + 1;
    const p = u - 1;
    return 1 + c3 * p * p * p + c1 * p * p;
  };
  const span = (t, a, b) => clamp01((t - a) / (b - a));
  /* 0 at the edges, 1 in the middle — for beats that rise and fall. */
  const bump = (t, centre, half) => {
    const d = Math.abs(t - centre) / half;
    return d >= 1 ? 0 : easeInOut(1 - d);
  };

  let stage, conveyor, offer, hook, capEl;
  let fmt, W, H;
  let cards = [];
  let plate = { start: 0, end: 0 };
  let staggered = [];
  let bound = false;   // resize listeners are attached on the first init only

  /* ---- the hook -------------------------------------------------------- */

  /* Each part is animated separately off the clock rather than arriving as one
     block: the eye gets led down to the number instead of being handed the
     whole card at once. Elements are cached because seek() runs 360 times a
     render and querying every frame is wasted work. */
  let hookParts = null;

  function buildHook() {
    hook.innerHTML = `
      <div class="l1"><span>Tu web profesional</span><span><i>por solo</i></span></div>
      <div class="amount">299&thinsp;€</div>
      <div class="rule"></div>
      <div class="l3">Diseño a medida y en marcha en <b>7 días</b>.</div>`;

    hookParts = {
      lines: Array.from(hook.querySelectorAll('.l1 span')),
      amount: hook.querySelector('.amount'),
      rule: hook.querySelector('.rule'),
      sub: hook.querySelector('.l3'),
    };
  }

  function drawHook(t) {
    const p = hookParts;
    if (!p) return;

    p.lines.forEach((el, i) => {
      const u = easeOutCubic(span(t, 0.06 + i * 0.11, 0.56 + i * 0.11));
      el.style.opacity = u.toFixed(3);
      el.style.transform = `translateY(${((1 - u) * H * 0.030).toFixed(1)}px)`;
    });

    // The number punches in slightly oversized and settles.
    const au = span(t, 0.26, 0.86);
    const ae = easeOutBack(au, 1.25);
    p.amount.style.opacity = clamp01(au * 2.2).toFixed(3);
    p.amount.style.transform = `scale(${(0.86 + 0.14 * ae).toFixed(4)})`;

    p.rule.style.transform = `scaleX(${easeOutCubic(span(t, 0.46, 1.00)).toFixed(4)})`;

    const su = easeOutCubic(span(t, 0.62, 1.12));
    p.sub.style.opacity = su.toFixed(3);
    p.sub.style.transform = `translateY(${((1 - su) * H * 0.018).toFixed(1)}px)`;
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
      const ch = VIEW_H * scale;

      const el = document.createElement('div');
      el.className = 'ad-card';
      el.style.width = cw + 'px';
      el.style.height = ch + 'px';

      const inner = document.createElement('div');
      inner.className = 'ad-site ' + site.id;
      inner.innerHTML = site.html;
      el.appendChild(inner);

      // Specular band that crosses the card as it passes — the cue that these
      // are physical objects catching light, not flat images pasted on blue.
      const glare = document.createElement('div');
      glare.className = 'glare';
      el.appendChild(glare);

      conveyor.appendChild(el);

      return {
        el,
        inner,
        glare,
        h: ch,
        scale,
        hero: i === HERO,
        caption: CAPTIONS[site.id] || site.id,
        dx: (((i * 53) % 7) - 3) * W * 0.028,
        rz: -7.4 + (((i * 29) % 5) - 2) * 0.55,
        ry: -11 + (((i * 17) % 5) - 2) * 1.1,
        rx: 4.6 + (((i * 41) % 5) - 2) * 0.5,
      };
    });

    const cardH = cards[0].h;
    slot = cardH * OVERLAP;
    // Card 0 waits below the bottom edge — far enough that the tilt's bounding
    // box stays out of frame while the hook is still holding.
    first = H + cardH * 1.05;
    const distance = (first - H * 0.5) + (cards.length - 1) * slot;
    cruise = distance / (T.flowEnd - T.beltStart);

    // When the hero card's centre crosses the middle of the frame.
    heroAt = T.beltStart + (first + HERO * slot - H * 0.5) / cruise;

    // Style tags for the mock sites. init() can be called again to switch
    // format in place, so this is injected once rather than once per call.
    if (!document.getElementById('site-styles')) {
      const css = document.createElement('style');
      css.id = 'site-styles';
      css.textContent = sites.map((s) => s.css).join('\n');
      document.head.appendChild(css);
    }
  }

  /* Distance the belt has covered by time t: still under the hook, then
     cruising, then accelerating away so the last card is gone before the offer
     squares up. */
  function beltDistance(t) {
    if (t <= T.beltStart) return 0;
    if (t <= T.flowEnd) return cruise * (t - T.beltStart);
    const dt = t - T.flowEnd;
    const a = (SWEEP_TOP * H - cruise) / (T.sweepEnd - T.flowEnd);
    return cruise * (T.flowEnd - T.beltStart) + cruise * dt + 0.5 * a * dt * dt;
  }

  /* ---- the offer ------------------------------------------------------- */

  function buildOffer() {
    offer.innerHTML = `
      <div class="eyebrow">Neris Studio · Diseño y desarrollo web</div>
      <h2>Tu web, <i>lista en 7 días</i></h2>
      <div class="rule"></div>
      <div class="lock">
        <div class="amount">299&thinsp;€</div>
        <div class="terms"><b>Pago único.</b><br><i>Sin cuotas ni permanencia.</i></div>
      </div>
      <ul>
        <li class="stagger"><i>—</i><span>Diseño <b>a medida</b>, no una plantilla</span></li>
        <li class="stagger"><i>—</i><span>Dominio y alojamiento <b>del primer año</b></span></li>
        <li class="stagger"><i>—</i><span>Textos, formulario y <em>visible en Google</em></span></li>
      </ul>
      <div class="cta stagger"><span>Pide la tuya en neris.studio</span><span class="arrow">→</span></div>`;

    staggered = Array.from(offer.querySelectorAll('.stagger'));
  }

  /* ---- the one function that draws a frame ----------------------------- */

  function seek(t) {
    t = Math.max(0, Math.min(DURATION, t));

    /* Hook: assembles, holds, then accelerates off the top so it reads as the
       first thing on the belt rather than a title card bolted to the front. */
    const hookGone = t >= T.hookGone;
    hook.style.visibility = hookGone ? 'hidden' : 'visible';
    if (!hookGone) {
      drawHook(t);
      const hu = span(t, T.hookOut, T.hookGone);
      hook.style.transform = `translate3d(0, ${(-easeInCubic(hu) * H * 1.25).toFixed(1)}px, 0)`;
    }

    const belt = beltDistance(t);

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

      // How far this card has crossed the frame: 0 entering at the bottom,
      // 1 leaving at the top. Drives the page scroll and the light band.
      const p = clamp01((H + c.h / 2 - centre) / (H + c.h));

      // The site scrolls inside its own window as the card travels.
      c.inner.style.transform =
        `scale(${c.scale}) translateY(${(-(SITE_H - VIEW_H) * p).toFixed(1)}px)`;

      // The band sweeps across while the card is around the middle of frame.
      const g = -115 + 230 * easeInOut(span(p, 0.22, 0.70));
      c.glare.style.transform = `translateX(${g.toFixed(1)}%)`;

      // Hero beat: this one straightens up and steps toward the camera as it
      // passes, then falls back into the rhythm of the belt.
      const h = c.hero ? bump(t, heroAt, HERO_HOLD) : 0;
      const k = 1 - h;

      c.el.style.transform =
        `translate3d(calc(-50% + ${(c.dx * k).toFixed(1)}px), ${top.toFixed(1)}px, 0)` +
        ` scale(${(1 + 0.065 * h).toFixed(4)})` +
        ` rotateZ(${(c.rz * k).toFixed(2)}deg)` +
        ` rotateY(${(c.ry * k).toFixed(2)}deg)` +
        ` rotateX(${(c.rx * k).toFixed(2)}deg)`;

      const d = Math.abs(centre - H * 0.5);
      if (d < nearestDist) { nearestDist = d; nearest = c; }
    }

    /* The offer brakes from belt speed to a standstill and untilts as it
       arrives — the last thing on the conveyor turns to face you. */
    const pu = span(t, T.plateIn, T.plateSet);
    // Overshoots the centre by a hair and settles back: the offer lands rather
    // than drifts to a stop.
    const travel = pu >= 1 ? 1 : easeOutBack(easeOutQuad(pu), 0.9);
    const top = plate.start + (plate.end - plate.start) * travel;
    const tilt = 1 - easeOutCubic(span(t, T.plateIn + 0.4, T.plateSet));
    const lift = 1 - 0.06 * (1 - clamp01(travel));

    offer.style.visibility = t >= T.plateIn ? 'visible' : 'hidden';
    offer.style.transform =
      `translate3d(calc(-50% + ${(22 * tilt).toFixed(1)}px), ${top.toFixed(1)}px, 0)` +
      ` scale(${lift.toFixed(4)})` +
      ` rotateZ(${(-7.4 * tilt).toFixed(2)}deg)` +
      ` rotateY(${(-11 * tilt).toFixed(2)}deg)` +
      ` rotateX(${(4.6 * tilt).toFixed(2)}deg)`;

    const rule = offer.querySelector('.rule');
    if (rule) rule.style.transform = `scaleX(${easeOutCubic(span(t, T.ruleIn, T.ruleIn + 0.5)).toFixed(4)})`;

    staggered.forEach((el, i) => {
      const isCta = el.classList.contains('cta');
      const start = isCta ? T.ctaIn : T.listIn + i * 0.13;
      const u = easeOutCubic(span(t, start, start + 0.45));
      el.style.opacity = u.toFixed(3);
      el.style.transform = `translateY(${((1 - u) * W * 0.020).toFixed(2)}px)`;
    });

    if (capEl) {
      capEl.textContent = t >= T.plateSet - 0.8
        ? 'neris.studio'
        : (t < T.hookOut ? '' : (nearest ? nearest.caption : ''));
    }
  }

  /* ---- boot ------------------------------------------------------------ */

  function layout(key) {
    fmt = FORMATS[key] || FORMATS['4x5'];
    W = fmt.w; H = fmt.h;
    // The offer plate and the hook scale off the smaller of the two axes so
    // they stay inside a square frame as comfortably as a 9:16 one.
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
    conveyor = document.getElementById('conveyor');
    offer = document.getElementById('offer');
    hook = document.getElementById('hook');

    layout(key);

    // `document.fonts.ready` alone is not enough: at this point nothing on the
    // page uses these families yet, so nothing has been requested and it
    // resolves immediately. Everything built below is then measured against
    // fallback metrics — a first render that disagrees with every later one.
    // Ask for the faces explicitly, then wait.
    await Promise.all([
      document.fonts.load("500 16px Montserrat"),
      document.fonts.load("700 16px Montserrat"),
      document.fonts.load("900 300px Montserrat"),
      document.fonts.load("italic 700 16px Montserrat"),
      document.fonts.load("400 16px 'Geist Mono'"),
      document.fonts.load("400 16px 'Work Sans'"),
      document.fonts.load("700 16px 'Work Sans'"),
      document.fonts.load("400 16px 'Instrument Serif'"),
      document.fonts.load("italic 400 16px 'Instrument Serif'"),
      document.fonts.load("400 16px Outfit"),
      document.fonts.load("700 16px Outfit"),
      document.fonts.load("400 16px Lora"),
      document.fonts.load("700 16px Lora"),
    ].map((p) => p.catch(() => null)));
    await document.fonts.ready;

    // init() runs again when the preview switches format, and by then fit()
    // has left a scale on the stage. Measure at scale 1 and let fit() put the
    // scale back afterwards.
    stage.style.transform = 'none';

    buildHook();
    buildCards();
    buildOffer();

    capEl = document.querySelector('.hud.br');

    // offsetHeight, not getBoundingClientRect: on a re-init the plate still
    // carries the tilt transform from the last frame drawn, and a rect is the
    // bounding box of the *rotated* element — tens of pixels too tall.
    const ph = offer.offsetHeight;
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
