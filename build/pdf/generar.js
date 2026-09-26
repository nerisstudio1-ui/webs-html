// Genera los dos PDF de descarga a partir de las páginas de esta carpeta.
//   node build/pdf/generar.js
// Levanta su propio servidor sobre la raíz del repositorio, para que las rutas
// relativas a assets/ (fuentes y logotipo) resuelvan igual que en la web.
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');

const RAIZ = path.resolve(__dirname, '../..');
const PUERTO = 8788;
const TIPOS = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.svg': 'image/svg+xml', '.woff2': 'font/woff2',
  '.jpg': 'image/jpeg', '.png': 'image/png',
};

const servidor = http.createServer((req, res) => {
  const f = path.join(RAIZ, decodeURIComponent(req.url.split('?')[0]));
  if (!f.startsWith(RAIZ) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) {
    res.writeHead(404); return res.end('no');
  }
  res.writeHead(200, { 'Content-Type': TIPOS[path.extname(f).toLowerCase()] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});

(async () => {
  await new Promise(r => servidor.listen(PUERTO, r));
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [origen, destino] of [
    ['biografia.html', 'assets/docs/cristina-falcon-biografia-completa.pdf'],
    ['dossier.html',   'assets/docs/cristina-falcon-dossier-prensa.pdf'],
  ]) {
    const p = await b.newPage();
    await p.goto(`http://localhost:${PUERTO}/build/pdf/${origen}`, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join(RAIZ, destino), format: 'A4', printBackground: true });
    await p.close();
    console.log('  ' + destino);
  }
  await b.close();
  servidor.close();
})();
