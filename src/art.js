/* Imagery for the mini-sites.
 *
 * The ad renders headless with no network and publishes under a CSP that
 * blocks remote images, so every "photo" in every mock site is painted here
 * on a canvas. Everything is driven by a seeded PRNG: the same seed always
 * paints the same pixels, which is what lets the frame renderer capture a
 * deterministic timeline. */

const ART = (() => {
  function rng(seed) {
    let s = seed >>> 0 || 1;
    return function () {
      s ^= s << 13; s >>>= 0;
      s ^= s >> 17;
      s ^= s << 5; s >>>= 0;
      return s / 4294967296;
    };
  }

  // Palettes are named for the mood each mini-site needs, not for the hue, so
  // a site asks for `dusk` and gets a consistent set of stops back.
  const PALETTES = {
    dusk:   ['#2b1d3a', '#7c4a5b', '#d98d6a', '#f3c28b', '#fbe7cd'],
    stone:  ['#b9b3aa', '#d7d2c9', '#efece6', '#9a948b', '#78736c'],
    moss:   ['#1d2a1f', '#38513a', '#6b8a63', '#a9bf95', '#dfe6cd'],
    ember:  ['#2a0f0b', '#7a2416', '#c4471f', '#e8823a', '#f6c68a'],
    tide:   ['#0d2330', '#14495c', '#2b7f92', '#7cbcc4', '#cfe6e6'],
    plum:   ['#1b1020', '#412048', '#7b3a6b', '#c06a8c', '#f0b6bd'],
    linen:  ['#e9e2d6', '#d8ccb8', '#c2b39c', '#f5f0e6', '#a89881'],
    ink:    ['#0a0a0b', '#1c1c20', '#33333a', '#55555f', '#7a7a85'],
    citrus: ['#3d2a06', '#8a5a10', '#d39320', '#eec257', '#f8e6a8'],
    steel:  ['#14171c', '#252b34', '#3d4652', '#66727f', '#a8b3bd'],
  };

  function lerp(a, b, t) { return a + (b - a) * t; }

  function hexToRgb(hex) {
    const n = parseInt(hex.slice(1), 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
  }

  function mix(c1, c2, t) {
    const a = hexToRgb(c1), b = hexToRgb(c2);
    return `rgb(${Math.round(lerp(a[0], b[0], t))},${Math.round(lerp(a[1], b[1], t))},${Math.round(lerp(a[2], b[2], t))})`;
  }

  /* A soft out-of-focus field: overlapping radial blooms over a vertical
   * gradient. Reads as a photograph at the size these cards are shown. */
  function bloom(ctx, w, h, pal, rand, opts) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, pal[opts.top]);
    g.addColorStop(1, pal[opts.bottom]);
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);

    const blobs = opts.blobs || 7;
    for (let i = 0; i < blobs; i++) {
      const x = rand() * w;
      const y = rand() * h;
      const r = (0.18 + rand() * 0.45) * Math.max(w, h);
      const c = pal[Math.floor(rand() * pal.length)];
      const rg = ctx.createRadialGradient(x, y, 0, x, y, r);
      rg.addColorStop(0, c);
      rg.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.globalAlpha = 0.30 + rand() * 0.35;
      ctx.fillStyle = rg;
      ctx.fillRect(0, 0, w, h);
    }
    ctx.globalAlpha = 1;
  }

  /* Horizon banding — the cue that reads "landscape" rather than "texture". */
  function horizon(ctx, w, h, pal, rand) {
    const hy = h * (0.52 + rand() * 0.16);
    const sky = ctx.createLinearGradient(0, 0, 0, hy);
    sky.addColorStop(0, pal[0]);
    sky.addColorStop(0.6, pal[2]);
    sky.addColorStop(1, pal[3]);
    ctx.fillStyle = sky;
    ctx.fillRect(0, 0, w, hy);

    const ground = ctx.createLinearGradient(0, hy, 0, h);
    ground.addColorStop(0, mix(pal[1], pal[0], 0.35));
    ground.addColorStop(1, pal[0]);
    ctx.fillStyle = ground;
    ctx.fillRect(0, hy, w, h - hy);

    // Ridge lines, back to front, each darker and taller.
    for (let layer = 0; layer < 3; layer++) {
      ctx.beginPath();
      ctx.moveTo(0, h);
      const amp = h * (0.06 + layer * 0.045);
      const base = hy + layer * h * 0.035;
      ctx.lineTo(0, base);
      for (let x = 0; x <= w; x += w / 18) {
        const y = base - Math.sin(x / w * (2.5 + layer) + rand() * 0.4) * amp * (0.5 + rand() * 0.5);
        ctx.lineTo(x, y);
      }
      ctx.lineTo(w, h);
      ctx.closePath();
      ctx.fillStyle = mix(pal[0], pal[1], 0.5 - layer * 0.18);
      ctx.globalAlpha = 0.85;
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  }

  /* Hard-edged planes with a light shaft — architecture and interiors.
   * Planes are drawn opaque and pushed toward the darkest palette stop, then a
   * single narrow shaft cuts across: earlier versions washed everything toward
   * mid-grey and the thumbnails read as empty boxes at card scale. */
  function planes(ctx, w, h, pal, rand) {
    ctx.fillStyle = mix(pal[0], pal[1], 0.35);
    ctx.fillRect(0, 0, w, h);

    for (let i = 0; i < 7; i++) {
      const x = rand() * w * 0.85;
      const y = rand() * h * 0.6;
      const pw = w * (0.18 + rand() * 0.5);
      const ph = h * (0.25 + rand() * 0.8);
      // Alternate between the deep and the light end of the palette so
      // neighbouring planes always separate tonally.
      const toward = i % 2 ? pal[4] : pal[0];
      ctx.fillStyle = mix(pal[1 + Math.floor(rand() * 3)], toward, 0.25 + rand() * 0.5);
      ctx.fillRect(x, y, pw, ph);
    }

    // Floor line, to stop it reading as a flat pattern.
    const fy = h * (0.74 + rand() * 0.1);
    ctx.fillStyle = mix(pal[0], pal[1], 0.15);
    ctx.fillRect(0, fy, w, h - fy);

    const shaft = ctx.createLinearGradient(w * 0.05, 0, w * 0.6, h);
    shaft.addColorStop(0, 'rgba(255,255,255,0.30)');
    shaft.addColorStop(0.32, 'rgba(255,255,255,0.04)');
    shaft.addColorStop(1, 'rgba(0,0,0,0.30)');
    ctx.fillStyle = shaft;
    ctx.fillRect(0, 0, w, h);
  }

  function grainAndVignette(ctx, w, h, rand, strength) {
    const img = ctx.getImageData(0, 0, w, h);
    const d = img.data;
    const amt = strength * 255;
    for (let i = 0; i < d.length; i += 4) {
      const n = (rand() - 0.5) * amt;
      d[i] += n; d[i + 1] += n; d[i + 2] += n;
    }
    ctx.putImageData(img, 0, 0);

    const v = ctx.createRadialGradient(w / 2, h / 2, Math.min(w, h) * 0.25, w / 2, h / 2, Math.max(w, h) * 0.78);
    v.addColorStop(0, 'rgba(0,0,0,0)');
    v.addColorStop(1, 'rgba(0,0,0,0.34)');
    ctx.fillStyle = v;
    ctx.fillRect(0, 0, w, h);
  }

  const KINDS = {
    landscape: (ctx, w, h, pal, rand) => horizon(ctx, w, h, pal, rand),
    interior:  (ctx, w, h, pal, rand) => planes(ctx, w, h, pal, rand),
    soft:      (ctx, w, h, pal, rand) => bloom(ctx, w, h, pal, rand, { top: 4, bottom: 1, blobs: 8 }),
    deep:      (ctx, w, h, pal, rand) => bloom(ctx, w, h, pal, rand, { top: 0, bottom: 2, blobs: 6 }),
    product:   (ctx, w, h, pal, rand) => {
      ctx.fillStyle = pal[3];
      ctx.fillRect(0, 0, w, h);
      const cx = w / 2, cy = h * 0.55, r = Math.min(w, h) * 0.30;
      const rg = ctx.createRadialGradient(cx - r * 0.35, cy - r * 0.5, r * 0.05, cx, cy, r * 1.5);
      rg.addColorStop(0, pal[4]);
      rg.addColorStop(0.55, pal[2]);
      rg.addColorStop(1, pal[1]);
      ctx.fillStyle = rg;
      ctx.beginPath();
      ctx.ellipse(cx, cy, r * 0.82, r, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = 'rgba(0,0,0,0.16)';
      ctx.beginPath();
      ctx.ellipse(cx, cy + r * 1.02, r * 0.9, r * 0.14, 0, 0, Math.PI * 2);
      ctx.fill();
    },
  };

  /* Returns a data URL. Painting to a detached canvas and handing back a URL
   * keeps the mini-sites plain HTML strings — no canvas nodes to wire up. */
  function make(kind, palette, seed, w, h) {
    w = w || 720; h = h || 480;
    const cv = document.createElement('canvas');
    cv.width = w; cv.height = h;
    const ctx = cv.getContext('2d');
    const pal = PALETTES[palette] || PALETTES.stone;
    const rand = rng(seed * 2654435761);
    (KINDS[kind] || KINDS.soft)(ctx, w, h, pal, rand);
    grainAndVignette(ctx, w, h, rand, 0.055);
    return cv.toDataURL('image/jpeg', 0.86);
  }

  /* Convenience for CSS `background-image`. */
  function bg(kind, palette, seed, w, h) {
    return `url(${make(kind, palette, seed, w, h)})`;
  }

  return { make, bg, PALETTES, mix };
})();
