/* Imagery for the mock sites.
 *
 * The render environment has no access to photo hosts, so every image in every
 * mock site is painted here. The first version of this file drew soft colour
 * fields, and the result was that all nine sites looked like the same site —
 * abstraction reads as "no photo". So these are *scenes*: each painter builds a
 * recognisable subject (a cup on a saucer, a lit stage, a window in a room)
 * and then grades it like a photograph — depth of field, bloom, grain,
 * vignette. At card scale that is what sells it as a picture.
 *
 * Everything runs off a seeded PRNG: the same seed always paints the same
 * pixels, which is what keeps the frame-by-frame render deterministic. */

const ART = (() => {
  function rng(seed) {
    let s = (seed >>> 0) || 1;
    return function () {
      s ^= s << 13; s >>>= 0;
      s ^= s >> 17;
      s ^= s << 5; s >>>= 0;
      return s / 4294967296;
    };
  }

  const lerp = (a, b, t) => a + (b - a) * t;

  function rgb(hex) {
    const n = parseInt(hex.slice(1), 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
  }

  function mix(c1, c2, t) {
    const a = rgb(c1), b = rgb(c2);
    return `rgb(${Math.round(lerp(a[0], b[0], t))},${Math.round(lerp(a[1], b[1], t))},${Math.round(lerp(a[2], b[2], t))})`;
  }

  const shade = (hex, t) => (t < 0 ? mix(hex, '#000000', -t) : mix(hex, '#ffffff', t));

  function vgrad(ctx, w, h, stops) {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    stops.forEach(([p, c]) => g.addColorStop(p, c));
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
  }

  function glow(ctx, x, y, r, colour, alpha) {
    const g = ctx.createRadialGradient(x, y, 0, x, y, r);
    g.addColorStop(0, colour);
    g.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.save();
    ctx.globalAlpha = alpha;
    ctx.globalCompositeOperation = 'lighter';
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  function ellipse(ctx, x, y, rx, ry, fill) {
    ctx.fillStyle = fill;
    ctx.beginPath();
    ctx.ellipse(x, y, rx, ry, 0, 0, Math.PI * 2);
    ctx.fill();
  }

  /* ---- scenes ---------------------------------------------------------- */

  /* Layered ridges under a graded sky. The haze between layers is what makes
     it read as distance rather than as stacked shapes. */
  function hills(ctx, w, h, rand, o) {
    const sky = o.sky || ['#1d1440', '#7d3f63', '#e08a5c', '#f6cf9b'];
    vgrad(ctx, w, h, [[0, sky[0]], [0.42, sky[1]], [0.72, sky[2]], [1, sky[3]]]);

    const sx = w * (0.24 + rand() * 0.5);
    const sy = h * (0.52 + rand() * 0.12);
    glow(ctx, sx, sy, h * 0.55, 'rgba(255,222,170,0.85)', 0.75);
    ellipse(ctx, sx, sy, h * 0.055, h * 0.055, 'rgba(255,246,225,0.95)');

    const base = h * 0.62;
    for (let layer = 0; layer < 4; layer++) {
      const y0 = base + layer * h * 0.085;
      const amp = h * (0.09 - layer * 0.015);
      ctx.beginPath();
      ctx.moveTo(0, h);
      ctx.lineTo(0, y0);
      const phase = rand() * 6;
      for (let x = 0; x <= w; x += w / 60) {
        const k = x / w;
        const y = y0 - (Math.sin(k * (3 + layer) + phase) * 0.6 + Math.sin(k * (7 + layer * 2) + phase) * 0.4) * amp;
        ctx.lineTo(x, y);
      }
      ctx.lineTo(w, h);
      ctx.closePath();
      // Far ridges sit closer to the sky colour: cheap, convincing aerial haze.
      ctx.fillStyle = mix(o.ridge || '#241a3d', sky[2], Math.max(0, 0.42 - layer * 0.14));
      ctx.fill();
    }
  }

  /* Overhead cup on a saucer. The crema ring and the offset shadow do most of
     the work; without the shadow it reads as a flat logo. */
  function coffee(ctx, w, h, rand, o) {
    const table = o.table || '#4a2f1d';
    vgrad(ctx, w, h, [[0, shade(table, 0.10)], [1, shade(table, -0.30)]]);

    // Wood grain.
    ctx.save();
    ctx.globalAlpha = 0.16;
    for (let i = 0; i < 26; i++) {
      ctx.fillStyle = i % 2 ? shade(table, 0.16) : shade(table, -0.2);
      const y = rand() * h;
      ctx.fillRect(0, y, w, 1 + rand() * 3);
    }
    ctx.restore();

    glow(ctx, w * 0.24, h * 0.10, h * 0.95, 'rgba(255,236,205,0.30)', 0.9);

    const cx = w * 0.52, cy = h * 0.55, r = Math.min(w, h) * 0.30;

    ctx.save();
    ctx.filter = 'blur(' + (r * 0.18).toFixed(1) + 'px)';
    ellipse(ctx, cx + r * 0.20, cy + r * 0.20, r * 1.28, r * 1.20, 'rgba(0,0,0,0.5)');
    ctx.restore();

    ellipse(ctx, cx, cy, r * 1.30, r * 1.26, o.saucer || '#efe7dc');
    ellipse(ctx, cx, cy, r * 1.30, r * 1.26, 'rgba(0,0,0,0)');
    ellipse(ctx, cx - r * 0.04, cy - r * 0.04, r * 1.14, r * 1.10, shade(o.saucer || '#efe7dc', 0.10));
    ellipse(ctx, cx, cy, r, r * 0.97, shade(o.saucer || '#efe7dc', -0.06));
    ellipse(ctx, cx, cy, r * 0.86, r * 0.83, o.crema || '#b4763c');
    ellipse(ctx, cx - r * 0.10, cy - r * 0.10, r * 0.58, r * 0.54, shade(o.crema || '#b4763c', 0.16));
    ellipse(ctx, cx + r * 0.06, cy + r * 0.08, r * 0.34, r * 0.30, shade(o.crema || '#b4763c', -0.22));

    // Rim highlight.
    ctx.strokeStyle = 'rgba(255,255,255,0.55)';
    ctx.lineWidth = Math.max(1.5, r * 0.035);
    ctx.beginPath();
    ctx.ellipse(cx, cy, r * 0.93, r * 0.90, 0, Math.PI * 0.85, Math.PI * 1.75);
    ctx.stroke();

    // Beans.
    for (let i = 0; i < 9; i++) {
      const a = rand() * Math.PI * 2;
      const d = r * (1.55 + rand() * 0.9);
      const bx = cx + Math.cos(a) * d, by = cy + Math.sin(a) * d * 0.8;
      ctx.save();
      ctx.translate(bx, by);
      ctx.rotate(rand() * Math.PI);
      ellipse(ctx, 0, 0, r * 0.14, r * 0.10, '#3a2113');
      ctx.fillStyle = '#20120a';
      ctx.fillRect(-r * 0.13, -r * 0.012, r * 0.26, r * 0.024);
      ctx.restore();
    }
  }

  /* A room with a window doing the lighting. The bright rectangle plus the
     light pool on the floor is the whole trick. */
  function room(ctx, w, h, rand, o) {
    const wall = o.wall || '#cfc7ba';
    const floor = o.floor || '#8d6a48';
    const hz = h * 0.66;
    vgrad(ctx, w, hz, [[0, shade(wall, 0.08)], [1, shade(wall, -0.14)]]);
    ctx.fillStyle = shade(wall, -0.14);
    ctx.fillRect(0, 0, w, hz);
    const g = ctx.createLinearGradient(0, hz, 0, h);
    g.addColorStop(0, shade(floor, -0.25));
    g.addColorStop(1, shade(floor, 0.06));
    ctx.fillStyle = g;
    ctx.fillRect(0, hz, w, h - hz);

    const wx = w * 0.56, wy = h * 0.10, ww = w * 0.34, wh = h * 0.46;
    ctx.fillStyle = o.light || '#fff6e2';
    ctx.fillRect(wx, wy, ww, wh);
    ctx.fillStyle = 'rgba(255,255,255,0.55)';
    ctx.fillRect(wx, wy, ww, wh * 0.4);
    ctx.strokeStyle = shade(wall, -0.55);
    ctx.lineWidth = Math.max(2, w * 0.006);
    ctx.strokeRect(wx, wy, ww, wh);
    ctx.beginPath();
    ctx.moveTo(wx + ww / 2, wy); ctx.lineTo(wx + ww / 2, wy + wh);
    ctx.moveTo(wx, wy + wh / 2); ctx.lineTo(wx + ww, wy + wh / 2);
    ctx.stroke();

    // Light spilling onto the floor.
    ctx.save();
    ctx.globalAlpha = 0.5;
    ctx.filter = 'blur(' + (w * 0.02).toFixed(1) + 'px)';
    ctx.fillStyle = o.light || '#fff6e2';
    ctx.beginPath();
    ctx.moveTo(wx - w * 0.12, h);
    ctx.lineTo(wx + ww * 0.1, hz);
    ctx.lineTo(wx + ww, hz);
    ctx.lineTo(wx + ww + w * 0.16, h);
    ctx.closePath();
    ctx.fill();
    ctx.restore();

    // Furniture: a low block and a tall one, both grounded with a shadow.
    const bw = w * 0.30, bh = h * 0.20;
    const bx = w * 0.08, by = hz - bh * 0.35;
    ctx.save();
    ctx.filter = 'blur(' + (w * 0.012).toFixed(1) + 'px)';
    ctx.fillStyle = 'rgba(0,0,0,0.42)';
    ctx.fillRect(bx - w * 0.01, by + bh * 0.92, bw * 1.1, h * 0.05);
    ctx.restore();
    ctx.fillStyle = o.object || '#3d4a44';
    ctx.fillRect(bx, by, bw, bh);
    ctx.fillStyle = shade(o.object || '#3d4a44', 0.14);
    ctx.fillRect(bx, by, bw, bh * 0.12);

    ctx.fillStyle = shade(o.object || '#3d4a44', -0.3);
    ctx.fillRect(w * 0.44, hz - h * 0.30, w * 0.055, h * 0.30);
    ellipse(ctx, w * 0.468, hz - h * 0.32, w * 0.06, h * 0.055, '#3f5f3a');
  }

  /* Sport court: perspective lines and a net. The converging side lines are
     what make a flat rectangle read as a photographed court. */
  function court(ctx, w, h, rand, o) {
    vgrad(ctx, w, h, [[0, shade(o.sky || '#101a16', 0.05)], [0.34, o.sky || '#101a16'], [1, shade(o.floor || '#1d5f4a', -0.1)]]);
    const hz = h * 0.34;
    const gf = ctx.createLinearGradient(0, hz, 0, h);
    gf.addColorStop(0, shade(o.floor || '#1d5f4a', -0.28));
    gf.addColorStop(1, shade(o.floor || '#1d5f4a', 0.12));
    ctx.fillStyle = gf;
    ctx.fillRect(0, hz, w, h - hz);

    ctx.strokeStyle = 'rgba(255,255,255,0.82)';
    ctx.lineWidth = Math.max(1.5, w * 0.004);
    // Side lines converging to a vanishing point.
    const vpx = w * 0.5;
    [[w * -0.25, w * 0.34], [w * 1.25, w * 0.66]].forEach(([nearX, farX]) => {
      ctx.beginPath();
      ctx.moveTo(nearX, h);
      ctx.lineTo(farX, hz);
      ctx.stroke();
    });
    // Cross lines, spaced so they bunch toward the horizon.
    for (let i = 1; i <= 5; i++) {
      const k = Math.pow(i / 6, 1.9);
      const y = h - (h - hz) * (1 - k);
      const spread = lerp(0.16, 0.75, 1 - k);
      ctx.globalAlpha = 0.35 + 0.5 * (1 - k);
      ctx.beginPath();
      ctx.moveTo(vpx - w * spread, y);
      ctx.lineTo(vpx + w * spread, y);
      ctx.stroke();
    }
    ctx.globalAlpha = 1;

    // Net.
    const ny = hz + (h - hz) * 0.30;
    const nh = h * 0.11;
    ctx.fillStyle = 'rgba(255,255,255,0.14)';
    ctx.fillRect(w * 0.18, ny, w * 0.64, nh);
    ctx.strokeStyle = 'rgba(255,255,255,0.34)';
    ctx.lineWidth = 1;
    for (let x = w * 0.18; x <= w * 0.82; x += w * 0.022) {
      ctx.beginPath(); ctx.moveTo(x, ny); ctx.lineTo(x, ny + nh); ctx.stroke();
    }
    ctx.fillStyle = 'rgba(255,255,255,0.9)';
    ctx.fillRect(w * 0.18, ny, w * 0.64, Math.max(2, h * 0.008));

    glow(ctx, w * 0.22, h * 0.06, h * 0.5, 'rgba(200,250,75,0.5)', 0.7);
    glow(ctx, w * 0.80, h * 0.05, h * 0.42, 'rgba(255,255,255,0.4)', 0.6);
  }

  /* Plated food, shot from above on a dark table. */
  function dish(ctx, w, h, rand, o) {
    vgrad(ctx, w, h, [[0, shade(o.table || '#1a120c', 0.10)], [1, shade(o.table || '#1a120c', -0.4)]]);
    glow(ctx, w * 0.30, h * 0.12, h * 0.9, 'rgba(255,214,150,0.28)', 0.85);

    const cx = w * 0.5, cy = h * 0.54, r = Math.min(w, h) * 0.34;
    ctx.save();
    ctx.filter = 'blur(' + (r * 0.2).toFixed(1) + 'px)';
    ellipse(ctx, cx + r * 0.16, cy + r * 0.2, r * 1.16, r * 1.1, 'rgba(0,0,0,0.62)');
    ctx.restore();

    ellipse(ctx, cx, cy, r, r * 0.96, o.plate || '#1f1a16');
    ellipse(ctx, cx, cy, r * 0.92, r * 0.88, shade(o.plate || '#1f1a16', 0.10));
    ctx.strokeStyle = 'rgba(255,255,255,0.28)';
    ctx.lineWidth = Math.max(1.5, r * 0.02);
    ctx.beginPath();
    ctx.ellipse(cx, cy, r * 0.98, r * 0.94, 0, Math.PI * 0.9, Math.PI * 1.8);
    ctx.stroke();

    // Food: a few overlapping warm masses plus herb specks.
    const food = o.food || ['#c2611f', '#8d3f16', '#e0a13d'];
    for (let i = 0; i < 7; i++) {
      const a = rand() * Math.PI * 2;
      const d = r * rand() * 0.42;
      ellipse(ctx, cx + Math.cos(a) * d, cy + Math.sin(a) * d * 0.85,
        r * (0.16 + rand() * 0.16), r * (0.12 + rand() * 0.13),
        food[Math.floor(rand() * food.length)]);
    }
    for (let i = 0; i < 22; i++) {
      const a = rand() * Math.PI * 2;
      const d = r * rand() * 0.55;
      ellipse(ctx, cx + Math.cos(a) * d, cy + Math.sin(a) * d * 0.85,
        r * 0.022, r * 0.016, i % 3 ? '#5d7b31' : '#e8dfc8');
    }
    glow(ctx, cx - r * 0.3, cy - r * 0.35, r * 0.9, 'rgba(255,226,180,0.5)', 0.5);
  }

  /* Concert: beams through haze over a crowd silhouette. */
  function stage(ctx, w, h, rand, o) {
    vgrad(ctx, w, h, [[0, o.top || '#1a0b2e'], [0.6, shade(o.top || '#1a0b2e', -0.3)], [1, '#07040d']]);

    const beams = o.beams || ['#ff4d6d', '#7b5cff', '#28c7ff'];
    for (let i = 0; i < 6; i++) {
      const x0 = w * (0.12 + i * 0.15);
      const spread = w * (0.10 + rand() * 0.10);
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';
      ctx.globalAlpha = 0.30 + rand() * 0.22;
      const g = ctx.createLinearGradient(x0, 0, x0, h * 0.85);
      g.addColorStop(0, beams[i % beams.length]);
      g.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.moveTo(x0 - w * 0.012, 0);
      ctx.lineTo(x0 + w * 0.012, 0);
      ctx.lineTo(x0 + spread, h * 0.85);
      ctx.lineTo(x0 - spread, h * 0.85);
      ctx.closePath();
      ctx.fill();
      ctx.restore();
      glow(ctx, x0, h * 0.02, h * 0.16, beams[i % beams.length], 0.8);
    }

    for (let i = 0; i < 30; i++) {
      glow(ctx, rand() * w, h * (0.2 + rand() * 0.5), h * (0.01 + rand() * 0.03),
        'rgba(255,255,255,0.5)', 0.25 + rand() * 0.3);
    }

    // Crowd: overlapping heads and shoulders along the bottom edge.
    ctx.fillStyle = '#05030a';
    const cy = h * 0.88;
    ctx.fillRect(0, cy + h * 0.06, w, h);
    for (let i = 0; i < 26; i++) {
      const x = (i / 25) * w + (rand() - 0.5) * w * 0.03;
      const s = h * (0.035 + rand() * 0.03);
      ellipse(ctx, x, cy + (rand() - 0.5) * h * 0.03, s * 0.62, s * 0.7, '#05030a');
      ctx.fillRect(x - s * 1.05, cy + s * 0.5, s * 2.1, h);
    }
  }

  /* Building facade: a grid of windows, a few of them lit. */
  function facade(ctx, w, h, rand, o) {
    vgrad(ctx, w, h, [[0, o.sky || '#9fb6c9'], [1, shade(o.sky || '#9fb6c9', 0.25)]]);

    const bw = w * 0.86, bx = w * 0.07, by = h * 0.10;
    ctx.fillStyle = o.wall || '#b9ac97';
    ctx.fillRect(bx, by, bw, h - by);
    const sideG = ctx.createLinearGradient(bx, 0, bx + bw, 0);
    sideG.addColorStop(0, 'rgba(255,255,255,0.24)');
    sideG.addColorStop(0.55, 'rgba(0,0,0,0)');
    sideG.addColorStop(1, 'rgba(0,0,0,0.34)');
    ctx.fillStyle = sideG;
    ctx.fillRect(bx, by, bw, h - by);

    const cols = 5, rows = 6;
    const gapx = bw / cols, gapy = (h - by) / rows;
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const x = bx + c * gapx + gapx * 0.22;
        const y = by + r * gapy + gapy * 0.20;
        const ww = gapx * 0.56, wh = gapy * 0.56;
        const lit = rand() > 0.68;
        ctx.fillStyle = lit ? (o.lit || '#ffd98a') : shade(o.glass || '#3b4750', rand() * 0.2 - 0.1);
        ctx.fillRect(x, y, ww, wh);
        ctx.fillStyle = 'rgba(255,255,255,0.18)';
        ctx.fillRect(x, y, ww, wh * 0.3);
        ctx.strokeStyle = shade(o.wall || '#b9ac97', -0.35);
        ctx.lineWidth = Math.max(1, w * 0.003);
        ctx.strokeRect(x, y, ww, wh);
        if (lit) glow(ctx, x + ww / 2, y + wh / 2, ww * 1.4, 'rgba(255,214,130,0.55)', 0.5);
      }
    }
  }

  /* Knitwear, close up: rows of V stitches with a soft fold shadow. */
  function knit(ctx, w, h, rand, o) {
    const base = o.yarn || '#b8452f';
    ctx.fillStyle = shade(base, -0.12);
    ctx.fillRect(0, 0, w, h);

    const cols = 15;
    const sw = w / cols;
    const sh = sw * 0.82;
    ctx.lineWidth = Math.max(2, sw * 0.20);
    ctx.lineCap = 'round';
    for (let y = -sh; y < h + sh; y += sh) {
      for (let x = -sw; x < w + sw; x += sw) {
        const off = (Math.round(y / sh) % 2) * sw * 0.5;
        const t = 0.10 + rand() * 0.14;
        ctx.strokeStyle = shade(base, t);
        ctx.beginPath();
        ctx.moveTo(x + off, y);
        ctx.lineTo(x + off + sw * 0.5, y + sh * 0.62);
        ctx.lineTo(x + off + sw, y);
        ctx.stroke();
      }
    }
    // Fold: a soft diagonal band of shadow and one of light.
    ctx.save();
    ctx.filter = 'blur(' + (w * 0.05).toFixed(1) + 'px)';
    ctx.globalAlpha = 0.55;
    ctx.fillStyle = '#000';
    ctx.beginPath();
    ctx.moveTo(0, h * 0.72); ctx.lineTo(w, h * 0.34); ctx.lineTo(w, h); ctx.lineTo(0, h);
    ctx.closePath(); ctx.fill();
    ctx.globalAlpha = 0.30;
    ctx.fillStyle = '#fff';
    ctx.beginPath();
    ctx.moveTo(0, h * 0.06); ctx.lineTo(w, -h * 0.12); ctx.lineTo(w, h * 0.2); ctx.lineTo(0, h * 0.34);
    ctx.closePath(); ctx.fill();
    ctx.restore();
  }

  /* Clean clinical interior: bright, cool, uncluttered. */
  function clinic(ctx, w, h, rand, o) {
    const wall = o.wall || '#e8f1f5';
    const hz = h * 0.70;
    vgrad(ctx, w, hz, [[0, '#ffffff'], [1, shade(wall, -0.10)]]);
    // Floor with a reflected sheen, so the room has a ground rather than a band.
    const fl = ctx.createLinearGradient(0, hz, 0, h);
    fl.addColorStop(0, shade(wall, -0.30));
    fl.addColorStop(0.45, shade(wall, -0.16));
    fl.addColorStop(1, shade(wall, -0.34));
    ctx.fillStyle = fl;
    ctx.fillRect(0, hz, w, h - hz);
    // Corner, to break the flat back wall.
    ctx.fillStyle = 'rgba(30,60,75,0.07)';
    ctx.fillRect(0, 0, w * 0.17, hz);

    ctx.fillStyle = '#ffffff';
    ctx.fillRect(w * 0.04, h * 0.08, w * 0.36, h * 0.5);
    glow(ctx, w * 0.22, h * 0.32, h * 0.6, 'rgba(255,255,255,0.9)', 0.8);

    // Chair and lamp arm — enough silhouette to read as a treatment room.
    const cxx = w * 0.62;
    ctx.fillStyle = o.accent || '#1a7fa8';
    ctx.beginPath();
    ctx.moveTo(cxx - w * 0.16, hz);
    ctx.lineTo(cxx + w * 0.20, hz);
    ctx.lineTo(cxx + w * 0.16, hz - h * 0.12);
    ctx.lineTo(cxx - w * 0.14, hz - h * 0.10);
    ctx.closePath(); ctx.fill();
    ctx.fillStyle = shade(o.accent || '#1a7fa8', -0.18);
    ctx.fillRect(cxx - w * 0.16, hz - h * 0.34, w * 0.10, h * 0.26);
    ctx.fillStyle = '#cfd8dc';
    ctx.fillRect(cxx + w * 0.20, hz - h * 0.46, w * 0.018, h * 0.46);
    ellipse(ctx, cxx + w * 0.13, hz - h * 0.46, w * 0.085, h * 0.045, '#eceff1');
    glow(ctx, cxx + w * 0.13, hz - h * 0.44, h * 0.22, 'rgba(255,255,255,0.85)', 0.7);

    // Cabinet run and a plant: an empty white box reads as a render, not a
    // room, so the scene needs a couple of everyday objects to sit in.
    ctx.fillStyle = '#f4f7f9';
    ctx.fillRect(0, hz - h * 0.16, w * 0.34, h * 0.16);
    ctx.fillStyle = '#dfe7ec';
    ctx.fillRect(0, hz - h * 0.17, w * 0.34, h * 0.016);
    ctx.strokeStyle = '#cdd8de';
    ctx.lineWidth = Math.max(1, w * 0.003);
    for (let i = 1; i < 3; i++) {
      ctx.beginPath();
      ctx.moveTo((w * 0.34 / 3) * i, hz - h * 0.155);
      ctx.lineTo((w * 0.34 / 3) * i, hz);
      ctx.stroke();
    }

    const px = w * 0.40, py = hz;
    ctx.fillStyle = '#c9d3d8';
    ctx.fillRect(px - w * 0.022, py - h * 0.07, w * 0.044, h * 0.07);
    for (let i = 0; i < 7; i++) {
      const a = -Math.PI / 2 + (i - 3) * 0.34;
      ellipse(ctx, px + Math.cos(a) * w * 0.045, py - h * 0.075 + Math.sin(a) * h * 0.05,
        w * 0.028, h * 0.018, i % 2 ? '#4e7d44' : '#3f6b3a');
    }

    ctx.save();
    ctx.filter = 'blur(' + (w * 0.015).toFixed(1) + 'px)';
    ctx.fillStyle = 'rgba(20,40,55,0.28)';
    ctx.fillRect(cxx - w * 0.18, hz - h * 0.006, w * 0.42, h * 0.03);
    ctx.restore();
  }

  /* Rails of clothing — a shop interior without needing a person in it. */
  function shop(ctx, w, h, rand, o) {
    const wall = o.wall || '#efe6d8';
    vgrad(ctx, w, h, [[0, shade(wall, 0.10)], [0.7, wall], [1, shade(wall, -0.22)]]);
    glow(ctx, w * 0.5, h * 0.02, h * 0.7, 'rgba(255,246,225,0.55)', 0.8);

    const rail = h * 0.30;
    ctx.fillStyle = '#8d8377';
    ctx.fillRect(w * 0.06, rail, w * 0.88, Math.max(2, h * 0.012));

    const palette = o.clothes || ['#b8452f', '#3f5b46', '#d9b26a', '#2c3d5c', '#8a6f9c'];
    let x = w * 0.09;
    let i = 0;
    while (x < w * 0.92) {
      const cw = w * (0.055 + rand() * 0.035);
      const ch = h * (0.34 + rand() * 0.20);
      const col = palette[i % palette.length];
      ctx.save();
      ctx.filter = 'blur(' + (w * 0.004).toFixed(1) + 'px)';
      ctx.fillStyle = shade(col, -0.12);
      ctx.beginPath();
      ctx.moveTo(x, rail + h * 0.02);
      ctx.lineTo(x + cw, rail + h * 0.02);
      ctx.lineTo(x + cw * 0.86, rail + ch);
      ctx.lineTo(x + cw * 0.14, rail + ch);
      ctx.closePath();
      ctx.fill();
      ctx.fillStyle = shade(col, 0.14);
      ctx.fillRect(x + cw * 0.12, rail + h * 0.03, cw * 0.22, ch * 0.9);
      ctx.restore();
      // Hanger hook.
      ctx.strokeStyle = '#6f675d';
      ctx.lineWidth = Math.max(1, w * 0.003);
      ctx.beginPath();
      ctx.arc(x + cw / 2, rail - h * 0.012, h * 0.014, Math.PI * 0.1, Math.PI * 0.9, true);
      ctx.stroke();
      x += cw * 1.12;
      i++;
    }
    ctx.save();
    ctx.filter = 'blur(' + (w * 0.03).toFixed(1) + 'px)';
    ctx.fillStyle = 'rgba(60,45,30,0.35)';
    ctx.fillRect(0, h * 0.86, w, h * 0.14);
    ctx.restore();
  }

  /* Pool water seen from above: caustics are the whole tell. Without the
     bright wavering net on the surface this is just a blue rectangle. */
  function water(ctx, w, h, rand, o) {
    const deep = o.deep || '#0d6f82';
    const shallow = o.shallow || '#4fc3c9';
    vgrad(ctx, w, h, [[0, shade(shallow, 0.18)], [0.45, shallow], [1, deep]]);

    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    for (let i = 0; i < 90; i++) {
      const x = rand() * w;
      const y = rand() * h;
      const len = w * (0.05 + rand() * 0.16);
      const thick = Math.max(1.5, h * (0.004 + rand() * 0.009));
      ctx.globalAlpha = 0.10 + rand() * 0.26;
      ctx.strokeStyle = 'rgba(226,255,255,1)';
      ctx.lineWidth = thick;
      ctx.lineCap = 'round';
      ctx.beginPath();
      ctx.moveTo(x, y);
      // Each caustic is a short wobbling arc, not a straight line.
      let px = x, py = y;
      const steps = 4;
      for (let k = 1; k <= steps; k++) {
        px += (len / steps) * (0.6 + rand() * 0.8);
        py += (rand() - 0.5) * h * 0.035;
        ctx.lineTo(px, py);
      }
      ctx.stroke();
    }
    ctx.restore();

    // Surface sheen from the top-left, and depth falling away at the bottom.
    glow(ctx, w * 0.18, h * 0.08, Math.max(w, h) * 0.6, 'rgba(255,255,255,0.30)', 0.8);
    const dg = ctx.createLinearGradient(0, h * 0.5, 0, h);
    dg.addColorStop(0, 'rgba(0,30,45,0)');
    dg.addColorStop(1, 'rgba(0,30,45,0.45)');
    ctx.fillStyle = dg;
    ctx.fillRect(0, h * 0.5, w, h * 0.5);
  }

  /* Rolling hills with cypresses and a farmhouse — the Tuscan postcard. The
     cypresses are what place it; the same hills without them read as anywhere. */
  function tuscan(ctx, w, h, rand, o) {
    vgrad(ctx, w, h, [[0, '#8fb3d4'], [0.30, '#cfd9d8'], [0.46, '#e8dcb6'], [0.52, '#c9c88d']]);
    glow(ctx, w * 0.74, h * 0.20, h * 0.8, 'rgba(255,238,186,0.95)', 0.85);

    const bands = [
      { y: 0.50, c: '#b6b273' },
      { y: 0.60, c: '#93a159' },
      { y: 0.72, c: '#67813f' },
      { y: 0.86, c: '#43602c' },
    ];
    bands.forEach((band, i) => {
      ctx.beginPath();
      ctx.moveTo(0, h);
      ctx.lineTo(0, h * band.y);
      const phase = rand() * 5;
      for (let x = 0; x <= w; x += w / 40) {
        const k = x / w;
        const y = h * band.y - Math.sin(k * (2.2 + i * 0.7) + phase) * h * (0.045 - i * 0.006);
        ctx.lineTo(x, y);
      }
      ctx.lineTo(w, h);
      ctx.closePath();
      ctx.fillStyle = band.c;
      ctx.fill();
    });

    // Farmhouse on the second ridge.
    const fx = w * (0.22 + rand() * 0.2), fy = h * 0.58;
    ctx.fillStyle = '#e8ddc6';
    ctx.fillRect(fx, fy - h * 0.065, w * 0.075, h * 0.065);
    ctx.fillStyle = '#9a5f43';
    ctx.beginPath();
    ctx.moveTo(fx - w * 0.006, fy - h * 0.065);
    ctx.lineTo(fx + w * 0.0375, fy - h * 0.095);
    ctx.lineTo(fx + w * 0.081, fy - h * 0.065);
    ctx.closePath();
    ctx.fill();

    // Low sun raking across the hills: without it the bands read as flat paper.
    const rake = ctx.createLinearGradient(w, h * 0.25, 0, h);
    rake.addColorStop(0, 'rgba(255,214,140,0.42)');
    rake.addColorStop(0.45, 'rgba(255,214,140,0.08)');
    rake.addColorStop(1, 'rgba(40,30,10,0.30)');
    ctx.fillStyle = rake;
    ctx.fillRect(0, h * 0.44, w, h * 0.56);

    // Cypress line along the track.
    for (let i = 0; i < 9; i++) {
      const t = i / 8;
      const cx = w * (0.52 + t * 0.44);
      const cy = h * (0.62 + t * 0.2);
      const ch2 = h * (0.12 + t * 0.10);
      ctx.fillStyle = i % 2 ? '#2f4a2c' : '#38562f';
      ctx.beginPath();
      ctx.ellipse(cx, cy - ch2 / 2, ch2 * 0.17, ch2 / 2, 0, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  /* A row of product bottles on a plinth — the skincare shot. */
  function bottles(ctx, w, h, rand, o) {
    const bgc = o.wall || '#e9d9d2';
    vgrad(ctx, w, h, [[0, shade(bgc, 0.10)], [0.72, bgc], [1, shade(bgc, -0.14)]]);
    glow(ctx, w * 0.5, h * 0.12, Math.max(w, h) * 0.62, 'rgba(255,250,244,0.55)', 0.8);

    const tones = o.tones || ['#6d2b24', '#8a3b2d', '#a9564a', '#5c2420'];
    const n = o.count || 4;
    const slotW = w / (n + 1);
    const baseY = h * 0.80;
    for (let i = 0; i < n; i++) {
      const cx = slotW * (i + 1);
      const bw = slotW * (0.42 + ((i * 7) % 3) * 0.05);
      const bh = h * (0.40 + ((i * 11) % 4) * 0.045);
      const col = tones[i % tones.length];

      ctx.save();
      ctx.filter = `blur(${(w * 0.012).toFixed(1)}px)`;
      ctx.fillStyle = 'rgba(60,30,25,0.35)';
      ctx.beginPath();
      ctx.ellipse(cx + bw * 0.1, baseY + h * 0.012, bw * 0.75, h * 0.02, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      // Body, with a highlight down one side and a cap on top.
      const g = ctx.createLinearGradient(cx - bw / 2, 0, cx + bw / 2, 0);
      g.addColorStop(0, shade(col, -0.22));
      g.addColorStop(0.3, shade(col, 0.16));
      g.addColorStop(0.62, col);
      g.addColorStop(1, shade(col, -0.3));
      ctx.fillStyle = g;
      roundRect(ctx, cx - bw / 2, baseY - bh, bw, bh, bw * 0.16);
      ctx.fill();

      ctx.fillStyle = shade(col, -0.4);
      roundRect(ctx, cx - bw * 0.19, baseY - bh - h * 0.045, bw * 0.38, h * 0.05, bw * 0.07);
      ctx.fill();

      ctx.fillStyle = 'rgba(255,255,255,0.72)';
      roundRect(ctx, cx - bw * 0.30, baseY - bh * 0.62, bw * 0.60, bh * 0.20, bw * 0.04);
      ctx.fill();
    }
  }

  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  /* Macro skin: a warm field with freckle speckle and a soft falloff. Abstract
     on purpose — close enough to read as a beauty crop, never a face. */
  function macro(ctx, w, h, rand, o) {
    const skin = o.skin || '#e0a883';
    vgrad(ctx, w, h, [[0, shade(skin, 0.18)], [0.55, skin], [1, shade(skin, -0.28)]]);

    for (let i = 0; i < 260; i++) {
      const x = rand() * w, y = rand() * h;
      const r = Math.min(w, h) * (0.004 + rand() * 0.012);
      ctx.globalAlpha = 0.07 + rand() * 0.16;
      ctx.fillStyle = rand() > 0.5 ? '#8a4f32' : '#b06f48';
      ctx.beginPath();
      ctx.ellipse(x, y, r, r * (0.7 + rand() * 0.5), 0, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;

    glow(ctx, w * 0.3, h * 0.24, Math.max(w, h) * 0.5, 'rgba(255,236,214,0.6)', 0.7);
    ctx.save();
    ctx.filter = `blur(${(w * 0.035).toFixed(1)}px)`;
    ctx.fillStyle = 'rgba(70,32,18,0.4)';
    ctx.fillRect(0, h * 0.84, w, h * 0.16);
    ctx.restore();
  }

  const SCENES = {
    hills, coffee, room, court, dish, stage, facade, knit, clinic, shop,
    water, tuscan, bottles, macro,
  };

  /* ---- photographic grading -------------------------------------------- */

  function grade(ctx, w, h, rand, opts) {
    // Depth of field: a blurred copy composited back over the bottom edge.
    if (opts.dof !== false) {
      const v = ctx.createLinearGradient(0, h * 0.66, 0, h);
      v.addColorStop(0, 'rgba(0,0,0,0)');
      v.addColorStop(1, 'rgba(0,0,0,0.22)');
      ctx.fillStyle = v;
      ctx.fillRect(0, h * 0.66, w, h * 0.34);
    }

    const img = ctx.getImageData(0, 0, w, h);
    const d = img.data;
    const amt = (opts.grain != null ? opts.grain : 0.05) * 255;
    for (let i = 0; i < d.length; i += 4) {
      const n = (rand() - 0.5) * amt;
      d[i] += n; d[i + 1] += n; d[i + 2] += n;
    }
    ctx.putImageData(img, 0, 0);

    const vig = ctx.createRadialGradient(w / 2, h * 0.46, Math.min(w, h) * 0.28, w / 2, h / 2, Math.max(w, h) * 0.78);
    vig.addColorStop(0, 'rgba(0,0,0,0)');
    vig.addColorStop(1, `rgba(0,0,0,${opts.vignette != null ? opts.vignette : 0.34})`);
    ctx.fillStyle = vig;
    ctx.fillRect(0, 0, w, h);
  }

  /* ---- public ---------------------------------------------------------- */

  const cache = new Map();

  function make(scene, seed, w, h, opts) {
    w = w || 720; h = h || 480;
    opts = opts || {};
    const key = [scene, seed, w, h, JSON.stringify(opts)].join('|');
    if (cache.has(key)) return cache.get(key);

    const cv = document.createElement('canvas');
    cv.width = w; cv.height = h;
    const ctx = cv.getContext('2d');
    const rand = rng(seed * 2654435761);
    (SCENES[scene] || hills)(ctx, w, h, rand, opts);
    grade(ctx, w, h, rand, opts);

    const url = cv.toDataURL('image/jpeg', 0.85);
    cache.set(key, url);
    return url;
  }

  const bg = (scene, seed, w, h, opts) => `url(${make(scene, seed, w, h, opts)})`;

  return { make, bg, mix, shade, SCENES };
})();
