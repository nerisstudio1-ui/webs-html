# -*- coding: utf-8 -*-
"""Encapsula una hoja de estilos dentro de un selector.

   Sirve para insertar la landing en un WordPress sin que sus estilos afecten
   al tema (ni el tema a los nuestros). Recorre las reglas de primer nivel,
   entra en las @media y deja intactas @font-face y @keyframes.
"""
import re

# Reglas que no se tocan: no llevan selectores de elementos
SIN_SELECTOR = ("@font-face", "@keyframes", "@-webkit-keyframes", "@import", "@charset")
# Reglas que agrupan otras y hay que recorrer por dentro
CONTENEDORAS = ("@media", "@supports", "@layer", "@container")

def _trocear(css):
    """Divide en bloques de primer nivel: (selector_o_regla, cuerpo) o texto suelto."""
    piezas, i, inicio, nivel = [], 0, 0, 0
    while i < len(css):
        c = css[i]
        if c == "{":
            if nivel == 0:
                cabeza = css[inicio:i]
                cuerpo_ini = i + 1
            nivel += 1
        elif c == "}":
            nivel -= 1
            if nivel == 0:
                piezas.append((cabeza, css[cuerpo_ini:i]))
                inicio = i + 1
        i += 1
    if css[inicio:].strip():
        piezas.append((None, css[inicio:]))
    return piezas

def _separar_comentarios(cabeza):
    """Los comentarios que preceden a una regla no forman parte del selector.
       Si se dejan pegados, el selector resultante es inválido y el navegador
       descarta la regla entera."""
    comentarios = "".join(re.findall(r"/\*.*?\*/", cabeza, re.S))
    limpio = re.sub(r"/\*.*?\*/", " ", cabeza, flags=re.S).strip()
    return comentarios, limpio

def _prefijar(selectores, ambito):
    salida = []
    for sel in selectores.split(","):
        s = sel.strip()
        if not s:
            continue
        if s in (":root", "html"):
            # las variables y los ajustes de raíz pasan al propio contenedor
            salida.append(ambito)
        elif s == "body":
            salida.append(ambito)
        elif s.startswith("body."):
            # estados que el JavaScript pone en <body>: se dejan como están
            salida.append(s)
        elif s.startswith(("*", ":focus-visible")):
            salida.append(f"{ambito} {s}" if s != "*" else f"{ambito} *")
        elif s.startswith("@"):
            salida.append(s)
        else:
            salida.append(f"{ambito} {s}")
    return ", ".join(salida)

def encapsular(css, ambito=".anahata"):
    fuera = []
    for cabeza, cuerpo in _trocear(css):
        if cabeza is None:
            fuera.append(cuerpo)
            continue
        comentarios, c = _separar_comentarios(cabeza)
        if comentarios:
            fuera.append(comentarios)
        if c.startswith(SIN_SELECTOR):
            fuera.append(f"{c}{{{cuerpo}}}")
        elif c.startswith(CONTENEDORAS):
            fuera.append(f"{c}{{{encapsular(cuerpo, ambito)}}}")
        else:
            fuera.append(f"{_prefijar(c, ambito)}{{{cuerpo}}}")
    return "\n".join(fuera)
