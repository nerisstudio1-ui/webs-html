# -*- coding: utf-8 -*-
"""Planning Instagram de ES ORIGEN — Septiembre 2026.
Replica la plantilla del calendario de agosto 2026 (Neris Studio)."""
import base64, html, pathlib

BASE = pathlib.Path("/tmp/claude-0/-home-user-webs-html/b56cda2c-87b5-591c-8a48-efe3a7e0cb71/scratchpad")
OUT  = BASE / "planning_esorigen.html"
LOGO = base64.b64encode((BASE / "logo_es_origen.png").read_bytes()).decode()

MES     = "Septiembre 2026"
SUB     = "Planning de contenido Instagram"
PIE_IZQ = "ES ORIGEN · Entrenamiento personalizado · Running y fuerza"
PIE_MID = f"Planning Instagram · {MES} · Elaborado por Neris Studio"

STATS = [("8", "POSTS", "post"), ("14", "STORIES", "cream"),
         ("Lun · Jue", "PUBLICAR", "brown"), ("18:00 h", "HORA FEED", "soft")]
COLUMNAS = [("LUNES", "POST"), ("MARTES", "STORY"), ("MIÉRCOLES", "STORY"),
            ("JUEVES", "POST"), ("VIERNES", "STORY")]

# calendario: filas de 5 · None = hueco · (dia, fmt, hora, linea1, linea2)
CAL = [
 [None,
  ("1", "STORY", "10:00", "Encuesta:", "¿Empiezas en septiembre?"),
  ("2", "STORY", "10:00", "Caja:", "¿Qué te frenó en verano?"),
  ("3", "POST", "18:00", "Septiembre no empieza", "el lunes que viene."),
  ("4", "STORY", "10:00", "Quiz:", "¿Cuántos días hacen falta?")],
 [("7", "POST", "18:00", "Las primeras tres semanas", "son las que deciden."),
  ("8", "STORY", "10:00", "Así ajustamos un plan", "cuando falla una semana."),
  ("9", "STORY", "10:00", "Encuesta:", "¿Empezar o seguir?"),
  ("10", "POST", "18:00", "El descanso", "también entrena."),
  ("11", "STORY", "10:00", "Consejo:", "la regla de los 10 minutos.")],
 [("14", "POST", "18:00", "Elige tu carrera", "de otoño."),
  ("15", "STORY", "10:00", "Encuesta:", "¿Qué distancia te llama?"),
  ("16", "STORY", "10:00", "Quiz:", "¿Cuánto se tarda en un 10K?"),
  ("17", "POST", "18:00", "Preparar una carrera", "no es correr más."),
  ("18", "STORY", "10:00", "Caja:", "¿Qué carrera tienes en mente?")],
 [("21", "POST", "18:00", "Qué cambia cuando", "entrenas con seguimiento."),
  ("22", "STORY", "10:00", "Backstage:", "una revisión semanal."),
  ("23", "STORY", "10:00", "Mito o realidad:", "si no acabas reventado, no vale."),
  ("24", "POST", "18:00", "Tu plan debería", "cambiar contigo."),
  ("25", "STORY", "10:00", "Encuesta:", "¿Sigues un plan o improvisas?")],
 [("28", "POST", "18:00", "Octubre es", "para consolidar."),
  ("29", "STORY", "10:00", "Caja:", "¿Qué has conseguido este mes?"),
  ("30", "STORY", "10:00", "Plazas abiertas", "para octubre."),
  None, None],
]

