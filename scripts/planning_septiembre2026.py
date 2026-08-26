# -*- coding: utf-8 -*-
"""Planning Instagram de Clàssics En Roig — Septiembre 2026.
Replica la plantilla del planning de agosto 2026 (Neris Studio)."""
import html

OUT = "/tmp/claude-0/-home-user-webs-html/b56cda2c-87b5-591c-8a48-efe3a7e0cb71/scratchpad/planning_sept.html"

MARCA   = "CLASSICS EN · ROIG"
MES     = "Septiembre 2026"
FOCO    = "Planning Instagram · Foco: la temporada alta y las bodas de otoño · Valencia"
PIE_IZQ = "Clàssics En Roig · Valencia · Coches clásicos para bodas · @classicsenroig"
PIE_DER = "Planning Instagram · Septiembre 2026 · Elaborado por Neris Studio · Página {n}"

STATS = [("6", "POSTS"), ("4", "BODAS"), ("9", "STORIES"),
         ("Lun·Jue", "PUBLICAR"), ("Valencia", "ÁREA")]
COLUMNAS = [("LUNES", "FEED"), ("MARTES", "STORY"), ("MIERCOLES", "DESCANSO"),
            ("JUEVES", "BODA"), ("VIERNES", "STORY")]
LEYENDA = ["REEL", "POST", "CARRUSEL", "BODA", "STORY"]

# (dia, formato, hora, titulo, descripcion, cta)   formato None = sin publicación
SEMANAS = [
 ("SEM 01 · 1-4 SEPT", "Empieza la temporada alta", [
  ("Mar 1", "STORY", "10:00", "Septiembre, el mes de las bodas",
   "Varias historias abriendo el mes: septiembre concentra buena parte de las bodas del año y la agenda "
   "se mueve semana a semana.", None),
  ("Mié 2", "POST", "18:00", "La flota, lista para septiembre",
   "Publicación de arranque de mes con los coches ya preparados para la temporada alta.",
   "Consulta disponibilidad para tu fecha."),
  ("Jue 3", "BODA", "18:00", "Boda de la semana al feed",
   "Publicación en el feed de la boda de esa semana, con fotos reales de la pareja.",
   "Cuéntanos tu boda y te asesoramos."),
  ("Vie 4", "STORY", "10:00", "El coche, antes de salir",
   "Behind the scenes corto: limpieza, revisión y últimos detalles la mañana de la boda.", None),
 ]),
 ("SEM 02 · 7-11 SEPT", "Reservar con tiempo", [
  ("Lun 7", "REEL", "18:00", "La llegada, a cámara lenta",
   "Reel del momento de la llegada: el coche parando, la puerta abriéndose y la pareja bajando.",
   "Descúbrelo en el perfil."),
  ("Mar 8", "STORY", "10:00", "¿Con cuánto tiempo se reserva?",
   "Tip. Lo habitual es reservar con ocho o diez meses de margen. Los sábados de otoño son los "
   "primeros en cerrarse.", None),
  ("Jue 10", "BODA", "18:00", "Boda real de la semana",
   "Espacio reservado para la boda de esa semana. Solo imágenes reales de la pareja, sin inventar "
   "nombres ni datos. Adaptar al caso real antes de publicar.",
   "Escríbenos si tienes dudas sobre tu boda."),
  ("Vie 11", "STORY", "10:00", "Fechas libres de otoño",
   "Historias con los fines de semana que siguen disponibles en octubre y noviembre.", None),
 ]),
 ("SEM 03 · 14-18 SEPT", "Las bodas de otoño", [
  ("Lun 14", "POST", "18:00", "La luz de octubre",
   "Por qué las bodas de otoño funcionan tan bien en fotografía: la luz baja antes y favorece los "
   "planos con el coche.", "Cuéntanos la fecha de tu boda."),
  ("Mar 15", "STORY", "10:00", "¿Fotos dentro o fuera del coche? (1/2)",
   "Sticker de pregunta, primera interactiva del mes. Sirve para recoger ideas reales para próximos "
   "contenidos.", None),
  ("Jue 17", "BODA", "18:00", "Boda de otoño en finca",
   "Boda de la semana en finca, aprovechando la llegada al atardecer.",
   "Consulta disponibilidad para tu fecha."),
  ("Vie 18", "STORY", "10:00", "Dato: la hora de la llegada",
   "Dato. El coche llega antes de la hora prevista para dar margen al tráfico y a las fotos previas.", None),
 ]),
 ("SEM 04 · 21-25 SEPT", "Lo que incluye el servicio", [
  ("Lun 21", "CARRUSEL", "18:00", "Qué incluye el servicio",
   "Horas acordadas, chófer, recorrido probado y decoración básica. Y qué se presupuesta aparte, "
   "para que no haya sorpresas. Informativo, no es una encuesta.",
   "Escríbenos y te pasamos presupuesto."),
  ("Mar 22", "STORY", "10:00", "¿Uno o dos coches? (2/2)",
   "Encuesta, segunda y última interactiva del mes, para conocer cómo se plantea la llegada.", None),
  ("Jue 24", "BODA", "18:00", "Dos coches, una misma boda",
   "Boda de la semana en la que la pareja llega por separado. Cómo se organizan los tiempos y "
   "los dos recorridos.", "Cuéntanos cómo es tu boda y te asesoramos."),
  ("Vie 25", "STORY", "10:00", "Resumen de la semana",
   "Repaso del contenido de la semana, en formato resumen — repost del post del lunes.", None),
 ]),
 ("SEM 05 · 28-30 SEPT", "Cierre de septiembre", [
  ("Lun 28", "REEL", "18:00", "Un mes de llegadas",
   "Reel recopilatorio con las llegadas de las bodas del mes.", "Descúbrelo en el perfil."),
  ("Mar 29", "STORY", "10:00", "Lo más visto de septiembre",
   "Repaso de las publicaciones que mejor han funcionado durante el mes.", None),
  ("Mié 30", "CARRUSEL", "18:00", "La agenda de 2027, abierta",
   "Cierre de mes con las fechas de 2027 que ya se pueden reservar, para quien va con tiempo.",
   "Escríbenos y te ayudamos a elegir."),
 ]),
]

