# -*- coding: utf-8 -*-
"""Planning Instagram de RK MBI Asesores Inmobiliarios — Septiembre 2026.
Replica la plantilla del planning de julio 2026 (Neris Studio)."""
import html

OUT = "/tmp/claude-0/-home-user-webs-html/b56cda2c-87b5-591c-8a48-efe3a7e0cb71/scratchpad/planning_rkmbi.html"

EYEBROW_A = "RK MBI ASESORES INMOBILIARIOS"
EYEBROW_B = "TORRENT, VALENCIA"
MES       = "Septiembre 2026"
SUB       = "Planning Instagram · Inmobiliaria premium Torrent"
PIE_IZQ   = "RK MBI Asesores Inmobiliarios · Torrent, Valencia · @rk_mbiasesores"
PIE_MID   = f"Planning Instagram · {MES} · Elaborado por Neris Studio"

STATS = [("8", "POSTS"), ("9", "STORIES"), ("Lun · Jue", "PUBLICAR"),
         ("18:00h", "HORA"), ("Valencia", "ÁREA")]
COLUMNAS = [("LUNES", "FEED"), ("MARTES", "STORY"), ("MIÉRCOLES", "DESCANSO"),
            ("JUEVES", "FEED"), ("VIERNES", "STORY")]

FMT = {  # formato: (color, tinte)
 "REEL":      ("#232A4D", "#ECEEF5"),
 "POST":      ("#3E6B50", "#EBF1ED"),
 "CARRUSEL":  ("#6E5A3E", "#F2EEE6"),
 "EDUCATIVO": ("#4A3F6E", "#EEEBF3"),
 "DESTACADO": ("#B2933F", "#FBF5E4"),
 "STORY":     ("#6B5E58", "#F0ECEA"),
}
LEYENDA = ["REEL", "POST", "CARRUSEL", "EDUCATIVO", "DESTACADO", "STORY"]

# calendario: 5 filas x 5 columnas · None = hueco sin fecha · (dia,) = descanso
CAL = [
 [None, ("1", "STORY", "10:00", "Encuesta: vender ahora o en 2027"), ("2",),
        ("3", "REEL", "18:00", "Septiembre: vuelven los compradores"),
        ("4", "STORY", "10:00", "Pregunta: ¿qué quieres saber antes de vender?")],
 [("7", "DESTACADO", "18:00", "Propiedad destacada de la semana"),
  ("8", "STORY", "10:00", "Quiz: ¿qué es una nota simple?"), ("9",),
  ("10", "EDUCATIVO", "18:00", "Los 5 papeles para poder vender"),
  ("11", "STORY", "10:00", "Slider: ¿tienes la documentación lista?")],
 [("14", "REEL", "18:00", "Lo que mira un comprador al entrar"),
  ("15", "STORY", "10:00", "Encuesta: ¿sabes qué es la plusvalía?"), ("16",),
  ("17", "CARRUSEL", "18:00", "Lo que cuesta vender tu casa"),
  ("18", "STORY", "10:00", "BTS: una tarde de firmas")],
 [("21", "POST", "18:00", "Caso real: vendida en semanas"),
  ("22", "STORY", "10:00", "Pregunta: ¿qué te preocupa al vender?"), ("23",),
  ("24", "EDUCATIVO", "18:00", "Cuánto tarda en venderse en Torrent"),
  ("25", "STORY", "10:00", "Testimonio: entrega de llaves")],
 [("28", "DESTACADO", "18:00", "Última propiedad del mes"),
  ("29", "STORY", "10:00", "CTA: compradores esperando"), ("30",), None, None],
]

