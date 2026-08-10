#!/usr/bin/env node
/* Grabs a handful of stills at chosen timestamps — the fast feedback loop
 * while art-directing, without waiting on a full render.
 * Usage: node tools/shots.mjs [format] [t1 t2 ...] */

import { launch } from './browser.mjs';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const key = process.argv[2] || '4x5';
const times = process.argv.slice(3).map(Number);
const stamps = times.length ? times : [0, 1.6, 3.2, 4.8, 6.4, 7.6, 9.2, 11.0];
const SIZES = { '4x5': [1080, 1350], '3x4': [1080, 1440], '9x16': [1080, 1920], '1x1': [1080, 1080] };
const [w, h] = SIZES[key];

const out = path.join(ROOT, 'dist', 'stills');
await mkdir(out, { recursive: true });

const browser = await launch();
const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
const errors = [];
page.on('pageerror', (e) => errors.push(String(e)));
page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });

await page.goto(`file://${path.join(ROOT, 'src', 'ad.html')}?f=${key}&render=1`, { waitUntil: 'load' });
await page.waitForFunction('window.__AD__ && window.__AD__.ready', null, { timeout: 30000 });

for (const t of stamps) {
  await page.evaluate((x) => window.__AD__.seek(x), t);
  const file = path.join(out, `${key}-t${String(t).replace('.', '_')}.png`);
  await page.locator('#stage').screenshot({ path: file, animations: 'disabled' });
  console.log('  ' + path.relative(ROOT, file));
}

if (errors.length) { console.error('\nPAGE ERRORS:\n' + errors.join('\n')); process.exitCode = 1; }
await browser.close();
