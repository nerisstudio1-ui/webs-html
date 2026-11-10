import json,os,sys
PX=sys.argv[1]; OUT=sys.argv[2]
def img(i): return f"file://{PX}/{i}.jpg"
SITES=[
 dict(id='restaurante',name='Brasa Nueve',font='Outfit',hero='A',bg='#f7f3ec',ink='#1c1814',acc='#c8502d',soft='#efe6d8',dark='#1c1814',rad=6,
  nav=['Carta','Reservas','El local','Contacto'],cta='Reservar mesa',tag='Cocina de brasa · València',
  h1='Fuego lento,<br>producto de mercado.',sub='Cocina mediterránea a la brasa en el corazón de Ruzafa. Abierto de martes a domingo.',
  heroimg=262978,stats=[('4,8','en reseñas'),('12','años cocinando'),('100%','producto local')],
  sect='Nuestra carta',cards=[(1279330,'Pastas frescas','Hechas cada mañana en casa.','desde 14 €'),(958545,'Para compartir','Entrantes pensados para el centro de la mesa.','desde 9 €'),(1640777,'De la huerta','Verduras de temporada a la brasa.','desde 11 €')],
  about=(67468,'Un local para quedarse','Una sala luminosa, mesas amplias y una cocina abierta donde todo pasa delante de ti.',['Menú de mediodía entre semana','Terraza cubierta todo el año','Grupos y celebraciones']),
  gal=[941861,696218,1267320,708587],quote=('La mejor brasa de la ciudad, y un trato que hace que vuelvas.','Lucía M.'),band='¿Mesa para esta semana?'),
 dict(id='estetica',name='Lúa Estética',font='Plus Jakarta Sans',hero='B',bg='#fbf6f3',ink='#2a2422',acc='#b9745f',soft='#f3e4dc',dark='#3a2c28',rad=28,
  nav=['Tratamientos','Bonos','Centro','Contacto'],cta='Pedir cita',tag='Centro de estética avanzada',
  h1='Tu piel, cuidada<br>con calma.',sub='Tratamientos faciales y corporales personalizados. Primera valoración gratuita.',
  heroimg=3757942,stats=[('+2.000','clientas'),('15','tratamientos'),('9 años','de experiencia')],
  sect='Tratamientos destacados',cards=[(3985329,'Limpieza facial profunda','Piel luminosa desde la primera sesión.','60 min · 55 €'),(3997989,'Masaje relajante','Descarga tensión de cuello y espalda.','45 min · 45 €'),(4041392,'Ritual de aceites','Hidratación intensa con cosmética natural.','75 min · 70 €')],
  about=(3738349,'Un espacio solo para ti','Cabinas individuales, cosmética profesional y un equipo titulado que te asesora sin prisas.',['Diagnóstico de piel personalizado','Bonos de 5 y 10 sesiones','Cita online en 1 minuto']),
  gal=[4041392,3065209,3993449,415829],quote=('Salgo siempre como nueva. Profesionales y muy atentas.','Marta R.'),band='Reserva tu primera valoración gratuita'),
 dict(id='inmobiliaria',name='Habita Norte',font='Manrope',hero='A',bg='#f5f6f4',ink='#14201b',acc='#1f6f54',soft='#e4ebe6',dark='#14201b',rad=14,
  nav=['Comprar','Alquilar','Vender','Contacto'],cta='Valorar mi casa',tag='Inmobiliaria · Valencia y área metropolitana',
  h1='Encuentra la casa<br>donde quieres vivir.',sub='Más de 300 viviendas seleccionadas y un equipo que te acompaña de la primera visita a la firma.',
  heroimg=323780,stats=[('320','viviendas activas'),('45 días','venta media'),('98%','clientes satisfechos')],
  sect='Viviendas destacadas',cards=[(1571460,'Ático con terraza · Ruzafa','3 hab · 2 baños · 128 m²','385.000 €'),(1396122,'Chalet independiente · La Eliana','4 hab · 3 baños · 240 m²','540.000 €'),(1457842,'Piso reformado · Benimaclet','2 hab · 1 baño · 82 m²','219.000 €')],
  about=(3184465,'Vender bien empieza por una buena valoración','Analizamos tu vivienda, preparamos el reportaje y filtramos a los compradores por ti.',['Valoración gratuita en 24 h','Reportaje fotográfico profesional','Gestión de hipoteca y notaría']),
  gal=[276724,271624,6585760,1080721],quote=('Vendimos en un mes y sin preocuparnos de nada.','Carlos y Ana'),band='¿Cuánto vale tu casa hoy?'),
 dict(id='yoga',name='Núcleo Studio',font='DM Sans',hero='C',bg='#f6f5f0',ink='#1d1f1a',acc='#5b6b3f',soft='#e8e9dc',dark='#23261d',rad=22,
  nav=['Clases','Horarios','Tarifas','Contacto'],cta='Clase de prueba',tag='Yoga · Pilates · Movimiento',
  h1='Muévete mejor.<br>Vive con más energía.',sub='Grupos reducidos de máximo 8 personas. Tu primera clase es gratis.',
  heroimg=4056723,stats=[('8','personas por clase'),('32','clases semanales'),('6','profesores')],
  sect='Nuestras clases',cards=[(3822906,'Yoga Vinyasa','Fuerza y flexibilidad en movimiento.','Todos los niveles'),(4498606,'Pilates suelo','Core fuerte y espalda sana.','Iniciación'),(841130,'Fuerza funcional','Entrena con técnica y sin lesiones.','Intermedio')],
  about=(416778,'Entrena acompañado','Profesores titulados que corrigen tu postura en cada sesión y adaptan los ejercicios a ti.',['Bono mensual sin permanencia','Reserva de plaza desde el móvil','Clases de mañana, mediodía y tarde']),
  gal=[1552242,3822906,4498606,4056723],quote=('En tres meses mi espalda ha cambiado por completo.','Elena G.'),band='Prueba una clase gratis esta semana'),
 dict(id='cafe',name='Tostado Café',font='Poppins',hero='B',bg='#f8f4ee',ink='#231a14',acc='#a35b2b',soft='#efe3d3',dark='#231a14',rad=18,
  nav=['Carta','Café de origen','Eventos','Contacto'],cta='Ver la carta',tag='Café de especialidad · Brunch',
  h1='Café de verdad,<br>tostado aquí.',sub='Desayunos, brunch y café de origen tostado cada semana en nuestro obrador.',
  heroimg=302899,stats=[('7','orígenes de café'),('8:00','abrimos cada día'),('4,9','en reseñas')],
  sect='Lo más pedido',cards=[(1126728,'Brunch para dos','Tabla de dulces, salados y dos cafés.','24 €'),(312418,'Flat white','Doble espresso y leche texturizada.','2,80 €'),(1855214,'Bollería del día','Horneada cada mañana.','desde 2 €')],
  about=(2788792,'Un sitio para quedarse','Mesas compartidas, wifi y buena música. Ven a trabajar, a leer o a ponerte al día.',['Café en grano para llevar','Leches vegetales sin coste','Reservas para grupos']),
  gal=[2253643,1126728,302899,312418],quote=('El mejor flat white del barrio, sin discusión.','Pablo S.'),band='Te esperamos con el café recién hecho'),
 dict(id='dental',name='Clínica Dental Sonría',font='Inter',hero='C',bg='#f4f8fb',ink='#10222e',acc='#1a7fc1',soft='#e0edf5',dark='#10222e',rad=20,
  nav=['Tratamientos','Equipo','Financiación','Contacto'],cta='Pedir cita',tag='Odontología general y estética',
  h1='Tu mejor sonrisa<br>empieza aquí.',sub='Primera visita y diagnóstico gratuitos. Financiación hasta 24 meses sin intereses.',
  heroimg=3845810,stats=[('+5.000','pacientes'),('20 años','de experiencia'),('24 h','urgencias')],
  sect='Tratamientos',cards=[(305568,'Implantes dentales','Recupera tu sonrisa con tecnología 3D.','Estudio gratuito'),(4047186,'Ortodoncia invisible','Alinea tus dientes sin brackets.','desde 59 €/mes'),(774909,'Blanqueamiento','Resultados visibles en una sesión.','199 €')],
  about=(2182970,'Un equipo que te explica todo','Te contamos cada paso del tratamiento con claridad y un presupuesto cerrado desde el primer día.',['Presupuesto sin compromiso','Sedación consciente disponible','Revisiones anuales incluidas']),
  gal=[305568,1239291,220453,3845810],quote=('Tenía pánico al dentista y aquí me lo han quitado.','Javier L.'),band='Pide tu primera visita gratuita'),
]
def page(s):
    r=s['rad']
    nav=''.join(f'<a>{n}</a>' for n in s['nav'])
    stats=''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in s['stats'])
    cards=''.join(f'<article><div class="ph" style="background-image:url({img(i)})"></div><div class="cb"><h3>{t}</h3><p>{d}</p><div class="row"><strong>{p}</strong><em>Ver más →</em></div></div></article>' for i,t,d,p in s['cards'])
    ai,at,ad,al=s['about']
    lis=''.join(f'<li><i></i>{x}</li>' for x in al)
    gal=''.join(f'<div style="background-image:url({img(i)})"></div>' for i in s['gal'])
    q,qa=s['quote']
    if s['hero']=='A':
        hero=f'''<header class="heroA" style="background-image:linear-gradient(90deg,rgba(0,0,0,.72),rgba(0,0,0,.25) 65%,rgba(0,0,0,.1)),url({img(s['heroimg'])})">
        <nav class="light"><b class="logo">{s['name']}</b><div class="links">{nav}</div><a class="btn">{s['cta']}</a></nav>
        <div class="ht"><span class="tag">{s['tag']}</span><h1>{s['h1']}</h1><p>{s['sub']}</p><div class="btns"><a class="btn big">{s['cta']}</a><a class="btn big ghost">Saber más</a></div></div></header>'''
    elif s['hero']=='B':
        hero=f'''<nav><b class="logo">{s['name']}</b><div class="links">{nav}</div><a class="btn">{s['cta']}</a></nav>
        <header class="heroB"><div class="ht"><span class="tag">{s['tag']}</span><h1>{s['h1']}</h1><p>{s['sub']}</p><div class="btns"><a class="btn big">{s['cta']}</a><a class="btn big ghost">Saber más</a></div>
        <div class="rev">★★★★★ <span>Más de 200 reseñas en Google</span></div></div><div class="hp" style="background-image:url({img(s['heroimg'])})"></div></header>'''
    else:
        hero=f'''<nav><b class="logo">{s['name']}</b><div class="links">{nav}</div><a class="btn">{s['cta']}</a></nav>
        <header class="heroC"><span class="tag">{s['tag']}</span><h1>{s['h1']}</h1><p>{s['sub']}</p><div class="btns"><a class="btn big">{s['cta']}</a><a class="btn big ghost">Saber más</a></div>
        <div class="hp" style="background-image:url({img(s['heroimg'])})"></div></header>'''
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family={s['font'].replace(' ','+')}:wght@400;500;600;700;800&display=block" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1440px;background:{s['bg']};color:{s['ink']};font-family:"{s['font']}",sans-serif;font-size:19px;line-height:1.5}}
a{{cursor:pointer}}
nav{{display:flex;align-items:center;gap:40px;padding:30px 80px}}
nav .logo{{font-size:28px;font-weight:800;letter-spacing:-.02em}}
nav .links{{display:flex;gap:38px;margin-left:auto;font-weight:500;font-size:18px}}
nav.light{{color:#fff}}
.btn{{display:inline-block;background:{s['acc']};color:#fff;font-weight:700;font-size:17px;padding:15px 28px;border-radius:{max(r,8)}px}}
.btn.big{{font-size:20px;padding:20px 36px}}
.btn.ghost{{background:transparent;color:inherit;box-shadow:inset 0 0 0 2px currentColor}}
.tag{{display:inline-block;font-size:15px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{s['acc']};margin-bottom:26px}}
h1{{font-size:92px;line-height:1.02;font-weight:800;letter-spacing:-.035em}}
h2{{font-size:56px;line-height:1.08;font-weight:800;letter-spacing:-.03em}}
.btns{{display:flex;gap:16px;margin-top:40px}}
.heroA{{height:900px;background-size:cover;background-position:center;color:#fff}}
.heroA .ht{{padding:130px 80px 0;max-width:900px}} .heroA .tag{{color:#fff;opacity:.9}}
.heroA p,.heroB p,.heroC p{{font-size:24px;margin-top:28px;max-width:620px;opacity:.86}}
.heroB{{display:grid;grid-template-columns:1fr 1fr;gap:60px;padding:50px 80px 90px;align-items:center}}
.heroB .hp{{height:720px;border-radius:{r*2}px;background-size:cover;background-position:center}}
.rev{{margin-top:44px;color:{s['acc']};font-size:22px;letter-spacing:.1em}} .rev span{{color:{s['ink']};font-size:17px;letter-spacing:0;opacity:.7;margin-left:10px}}
.heroC{{text-align:center;padding:70px 80px 0}} .heroC p{{margin-left:auto;margin-right:auto}} .heroC .btns{{justify-content:center}}
.heroC .hp{{height:640px;margin-top:70px;border-radius:{r*2}px;background-size:cover;background-position:center}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);margin:0 80px;padding:64px 0;border-bottom:2px solid {s['soft']}}}
.stats div{{text-align:center}} .stats b{{display:block;font-size:66px;font-weight:800;letter-spacing:-.03em;color:{s['acc']};line-height:1}} .stats span{{font-size:19px;opacity:.75;font-weight:500}}
section{{padding:100px 80px}}
.head{{display:flex;align-items:end;justify-content:space-between;margin-bottom:50px}} .head a{{font-weight:700;color:{s['acc']};font-size:20px}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}}
article{{background:#fff;border-radius:{r}px;overflow:hidden;box-shadow:0 14px 40px rgba(0,0,0,.07)}}
.ph{{height:300px;background-size:cover;background-position:center}}
.cb{{padding:28px}} h3{{font-size:26px;font-weight:700;letter-spacing:-.01em}} .cb p{{opacity:.7;margin-top:6px}}
.row{{display:flex;justify-content:space-between;align-items:center;margin-top:22px;padding-top:20px;border-top:2px solid {s['soft']}}} .row strong{{font-size:22px}} .row em{{font-style:normal;font-weight:700;color:{s['acc']}}}
.about{{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;background:{s['soft']}}}
.about .ap{{height:620px;border-radius:{r*2}px;background-size:cover;background-position:center}}
.about p{{font-size:22px;margin-top:24px;opacity:.8}} ul{{list-style:none;margin:34px 0 40px}} li{{display:flex;align-items:center;gap:16px;font-size:21px;font-weight:600;padding:14px 0;border-bottom:2px solid rgba(0,0,0,.07)}}
li i{{width:26px;height:26px;border-radius:50%;background:{s['acc']};flex:none;position:relative}} li i:after{{content:"";position:absolute;left:8px;top:6px;width:7px;height:11px;border:solid #fff;border-width:0 3px 3px 0;transform:rotate(45deg)}}
.gal{{display:grid;grid-template-columns:1.4fr 1fr 1fr;grid-template-rows:300px 300px;gap:20px}} .gal div{{border-radius:{r}px;background-size:cover;background-position:center}} .gal div:first-child{{grid-row:span 2}} .gal div:last-child{{grid-column:span 2}}
.quote{{background:{s['dark']};color:#fff;text-align:center;padding:110px 200px}} .quote q{{display:block;font-size:50px;font-weight:700;line-height:1.2;letter-spacing:-.02em;quotes:"“" "”"}} .quote span{{display:block;margin-top:30px;opacity:.7;font-size:20px}} .quote .st{{color:#f5b942;font-size:28px;letter-spacing:.2em;margin-bottom:26px;opacity:1}}
.band{{background:{s['acc']};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:80px}} .band .btn{{background:#fff;color:{s['acc']}}}
footer{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;padding:70px 80px;font-size:17px}} footer b{{display:block;margin-bottom:14px;font-size:19px}} footer span{{display:block;opacity:.7;line-height:1.9}}
</style></head><body>
{hero}
<div class="stats">{stats}</div>
<section><div class="head"><h2>{s['sect']}</h2><a>Ver todo →</a></div><div class="cards">{cards}</div></section>
<section class="about"><div class="ap" style="background-image:url({img(ai)})"></div><div><span class="tag">Sobre nosotros</span><h2>{at}</h2><p>{ad}</p><ul>{lis}</ul><a class="btn big">{s['cta']}</a></div></section>
<section><div class="head"><h2>Galería</h2><a>@{s['id']} →</a></div><div class="gal">{gal}</div></section>
<div class="quote"><span class="st">★★★★★</span><q>{q}</q><span>{qa} · Reseña verificada</span></div>
<div class="band"><h2>{s['band']}</h2><a class="btn big">{s['cta']}</a></div>
<footer><div><b style="font-size:26px">{s['name']}</b><span>{s['tag']}</span></div><div><b>Horario</b><span>Lunes a viernes<br>9:00 – 20:00</span></div><div><b>Contacto</b><span>Teléfono y WhatsApp<br>Formulario web</span></div><div><b>Síguenos</b><span>Instagram<br>Google Maps</span></div></footer>
</body></html>'''
for s in SITES: open(f"{OUT}/{s['id']}.html",'w').write(page(s))
print(' '.join(s['id'] for s in SITES))