# semanas: (titulo, tema, color, [5 slots]) · slot = (fmt, fecha, titular, [lineas])
SEMANAS = [
 ("SEMANA 01 · 1 - 4 SEPTIEMBRE", "Arranque de temporada.", "#6B5144", [
  None,
  ("STORY", "Mar 1 · 10:00", "¿Empiezas en septiembre?",
   ["Encuesta: Sí, este mes / Lo estoy pensando.",
    "Visual: foto real de una salida temprano.",
    "Compartir resultado al día siguiente."]),
  ("STORY", "Mié 2 · 10:00", "¿Qué te frenó en verano?",
   ["Caja de respuestas abierta.",
    "Calor, viajes o falta de plan.",
    "Guardar respuestas para los contenidos del mes."]),
  ("POST", "Jue 3 · 18:00", "Septiembre no empieza el lunes que viene.",
   ["Carrusel: hoy, mañana, la semana que viene.",
    "Mensaje: el mejor día para empezar es el que ya está en el calendario.",
    "CTA: Empieza con un plan, no con una promesa."]),
  ("STORY", "Vie 4 · 10:00", "¿Cuántos días hacen falta?",
   ["Quiz: 2 / 3 / 5 días por semana.",
    "Respuesta: menos de los que crees, bien repartidos.",
    "Cierre: lo importante es sostenerlo."]),
 ]),
 ("SEMANA 02 · 7 - 11 SEPTIEMBRE", "Constancia: las primeras semanas.", "#A1B1CE", [
  ("POST", "Lun 7 · 18:00", "Las primeras tres semanas son las que deciden.",
   ["Carrusel: empezar suave, repartir, medir, descansar.",
    "Mensaje: la constancia gana a la intensidad.",
    "CTA: Guarda el post y revísalo en tres semanas."]),
  ("STORY", "Mar 8 · 10:00", "Así ajustamos un plan.",
   ["Backstage: qué hacemos cuando falla una semana.",
    "Texto breve, cercano y profesional.",
    "Sin necesidad de interacción."]),
  ("STORY", "Mié 9 · 10:00", "¿Qué te cuesta más?",
   ["Encuesta: Empezar / Seguir.",
    "Foto real de entrenamiento.",
    "Cierre: casi siempre es lo segundo."]),
  ("POST", "Jue 10 · 18:00", "El descanso también entrena.",
   ["Carrusel: sueño, días suaves, carga y recuperación.",
    "Mensaje: entrenar sin descansar es solo cansarse.",
    "CTA: ¿Cuántos días descansas a la semana?"]),
  ("STORY", "Vie 11 · 10:00", "La regla de los 10 minutos.",
   ["Consejo: si no te apetece, sal solo diez minutos.",
    "Casi siempre acabas haciendo la sesión entera.",
    "Visual: zapatillas y puerta."]),
 ]),
 ("SEMANA 03 · 14 - 18 SEPTIEMBRE", "Tu objetivo de otoño.", "#8C7A6C", [
  ("POST", "Lun 14 · 18:00", "Elige tu carrera de otoño.",
   ["Carrusel: 5K, 10K, media y trail.",
    "Mensaje: un objetivo con fecha cambia el entrenamiento.",
    "CTA: Cuéntanos tu objetivo y preparamos el plan."]),
  ("STORY", "Mar 15 · 10:00", "¿Qué distancia te llama?",
   ["Encuesta por pantallas: 5K / 10K / media.",
    "Una foto para cada distancia.",
    "Objetivo: detectar intereses."]),
  ("STORY", "Mié 16 · 10:00", "¿Cuánto se tarda en preparar un 10K?",
   ["Quiz con opciones.",
    "Respuesta: depende del punto de partida.",
    "Lo habitual: entre 8 y 12 semanas."]),
  ("POST", "Jue 17 · 18:00", "Preparar una carrera no es correr más.",
   ["Carrusel: series, tirada larga, fuerza y descanso.",
    "Mensaje: cada sesión tiene una función.",
    "CTA: Empieza desde tu nivel."]),
  ("STORY", "Vie 18 · 10:00", "¿Qué carrera tienes en mente?",
   ["Caja de respuestas abierta.",
    "Recoger fechas y distancias reales.",
    "CTA: responde y te orientamos."]),
 ]),
 ("SEMANA 04 · 21 - 25 SEPTIEMBRE", "Seguimiento y ajustes.", "#6B5144", [
  ("POST", "Lun 21 · 18:00", "Qué cambia cuando entrenas con seguimiento.",
   ["Carrusel: plan adaptado, revisión semanal, ajustes, dudas resueltas.",
    "Mensaje: no es tener un plan, es tener a alguien mirándolo.",
    "CTA: Escríbenos y te contamos cómo trabajamos."]),
  ("STORY", "Mar 22 · 10:00", "Una revisión semanal por dentro.",
   ["Backstage: cómo se ajusta un plan real.",
    "Sin datos ni nombres de clientes.",
    "Humaniza la marca."]),
  ("STORY", "Mié 23 · 10:00", "Mito o realidad.",
   ["“Si no acabas reventado, no ha valido.”",
    "Respuesta: mito. La mayoría de sesiones son suaves.",
    "Sticker de quiz."]),
  ("POST", "Jue 24 · 18:00", "Tu plan debería cambiar contigo.",
   ["Foto de una planificación en revisión.",
    "Mensaje: el plan de septiembre no es el de noviembre.",
    "CTA: Guarda el post y revisa tu entrenamiento."]),
  ("STORY", "Vie 25 · 10:00", "¿Sigues un plan o improvisas?",
   ["Encuesta: Tengo plan / Voy sobre la marcha.",
    "Compartir el resultado.",
    "Cierre: improvisar también es una decisión."]),
 ]),
 ("SEMANA 05 · 28 - 30 SEPTIEMBRE", "Cierre de mes y octubre.", "#A1B1CE", [
  ("POST", "Lun 28 · 18:00", "Octubre es para consolidar.",
   ["Balance del mes y qué toca ahora.",
    "Foto potente de otoño en pista o carretera.",
    "CTA: Plazas abiertas · Solicita información."]),
  ("STORY", "Mar 29 · 10:00", "¿Qué has conseguido este mes?",
   ["Caja de respuestas abierta.",
    "Repostear las respuestas con permiso.",
    "Refuerzo de comunidad."]),
  ("STORY", "Mié 30 · 10:00", "Plazas abiertas para octubre.",
   ["Encuesta: Quiero información / Tengo dudas.",
    "Visual de marca + fotografía deportiva.",
    "CTA directo a mensaje privado."]),
  None, None,
 ]),
]