# semanas: (codigo, tema, color, [4 slots: feed lun, story mar, feed jue, story vie])
# slot = (formato, fecha, titulo, descripcion, cta) · None = vacío
SEMANAS = [
 ("Sem 01 · 1-4 sept", "Vuelve el mercado · arranque de curso", "#232A4D", [
  None,
  ("STORY", "Mar 1 · 10:00 — ENCUESTA", "Vender ahora o esperar a 2027",
   "Tipo: encuesta 'AHORA' / 'ESPERO'. After si AHORA: 'Septiembre y octubre "
   "concentran la mejor demanda. Hablamos.'", None),
  ("REEL", "Jue 3 · 18:00", "Septiembre: vuelven los compradores",
   "Reel 20-30s. Texto sobre vídeo: 'En septiembre se reactivan las búsquedas en Torrent'. "
   "Mostrar zona y movimiento de visitas. Tono cercano, sin presión.",
   "Valoramos tu casa sin compromiso. Escríbenos."),
  ("STORY", "Vie 4 · 10:00 — PREGUNTA", "¿Qué quieres saber antes de vender?",
   "Tipo: caja de preguntas abierta. Usar las respuestas para los educativos "
   "del mes.", None),
 ]),
 ("Sem 02 · 7-11 sept", "Los papeles en regla · documentación", "#B2933F", [
  ("DESTACADO", "Lun 7 · 18:00", "Propiedad destacada de la semana",
   "ESPACIO RESERVADO según propiedad disponible. Foto exterior + interior. Copy con m2, "
   "hab, zona y precio orientativo. Estructura adaptable.",
   "Agenda tu visita privada. Escríbenos."),
  ("STORY", "Mar 8 · 10:00 — QUIZ", "¿Sabes qué es una nota simple?",
   "Tipo: quiz con opciones. Revela la respuesta después. Posiciona conocimiento "
   "sin sonar técnico.", None),
  ("EDUCATIVO", "Jue 10 · 18:00", "Los 5 papeles que necesitas para vender",
   "Post educativo: nota simple, certificado energético, cédula de habitabilidad, ITE si "
   "aplica y último recibo del IBI. Qué es cada uno y cuánto tarda en salir.",
   "Los pedimos nosotros. Tú no mueves un papel."),
  ("STORY", "Vie 11 · 10:00 — SLIDER", "¿Tienes tu documentación lista?",
   "Tipo: slider 0-100. After: 'Si te sale bajo, lo resolvemos nosotros antes "
   "de publicar.'", None),
 ]),
 ("Sem 03 · 14-18 sept", "Cuánto cuesta vender · gastos e impuestos", "#3E6B50", [
  ("REEL", "Lun 14 · 18:00", "Lo que mira un comprador al entrar",
   "Reel dentro de una vivienda: entrada, luz y cocina. Los tres puntos que deciden una "
   "visita. Transiciones limpias, música tranquila.",
   "Reserva tu visita por DM."),
  ("STORY", "Mar 15 · 10:00 — ENCUESTA", "¿Sabes cuánto se paga de plusvalía?",
   "Tipo: encuesta 'SÍ' / 'NI IDEA'. After: 'Depende del caso. Te lo calculamos "
   "gratis.'", None),
  ("CARRUSEL", "Jue 17 · 18:00", "Lo que cuesta vender tu casa",
   "S1 Plusvalía municipal. S2 IRPF por la ganancia. S3 Notaría y registro. S4 Certificado "
   "energético. S5 Honorarios. Cifras orientativas, sin promesas.",
   "Te hacemos el cálculo antes de empezar."),
  ("STORY", "Vie 18 · 10:00 — BTS", "Una tarde de firmas",
   "Tipo: stories BTS en notaría. Mostrar al equipo trabajando, sin datos ni caras de "
   "clientes sin permiso. Humaniza la marca.", None),
 ]),
 ("Sem 04 · 21-25 sept", "Prueba social · casos reales", "#6E5A3E", [
  ("POST", "Lun 21 · 18:00", "Caso real: vendida en [X] semanas",
   "Post prueba social. Foto de la vivienda o cartel VENDIDO. Copy: precio ajustado, "
   "comprador cualificado, cierre sin sobresaltos. Sin datos privados.",
   "¿Tu casa la siguiente? Te explicamos cómo."),
  ("STORY", "Mar 22 · 10:00 — PREGUNTA", "¿Qué es lo que más te preocupa al vender?",
   "Tipo: caja de preguntas. Recoge objeciones reales para rebatirlas en octubre.", None),
  ("EDUCATIVO", "Jue 24 · 18:00", "Cuánto tarda de verdad en venderse en Torrent",
   "Post educativo: tiempos reales según zona y precio de salida. Por qué las tres primeras "
   "semanas de publicación deciden la venta. Datos propios de cartera.",
   "Te damos el dato de tu zona."),
  ("STORY", "Vie 25 · 10:00 — TESTIMONIO", "Entrega de llaves",
   "Tipo: stories con vídeo o foto real de una entrega. Prueba social emocional, "
   "sin texto comercial.", None),
 ]),
 ("Sem 05 · 28-30 sept", "Compradores activos · cierre de mes", "#4A3F6E", [
  ("DESTACADO", "Lun 28 · 18:00", "Última propiedad del mes",
   "Cierre de cartera de septiembre. Propiedad con visitas abiertas. Crear urgencia real "
   "(pocas visitas disponibles).",
   "Reserva la tuya antes de que entre octubre."),
  ("STORY", "Mar 29 · 10:00 — CTA", "Cartera activa: compradores esperando",
   "Tipo: CTA cierre de mes. 'Si octubre es tu mes para vender, septiembre es para "
   "empezar. Escríbenos.'", None),
  None, None,
 ]),
]

