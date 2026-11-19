"""
Avisa de textos ilegibles: los que quedan del mismo color que su fondo.

    python3 comprobar-contraste.py calma-elementor.html

Devuelve 1 si encuentra alguno, para poder encadenarlo con el resto.
Se salta el hero y la franja, donde el texto va sobre una foto y esta
comprobación no tiene sentido.
"""
import glob, os, sys
from playwright.sync_api import sync_playwright

def chromium():
    """El Chromium del contenedor cambia de carpeta con cada actualización."""
    for patron in ('/opt/pw-browsers/chromium-*/chrome-linux*/chrome',
                   '/opt/pw-browsers/chromium/chrome-linux*/chrome'):
        encontrados = sorted(glob.glob(patron))
        if encontrados:
            return encontrados[-1]
    sys.exit('No encuentro Chromium en /opt/pw-browsers')

AUDIT = """() => {
  const lum = c => { const [r,g,b] = c.match(/\\d+/g).map(Number).map(v=>{
      v/=255; return v<=.03928 ? v/12.92 : Math.pow((v+.055)/1.055, 2.4);});
    return .2126*r + .7152*g + .0722*b; };
  const fondoReal = el => { let n = el;
    while (n) { const bg = getComputedStyle(n).backgroundColor;
      if (bg && !/rgba\\(0, 0, 0, 0\\)|transparent/.test(bg)) return bg;
      n = n.parentElement; }
    return 'rgb(255,255,255)'; };
  const malos = [];
  document.querySelectorAll('.btn, .sticky-book, .nav a, .clase, h1, h2, h3, h4, p, li, summary')
    .forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width < 8 || r.height < 8) return;
      if (!el.textContent.trim()) return;
      /* El hero y la franja llevan el texto sobre una foto, no sobre un
         color: ahí esta comprobación no sirve y daría falsos avisos. */
      if (el.closest('.hero, .franja')) return;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.display === 'none') return;
      const c = lum(cs.color), f = lum(fondoReal(el));
      const ratio = (Math.max(c,f) + .05) / (Math.min(c,f) + .05);
      if (ratio < 2.2) malos.push({
        texto: el.textContent.trim().slice(0, 34),
        clase: (el.className || el.tagName).toString().slice(0, 26),
        color: cs.color, fondo: fondoReal(el), contraste: +ratio.toFixed(2) });
    });
  return malos;
}"""

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=chromium())
    fallo = False
    for archivo in sys.argv[1:]:
        for w, h, et in [(393, 852, 'movil'), (1440, 900, 'escritorio')]:
            p = b.new_page(viewport={'width': w, 'height': h})
            p.goto('file://' + os.path.abspath(archivo)); p.wait_for_timeout(1100)
            p.evaluate("document.querySelectorAll('.reveal,.hero__slogan').forEach(e=>e.classList.add('is-in'))")
            p.wait_for_timeout(300)
            malos = p.evaluate(AUDIT)
            estado = 'OK' if not malos else f'{len(malos)} ILEGIBLES'
            print(f'  {archivo:14} {et:11} {estado}')
            for m in malos:
                fallo = True
                print(f'     · "{m["texto"]}" ({m["clase"]}) {m["color"]} sobre {m["fondo"]} → {m["contraste"]}')
            p.close()
    b.close()
    sys.exit(1 if fallo else 0)