BROWN, PERI, SOFT, CREAM, BG = "#6B5144", "#A1B1CE", "#E9EEF6", "#F4EFE7", "#FBF8F3"
BORDER, INK = "#D9CEC2", "#332B27"

def esc(t):
    return html.escape(str(t))

CSS = f"""
@page {{ size:A4 landscape; margin:0; }}
* {{ box-sizing:border-box; -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
body {{ margin:0; font-family:Helvetica, Arial, sans-serif; color:{INK}; }}
.page {{ width:297mm; height:210mm; display:flex; flex-direction:column;
         background:{BG}; page-break-after:always; overflow:hidden; }}
.page:last-child {{ page-break-after:auto; }}

.head {{ display:flex; align-items:center; padding:3mm 8mm 2mm; gap:6mm; }}
.head img {{ height:15mm; }}
.head .tit {{ border-left:.4pt solid {BORDER}; padding-left:7mm; flex:1; }}
.head .eyebrow {{ font-size:6.6pt; font-weight:bold; letter-spacing:.16em; color:{PERI};
                  border-bottom:.5mm solid {PERI}; padding-bottom:1.6mm; display:inline-block;
                  min-width:62mm; }}
.head h1 {{ margin:1.5mm 0 0; font-size:15.5pt; font-weight:bold; color:{BROWN}; }}
.head .sub {{ font-size:8.2pt; color:{BROWN}; margin-top:1.2mm; opacity:.85; }}
.stats {{ display:flex; gap:2.6mm; }}
.stat {{ width:25mm; border-radius:1.6mm; text-align:center; padding:2.8mm 1mm; }}
.stat .n {{ font-size:12pt; font-weight:bold; color:{INK}; }}
.stat .l {{ font-size:5.7pt; letter-spacing:.14em; color:{BROWN}; margin-top:1.4mm; }}
.stat.post {{ background:{PERI}; }} .stat.cream {{ background:{CREAM}; }}
.stat.soft {{ background:{SOFT}; }}
.stat.brown {{ background:{BROWN}; }} .stat.brown .n, .stat.brown .l {{ color:#fff; }}

.legend {{ display:flex; align-items:center; gap:3mm; padding:1mm 8mm 0; }}
.legend .lbl {{ font-size:6.2pt; letter-spacing:.15em; color:{BROWN}; margin-right:2mm; }}
.legend .p {{ width:34mm; text-align:center; font-size:6.3pt; font-weight:bold;
              letter-spacing:.12em; padding:1.2mm 0; border-radius:6mm; color:{BROWN}; }}
.legend .p.post {{ background:{PERI}; }}
.legend .p.story {{ background:{CREAM}; border:.4pt solid {BORDER}; }}

.cols {{ display:grid; grid-template-columns:repeat(5,1fr); gap:2.2mm;
         padding:2.4mm 8mm 1.8mm; text-align:center; }}
.cols div {{ border-radius:1.2mm; padding:1.5mm 1mm; }}
.cols .d {{ font-size:8pt; font-weight:bold; color:{BROWN}; letter-spacing:.05em; }}
.cols .r {{ font-size:5.8pt; letter-spacing:.14em; color:{BROWN}; margin-top:.8mm; opacity:.8; }}

.grid {{ display:grid; grid-template-columns:repeat(5,1fr); grid-auto-rows:1fr;
         gap:2.2mm; padding:0 8mm 3mm; flex:1; }}
.cell {{ border:.4pt solid {BORDER}; border-radius:1.6mm; overflow:hidden;
         display:flex; flex-direction:column; }}
.cell .r1 {{ padding:1.5mm 2.2mm 1.2mm; }}
.cell .badge {{ display:inline-block; font-size:6.6pt; font-weight:bold; color:#fff;
                padding:.7mm 2.4mm; border-radius:4mm; }}
.cell .bar {{ display:flex; justify-content:space-between; align-items:center;
              padding:1.2mm 2.4mm; font-size:6pt; font-weight:bold; letter-spacing:.11em; }}
.cell .bar .h {{ font-weight:normal; letter-spacing:.02em; opacity:.9; }}
.cell .bd {{ flex:1; padding:2.2mm 2.2mm; font-size:7.4pt; line-height:1.38; }}
.cell.blank {{ background:{BG}; border-color:{BORDER}; opacity:.45; }}
.cell.post {{ background:{SOFT}; }}
.cell.post .badge {{ background:{PERI}; color:{INK}; }}
.cell.post .bar {{ background:{PERI}; color:{INK}; }}
.cell.story {{ background:{BG}; }}
.cell.story .badge {{ background:{BROWN}; }}
.cell.story .bar {{ background:{BROWN}; color:#fff; }}

.wgrid {{ display:grid; grid-template-columns:repeat(5,1fr); gap:1.6mm;
          padding:1.2mm 8mm 2.6mm; flex:1;
          grid-template-rows:auto repeat(5, 1fr); }}
.whead {{ border-radius:1.4mm; padding:1.9mm 2.6mm; color:#fff; }}
.whead.light {{ color:{BROWN}; }}
.whead .c {{ font-size:7.1pt; font-weight:bold; letter-spacing:.04em; }}
.whead .s {{ font-size:5.9pt; margin-top:.8mm; opacity:.85; }}
.icard {{ border:.4pt solid {BORDER}; border-radius:1.4mm; overflow:hidden;
          display:flex; flex-direction:column; }}
.icard .bar {{ display:flex; justify-content:space-between; align-items:center;
               padding:1mm 2.2mm; font-size:5.7pt; font-weight:bold; letter-spacing:.11em; }}
.icard .bar .d {{ font-weight:normal; letter-spacing:.02em; opacity:.9; }}
.icard .bd {{ flex:1; padding:1.4mm 2mm 1.5mm; }}
.icard .t {{ font-size:6.8pt; font-weight:bold; color:{BROWN};
             border-bottom:.4pt solid {BORDER}; padding-bottom:1.2mm; line-height:1.22; }}
.icard .x {{ font-size:5.6pt; color:{INK}; line-height:1.26; margin-top:.9mm; opacity:.85; }}
.icard.post {{ background:{SOFT}; }} .icard.post .bar {{ background:{PERI}; color:{INK}; }}
.icard.story {{ background:{BG}; }} .icard.story .bar {{ background:{BROWN}; color:#fff; }}

.foot {{ background:{BROWN}; color:#fff; padding:2.8mm 8mm; display:flex;
         justify-content:space-between; font-size:6.6pt; }}
.foot .l {{ font-weight:bold; }}
.foot .mid, .foot .r {{ opacity:.85; }}
"""