NOTAS = [
 ("Bodas reales", "Las publicaciones de los jueves 3, 10, 17 y 24 dependen de que haya boda esa semana. "
                  "Solo imágenes reales de la pareja, con su permiso y el del fotógrafo. Si alguna semana "
                  "no hay boda, se sustituye por contenido de flota."),
 ("Interactivas", "Dos por mes, como en agosto: pregunta el 15 y encuesta el 22. No se acumulan en la "
                  "misma semana."),
 ("Horarios", "Feed y bodas a las 18:00, historias a las 10:00. Se mantiene el patrón de agosto: "
              "lunes y jueves de publicación, miércoles de descanso."),
 ("Material", "Hacen falta fotos de la flota con luz de otoño y vídeo de una llegada para el reel del "
              "día 7. Conviene grabarlo en las bodas de las dos primeras semanas."),
]

# ---- calendario: 5 filas x 5 columnas (lun-vie) ------------------------------
CAL = [
 [None,                                  ("1", "STORY", "10:00", "Septiembre, el mes de las bodas"),
  ("2", "POST", "18:00", "La flota, lista para septiembre"),
  ("3", "BODA", "18:00", "Boda de la semana al feed"),
  ("4", "STORY", "10:00", "El coche, antes de salir")],
 [("7", "REEL", "18:00", "La llegada, a cámara lenta"),
  ("8", "STORY", "10:00", "¿Con cuánto tiempo se reserva?"),
  ("9", None, None, "Sin publicación"),
  ("10", "BODA", "18:00", "Boda real de la semana"),
  ("11", "STORY", "10:00", "Fechas libres de otoño")],
 [("14", "POST", "18:00", "La luz de octubre"),
  ("15", "STORY", "10:00", "¿Fotos dentro o fuera del coche?"),
  ("16", None, None, "Sin publicación"),
  ("17", "BODA", "18:00", "Boda de otoño en finca"),
  ("18", "STORY", "10:00", "Dato: la hora de la llegada")],
 [("21", "CARRUSEL", "18:00", "Qué incluye el servicio"),
  ("22", "STORY", "10:00", "¿Uno o dos coches?"),
  ("23", None, None, "Sin publicación"),
  ("24", "BODA", "18:00", "Dos coches, una misma boda"),
  ("25", "STORY", "10:00", "Resumen de la semana")],
 [("28", "REEL", "18:00", "Un mes de llegadas"),
  ("29", "STORY", "10:00", "Lo más visto de septiembre"),
  ("30", "CARRUSEL", "18:00", "La agenda de 2027, abierta"),
  None, None],
]

def esc(t):
    return html.escape(str(t))

