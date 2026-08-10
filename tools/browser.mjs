/* Chromium lookup.
 *
 * This environment ships a pre-installed Chromium under PLAYWRIGHT_BROWSERS_PATH
 * whose build number will not always match whatever playwright version npm
 * resolved. Rather than re-downloading a browser, point Playwright at the one
 * that is already here and fall back to its own bundled lookup elsewhere. */

import { chromium } from 'playwright';
import { existsSync, readdirSync } from 'node:fs';
import path from 'node:path';

export function chromiumPath() {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;

  const root = process.env.PLAYWRIGHT_BROWSERS_PATH || '/opt/pw-browsers';
  if (!existsSync(root)) return undefined;

  const dirs = readdirSync(root)
    .filter((d) => /^chromium-\d+$/.test(d))
    .sort((a, b) => Number(b.split('-')[1]) - Number(a.split('-')[1]));

  for (const d of dirs) {
    const bin = path.join(root, d, 'chrome-linux', 'chrome');
    if (existsSync(bin)) return bin;
  }
  return undefined;
}

export function launch(extra = {}) {
  const executablePath = chromiumPath();
  return chromium.launch({
    ...(executablePath ? { executablePath } : {}),
    args: [
      '--force-color-profile=srgb',
      '--disable-lcd-text',
      '--font-render-hinting=none',
      '--hide-scrollbars',
      ...(extra.args || []),
    ],
    ...extra,
  });
}
