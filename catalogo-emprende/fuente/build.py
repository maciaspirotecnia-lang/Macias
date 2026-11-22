import sys, os
S = sys.argv[1]
W = S + '/web/'
F = S + '/fonts/'
WA = 'https://wa.me/message/LAS2WAECZZRSK1'
IG = 'https://www.instagram.com/pirotecniamacias__'
MAPS = 'https://maps.app.goo.gl/aJCDFC2kRHKGPqhB8'
FECHA = '4 de diciembre'

def m(n):
    return '$' + f'{int(round(n)):,}'.replace(',', '.')

# ---------------- PRODUCTOS (solo lista de precios) ----------------
def neg(name, img, price, ul, line):
    return dict(k='neg', name=name, img=img, price=price, ul=ul, line=line)
def unit(name, img, price, pl, n, sell, line, sl='cada uno'):
    return dict(k='unit', name=name, img=img, price=price, pl=pl, n=n, sell=sell, line=line, sl=sl)

TOTES = unit('Totes', 'Sonidos-08', 40000, 'paca x100', 100, 500, 'El que más se lleva la gente.')
METRA = unit('Metralleta 16 tiros', 'Sonidos-05', 40000, 'paca x40', 40, 3000, 'Barata, rápida y se vende sola.')
TRUENO = unit('Mini Trueno', 'Sonidos-03', 230000, 'paca x50 cajas', 50, 8000, 'El sonido que todos piden.', 'cada caja')
CEBO = unit('Cebollitas o Palomitas', 'Sonidos-02', 150000, 'paca x50 cajitas', 50, 5000, 'Diversión para toda la familia.', 'cada cajita')
MECHA = unit('Mecha Mini Fo', 'Sonidos-04', 40000, 'paca x40 cajitas', 40, 2000, 'Poquita plata, buena ganancia.', 'cada cajita')
ROSITA = unit('Rosita China Craqueante', 'Sonidos-06', 60000, 'paca x12 sachets', 12, 8000, 'Gira, suena y alegra la calle.', 'cada sachet')
MARTI = unit('Martinicas', 'Sonidos-12', 30000, 'paca x4 hojas', 4, 10000, 'Cada hoja trae 150.', 'cada hoja')
BARRIL = unit('Barril Cracker', 'Sonidos-13', 35000, 'paca x6', 6, 8000, 'Pequeño pero muy sonador.')
GOLPES = neg('4 Golpes', 'Sonidos-01', 45000, 'paquete x20 por 6', 'Cuatro golpes de pura emoción.')
SONIDO = [TOTES, METRA, TRUENO, CEBO, MECHA, ROSITA, MARTI, BARRIL, GOLPES]
SONIDO_EXTRA = [('Mega Pop cebollitas (24x12x20)', 82500)]

V7 = unit('Volcán No. 7 Premium', 'Volcanes-04', 300000, 'paca x12', 12, 35000, 'El volcán más vistoso de la lista.')
VBRI = unit('Volcán Brillante', 'Volcanes-02', 72000, 'paca x12', 12, 10000, 'Brilla bonito y deja buena plata.')
V4 = unit('Volcán No. 4', 'Volcanes-03', 72000, 'paca x12', 12, 8000, 'Colores para alegrar la noche.')
VCITO = unit('Volcancito', 'Volcanes-01', 15000, 'bolsa x10', 10, 3000, 'Pequeñito y facilito de vender.')
CHISP = unit('Chispitas', 'Chispitas-01', 20000, 'paca x12 cajitas', 12, 3000, 'Luz para las fotos de diciembre.', 'cada cajita')
LUCES = [V7, VBRI, V4, VCITO, CHISP]
VELA = dict(name='Vela Cracker 15 tiros', price=75000, n=12, sell=10000, pl='paca x12')
LUCES_EXTRA = [('Vela Cracker 15 tiros · paca x12', f'{m(75000)} → vende c/u a {m(10000)} · ganas {m(10000-75000/12)} c/u'),
               ('Vela Cracker 20 tiros', f'{m(45000)} · venta negociable'),
               ('Vela Cracker 25 tiros', f'{m(50000)} · venta negociable'),
               ('Vela Cracker 30 tiros', f'{m(72000)} · venta negociable'),
               ('Misil 25 tiros', f'{m(40000)} · venta negociable'),
               ('Bazuca de Luces 888 (8x1)', f'{m(300000)} · venta negociable')]

