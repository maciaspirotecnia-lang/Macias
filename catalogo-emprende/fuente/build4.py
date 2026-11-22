import sys, os
S = sys.argv[1]
W = S + '/web3/'
F = S + '/fonts/'
WA = 'https://wa.me/message/LAS2WAECZZRSK1'
IG = 'https://www.instagram.com/pirotecniamacias__'
MAPS = 'https://maps.app.goo.gl/aJCDFC2kRHKGPqhB8'
FECHA = '4 de diciembre'
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'icons4.py')).read())  # ic(), I, WA_ICON

def m(n):
    return '$' + f'{int(round(n)):,}'.replace(',', '.')

# ---------------- PRODUCTOS (precios de la lista Macías) ----------------
# 'unit' = tiene precio por paca y precio por unidad -> se muestra el AHORRO de comprar la paca
# 'neg'  = solo precio por mayor -> se muestra el precio grande + descuento por cantidad
def neg(name, img, price, ul, line, tag=None):
    return dict(k='neg', name=name, img=img, price=price, ul=ul, line=line, tag=tag)
def unit(name, img, price, pl, n, sell, line, sl='c/u', tag=None):
    return dict(k='unit', name=name, img=img, price=price, pl=pl, n=n, sell=sell, line=line, sl=sl, tag=tag)

TAG_TOP = ('MÁS VENDIDO', 'gold')
TAG_SAVE = ('MÁS AHORRO', 'red')
TAG_LOW = ('PACA ECONÓMICA', 'cream')
TAG_BIG = ('PARA CELEBRAR EN GRANDE', 'gold')

TOTES = unit('Totes', 'Sonidos-08', 40000, 'paca x100', 100, 500, 'El que más se lleva la gente.', tag=TAG_TOP)
METRA = unit('Metralleta 16 tiros', 'Sonidos-05', 40000, 'paca x40', 40, 3000, 'Barata, rápida y nunca falta.', tag=TAG_LOW)
TRUENO = unit('Mini Trueno', 'Sonidos-03', 230000, 'paca x50 cajas', 50, 8000, 'El sonido que todos piden.', 'la caja', tag=TAG_SAVE)
CEBO = unit('Cebollitas o Palomitas', 'Sonidos-02', 150000, 'paca x50 cajitas', 50, 5000, 'Diversión para toda la familia.', 'la cajita')
MECHA = unit('Mecha Mini Fo', 'Sonidos-04', 40000, 'paca x40 cajitas', 40, 2000, 'Poquita plata, mucha diversión.', 'la cajita', tag=TAG_LOW)
ROSITA = unit('Rosita China Craqueante', 'Sonidos-06', 60000, 'paca x12 sachets', 12, 8000, 'Gira, suena y alegra la calle.', 'el sachet')
MARTI = unit('Martinicas', 'Sonidos-12', 30000, 'paca x4 hojas', 4, 10000, 'Cada hoja trae 150.', 'la hoja')
BARRIL = unit('Barril Cracker', 'Sonidos-13', 35000, 'paca x6', 6, 8000, 'Pequeño pero muy sonador.')
GOLPES = neg('4 Golpes', 'Sonidos-01', 45000, 'paquete x20 por 6', 'Cuatro golpes de pura emoción.')

V7 = unit('Volcán No. 7 Premium', 'Volcanes-04', 300000, 'paca x12', 12, 35000, 'El volcán más vistoso de la lista.', tag=TAG_SAVE)
VBRI = unit('Volcán Brillante', 'Volcanes-02', 72000, 'paca x12', 12, 10000, 'Brilla bonito y alegra la noche.')
V4 = unit('Volcán No. 4', 'Volcanes-03', 72000, 'paca x12', 12, 8000, 'Colores para toda la familia.')
VCITO = unit('Volcancito', 'Volcanes-01', 15000, 'bolsa x10', 10, 3000, 'Pequeñito y económico.', tag=TAG_LOW)
CHISP = unit('Chispitas', 'Chispitas-01', 20000, 'paca x12 cajitas', 12, 3000, 'Luz para las fotos de diciembre.', 'la cajita')
VELA = dict(name='Vela Cracker 15 tiros', price=75000, n=12, sell=10000, pl='paca x12', img=None)
LUCES_EXTRA = [('Vela Cracker 15 tiros · paca x12', f'{m(75000)} · ahorras {m(10000*12-75000)}'),
               ('Vela Cracker 20 · 25 · 30 tiros', f'{m(45000)} · {m(50000)} · {m(72000)}'),
               ('Misil 25 tiros', f'{m(40000)}'),
               ('Bazuca de Luces 888 (8x1)', f'{m(300000)}')]

