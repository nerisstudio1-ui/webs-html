# -*- coding: utf-8 -*-
"""Descarga tipografías de Google Fonts y las deja auto-alojadas en assets/fonts/.
   Ventajas: cargan más rápido y la web no conecta con servidores de Google (mejor para el RGPD)."""
import os, re, subprocess, sys

DEST = "assets/fonts"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")  # necesario para que Google sirva woff2

def css_de(familia):
    url = f"https://fonts.googleapis.com/css2?family={familia}&display=swap"
    r = subprocess.run(["curl", "-sS", "--max-time", "30", "-A", UA, url],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[:200])
    return r.stdout

# Subconjuntos que necesitamos; el resto (cirílico, griego, vietnamita) se descarta.
SUBSETS = ("latin", "latin-ext")

def descargar(familias):
    os.makedirs(DEST, exist_ok=True)
    reglas = []
    for familia in familias:
        css = css_de(familia)
        # Google antecede cada @font-face con un comentario que nombra el subconjunto:
        # /* latin */ @font-face { ... }
        bloques = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*{[^}]+})", css)
        if not bloques:  # por si algún día deja de incluir el comentario
            bloques = [("latin", b) for b in re.findall(r"@font-face\s*{[^}]+}", css)]
        for subset, bloque in bloques:
            if subset not in SUBSETS:
                continue
            m_url = re.search(r"url\((https://[^)]+\.woff2)\)", bloque)
            m_fam = re.search(r"font-family:\s*'([^']+)'", bloque)
            m_pes = re.search(r"font-weight:\s*([\d ]+)", bloque)
            m_est = re.search(r"font-style:\s*(\w+)", bloque)
            if not (m_url and m_fam):
                continue
            peso = m_pes.group(1).replace(" ", "-") if m_pes else "400"
            estilo = m_est.group(1) if m_est else "normal"
            nombre = f"{m_fam.group(1).replace(' ', '-').lower()}-{peso}-{estilo}-{subset}.woff2"
            ruta = os.path.join(DEST, nombre)
            if not os.path.exists(ruta):
                subprocess.run(["curl", "-sS", "--max-time", "60", "-o", ruta, m_url.group(1)], check=True)
            reglas.append(bloque.replace(m_url.group(1), f"../fonts/{nombre}") + "\n")
    return "".join(reglas)

if __name__ == "__main__":
    familias = sys.argv[1:] or [
        "Playfair+Display:ital,wght@0,400;0,500;1,400",
        "DM+Sans:wght@300;400;500",
    ]
    css = descargar(familias)
    with open(f"{DEST}/fuentes.css", "w", encoding="utf-8") as f:
        f.write("/* Tipografías auto-alojadas · generado por _fuentes.py */\n" + css)
    print(f"{len(re.findall('@font-face', css))} caras descargadas en {DEST}")