TORTAS = [
    neg('Torta Británica 15 tiros', 'Torta-01', 120000, 'c/u', 'Pequeña, bonita y fácil de vender.'),
    neg('Torta de 16 tiros 0,8"', 'Torta-02', 50000, 'c/u', 'La más económica para empezar.'),
    neg('Torta 19 tiros calibre 25', 'Torta-03', 120000, 'c/u', 'Pirulo, árbol de plata y crisantema.'),
    neg('Torta 19 tiros calibre 30 Orión', 'Torta-04', 130000, 'c/u', 'Calibre 30: más grande, más show.'),
    neg('Torta Amazonia 25 tiros', 'Torta-05', 70000, 'c/u', '25 tiros a un precio cómodo.'),
    neg('Torta de 25 tiros 0,8"', 'Torta-06', 80000, 'c/u', 'Varios diseños para escoger.'),
    neg('Torta Cocodrilo 50 tiros', 'Torta-08', 160000, 'c/u', 'Sale en abanico. ¡Un show!'),
    neg('Torta Canto del Fénix 64 tiros', 'Torta-09', 200000, 'c/u', 'Llama la atención desde la caja.'),
    neg('Torta Colombiana 70 tiros', 'Torta-10', 250000, 'c/u', 'Para la noche del 24 y del 31.'),
    neg('Torta La Ricura 88 tiros 1"', 'Torta-11', 380000, 'c/u', 'Calibre de 1 pulgada.'),
    neg('Torta Apache 100 tiros', 'Torta-12', 350000, 'c/u', 'Para los que quieren lo grande.'),
    neg('Torta Ritmo de la Noche 100 tiros', 'Torta-13', 980000, 'caja x4', 'Viene en caja de 4: rinde para vender.'),
    neg('Torta 100 tiros Multicolor y Sauce Azul', 'Torta-14', 450000, 'c/u', 'Colores y lluvia azul en el cielo.'),
]
TORTAS_EXTRA = [('Torta de 19 tiros 0,8"', 60000), ('Torta 49 tiros 0,8"', 160000),
                ('Torta 100 tiros Tanque de Guerra', 350000), ('Torta de 138 tiros', 400000)]

VOLADORES = [
    neg('Viaje a Marte', 'Voladores-01', 100000, 'paca x10', 'Diez voladores que suben alto.'),
    neg('Volador 5 tiros + 1 bomba', 'Voladores-04', 50000, 'caja x6', 'Cinco tiros y cierra con bomba.'),
    neg('Cohete Lunar', 'Voladores-02', 60000, 'paca x12 bolsitas', 'Viene en bolsitas, listo para vender.'),
    neg('Volador importado 1 golpe', 'Voladores-06', 50000, 'paca x12', 'El volador de toda la vida.'),
    neg('Misil 100 tiros', 'Voladores-05', 35000, 'c/u', '100 tiros de luces en una caja.'),
]

def gain(p):
    if p.get('k') == 'neg' or not p.get('n'):
        return None
    return p['sell'] - p['price'] / p['n'], p['sell'] * p['n'] - p['price']