def esc(t):
    return html.escape(str(t))

CSS = """
@page { size:A4 landscape; margin:0; }
* { box-sizing:border-box; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body { margin:0; font-family:Helvetica, Arial, sans-serif; color:#262B36; }
.page { width:297mm; height:210mm; display:flex; flex-direction:column;
        background:#FBF9F4; page-break-after:always; overflow:hidden; }
.page:last-child { page-break-after:auto; }

.head { background:#fff; padding:5.2mm 8mm 4.4mm; display:flex; align-items:flex-start;
        justify-content:space-between; border-bottom:.9mm solid #B89A5A; }
.head .tit { border-left:1mm solid #B89A5A; padding-left:4mm; }
.eyebrow { font-size:7.2pt; font-weight:bold; letter-spacing:.07em; color:#1A2238; }
.eyebrow .g { color:#B89A5A; }
.head h1 { margin:1.6mm 0 0; font-size:21pt; font-weight:bold; color:#1A2238; letter-spacing:-.01em; }
.head .sub { font-size:8pt; font-style:italic; color:#888C97; margin-top:1.4mm; }
.stats { display:flex; gap:2.4mm; }
.stat { width:25mm; border:.4pt solid #E2E0DA; border-radius:1.3mm; background:#fff;
        text-align:center; padding:2.8mm 1mm; }
.stat.dark { background:#1A2238; border-color:#1A2238; }
.stat .n { font-size:11.5pt; font-weight:bold; color:#1A2238; }
.stat .l { font-size:5.9pt; letter-spacing:.15em; color:#8A8F99; margin-top:1.2mm; }
.stat.dark .n { color:#fff; } .stat.dark .l { color:#C0C4CE; }

.legend { display:flex; align-items:center; gap:2mm; padding:3mm 8mm 0; }
.legend .lbl { font-size:6.3pt; letter-spacing:.16em; color:#8A8F99; margin-right:2mm; }
.chip { color:#fff; font-size:6.1pt; font-weight:bold; letter-spacing:.09em;
        padding:1.1mm 2.6mm; border-radius:1mm; }

.cols { display:grid; grid-template-columns:repeat(5,1fr); gap:2.6mm;
        padding:3.4mm 8mm 2mm; text-align:center; }
.cols .d { font-size:9pt; font-weight:bold; color:#1A2238; letter-spacing:.04em; }
.cols .r { font-size:6.1pt; letter-spacing:.14em; color:#9A9EA8; margin-top:.9mm; }

.grid { display:grid; grid-template-columns:repeat(5,1fr); grid-auto-rows:1fr;
        gap:2.6mm; padding:0 8mm 4mm; flex:1; }
.cell { background:#fff; border:.4pt solid #E6E2D8; border-radius:1.4mm;
        overflow:hidden; display:flex; flex-direction:column; }
.cell .r1 { display:flex; align-items:center; justify-content:space-between;
            padding:1.7mm 2.2mm 1.5mm; }
.cell .badge { color:#fff; font-size:7.2pt; font-weight:bold; padding:.5mm 1.9mm;
               border-radius:1mm; }
.cell .ig { font-size:5.5pt; color:#B6B2AC; letter-spacing:.1em; }
.cell .bar { display:flex; justify-content:space-between; align-items:center;
             color:#fff; padding:1.2mm 2.2mm; font-size:6.1pt; font-weight:bold;
             letter-spacing:.09em; }
.cell .bar .h { font-weight:normal; opacity:.9; letter-spacing:.02em; }
.cell .bd { flex:1; padding:2.2mm; font-size:7.1pt; line-height:1.3; color:#262B36; }
.cell.off { background:#F3F1EA; border-color:#E6E2D8; }
.cell.off .badge { background:#E6E2D8; color:#AAA69E; }
.cell.blank { background:#F3F1EA; border-color:#E6E2D8; }

.wgrid { display:grid; grid-template-columns:repeat(5,1fr); gap:2.6mm;
         padding:3.6mm 8mm 4mm; flex:1; grid-template-rows:auto 1fr 1fr 1fr 1fr; }
.whead { border-radius:1.4mm; color:#fff; padding:2.5mm 3mm; }
.whead .c { font-size:8.4pt; font-weight:bold; letter-spacing:.03em; }
.whead .s { font-size:6.5pt; font-style:italic; margin-top:1mm; color:rgba(255,255,255,.82); }
.icard { border:.4pt solid #E6E2D8; border-radius:1.4mm; padding:2.5mm 2.7mm;
         display:flex; flex-direction:column; }
.icard .top { display:flex; justify-content:space-between; align-items:baseline; }
.icard .top .f { font-size:6pt; font-weight:bold; letter-spacing:.09em; }
.icard .top .d { font-size:5.9pt; color:#8A8F99; }
.icard .t { font-size:8pt; font-weight:bold; color:#1A2238; margin-top:1.7mm; line-height:1.25; }
.icard .x { font-size:6.7pt; color:#5C616B; line-height:1.38; margin-top:1.5mm; }
.icard .cta { margin-top:auto; padding-top:2.4mm; font-size:6.6pt; font-weight:bold; }

.foot { background:#1A2238; color:#C9CCD4; padding:2.8mm 8mm; display:flex;
        justify-content:space-between; font-size:6.6pt; }
.foot .mid { color:#B89A5A; }
"""

