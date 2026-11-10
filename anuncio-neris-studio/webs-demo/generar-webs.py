import sys,os
PX=sys.argv[1].split(','); OUT=sys.argv[2]
def img(i):
    for d in PX:
        p=f"{d}/{i}.jpg"
        if os.path.exists(p): return f"file://{p}"
    raise SystemExit(f"missing {i}")
def bgi(i,pos='center'): return f"background-image:url({img(i)});background-position:{pos}"

def nav(s,light=False):
    links=''.join(f'<a>{n}</a>' for n in s['nav'])
    return f'<nav class="{"lt" if light else ""}"><b class="logo">{s["name"]}</b><div class="links">{links}</div><a class="pillb">{s["cta"]}</a></nav>'
def heroCard(s,photo,h1,cap,pos='center'):
    links=''.join(f'<a>{n}</a>' for n in s['nav'])
    return f'''<header class="heroCard"><div class="hc" style="{bgi(photo,pos)}"><div class="shade"></div>
    <div class="top"><b class="lg">{s["name"]}</b><div class="links">{links}</div><a class="pillw">{s["cta"]}</a></div>
    <h1>{h1}</h1><div class="cap"><p>{cap}</p><a class="pillw">{s["cta"]} →</a></div></div></header>'''
def heroSplit(s,photo,tag,h1,p,pos='center'):
    return nav(s)+f'''<header class="heroSplit"><div><span class="lab">{tag}</span><h1>{h1}</h1><p>{p}</p><div class="btns"><a class="pilld">{s["cta"]}</a><a class="pillo">Ver más</a></div></div><div class="hp" style="{bgi(photo,pos)}"><span>{s["name"]} — 2026</span></div></header>'''
def heroCenter(s,photo,tag,h1,p,pos='center'):
    return nav(s)+f'''<header class="heroCenter"><span class="lab">{tag}</span><h1>{h1}</h1><p>{p}</p><div class="btns"><a class="pilld">{s["cta"]}</a><a class="pillo">Ver más</a></div><div class="hp" style="{bgi(photo,pos)}"></div></header>'''
def splitDark(photo,label,items,cap,pos='center',flip=False):
    li=''.join(f'<li class="{"on" if k==len(items)-1 else ""}">{x}</li>' for k,x in enumerate(items))
    return f'''<section class="splitDark {"flip" if flip else ""}"><div class="ph" style="{bgi(photo,pos)}"><p>{cap}</p></div><div class="dk"><span class="lab lw">{label}</span><ul>{li}</ul></div></section>'''
def testimonials(title,items):
    cards=''.join(f'''<div class="tp" style="{bgi(ph,'center top')}"><span><b>{n}</b>{r}</span></div><div class="tq"><q>{q}</q><div class="st"><div><b>{a}</b><i>{al}</i></div><div><b>{b}</b><i>{bl}</i></div><a class="pillg">Leer caso</a></div></div>''' for ph,q,n,r,a,al,b,bl in items)
    return f'''<section class="testi"><h2>{title}</h2><div class="trow">{cards}</div><div class="arr"><a class="on">←</a><a>→</a></div></section>'''
def rows(label,title,items):
    r=''.join(f'''<div class="r"><span>0{k+1}</span><h3>{t}</h3><p>{d}</p><div class="th" style="{bgi(ph)}"></div></div>''' for k,(t,d,ph) in enumerate(items))
    return f'''<section class="rows"><div class="rh"><span class="lab">{label}</span><h2>{title}</h2></div>{r}</section>'''
def gallery(label,title,items):
    g=''.join(f'<div style="{bgi(ph)}"><span>{c}</span></div>' for ph,c in items)
    return f'''<section class="gal"><div class="rh"><span class="lab">{label}</span><h2>{title}</h2></div><div class="g">{g}</div></section>'''
def statement(label,text):
    return f'<section class="state"><span class="lab">{label}</span><p>{text}</p></section>'
def stats(items):
    return '<section class="stats">'+''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in items)+'</section>'
def cta(s,h,p):
    return f'''<footer><span class="lab lw">Contacto</span><h2>{h}</h2><p>{p}</p><a class="pillw big">{s["cta"]} →</a><div class="fc"><b>{s["name"]}</b><span>Instagram</span><span>LinkedIn</span><span>Aviso legal</span><span>© 2026</span></div></footer>'''