def cabecera(titulo, sub, stats):
    s = ""
    if stats:
        s = '<div class="stats">' + "".join(
            f'<div class="stat {cls}"><div class="n">{esc(n)}</div>'
            f'<div class="l">{esc(l)}</div></div>' for n, l, cls in STATS) + "</div>"
    return (f'<div class="head"><img src="data:image/png;base64,{LOGO}" alt="ES ORIGEN">'
            f'<div class="tit"><div class="eyebrow">ES ORIGEN</div><h1>{esc(titulo)}</h1>'
            f'<div class="sub">{esc(sub)}</div></div>{s}</div>')

def pie(n):
    return (f'<div class="foot"><div class="l">{esc(PIE_IZQ)}</div>'
            f'<div class="mid">{esc(PIE_MID)}</div><div class="r">{n} / 2</div></div>')

h = ['<!doctype html><html lang="es"><head><meta charset="utf-8">',
     f'<title>ES ORIGEN - Planning Instagram {MES}</title>',
     f"<style>{CSS}</style></head><body>"]

# ---------------- PÁGINA 1
h.append(f'<div class="page">{cabecera(MES, SUB, True)}')
h.append(f'<div class="legend"><span class="lbl">LEYENDA</span>'
         f'<span class="p post">POST</span><span class="p story">STORY</span></div>')