def cabecera(titulo, con_stats):
    stats = ""
    if con_stats:
        stats = '<div class="stats">' + "".join(
            f'<div class="stat{" dark" if i == len(STATS) - 1 else ""}">'
            f'<div class="n">{esc(n)}</div><div class="l">{esc(l)}</div></div>'
            for i, (n, l) in enumerate(STATS)) + "</div>"
    return (f'<div class="head"><div class="tit">'
            f'<div class="eyebrow">{esc(EYEBROW_A)} <span class="g">· {esc(EYEBROW_B)}</span></div>'
            f'<h1>{esc(titulo)}</h1><div class="sub">{esc(SUB)}</div></div>{stats}</div>')

def pie(n):
    return (f'<div class="foot"><div>{esc(PIE_IZQ)}</div>'
            f'<div class="mid">{esc(PIE_MID)}</div><div>{n} / 2</div></div>')

h = ['<!doctype html><html lang="es"><head><meta charset="utf-8">',
     f'<title>RK MBI · Planning Instagram {MES} · Neris Studio</title>',
     f"<style>{CSS}</style></head><body>"]

# ---------------- PÁGINA 1
h.append(f'<div class="page">{cabecera(MES, True)}')
h.append('<div class="legend"><span class="lbl">LEYENDA</span>' + "".join(
    f'<span class="chip" style="background:{FMT[f][0]}">{esc(f)}</span>' for f in LEYENDA) + "</div>")
h.append('<div class="cols">' + "".join(
    f'<div><div class="d">{esc(d)}</div><div class="r">{esc(r)}</div></div>'
    for d, r in COLUMNAS) + "</div>")
h.append('<div class="grid">')
for fila in CAL:
    for celda in fila:
        if celda is None:
            h.append('<div class="cell blank"></div>')
        elif len(celda) == 1:
            h.append(f'<div class="cell off"><div class="r1">'
                     f'<span class="badge">{esc(celda[0])}</span></div></div>')
        else:
            num, fmt, hora, titulo = celda
            col, tint = FMT[fmt]
            h.append(f'<div class="cell" style="border-left:1mm solid {col}">'
                     f'<div class="r1"><span class="badge" style="background:{col}">{esc(num)}</span>'
                     f'<span class="ig">IG</span></div>'
                     f'<div class="bar" style="background:{col}"><span>{esc(fmt)}</span>'
                     f'<span class="h">{esc(hora)}</span></div>'
                     f'<div class="bd" style="background:{tint}">{esc(titulo)}</div></div>')
h.append("</div>" + pie(1) + "</div>")

# ---------------- PÁGINA 2
h.append(f'<div class="page">{cabecera("Brief semanal", False)}')
h.append('<div class="wgrid">')
for cod, tema, color, _ in SEMANAS:
    h.append(f'<div class="whead" style="background:{color}"><div class="c">{esc(cod)}</div>'
             f'<div class="s">{esc(tema)}</div></div>')
for fila in range(4):
    for _, _, _, slots in SEMANAS:
        slot = slots[fila]
        if slot is None:
            h.append("<div></div>")
            continue
        fmt, fecha, titulo, desc, cta = slot
        col, tint = FMT[fmt]
        cta_html = (f'<div class="cta" style="color:{col}">→ {esc(cta)}</div>' if cta else "")
        h.append(f'<div class="icard" style="background:{tint};border-left:1mm solid {col}">'
                 f'<div class="top"><span class="f" style="color:{col}">{esc(fmt)}</span>'
                 f'<span class="d">{esc(fecha)}</span></div>'
                 f'<div class="t">{esc(titulo)}</div><div class="x">{esc(desc)}</div>'
                 f"{cta_html}</div>")
h.append("</div>" + pie(2) + "</div>")

h.append("</body></html>")
open(OUT, "w", encoding="utf-8").write("".join(h))
print("html ->", OUT)