SITES=[
 dict(id='consultoria',name='Norte & Co',cta='Hablemos',nav=['Servicios','Equipo','Casos','Recursos'],serif='Instrument Serif',sans='Inter Tight',bg='#dfe2e1',ink='#1b2220',dark='#1e2523',acc='#1e2523',card='#f4f5f3',
  body=lambda s: heroCard(s,3760263,'Personas que hacen<br>crecer tu empresa.','Consultoría de talento y cultura para equipos que quieren trabajar mejor.','center 30%')
   +statement('Qué hacemos','Ayudamos a empresas en crecimiento a <em>decidir mejor</em>, ordenar sus equipos y construir una cultura que retiene talento.')
   +testimonials('Lo que cambia cuando trabajamos juntos',[(3777943,'Antes, cada decisión rebotaba entre equipos. Nos ayudaron a definir cómo se decide.','Daniel Ortega','Director de operaciones','+34%','Decisiones más rápidas','−42%','Rotación anual'),(3769021,'Por fin tenemos un proceso de selección claro y una bienvenida que funciona.','Paula Méndez','Responsable de personas','×2','Candidaturas válidas','21 días','Para cubrir vacantes')])
   +splitDark(6626903,'A quién acompañamos',['Empresas en crecimiento','Fundadores','Equipos de personas','Equipos híbridos','Empresas tecnológicas'],'Estructuras que evolucionan con el equipo, sin perder el foco en las personas.','center 20%')
   +rows('Servicios','Un acompañamiento completo',[('Selección y talento','Procesos claros para encontrar a quien encaja de verdad.',3184291),('Cultura y valores','Definimos cómo trabajáis y cómo lo contáis.',3182812),('Estructura y roles','Organigramas que se entienden y se usan.',7688336)])
   +stats([('120+','empresas acompañadas'),('12','años de experiencia'),('94%','renuevan con nosotros'),('8','países')])
   +cta(s,'Empieza por una conversación.','Cuéntanos en qué punto está tu equipo y te proponemos un primer paso.')),
 dict(id='interiorismo',name='Estudio Alba',cta='Pedir propuesta',nav=['Proyectos','Estudio','Proceso','Contacto'],serif='Instrument Serif',sans='DM Sans',bg='#efece6',ink='#24211d',dark='#26221d',acc='#8a5a3c',card='#faf8f4',
  body=lambda s: heroSplit(s,1866149,'Interiorismo · València','Espacios serenos,<br><em>hechos para vivirlos.</em>','Diseñamos viviendas y locales con materiales honestos, luz natural y atención al detalle.')
   +stats([('86','proyectos entregados'),('14','años de estudio'),('100%','llave en mano'),('3','premios de diseño')])
   +gallery('Proyectos','Selección reciente',[(4352247,'Casa Turia — 2026'),(6782567,'Ático Cabanyal — 2025'),(2440471,'Loft Ruzafa — 2025')])
   +splitDark(1090638,'Cómo trabajamos',['Escucha','Concepto','Materiales','Obra','Entrega'],'Un único equipo desde el primer boceto hasta el último detalle.',flip=True)
   +rows('Servicios','Del plano a la llave',[('Vivienda','Reformas integrales y obra nueva.',6312362),('Locales','Espacios comerciales con identidad.',1350789),('Mobiliario a medida','Piezas diseñadas para cada estancia.',1743227)])
   +statement('Filosofía','Creemos en casas que <em>envejecen bien</em>: menos objetos, mejores materiales y una luz que cambia a lo largo del día.')
   +cta(s,'¿Hablamos de tu espacio?','Primera visita y anteproyecto sin compromiso.')),
 dict(id='pilates',name='Forma Estudio',cta='Reservar clase',nav=['Clases','Horarios','Equipo','Tarifas'],serif='Newsreader',sans='Inter Tight',bg='#e8e6df',ink='#23261f',dark='#2a2f28',acc='#5d6a4c',card='#f6f5f0',
  body=lambda s: heroCard(s,8436587,'Muévete con calma.<br>Vive con fuerza.','Pilates y yoga en grupos reducidos. Tu primera clase es gratuita.','center 40%')
   +rows('Clases','Encuentra tu ritmo',[('Pilates reformer','Fuerza profunda y postura, con máquina.',6111616),('Yoga vinyasa','Movimiento fluido guiado por la respiración.',3822906),('Suelo y movilidad','Para empezar o recuperar sin prisa.',4498606)])
   +splitDark(4056723,'Para quién',['Si empiezas de cero','Si pasas el día sentado','Si vuelves tras una lesión','Si buscas constancia','Si quieres sentirte mejor'],'Máximo ocho personas por sesión. Corregimos cada postura.','center')
   +testimonials('Historias del estudio',[(3394658,'En tres meses mi espalda ha cambiado por completo. Es mi hora favorita de la semana.','Elena Garrido','Alumna desde 2024','8','Personas por clase','32','Clases semanales'),(2379004,'Llegué con dolor lumbar y sin constancia. Ahora no me salto ni una.','Marc Soler','Alumno desde 2025','6','Profesores titulados','4,9','Valoración media')])
   +statement('El estudio','Un espacio luminoso y tranquilo en el centro, pensado para que <em>desconectes al entrar</em> y salgas con más energía.')
   +cta(s,'Tu primera clase, gratis.','Reserva plaza en un minuto desde el móvil.')),
 dict(id='restaurante',name='Casa Olmo',cta='Reservar mesa',nav=['Carta','Bodega','El espacio','Eventos'],serif='Instrument Serif',sans='DM Sans',bg='#ece7df',ink='#1f1b17',dark='#1d1916',acc='#9a4a2a',card='#f8f5ef',
  body=lambda s: heroCenter(s,941861,'Cocina de mercado · Desde 2014','Fuego lento,<br><em>producto de temporada.</em>','Una carta corta que cambia cada semana, brasa de encina y una bodega de pequeños productores.','center 60%')
   +splitDark(262978,'La carta',['Entrantes','Brasa','Arroces','Postres','Menú degustación'],'Siete pases que recorren la temporada. De martes a sábado.','center')
   +gallery('El espacio','Una sala para quedarse',[(67468,'Sala principal'),(696218,'Mesa compartida'),(2253643,'Barra y cocina vista')])
   +statement('Filosofía','Compramos cada mañana en el mercado y cocinamos <em>sin esconder el producto</em>. Lo demás es tiempo y fuego.')
   +rows('Experiencias','Más que una cena',[('Menú degustación','Siete pases y maridaje opcional.',1279330),('Eventos privados','La sala entera para tu celebración.',2788792),('Mesa del chef','Seis asientos frente a la cocina.',958545)])
   +stats([('4,8','valoración media'),('12','años cocinando'),('40','referencias en bodega'),('7','pases')])
   +cta(s,'¿Mesa para esta semana?','Reservas online con confirmación inmediata.')),
 dict(id='clinica',name='Clínica Sera',cta='Pedir cita',nav=['Tratamientos','Equipo','Tecnología','Contacto'],serif='Newsreader',sans='DM Sans',bg='#eeeae6',ink='#2a2422',dark='#2d2623',acc='#a8705a',card='#faf7f4',
  body=lambda s: heroSplit(s,3985329,'Dermatología y estética','El cuidado de tu piel,<br><em>con criterio médico.</em>','Tratamientos personalizados, tecnología avanzada y un equipo que te explica cada paso.','center')
   +statement('Nuestra forma de trabajar','Cada piel es distinta. Por eso empezamos siempre por <em>un diagnóstico</em> y no por un tratamiento.')
   +rows('Tratamientos','Qué podemos hacer por ti',[('Dermatología clínica','Diagnóstico y seguimiento de la piel.',3738349),('Medicina estética','Resultados naturales, sin excesos.',2811087),('Cuidado facial','Protocolos adaptados a tu piel.',4041392)])
   +splitDark(3586798,'Primera visita',['Escuchamos','Analizamos tu piel','Diseñamos el plan','Tratamos','Acompañamos'],'Una hora contigo antes de recomendarte nada.','center 20%',flip=True)
   +testimonials('Pacientes que confían en nosotros',[(1065084,'Me explicaron todo con calma y el resultado es justo lo que buscaba: natural.','Laura Vidal','Paciente desde 2023','+5.000','Pacientes atendidos','15','Años de experiencia'),(3757942,'Por fin una clínica que no intenta venderte de más. Salgo siempre tranquila.','Marta Roca','Paciente desde 2024','98%','Nos recomiendan','1 h','Primera consulta')])
   +cta(s,'Tu piel, en buenas manos.','Primera valoración sin compromiso.')),
]
CSS='''
*{box-sizing:border-box;margin:0;padding:0}
body{width:1440px;background:var(--bg);color:var(--ink);font-family:var(--sans),sans-serif;font-size:17px;line-height:1.5;-webkit-font-smoothing:antialiased}
[style*="background-image"]{background-size:cover;filter:saturate(1.18) contrast(1.07) brightness(1.04)}
h1,h2,h3,.state p,.splitDark li,.stats b,.tq .st b{font-family:var(--serif),serif;font-weight:400;letter-spacing:-.015em}
em{font-style:italic}
.lab{display:inline-block;align-self:flex-start;font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;padding:8px 14px;border-radius:99px;border:1px solid color-mix(in srgb,var(--ink) 25%,transparent)}
.lab.lw{border-color:#ffffff40;color:#fff}
nav{display:flex;align-items:center;padding:28px 48px}.logo{font-size:22px;font-weight:600;letter-spacing:-.02em}
.links{display:flex;gap:34px;margin:0 auto;font-size:15px;font-weight:500}
.pillb,.pilld{background:var(--ink);color:var(--bg);padding:12px 22px;border-radius:99px;font-size:15px;font-weight:500}
.pillo{padding:12px 22px;border-radius:99px;font-size:15px;font-weight:500;border:1px solid color-mix(in srgb,var(--ink) 30%,transparent)}
.pillw{background:#fff;color:#111;padding:12px 22px;border-radius:99px;font-size:15px;font-weight:500}.pillw.big{display:inline-block;font-size:18px;padding:18px 34px}
.pillg{background:#eceeec;color:#222;padding:10px 18px;border-radius:99px;font-size:14px;font-weight:500;margin-left:auto;align-self:center}
.btns{display:flex;gap:12px;margin-top:38px}
.heroCard{padding:20px}.hc{position:relative;height:840px;border-radius:30px;overflow:hidden;color:#fff;filter:none!important}
.hc .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.26),rgba(0,0,0,0) 28%,rgba(0,0,0,0) 55%,rgba(0,0,0,.5))}
.hc .top{position:absolute;left:24px;right:24px;top:24px;display:flex;align-items:center}.hc .lg{background:#fff;color:#111;padding:12px 20px;border-radius:14px;font-size:20px;font-weight:600;letter-spacing:-.02em}
.hc h1{position:absolute;left:44px;bottom:48px;font-size:96px;line-height:.98}
.hc .cap{position:absolute;right:44px;bottom:52px;width:320px;font-size:16px}.hc .cap p{margin-bottom:20px;opacity:.92}
.heroSplit{display:grid;grid-template-columns:1fr 600px;gap:70px;padding:40px 48px 80px;align-items:end}
.heroSplit h1{font-size:98px;line-height:.98;margin-top:34px}.heroSplit p,.heroCenter p{font-size:19px;max-width:470px;margin-top:30px;opacity:.75}
.heroSplit .hp{height:720px;border-radius:30px;position:relative}.heroSplit .hp span{position:absolute;left:24px;bottom:22px;color:#fff;font-size:14px}
.heroCenter{text-align:center;padding:60px 48px 0}.heroCenter h1{font-size:108px;line-height:.98;margin-top:30px}.heroCenter p{margin:30px auto 0}.heroCenter .btns{justify-content:center}
.heroCenter .hp{height:660px;border-radius:30px;margin-top:70px}
.state{padding:150px 220px;text-align:center}.state p{font-size:58px;line-height:1.14;margin-top:34px}
.testi{padding:110px 48px 90px;background:color-mix(in srgb,var(--bg) 82%,#8a9390)}.testi h2{font-size:60px;text-align:center;margin-bottom:64px}
.trow{display:grid;grid-template-columns:270px 1fr 270px 1fr;gap:16px}
.tp{height:440px;border-radius:24px;position:relative}.tp span{position:absolute;left:18px;bottom:16px;color:#fff;font-size:13px;line-height:1.4}.tp b{display:block;font-weight:600}
.tq{background:var(--card);border-radius:24px;padding:30px;display:flex;flex-direction:column;justify-content:space-between;height:440px}
.tq q{font-size:27px;line-height:1.22;font-weight:500;letter-spacing:-.02em;quotes:"“" "”"}
.tq .st{display:flex;gap:34px}.tq .st b{display:block;font-size:34px}.tq .st i{font-style:normal;font-size:13px;opacity:.6}
.arr{display:flex;gap:10px;justify-content:center;margin-top:44px}.arr a{width:54px;height:54px;border-radius:18px;background:var(--card);display:grid;place-items:center;font-size:20px}.arr .on{background:var(--dark);color:#fff}
.splitDark{display:grid;grid-template-columns:46% 54%;height:860px;background:var(--dark);color:#fff}.splitDark.flip{grid-template-columns:54% 46%}.splitDark.flip .ph{order:2}
.splitDark .ph{position:relative}.splitDark .ph p{position:absolute;left:40px;bottom:36px;width:330px;font-size:15px;line-height:1.45}
.splitDark .dk{padding:90px 80px;display:flex;flex-direction:column;justify-content:flex-end;filter:none}
.splitDark ul{list-style:none;margin-top:36px}.splitDark li{font-size:66px;line-height:1.12;color:#ffffff4d}.splitDark li.on{color:#fff}
.rows,.gal{padding:120px 48px}.rh{display:flex;align-items:end;justify-content:space-between;margin-bottom:56px}.rh h2{font-size:68px;line-height:1}
.r{display:grid;grid-template-columns:90px 1fr 380px 230px;align-items:center;gap:30px;padding:30px 0;border-top:1px solid color-mix(in srgb,var(--ink) 16%,transparent)}
.r span{font-size:14px;opacity:.5}.r h3{font-size:46px}.r p{font-size:16px;opacity:.7}.th{height:140px;border-radius:16px}
.g{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px}.g div{height:620px;border-radius:26px;position:relative}.g div:nth-child(2){height:540px;margin-top:80px}.g span{position:absolute;left:22px;bottom:20px;color:#fff;font-size:15px;font-weight:500;text-shadow:0 1px 12px #0008}
.stats{display:grid;grid-template-columns:repeat(4,1fr);margin:0 48px;border-top:1px solid color-mix(in srgb,var(--ink) 16%,transparent);border-bottom:1px solid color-mix(in srgb,var(--ink) 16%,transparent)}
.stats div{padding:52px 30px;border-left:1px solid color-mix(in srgb,var(--ink) 16%,transparent)}.stats div:first-child{border:0;padding-left:0}.stats b{display:block;font-size:84px;line-height:1}.stats span{font-size:15px;opacity:.65}
footer{background:var(--dark);color:#fff;padding:110px 48px 40px;margin-top:0}footer h2{font-size:128px;line-height:.98;margin:34px 0 26px;max-width:1100px}footer p{font-size:19px;opacity:.7;margin-bottom:40px}
.fc{display:flex;gap:40px;margin-top:120px;padding-top:28px;border-top:1px solid #ffffff26;font-size:14px;opacity:.8}.fc b{margin-right:auto;font-size:18px}
'''
for s in SITES:
    fam='&'.join(f"family={f.replace(' ','+')}:ital,wght@0,400;0,500;0,600;1,400" if f not in('Instrument Serif',) else "family=Instrument+Serif:ital@0;1" for f in (s['serif'],s['sans']))
    html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?{fam}&display=block" rel="stylesheet">
<style>:root{{--bg:{s['bg']};--ink:{s['ink']};--dark:{s['dark']};--acc:{s['acc']};--card:{s['card']};--serif:"{s['serif']}";--sans:"{s['sans']}"}}{CSS}</style></head><body>{s['body'](s)}</body></html>'''
    open(f"{OUT}/{s['id']}.html",'w').write(html)
print(' '.join(s['id'] for s in SITES))