CSS = """
@page { size: A4 landscape; margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin:0; font-family: Helvetica, Arial, sans-serif; color:#2A1A1F; }
.page { width:297mm; height:210mm; position:relative; overflow:hidden;
        page-break-after:always; background:#fff; }
.page:last-child { page-break-after:auto; }

.band { background:#5E2230; color:#fff; padding:7mm 12.5mm 6mm; position:relative; }
.band .marca { font-size:15.5pt; font-weight:bold; letter-spacing:.20em; }
.band .mes { color:#E2CD90; font-size:10pt; font-weight:bold; margin-top:2.6mm; }
.band .foco { font-size:7.6pt; color:#E7D3D6; margin-top:1.2mm; }
.band .agencia { position:absolute; right:12.5mm; top:7.5mm; text-align:right; }
.band .agencia .n { color:#E2CD90; font-size:8.4pt; font-weight:bold; letter-spacing:.08em; }
.band .agencia .s { color:#F0E2E4; font-size:7.4pt; margin-top:1.4mm; }

.body { padding:6mm 12.5mm 0; }

.stats { display:flex; gap:3mm; }
.stat { flex:1; background:#FBF7F2; border:.5pt solid #E8DED6; border-radius:1.6mm;
        text-align:center; padding:3.4mm 1mm; }
.stat .n { font-size:13.5pt; font-weight:bold; color:#5E2230; }
.stat .l { font-size:6.4pt; letter-spacing:.17em; color:#A9A0A1; margin-top:1.3mm; }

.legend { display:flex; align-items:center; gap:2.6mm; margin:3.2mm 0 4mm; }
.legend .lbl { font-size:7pt; font-weight:bold; letter-spacing:.12em; color:#5E2230;
               width:20mm; }
.pill { display:inline-block; padding:1.2mm 0; border-radius:3mm; font-size:6.4pt;
        font-weight:bold; letter-spacing:.11em; text-align:center; min-width:23mm; }
.p-REEL{background:#F4E9EB;color:#875964} .p-POST{background:#EAEFE9;color:#4F6A54}
.p-CARRUSEL{background:#F4EEE2;color:#8E7134} .p-BODA{background:#F7ECEE;color:#A05A66}
.p-STORY{background:#F1ECE6;color:#8A7E7A}
.legend .pill { flex:0 0 auto; min-width:26mm; }

.cols { display:flex; gap:3mm; margin-bottom:2.6mm; }
.col { flex:1; background:#F0E8E1; border-radius:1.4mm; text-align:center; padding:2.2mm 1mm; }
.col .d { font-size:8pt; font-weight:bold; color:#5E2230; letter-spacing:.06em; }
.col .r { font-size:6.3pt; letter-spacing:.15em; color:#A0918F; margin-top:1mm; }

.grid { border:.5pt solid #E8DED6; border-radius:1.4mm; overflow:hidden; }
.grow { display:flex; border-bottom:.5pt solid #E8DED6; }
.grow:last-child { border-bottom:none; }
.gcell { flex:1; border-right:.5pt solid #E8DED6; padding:2.4mm 2.6mm; height:21mm; }
.gcell:last-child { border-right:none; }
.gcell.off { background:#F0E8E1; }
.gcell.empty { background:#fff; }
.gcell .top { display:flex; align-items:baseline; }
.gcell .num { font-size:11pt; font-weight:bold; color:#5E2230; }
.gcell .ig { font-size:5.8pt; color:#B7ABAC; margin-left:1.5mm; letter-spacing:.08em; }
.gcell .mid { display:flex; align-items:center; justify-content:space-between; margin:1.4mm 0 1.6mm; }
.gcell .mid .pill { min-width:19mm; padding:.9mm 0; font-size:5.9pt; }
.gcell .hora { font-size:6.3pt; color:#A9A0A1; }
.gcell .t { font-size:7pt; color:#2A1A1F; line-height:1.3; }
.gcell .nopub { font-size:7pt; color:#A0918F; font-style:italic; margin-top:2.4mm; }

.intro { font-size:7.6pt; color:#8A7E80; font-style:italic; margin-bottom:2.4mm; }
.sem { display:flex; align-items:baseline; gap:6mm; margin:3.6mm 0 2.4mm; }
.sem .c { font-size:9.4pt; font-weight:bold; color:#5E2230; letter-spacing:.03em; min-width:34mm; }
.sem .t { font-size:8pt; color:#8A7E80; font-style:italic; }
.sem:first-of-type { margin-top:0; }

.item { display:flex; border:.5pt solid #E8DED6; border-radius:1.6mm; padding:2.8mm 3mm;
        margin-bottom:2.2mm; align-items:flex-start; }
.item .fecha { width:22mm; flex:0 0 22mm; }
.item .fecha .d { font-size:8pt; font-weight:bold; color:#2A1A1F; }
.item .fecha .h { font-size:6.6pt; color:#A9A0A1; margin-top:1mm; }
.item .badge { width:26mm; flex:0 0 26mm; }
.item .badge .pill { min-width:22mm; }
.item .cuerpo { flex:1; padding-right:5mm; }
.item .cuerpo .t { font-size:8pt; font-weight:bold; color:#5E2230; }
.item .cuerpo .d { font-size:7.2pt; color:#4A3D41; line-height:1.4; margin-top:1.2mm; }
.item .cta { width:62mm; flex:0 0 62mm; font-size:7.1pt; font-style:italic; }
.item .cta.si { color:#C2A55C; }
.item .cta.no { color:#A9A2A3; }

.nota { display:flex; border:.5pt solid #E8DED6; border-radius:1.6mm; padding:3mm 3.2mm;
        margin-bottom:2.4mm; }
.nota .k { width:34mm; flex:0 0 34mm; font-size:8pt; font-weight:bold; color:#5E2230; }
.nota .v { flex:1; font-size:7.2pt; color:#4A3D41; line-height:1.45; }

.foot { position:absolute; left:12.5mm; right:12.5mm; bottom:7mm; display:flex;
        justify-content:space-between; font-size:6.6pt; color:#A9A0A1; }
"""

