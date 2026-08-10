#!/usr/bin/env node
/* Renders src/ad.html to an MP4 per Facebook placement.
 *
 * The page exposes a deterministic `window.__AD__.seek(t)`, so instead of
 * screen-recording in real time (which drops frames and bakes in whatever the
 * machine was doing) we step the timeline frame by frame, screenshot each one,
 * and hand the sequence to ffmpeg. Same input, same output, every run. */

import { launch } from './browser.mjs';
import { spawn } from 'node:child_process';
import { mkdir, rm, readdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PAGE = path.join(ROOT, 'src', 'ad.html');
const OUT = path.join(ROOT, 'dist');
const FPS = 30;

const FORMATS = {
  '4x5':  { w: 1080, h: 1350, label: 'feed-4x5' },
  '3x4':  { w: 1080, h: 1440, label: 'feed-3x4' },
  '9x16': { w: 1080, h: 1920, label: 'reels-9x16' },
  '1x1':  { w: 1080, h: 1080, label: 'feed-1x1' },
};

function ffmpegPath() {
  if (process.env.FFMPEG) return process.env.FFMPEG;
  const candidates = [
    '/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2',
    '/usr/bin/ffmpeg',
    '/usr/local/bin/ffmpeg',
  ];
  return candidates.find((p) => existsSync(p)) || 'ffmpeg';
}

function run(cmd, args) {
  return new Promise((resolve, reject) => {
    const p = spawn(cmd, args, { stdio: ['ignore', 'ignore', 'pipe'] });
    let err = '';
    p.stderr.on('data', (d) => { err += d; });
    p.on('close', (code) => (code === 0 ? resolve() : reject(new Error(err.slice(-2500)))));
    p.on('error', reject);
  });
}

async function renderFormat(browser, key) {
  const fmt = FORMATS[key];
  const frameDir = path.join(OUT, '.frames-' + key);
  await rm(frameDir, { recursive: true, force: true });
  await mkdir(frameDir, { recursive: true });

  const page = await browser.newPage({
    viewport: { width: fmt.w, height: fmt.h },
    deviceScaleFactor: 1,
  });

  const errors = [];
  page.on('pageerror', (e) => errors.push(String(e)));

  await page.goto(`file://${PAGE}?f=${key}&render=1`, { waitUntil: 'load' });
  await page.waitForFunction('window.__AD__ && window.__AD__.ready', null, { timeout: 30000 });

  if (errors.length) throw new Error(`page errors in ${key}:\n` + errors.join('\n'));

  const duration = await page.evaluate('window.__AD__.duration');
  const total = Math.round(duration * FPS);
  const stage = page.locator('#stage');

  process.stdout.write(`  ${key} ${fmt.w}x${fmt.h} — ${total} frames `);

  for (let i = 0; i < total; i++) {
    await page.evaluate((t) => window.__AD__.seek(t), i / FPS);
    await stage.screenshot({
      path: path.join(frameDir, String(i).padStart(4, '0') + '.png'),
      animations: 'disabled',
    });
    if (i % 45 === 0) process.stdout.write('.');
  }
  await page.close();

  const count = (await readdir(frameDir)).length;
  if (count !== total) throw new Error(`${key}: expected ${total} frames, captured ${count}`);

  const out = path.join(OUT, `neris-webs-299-${fmt.label}.mp4`);
  await run(ffmpegPath(), [
    '-y', '-loglevel', 'error',
    '-framerate', String(FPS),
    '-i', path.join(frameDir, '%04d.png'),
    // Meta re-encodes on upload, so hand it a clean high-bitrate H.264 with
    // the pixel format and even dimensions every player expects.
    '-c:v', 'libx264',
    '-profile:v', 'high',
    '-crf', '17',
    '-preset', 'slow',
    '-pix_fmt', 'yuv420p',
    '-movflags', '+faststart',
    '-r', String(FPS),
    out,
  ]);

  await rm(frameDir, { recursive: true, force: true });
  process.stdout.write(` -> ${path.relative(ROOT, out)}\n`);
  return out;
}

async function main() {
  const requested = process.argv.slice(2).filter((a) => !a.startsWith('-'));
  const keys = requested.length ? requested : Object.keys(FORMATS);
  const unknown = keys.filter((k) => !FORMATS[k]);
  if (unknown.length) {
    console.error(`unknown format(s): ${unknown.join(', ')}`);
    console.error(`available: ${Object.keys(FORMATS).join(', ')}`);
    process.exit(1);
  }

  await mkdir(OUT, { recursive: true });
  const browser = await launch();

  console.log(`rendering ${keys.length} format(s) at ${FPS} fps`);
  try {
    for (const key of keys) await renderFormat(browser, key);
  } finally {
    await browser.close();
  }
  console.log('done');
}

main().catch((e) => { console.error(e); process.exit(1); });