TORTAS = [
    neg('Torta Británica 15 tiros', 'Torta-01', 120000, 'c/u', 'Pequeña, bonita y llamativa.'),
    neg('Torta de 16 tiros 0,8"', 'Torta-02', 50000, 'c/u', 'La torta más económica.', ('LA MÁS ECONÓMICA', 'cream')),
    neg('Torta 19 tiros calibre 25', 'Torta-03', 120000, 'c/u', 'Pirulo, árbol de plata y crisantema.'),
    neg('Torta 19 tiros calibre 30 Orión', 'Torta-04', 130000, 'c/u', 'Calibre 30: más grande, más show.'),
    neg('Torta Amazonia 25 tiros', 'Torta-05', 70000, 'c/u', '25 tiros a un precio cómodo.'),
    neg('Torta de 25 tiros 0,8"', 'Torta-06', 80000, 'c/u', 'Varios diseños para escoger.'),
    neg('Torta Cocodrilo 50 tiros', 'Torta-08', 160000, 'c/u', 'Sale en abanico. ¡Un show!'),
    neg('Torta Canto del Fénix 64 tiros', 'Torta-09', 200000, 'c/u', 'Llama la atención desde la caja.'),
    neg('Torta Colombiana 70 tiros', 'Torta-10', 250000, 'c/u', 'Para la noche del 24 y del 31.'),
    neg('Torta La Ricura 88 tiros 1"', 'Torta-11', 380000, 'c/u', 'Calibre de 1 pulgada.'),
    neg('Torta Apache 100 tiros', 'Torta-12', 350000, 'c/u', 'Para los que quieren lo grande.'),
    neg('Torta 100 tiros Multicolor y Sauce Azul', 'Torta-14', 450000, 'c/u', 'Colores y lluvia azul en el cielo.'),
]
RITMO = neg('Torta Ritmo de la Noche 100 tiros', 'Torta-13', 980000, 'caja x4', 'Viene en caja de 4 tortas.', TAG_BIG)
TORTAS_EXTRA = [('Torta de 19 tiros 0,8"', 60000), ('Torta 49 tiros 0,8"', 160000),
                ('Torta 100 tiros Tanque de Guerra', 350000), ('Torta de 138 tiros', 400000)]

VOLADORES = [
    neg('Viaje a Marte', 'Voladores-01', 100000, 'paca x10', 'Diez voladores que suben alto.'),
    neg('Volador 5 tiros + 1 bomba', 'Voladores-04', 50000, 'caja x6', 'Cinco tiros y cierra con bomba.'),
    neg('Cohete Lunar', 'Voladores-02', 60000, 'paca x12 bolsitas', 'Viene en bolsitas.'),
    neg('Volador importado 1 golpe', 'Voladores-06', 50000, 'paca x12', 'El volador de toda la vida.'),
    neg('Misil 100 tiros', 'Voladores-05', 35000, 'c/u', '100 tiros de luces en una caja.'),
]

def save(p):
    """Ahorro de comprar la paca frente a comprar unidad por unidad (precio por unidad de la lista)."""
    if p.get('k') == 'neg' or not p.get('n'):
        return None
    return p['sell'] * p['n'] - p['price']