h.append('<div class="cols">' + "".join(
    f'<div style="background:{SOFT if r == "POST" else CREAM}">'
    f'<div class="d">{esc(d)}</div><div class="r">{esc(r)}</div></div>'
    for d, r in COLUMNAS) + "</div>")
h.append('<div class="grid">')
for fila in CAL:
    for celda in fila:
        if celda is None:
            h.append('<div class="cell blank"></div>')
            continue
        num, fmt, hora, l1, l2 = celda
        cls = "post" if fmt == "POST" else "story"
        h.append(f'<div class="cell {cls}"><div class="r1">'
                 f'<span class="badge">{esc(num)}</span></div>'
                 f'<div class="bar"><span>{esc(fmt)}</span><span class="h">{esc(hora)}</span></div>'
                 f'<div class="bd">{esc(l1)}<br>{esc(l2)}</div></div>')
h.append("</div>" + pie(1) + "</div>")

# ---------------- PÁGINA 2
h.append(f'<div class="page">{cabecera("Brief semanal", f"Contenido detallado y stories - {MES}", False)}')
h.append('<div class="wgrid">')
for tit, tema, color, _ in SEMANAS:
    light = " light" if color == PERI else ""
    h.append(f'<div class="whead{light}" style="background:{color}">'
             f'<div class="c">{esc(tit)}</div><div class="s">{esc(tema)}</div></div>')
for fila in range(5):
    for _, _, _, slots in SEMANAS:
        slot = slots[fila]
        if slot is None:
            h.append("<div></div>")
            continue
        fmt, fecha, titular, lineas = slot
        cls = "post" if fmt == "POST" else "story"
        cuerpo = "".join(f'<div class="x">{esc(x)}</div>' for x in lineas)
        h.append(f'<div class="icard {cls}"><div class="bar"><span>{esc(fmt)}</span>'
                 f'<span class="d">{esc(fecha)}</span></div>'
                 f'<div class="bd"><div class="t">{esc(titular)}</div>{cuerpo}</div></div>')
h.append("</div>" + pie(2) + "</div>")

h.append("</body></html>")
OUT.write_text("".join(h), encoding="utf-8")
print("html ->", OUT)