def per_txt(per):
    if per == int(per):
        return m(per)
    return 'más de ' + m(int(per // 100) * 100)

# ---------------- ICONOS ----------------
def ic(path, size=40, sw=1.6):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'
I = {
 'pick': '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
 'video': '<rect x="2" y="5" width="14" height="14" rx="2"/><path d="m22 8-6 4 6 4z"/>',
 'money': '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>',
 'box': '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
 'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M8 7h8M8 11h6"/>',
 'hand': '<path d="M12 21s-7-4.4-9.3-9A5 5 0 0 1 12 6a5 5 0 0 1 9.3 6c-2.3 4.6-9.3 9-9.3 9z"/>',
 'gift': '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v9H5v-9"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 0 1 0 5"/>',
 'truck': '<path d="M1 3h15v13H1zM16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
 'tag': '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/>',
 'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'chat': '<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/>',
 'id': '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="11" r="2.5"/><path d="M5.5 17a3.5 3.5 0 0 1 7 0M15 9h3M15 13h3"/>',
 'drop': '<path d="M12 2.7 6.3 8.4a8 8 0 1 0 11.4 0z"/><path d="M4 4l16 16"/>',
 'doc': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13l2 2 4-4"/>',
 'talk': '<circle cx="9" cy="7" r="4"/><path d="M2 21v-2a4 4 0 0 1 4-4h6a4 4 0 0 1 4 4v2"/><path d="M19 8v4M17 10h4"/>',
 'pin': '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 'ig': '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
 'check': '<path d="M20 6 9 17l-5-5"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 'key': '<circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 9.8-9.8M17 6l3 3M14.5 8.5l2 2"/>',
 'eye': '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8S1 12 1 12z"/><circle cx="12" cy="12" r="3"/>',
}

# ---------------- COMPONENTES ----------------
def chrome(label, n):
    return f'''<div class="hdr"><img class="mini-logo" src="{W}Logo-01.png"><div class="hdr-lbl"><i></i>{label}</div></div>
<div class="ftr"><span>Macías Pirotecnia <b>|</b> Celebra cada momento.</span><a href="{WA}">Pide por WhatsApp →</a><span class="pg">{n:02d}</span></div>'''

def page(n, theme, label, body, cls=''):
    return f'<section class="page {theme} {cls}">{chrome(label, n)}{body}</section>'

def card(p, size='m'):
    g = gain(p)
    head = f'<div class="ph"><img src="{W}{p["img"]}.jpg"></div><h3>{p["name"]}</h3><p class="line">{p["line"]}</p>'
    if p['k'] == 'neg':
        nums = f'<div class="nums"><div><small>Compras</small><b>{m(p["price"])}</b><em>{p["ul"]}</em></div><div><small>Vendes</small><b class="soft">Negociable</b><em>tú pones el precio</em></div></div>'
        win = '<div class="win neg"><small>Tu ganancia</small><b>Tú decides</b></div>'
    else:
        nums = f'<div class="nums"><div><small>Compras</small><b>{m(p["price"])}</b><em>{p["pl"]}</em></div><div><small>Vendes {p["sl"]} a</small><b>{m(p["sell"])}</b><em>precio sugerido</em></div></div>'
        per, tot = g
        if per == int(per):
            win = f'<div class="win"><small>Ganas</small><b>{m(per)}</b><em>por {p["sl"]}<br><strong>{m(tot)} la paca</strong></em></div>'
        else:
            win = f'<div class="win"><small>Ganas</small><b>{m(tot)}</b><em>por paca<br><strong>{per_txt(per)} c/u</strong></em></div>'
    return f'<div class="card {size}">{head}{nums}{win}</div>'

def grid(items, cols, size='m', cell=''):
    return f'<div class="grid c{cols}">' + ''.join(card(p, size) for p in items) + cell + '</div>'

def opener(num, title, sub):
    return f'<div class="opener"><div class="op-num">{num}</div><div><h2>{title}</h2><p>{sub}</p></div></div>'

def xcell(title, rows, note=''):
    lis = ''.join(f'<li>{a}<b>{b}</b></li>' for a, b in rows)
    return f'<div class="xcell"><h4>{title}</h4><ul>{lis}</ul>{note}<a class="xbtn" href="{WA}">Pídenos la foto →</a></div>'

pages = []
# 1 PORTADA
pages.append(f'''<section class="page cover">
<div class="cv-photo" style="background-image:url('{W}cover.jpg')"></div>
<img class="cv-logo" src="{W}Logo-01.png">
<div class="cv-band">
 <div class="cv-kicker">Catálogo para emprendedores · Diciembre 2026</div>
 <h1>EMPRENDE CON <span>MACÍAS</span></h1>
 <div class="cv-rule"></div>
 <div class="cv-meta">
  <div><b>Este diciembre,</b>la plata la ganas tú.</div>
  <div><b>Inversión</b>desde $100.000</div>
  <div><b>Precios especiales</b>hasta el {FECHA}</div>
  <div><b>Valledupar</b>más de 10 años</div>
 </div>
</div>
<div class="cv-strip">Macías Pirotecnia <span>|</span> Celebra cada momento.</div>
</section>''')

# 2 HISTORIA
pages.append(page(2, 'cream', 'Tu historia', f'''
<div class="st-photo"><img src="{W}Fotos-03.jpg"></div>
<div class="st-grid">
 <div><div class="kicker">Seamos sinceros</div><h2 class="st-title">Cada diciembre pasa lo mismo.</h2></div>
 <div class="st-copy">
  <p class="lead">La plata de la ropita del 24 y del 31… <b>se embolata.</b></p>
  <p>Llegan las fiestas, los gastos suben y el bolsillo no alcanza.</p>
  <p class="lead">Pero hay algo que <b>nunca falta</b> en diciembre: <b>la pólvora.</b></p>
  <p>Todos la buscan. Todos la compran.</p>
 </div>
</div>
<div class="st-q">¿Y si esta vez<br><span>se la vendes tú?</span></div>
<p class="st-foot">No necesitas local ni saber de negocios. Vendes desde tu casa, con tu celular. Nosotros te enseñamos.</p>
'''))

# 3 CÓMO FUNCIONA
steps = [('pick', 'Eliges tus productos', 'Miras este catálogo y escoges lo que quieres vender. Empiezas desde $100.000.'),
         ('video', 'Recibes videos y catálogo', 'Te damos videos con la marca Macías y un catálogo para que publiques en tus estados y redes.'),
         ('money', 'Vendes y ganas', 'Publicas, tus clientes te escriben, vendes… y la ganancia es toda tuya.')]
st = ''.join(f'<div class="step"><div class="step-num">0{i+1}</div><div class="step-ic">{ic(I[k],30)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (k, t, d) in enumerate(steps))
pages.append(page(3, 'dark', 'Cómo funciona', f'''
<div class="kicker">Así de fácil</div><h2 class="big">Cómo funciona</h2>
<p class="sub">Solo 3 pasos. Si sabes usar WhatsApp, sabes hacer esto.</p>
<div class="steps">{st}</div>
<div class="quote">“Tú pones las ganas.<br><span>Macías pone el producto.”</span></div>
'''))

# 4 QUÉ RECIBES
rec = [('box', 'Productos de calidad', 'Pólvora que la gente ya conoce y pide, a precio de mayorista.'),
       ('video', 'Videos con la marca Macías', 'Listos para subir a tus estados de WhatsApp y redes.'),
       ('book', 'Catálogo para vender', 'Para que tus clientes vean todo y escojan rápido.'),
       ('hand', 'Acompañamiento paso a paso', 'No te dejamos solo. Te ayudamos desde tu primer pedido.')]
rc = ''.join(f'<div class="rec"><div class="rec-ic">{ic(I[k],26)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in rec)
pages.append(page(4, 'cream', 'Qué recibes', f'''
<div class="rc-top">
 <div class="rc-photo"><div class="blk"></div><img src="{W}Fotos-02.jpg"></div>
 <div><div class="kicker">Todo lo que te llevas</div><h2 class="big dark-t">Qué recibes</h2>
 <p class="sub">No solo compras pólvora. Te llevas un negocio listo para arrancar.</p></div>
</div>
<div class="rec-grid">{rc}</div>
'''))

# 5 MÁS VENDIDOS
best = [TOTES, METRA, TRUENO, CEBO]
bc = ''
for i, p in enumerate(best):
    per, tot = gain(p)
    bc += f'''<div class="best"><div class="ph"><img src="{W}{p["img"]}.jpg"><span class="rank">0{i+1}</span></div>
<h3>{p["name"]}</h3><p class="line">Compras {m(p["price"])} · {p["pl"]}</p>
<div class="best-g"><small>Ganas</small><b>{m(per)}</b><em>por {p["sl"]}</em></div><div class="best-t">{m(tot)} por toda la paca</div></div>'''
pages.append(page(5, 'dark', 'Los más vendidos', f'''
<div class="kicker">Lo que más se lleva la gente</div><h2 class="big">Los más vendidos</h2>
<p class="sub">Sonidos y explosivos: <b>salen rápido y dejan buena plata.</b> Si no sabes por dónde empezar, empieza por aquí.</p>
<div class="best-grid">{bc}</div>'''))

# 6-7 SONIDO
pages.append(page(6, 'cream', 'Sonido y explosión', f'''
{opener('01', 'Sonido y explosión', 'Lo que más se mueve en la cuadra. Compras la paca y vendes por unidad.')}
{grid(SONIDO[0:4], 2, 'l')}'''))
pages.append(page(7, 'cream', 'Sonido y explosión', grid(SONIDO[4:9], 3, 'xs',
    xcell('También tenemos', [(SONIDO_EXTRA[0][0], f'{m(SONIDO_EXTRA[0][1])} · venta negociable')]))))

# 8 LUCES
pages.append(page(8, 'dark', 'Luces y volcanes', f'''
{opener('02', 'Luces y volcanes', 'Brillan bonito, no asustan y son perfectos para las fotos en familia.')}
{grid(LUCES, 3, 'xs', xcell('Más luces', LUCES_EXTRA))}'''))

# 9-11 TORTAS
pages.append(page(9, 'cream', 'Tortas pirotécnicas', f'''
{opener('03', 'Tortas pirotécnicas', 'Las reinas del 24 y del 31. Tú pones el precio de venta y decides tu ganancia.')}
{grid(TORTAS[0:4], 2, 'l')}'''))
pages.append(page(10, 'cream', 'Tortas pirotécnicas', grid(TORTAS[4:10], 3, 'xs')))
pages.append(page(11, 'cream', 'Tortas pirotécnicas', grid(TORTAS[10:13], 3, 'xs',
    '') + f'<div class="extra">{xcell("También tenemos", [(n, m(p) + " · venta negociable") for n, p in TORTAS_EXTRA])}</div>'))

# 12 VOLADORES
pages.append(page(12, 'dark', 'Voladores y misiles', f'''
{opener('04', 'Voladores y misiles', 'Suben, suenan y llenan el cielo. Tú pones el precio de venta.')}
{grid(VOLADORES, 3, 'xs', '<div class="xcell"><h4>¿No ves un producto?</h4><p>Escríbenos y te mandamos la foto y el precio.</p><a class="xbtn" href="' + WA + '">Escribir por WhatsApp →</a></div>')}'''))

# 13 KITS
kits = [('Kit Arranque', 'Para empezar sin miedo', [METRA, MECHA, VCITO, TOTES]),
        ('Kit Pro', 'Para los que van en serio', [CEBO, V4, VBRI, VELA, METRA]),
        ('Kit Jefe', 'Para mandar en diciembre', [TRUENO, CEBO, V7, ROSITA, VELA])]
kh = ''
for i, (kn, ks, items) in enumerate(kits):
    inv = sum(p['price'] for p in items); venta = sum(p['sell'] * p['n'] for p in items)
    lis = ''.join(f'<li>{ic(I["check"],13,2)} 1 {p["pl"].split(" ")[0]} de {p["name"]}</li>' for p in items)
    bono = '<div class="kit-bono">Incluye bono de bienvenida</div>' if inv >= 750000 else ''
    kh += f'''<div class="kit k{i}"><div class="kit-top"><h3>{kn}</h3><p>{ks}</p></div><ul>{lis}</ul>
<div class="kit-nums"><div><small>Inviertes</small><b>{m(inv)}</b></div><div><small>Vendes</small><b>{m(venta)}</b></div></div>
<div class="kit-gain"><small>Tu ganancia</small><b>{m(venta - inv)}</b></div>{bono}</div>'''
pages.append(page(13, 'cream', 'Kits armados', f'''
<div class="kicker">Combos listos</div><h2 class="big dark-t">Kits armados</h2>
<p class="sub">No pienses mucho: escoge tu kit, pídelo por WhatsApp y empieza a vender.</p>
<div class="kits">{kh}</div>
<p class="fine">Ganancia calculada vendiendo todo al precio sugerido de este catálogo.</p>
<div class="band"><img src="{W}Fotos-02.jpg"><div><h3>¿Quieres otro combo?</h3><p>Dinos cuánta plata quieres invertir y te ayudamos a escoger. Desde <b>$750.000</b> te llevas el bono de bienvenida.</p></div></div>'''))

# 14 ESCALERA
lad = [('$100.000', 'Empiezas tu negocio', 'Productos + videos con la marca Macías + acompañamiento.', 'box'),
       ('$750.000', 'Bono de bienvenida', 'Con tu primer pedido desde $750.000 te damos un regalo.', 'gift'),
       ('Más de $1.200.000', 'Tu propio catálogo', 'Un catálogo personalizado con el logo de Macías y todos tus productos, sin precios para que pongas los tuyos. Más los mensajes listos para WhatsApp.', 'book'),
       ('$[        ]', 'Descuento extra', 'Descuento de [   ]% en tu pedido.', 'tag'),
       ('$[        ]', 'Envío gratis', 'Te llevamos el pedido sin costo.', 'truck')]
lh = ''.join(f'<div class="rung r{i}"><div class="rung-ic">{ic(I[k],24)}</div><div class="rung-amt"><small>{'Compras' if a.startswith('Más') else 'Desde'}</small>{a}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (a, t, d, k) in enumerate(lad))
pages.append(page(14, 'dark', 'Beneficios', f'''
<div class="kicker">Entre más compras, más ganas</div><h2 class="big">Escalera de beneficios</h2>
<p class="sub">Cada escalón te da algo más. ¿Hasta dónde quieres subir?</p>
<div class="ladder">{lh}</div>
<div class="urgent">{ic(I['clock'],28)}<div><b>Precios especiales hasta el {FECHA}.</b><span>Después de esa fecha los precios pueden cambiar. ¡Aprovecha ahora!</span></div></div>'''))

# 15 CALCULADORA + MENSAJES
ch = ''
for p in [TOTES, METRA, TRUENO, V7]:
    per, tot = gain(p)
    ch += f'<div class="calc-row"><span>Si vendes <b>100</b> {p["name"].lower()}</span><b class="cg">ganas {m(per*100)}</b></div>' if p is TOTES else f'<div class="calc-row"><span>Si vendes <b>10</b> {p["name"]}</span><b class="cg">ganas {m(per*10)}</b></div>'
msgs = ['🎆 ¡Llegó la pólvora de diciembre! Totes, volcanes, tortas y más. Escríbeme y te mando fotos y precios. 🔥',
        '✨ Este 24 y 31 celebra en grande. Tengo productos Macías listos para entregar. ¡Pide el tuyo antes de que se acaben!',
        '🎇 ¿Ya tienes la pólvora para la noche buena? Te la llevo. Pregúntame sin compromiso. 📲']
mh = ''.join(f'<div class="msg">{x}</div>' for x in msgs)
pages.append(page(15, 'cream', 'Herramientas de regalo', f'''
<div class="two">
 <div class="calc"><div class="kicker gold">Haz las cuentas</div><h2>Calculadora sencilla</h2>{ch}
 <p class="fine left">Con los precios sugeridos de este catálogo.</p></div>
 <div class="gifts">
  <div class="kicker">De regalo para ti</div>
  <h2 class="dark-t">Guía de ventas + mensajes listos</h2>
  <p>Te regalamos una guía fácil para vender y mensajes listos para tus <b>estados de WhatsApp</b>. Solo copias, pegas y publicas.</p>
  <div class="msgs"><div class="msgs-title">{ic(I['chat'],14,2)} Así se ven tus mensajes</div>{mh}</div>
 </div>
</div>
<div class="cta-band"><div><h3>Ya hiciste las cuentas. Ahora te toca a ti.</h3><p>Escríbenos: <b>“Quiero emprender con Macías”</b></p></div><a href="{WA}">Ir a WhatsApp →</a></div>'''))

# 16 POLÍTICAS
pol = [('money', 'Empieza desde $100.000', 'Tu primer pedido puede ser desde $100.000. Así empiezas tranquilo.'),
       ('key', 'Pagos', 'Pagas por llave o en efectivo. Fácil y rápido.'),
       ('video', 'Videos solo para clientes Macías', 'Los videos con la marca Macías se entregan únicamente a quienes compran sus productos en Macías. Si los productos no se compran con nosotros, no se entregan los videos.'),
       ('shield', 'Cuida la marca', 'Los videos solo se usan para vender productos comprados en Macías. No se pueden editar ni quitarles la marca.'),
       ('eye', 'Revisa tu pedido', 'Al recibir, revisa bien todos tus productos antes de irte.'),
       ('doc', 'Sin devoluciones', 'No se hacen devoluciones. Por eso es importante revisar todo al recibir.')]
ph = ''.join(f'<div class="pol"><div class="pol-ic">{ic(I[k],22)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for k, t, d in pol)
pages.append(page(16, 'dark', 'Políticas', f'''
<div class="kicker">Reglas claras, negocio tranquilo</div><h2 class="big">Nuestras políticas</h2>
<p class="sub">Así trabajamos juntos, para que a ti y a nosotros nos vaya bien.</p>
<div class="pols">{ph}</div>'''))

# 17 VENTA RESPONSABLE
vr = [('id', 'No vendas a menores de edad', 'La pólvora es solo para adultos. Si tienes duda, pide la cédula.'),
      ('drop', 'Guarda bien tus productos', 'En un lugar seco, fresco y seguro, lejos del fuego y de los niños.'),
      ('doc', 'Consulta los permisos', 'Pregunta qué permisos necesitas para vender en tu barrio o municipio.'),
      ('talk', 'Enseña a usarlos', 'Explícale a tu cliente cómo usar cada producto. Un cliente feliz vuelve.')]
vh = ''.join(f'<div class="vr"><div class="vr-ic">{ic(I[k],26)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in vr)
pages.append(page(17, 'cream', 'Venta responsable', f'''
<div class="kicker">Vender bien es vender seguro</div><h2 class="big dark-t">Venta responsable</h2>
<p class="sub">Un buen negocio cuida a sus clientes. Con estos 4 consejos, tu diciembre será alegre <b>y seguro</b>.</p>
<div class="vr-grid">{vh}</div>
<div class="vr-photo"><img src="{W}Fotos-03.jpg"></div>'''))

# 18 CONTRAPORTADA
pages.append(f'''<section class="page back">
<div class="bk-top">
 <img class="bk-logo" src="{W}Logo-01.png">
 <div class="kicker gold">¿Listo para tu primer pedido?</div>
 <h1>ESCRÍBENOS<br>AL <span>WHATSAPP</span></h1>
 <p>y dinos:</p>
 <a class="bk-cta" href="{WA}">“Quiero emprender con Macías”</a>
</div>
<div class="bk-bottom">
 <div class="contacts">
  <a href="{WA}" class="ct"><img src="{W}qr-wa.png"><div>{ic(I['chat'],18,2)}<b>WhatsApp</b><span>Toca o escanea</span></div></a>
  <a href="{IG}" class="ct"><img src="{W}qr-ig.png"><div>{ic(I['ig'],18,2)}<b>Instagram</b><span>@pirotecniamacias__</span></div></a>
  <a href="{MAPS}" class="ct"><img src="{W}qr-maps.png"><div>{ic(I['pin'],18,2)}<b>Ubicación</b><span>Valledupar, Cesar</span></div></a>
 </div>
 <div class="bk-close">Macías Pirotecnia <span>|</span> Celebra cada momento.</div>
</div>
</section>''')

CSS = open(os.path.join(os.path.dirname(__file__), 'style.css')).read().replace('{F}', F)
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Emprende con Macías</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(S + '/catalogo.html', 'w').write(html)
print(len(pages), 'pages')