def each_cost(p):
    c = p['price'] / p['n']
    return m(c) if c == int(c) else 'menos de ' + m(-(-c // 100) * 100)

# ---------------- COMPONENTES ----------------
def chrome(label, n):
    return f'''<div class="hdr"><img class="mini-logo" src="{W}Logo-01.png"><div class="hdr-lbl"><i></i>{label}</div></div>
<div class="ftr"><span class="ftr-close">Macías Pirotecnia <b>|</b> Celebra cada momento.</span><a class="wa-btn" href="{WA}">{WA_ICON} Pide por WhatsApp</a><span class="pg">{n:02d}</span></div>'''

N = [0]
def page(theme, label, body):
    N[0] += 1
    return f'<section class="page {theme}">{chrome(label, N[0])}{body}</section>'

def tag_html(p):
    t = p.get('tag')
    return f'<span class="tag t-{t[1]}">{t[0]}</span>' if t else ''

def hero(p):
    """Lo más grande de cada tarjeta: el ahorro (o el precio por mayor si no hay precio por unidad)."""
    if p['k'] == 'neg':
        return f'<div class="win price-hero"><small>Precio por mayor</small><b>{m(p["price"])}</b><em>{p["ul"]}<br><strong>Pide descuento por cantidad</strong></em></div>'
    return f'<div class="win"><small>Ahorras</small><b>{m(save(p))}</b><em>comprando la paca<br><strong>cada uno te sale a {each_cost(p)}</strong></em></div>'

def precios(p):
    if p['k'] == 'neg':
        return f'<p class="pline">{p["line"]}</p>'
    return f'<div class="price"><span>Por mayor</span><b>{m(p["price"])}</b><em>{p["pl"]}</em></div><div class="sell">Por unidad: <b>{m(p["sell"])}</b> {p["sl"]}</div>'

def card_v(p, v):
    return f'''<div class="cv"><div class="stage s-{v}"><img src="{W}{p["img"]}_{v}.jpg">{tag_html(p)}</div>
<div class="cv-body">{hero(p)}<h3>{p["name"]}</h3>{precios(p)}</div></div>'''
def card_h(p, v):
    return f'''<div class="ch"><div class="stage s-{v}"><img src="{W}{p["img"]}_{v}.jpg">{tag_html(p)}</div>
<div class="ch-body">{hero(p)}<h3>{p["name"]}</h3>{precios(p)}</div></div>'''
def grid_v(items, v):
    return '<div class="gv">' + ''.join(card_v(p, v) for p in items) + '</div>'
def grid_h(items, v, cell='', cls=' op'):
    return f'<div class="gh{cls}">' + ''.join(card_h(p, v) for p in items) + cell + '</div>'
def opener(num, title, sub):
    return f'<div class="opener"><div class="op-num">{num}</div><div><h2>{title}</h2><p>{sub}</p></div></div>'
def mini_head(title, sub):
    return f'<div class="mini-head"><h2>{title}</h2><p>{sub}</p></div>'
def xcell(title, rows, note=''):
    lis = ''.join(f'<li>{a}<b>{b}</b></li>' for a, b in rows)
    return f'<div class="xcell"><h4>{title}</h4><ul>{lis}</ul>{note}<a class="xlink" href="{WA}">Pídenos la foto →</a></div>'

pages = []

# 1 PORTADA
N[0] += 1
pages.append(f'''<section class="page cover">
<div class="cv-photo" style="background-image:url('{W}cover.jpg')"></div>
<img class="cv-logo" src="{W}Logo-01.png">
<div class="cv-band">
 <div class="cv-kicker">Catálogo Macías · Diciembre 2026</div>
 <h1>AL POR MAYOR <span>CON MACÍAS</span></h1>
 <p class="cv-phrase">Entre más compras, <b>más ahorras.</b></p>
 <div class="cv-meta">
  <div><b>Pedidos</b>desde $100.000</div>
  <div><b>Precios especiales</b>hasta el {FECHA}</div>
  <div><b>Valledupar</b>más de 10 años</div>
 </div>
</div>
<div class="cv-strip">Macías Pirotecnia <span>|</span> Celebra cada momento.</div>
</section>''')

# 2 POR QUÉ COMPRAR AL POR MAYOR
why = [('money', 'Pagas menos por unidad', 'Comprando la paca, cada producto te sale mucho más barato.'),
       ('tag', 'Descuentos por cantidad', 'Entre más grande tu pedido, más beneficios te llevas.'),
       ('box', 'Todo en un solo lugar', 'Tortas, volcanes, luces, voladores y sonido.')]
wh = ''.join(f'<div class="why"><div class="rec-ic">{ic(I[k],28)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in why)
pages.append(page('cream', 'Compra al por mayor', f'''
<div class="st-photo"><img src="{W}Fotos-03.jpg"></div>
<div class="kicker">Para el 24, el 31 y tus celebraciones</div>
<h2 class="big dark-t">Celebra en grande, paga menos.</h2>
<p class="lead">Para la familia, la empresa, el barrio o tu evento: <b>compra en cantidad y ahorra.</b></p>
<div class="why-row">{wh}</div>
'''))

# 3 CONFIANZA
pages.append(page('dark', 'Confianza', f'''
<div class="kicker">Por qué comprar en Macías</div>
<div class="tr-hero"><div class="tr-num">+10</div><div><h2>AÑOS EN<br><span>VALLEDUPAR</span></h2><p>Más de 10 años celebrando contigo. Conocemos lo que la gente busca en diciembre.</p></div></div>
<div class="tr-obj"><h3>“¿Y si no sé cuánto pedir?”</h3><p>Tranquilo. Escríbenos, cuéntanos para qué es y te ayudamos a armar tu pedido.</p></div>
<div class="tr-test">
 <div class="tr-q">{ic(I['quote'],34,1.4)}</div>
 <div class="tr-ph">[TESTIMONIO]</div>
 <p class="tr-hint">Aquí va la experiencia real de un cliente Macías.</p>
 <div class="tr-who">— [Nombre del cliente] · [Barrio]</div>
</div>
'''))

# 4 CÓMO COMPRAR
steps = [('pick', 'Escoges tus productos', 'Miras este catálogo y eliges productos y cantidades. Pedidos desde $100.000.'),
         ('chat', 'Nos escribes por WhatsApp', 'Te confirmamos el pedido, los precios y tu descuento por cantidad.'),
         ('key', 'Pagas y revisas', 'Pagas por llave o en efectivo y revisas bien tu pedido al recibirlo.')]
st = ''.join(f'<div class="step"><div class="step-num">0{i+1}</div><div class="step-ic">{ic(I[k],30)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (k, t, d) in enumerate(steps))
pages.append(page('cream', 'Cómo comprar', f'''
<div class="kicker">Así de fácil</div><h2 class="big dark-t">Cómo comprar</h2>
<p class="sub">Solo 3 pasos. Todo por WhatsApp.</p>
<div class="steps">{st}</div>
<div class="quote">“Tú escoges.<br><span>Macías te lo tiene listo.”</span></div>
'''))

# 5 LOS MÁS VENDIDOS
pages.append(page('dark', 'Sonido y explosión', f'''
{opener('01', 'Los más vendidos', 'Sonido y explosión: lo que más se lleva la gente. Por paca te sale mucho más barato.')}
{grid_v([TOTES, METRA, TRUENO, CEBO], 'd')}'''))

# 6 SONIDO 2
pages.append(page('cream', 'Sonido y explosión', f'''
{mini_head('Más sonido y explosión', 'Pacas que rinden para toda la noche.')}
{grid_h([MECHA, ROSITA, MARTI, BARRIL, GOLPES], 'l', xcell('También tenemos', [('Mega Pop cebollitas (24x12x20)', f'{m(82500)} · por unidad {m(5000)}')]), cls=' mh')}'''))

# 7 LUCES
pages.append(page('dark', 'Luces y volcanes', f'''
{opener('02', 'Luces y volcanes', 'Brillan bonito y son perfectos para las fotos en familia.')}
{grid_h([V7, VBRI, V4, VCITO, CHISP], 'd', xcell('Más luces', LUCES_EXTRA))}'''))

# 8-10 TORTAS
pages.append(page('cream', 'Tortas pirotécnicas', f'''
{opener('03', 'Tortas pirotécnicas', 'Las reinas del 24 y del 31. Si llevas varias, pide tu descuento.')}
{grid_h(TORTAS[0:6], 'l')}'''))
pages.append(page('dark', 'Tortas pirotécnicas', f'''
{mini_head('Más tortas', 'Para la noche buena y el año nuevo.')}
{grid_h(TORTAS[6:12], 'd', cls=' mh')}'''))
ex = ''.join(f'<li><span>{n}</span><b>{m(p)}</b></li>' for n, p in TORTAS_EXTRA)
pages.append(page('cream', 'Tortas pirotécnicas', f'''
{mini_head('La torta estrella', 'Para los que quieren celebrar en grande.')}
<div class="feat"><div class="stage s-d"><img src="{W}{RITMO["img"]}_d.jpg">{tag_html(RITMO)}</div>
<div class="feat-body">{hero(RITMO)}<h3>{RITMO["name"]}</h3>{precios(RITMO)}</div></div>
<div class="two-cells">
 <div class="xcell"><h4>También tenemos</h4><ul class="rows">{ex}</ul><p class="xnote">Precio por mayor. Pídenos la foto.</p></div>
 <div class="help"><div class="help-q">?</div><h3>¿No sabes cuál torta escoger?</h3><p>Escríbenos, cuéntanos para qué es y te ayudamos a elegir.</p></div>
</div>'''))

# 11 VOLADORES
pages.append(page('dark', 'Voladores y misiles', f'''
{opener('04', 'Voladores y misiles', 'Suben, suenan y llenan el cielo. Si llevas varios, pide tu descuento.')}
{grid_h(VOLADORES, 'd', '<div class="xcell"><h4>¿No ves un producto?</h4><p class="xp">Escríbenos y te mandamos la foto y el precio.</p></div>')}'''))

# 12 DONDE MÁS AHORRAS
rank = sorted([TRUENO, V7, CEBO, METRA, VBRI, MECHA], key=lambda p: -save(p))
rk = ''
for i, p in enumerate(rank):
    rk += f'''<div class="rk"><div class="rk-n">0{i+1}</div><img src="{W}{p["img"]}_l.jpg"><div class="rk-t"><span>Compras 1 {p["pl"].split(" ")[0]} de</span><b>{p["name"]}</b><em>Pagas {m(p["price"])} · por unidad serían {m(p["sell"]*p["n"])}</em></div><div class="rk-g"><small>Ahorras</small><b>{m(save(p))}</b></div></div>'''
pages.append(page('cream', 'Tu ahorro', f'''
<div class="kicker">Haz la cuenta</div><h2 class="big dark-t">Donde más <span class="red-t">ahorras</span></h2>
<p class="sub">Mira cuánto ahorras comprando la paca completa en vez de unidad por unidad.</p>
<div class="ranking">{rk}</div>
<div class="calc-box"><p>Si compras <b>3 pacas de Metralleta</b> pagas {m(120000)}. Por unidad te costarían {m(360000)}…</p><div>Ahorras <span>{m(240000)}</span></div></div>
<p class="fine">Comparado con el precio por unidad de nuestra lista de precios.</p>'''))

# 13 COMBOS
kits = [('Combo Familiar', 'Para celebrar en casa', [METRA, MECHA, VCITO, TOTES]),
        ('Combo Fiesta', 'Para la noche del 24 y el 31', [CEBO, V4, VBRI, VELA, METRA]),
        ('Combo Gran Celebración', 'Para celebrar en grande', [TRUENO, CEBO, V7, ROSITA, VELA])]
kh = ''
for i, (kn, ks, items) in enumerate(kits):
    pay = sum(p['price'] for p in items); unit_total = sum(p['sell'] * p['n'] for p in items)
    thumbs = ''.join(f'<img src="{W}{p["img"]}_l.jpg">' for p in items if p.get('img'))
    lis = ''.join(f'<li>{ic(I["check"],13,2)} 1 {p["pl"].split(" ")[0]} de {p["name"]}</li>' for p in items)
    bono = '<div class="kit-bono">+ Regalo de bienvenida</div>' if pay >= 750000 else ''
    kh += f'''<div class="kit k{i}"><div class="kit-top"><h3>{kn}</h3><p>{ks}</p></div><div class="kit-th">{thumbs}</div>
<div class="kit-gain"><small>Ahorras</small><b>{m(unit_total - pay)}</b></div>
<div class="kit-nums"><div><small>Pagas</small><b>{m(pay)}</b></div><div><small>Por unidad</small><b class="strike">{m(unit_total)}</b></div></div>
<ul>{lis}</ul>{bono}</div>'''
pages.append(page('dark', 'Combos al por mayor', f'''
<div class="kicker">Combos listos</div><h2 class="big">Combos al por mayor</h2>
<p class="sub">No pienses mucho: escoge tu combo y pídelo por WhatsApp.</p>
<div class="kits">{kh}</div>
<p class="fine">Ahorro comparado con el precio por unidad de nuestra lista de precios.</p>
<div class="band"><h3>¿Quieres armar tu propio combo?</h3><p>Dinos qué necesitas y te ayudamos a escoger. Desde <b>$750.000</b> te llevas un regalo de bienvenida.</p></div>'''))

# 14 ESCALERA DE DESCUENTOS
lad = [('Desde', '$100.000', 'Haces tu pedido al por mayor', 'Precios de mayorista en todo el catálogo.', 'box'),
       ('Desde', '$750.000', 'Regalo de bienvenida', 'Con tu primer pedido desde $750.000 te damos un regalo.', 'gift'),
       ('Desde', '$[        ]', 'Descuento por cantidad', 'Descuento de [   ]% en tu pedido.', 'tag'),
       ('Desde', '$[        ]', 'Más descuento', 'Descuento de [   ]% en tu pedido.', 'tag'),
       ('Desde', '$[        ]', 'Envío gratis', 'Te llevamos el pedido sin costo.', 'truck')]
lh = ''.join(f'<div class="rung r{i}"><div class="rung-ic">{ic(I[k],24)}</div><div class="rung-amt"><small>{s}</small>{a}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (s, a, t, d, k) in enumerate(lad))
pages.append(page('cream', 'Descuentos', f'''
<div class="kicker">Entre más compras, más ahorras</div><h2 class="big dark-t">Escalera de descuentos</h2>
<p class="sub">Cada escalón te da algo más. ¿Hasta dónde quieres subir?</p>
<div class="ladder">{lh}</div>
<div class="urgent">{ic(I['clock'],30)}<div><b>Precios especiales hasta el {FECHA}.</b><span>Después de esa fecha los precios pueden cambiar.</span></div></div>'''))

# 15 POLÍTICAS
pol = [('money', 'Pedidos desde $100.000', 'Tu pedido al por mayor puede ser desde $100.000.'),
       ('key', 'Pagos', 'Pagas por llave o en efectivo.'),
       ('eye', 'Revisa tu pedido', 'Al recibir, revisa bien todos tus productos antes de irte.'),
       ('doc', 'Sin devoluciones', 'No se hacen devoluciones. Por eso es importante revisar todo al recibir.'),
       ('shield', 'Después de la entrega', 'Una vez entregado el pedido, Macías no se hace responsable si la pólvora se daña o se descompone por humedad, calor, mal almacenamiento o mal uso.'),
       ('clock', 'Precios por tiempo limitado', f'Los precios especiales de este catálogo son válidos hasta el {FECHA}.')]
ph = ''.join(f'<div class="pol"><div class="pol-ic">{ic(I[k],22)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for k, t, d in pol)
pages.append(page('dark', 'Políticas', f'''
<div class="kicker">Reglas claras, compra tranquila</div><h2 class="big">Nuestras políticas</h2>
<p class="sub">Así trabajamos, para que tu compra salga bien.</p>
<div class="pols">{ph}</div>'''))

# 16 USO RESPONSABLE
vr = [('id', 'Solo para mayores de edad', 'La pólvora la manipulan solo los adultos. Nunca la dejes en manos de niños.'),
      ('drop', 'Guárdala bien', 'En un lugar seco, fresco y seguro, lejos del fuego, del calor y de los niños.'),
      ('doc', 'Consulta las normas', 'Pregunta qué está permitido en tu barrio o municipio antes de usarla.'),
      ('talk', 'Lee las instrucciones', 'Antes de prender cada producto, lee cómo se usa y mantén distancia.')]
vh = ''.join(f'<div class="vr"><div class="rec-ic">{ic(I[k],26)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in vr)
pages.append(page('cream', 'Uso responsable', f'''
<div class="kicker">Celebrar bien es celebrar seguro</div><h2 class="big dark-t">Uso responsable</h2>
<p class="sub">Con estos 4 consejos, tu diciembre será alegre <b>y seguro</b>.</p>
<div class="vr-grid">{vh}</div>
<div class="vr-photo"><img src="{W}Fotos-03.jpg"></div>'''))

# 17 CONTRAPORTADA
pages.append(f'''<section class="page back">
<div class="bk-bg" style="background-image:url('{W}Fotos-03.jpg')"></div>
<img class="bk-logo" src="{W}Logo-01.png">
<div class="bk-kicker">¿Listo para hacer tu pedido?</div>
<h1>COMPRA EN CANTIDAD<br><span>Y AHORRA</span></h1>
<p class="bk-step">Toca el botón y escríbenos:<br><b>“Quiero hacer un pedido al por mayor”</b></p>
<a class="bk-btn" href="{WA}">{WA_ICON.replace('width="13" height="13"','width="30" height="30"')} ESCRÍBENOS AL WHATSAPP</a>
<div class="bk-links"><a href="{IG}">{ic(I['ig'],18,2)} @pirotecniamacias__</a><a href="{MAPS}">{ic(I['pin'],18,2)} Valledupar, Cesar · Ver en el mapa</a></div>
<div class="bk-close">Macías Pirotecnia <span>|</span> Celebra cada momento.</div>
</section>''')

CSS = open(os.path.join(HERE, 'style3.css')).read().replace('{F}', F) + open(os.path.join(HERE, 'style4.css')).read()
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Macías al por mayor</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(S + '/catalogo4.html', 'w').write(html)
print(len(pages), 'pages')