def band(subtitulo):
    return (f'<div class="band"><div class="marca">{esc(MARCA)}</div>'
            f'<div class="mes">{esc(MES)}</div><div class="foco">{esc(FOCO)}</div>'
            f'<div class="agencia"><div class="n">NERIS STUDIO</div>'
            f'<div class="s">{esc(subtitulo)}</div></div></div>')

def foot(n):
    return (f'<div class="foot"><div>{esc(PIE_IZQ)}</div>'
            f'<div>{esc(PIE_DER.format(n=n))}</div></div>')

def pill(fmt, extra=""):
    return f'<span class="pill p-{fmt}{extra}">{esc(fmt)}</span>'

h = [f'<!doctype html><html lang="es"><head><meta charset="utf-8">',
     f'<title>Clàssics En Roig · Planning Instagram {MES} · Neris Studio</title>',
     f"<style>{CSS}</style></head><body>"]

# ---------------- PÁGINA 1 · CALENDARIO
h.append(f'<div class="page">{band("Calendario del mes")}<div class="body">')
h.append('<div class="stats">' + "".join(
    f'<div class="stat"><div class="n">{esc(n)}</div><div class="l">{esc(l)}</div></div>'
    for n, l in STATS) + "</div>")
h.append('<div class="legend"><div class="lbl">LEYENDA</div>'
         + "".join(pill(f) for f in LEYENDA) + "</div>")
h.append('<div class="cols">' + "".join(
    f'<div class="col"><div class="d">{esc(d)}</div><div class="r">{esc(r)}</div></div>'
    for d, r in COLUMNAS) + "</div>")
h.append('<div class="grid">')
for fila in CAL:
    h.append('<div class="grow">')
    for celda in fila:
        if celda is None:
            h.append('<div class="gcell empty"></div>')
            continue
        num, fmt, hora, titulo = celda
        if fmt is None:
            h.append(f'<div class="gcell off"><div class="top"><span class="num">{esc(num)}</span>'
                     f'<span class="ig">IG</span></div>'
                     f'<div class="nopub">{esc(titulo)}</div></div>')
            continue
        h.append(f'<div class="gcell"><div class="top"><span class="num">{esc(num)}</span>'
                 f'<span class="ig">IG</span></div>'
                 f'<div class="mid">{pill(fmt)}<span class="hora">{esc(hora)}</span></div>'
                 f'<div class="t">{esc(titulo)}</div></div>')
    h.append("</div>")
h.append("</div></div>" + foot(1) + "</div>")

# ---------------- PÁGINAS DE BRIEF
def bloque_semana(cod, tema, items):
    out = [f'<div class="sem"><div class="c">{esc(cod)}</div><div class="t">{esc(tema)}</div></div>']
    for dia, fmt, hora, titulo, desc, cta in items:
        cta_html = (f'<div class="cta si">{esc(cta)}</div>' if cta
                    else '<div class="cta no">Sin CTA — formato informativo</div>')
        out.append(f'<div class="item"><div class="fecha"><div class="d">{esc(dia)}</div>'
                   f'<div class="h">{esc(hora)}</div></div>'
                   f'<div class="badge">{pill(fmt)}</div>'
                   f'<div class="cuerpo"><div class="t">{esc(titulo)}</div>'
                   f'<div class="d">{esc(desc)}</div></div>{cta_html}</div>')
    return "".join(out)

paginas = [(SEMANAS[0:2], "Brief semanal", True),
           (SEMANAS[2:4], "Brief semanal (cont.)", False),
           (SEMANAS[4:5], "Brief semanal (cont.)", False)]
n = 2
for semanas, sub, con_intro in paginas:
    h.append(f'<div class="page">{band(sub)}<div class="body">')
    if con_intro:
        h.append(f'<div class="intro">Ideas, copys y stories — {esc(MES)}</div>')
    for cod, tema, items in semanas:
        h.append(bloque_semana(cod, tema, items))
    if n == 4:
        h.append('<div class="sem"><div class="c">NOTAS DEL MES</div>'
                 '<div class="t">Antes de publicar</div></div>')
        for k, v in NOTAS:
            h.append(f'<div class="nota"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>')
    h.append("</div>" + foot(n) + "</div>")
    n += 1

h.append("</body></html>")
open(OUT, "w", encoding="utf-8").write("".join(h))
print("html ->", OUT)
