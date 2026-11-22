import sys, os
S = sys.argv[1]
W = S + '/web/'
F = S + '/fonts/'
WA = 'https://wa.me/message/LAS2WAECZZRSK1'
IG = 'https://www.instagram.com/pirotecniamacias__'
MAPS = 'https://maps.app.goo.gl/aJCDFC2kRHKGPqhB8'

def m(n):  # money
    return '$' + f'{int(round(n)):,}'.replace(',', '.')

# ---------------- PRODUCT DATA (solo lista de precios) ----------------
# kind 'neg' = sin precio al detalle -> negociable ; 'unit' = con precio por unidad
def neg(name, img, price, unit_lbl, line):
    return dict(k='neg', name=name, img=img, price=price, ul=unit_lbl, line=line)
def unit(name, img, price, pack_lbl, n, sell, line, sell_lbl='cada uno'):
    return dict(k='unit', name=name, img=img, price=price, pl=pack_lbl, n=n, sell=sell, line=line, sl=sell_lbl)

TORTAS = [
    neg('Torta de 15 tiros', 'Torta-01', 120000, 'c/u', 'Pequeña, bonita y fácil de vender.'),
    neg('Torta de 16 tiros 0,8"', 'Torta-02', 50000, 'c/u', 'La más económica para empezar.'),
    neg('Torta 19 tiros calibre 25', 'Torta-03', 120000, 'c/u', 'Pirulo, árbol de plata y crisantema.'),
    neg('Torta 19 tiros calibre 30 Orión', 'Torta-04', 130000, 'c/u', 'Calibre 30: más grande, más show.'),
    neg('Torta Amazonia 25 tiros', 'Torta-05', 70000, 'c/u', '25 tiros a un precio cómodo.'),
    neg('Torta de 25 tiros 0,8"', 'Torta-06', 80000, 'c/u', 'Varios diseños para escoger.'),
    neg('Torta de 42 tiros', 'Torta-07', 130000, 'c/u', 'Más tiros, más aplausos.'),
    neg('Torta Cocodrilo 50 tiros', 'Torta-08', 160000, 'c/u', 'Sale en abanico. ¡Un show!'),
    neg('Torta Canto del Fénix 64 tiros', 'Torta-09', 200000, 'c/u', 'Llama la atención desde la caja.'),
    neg('Torta Colombiana 70 tiros', 'Torta-10', 250000, 'c/u', 'Para la noche del 24 y del 31.'),
    neg('Torta La Ricura 88 tiros 1"', 'Torta-11', 380000, 'c/u', 'Calibre de 1 pulgada. ¡Pura ricura!'),
    neg('Torta Apache 100 tiros', 'Torta-12', 350000, 'c/u', 'Para los que quieren lo grande.'),
    neg('Torta Ritmo de la Noche 100 tiros', 'Torta-13', 980000, 'caja x4', 'Viene en caja de 4: rinde para vender.'),
    neg('Torta 100 tiros Multicolor y Sauce Azul', 'Torta-14', 450000, 'c/u', 'Colores y lluvia azul en el cielo.'),
]
TORTAS_EXTRA = [('Torta de 19 tiros 0,8"', 60000), ('Torta 49 tiros 0,8"', 160000),
                ('Torta 100 tiros Tanque de Guerra', 350000), ('Torta de 138 tiros', 400000)]

SONIDO = [
    unit('Metralleta 16 tiros', 'Sonidos-05', 40000, 'paca x40', 40, 3000, 'Barata, rápida y se vende sola.'),
    unit('Mini Trueno', 'Sonidos-03', 230000, 'paca x50 cajas', 50, 8000, 'El sonido que todos piden.', 'cada caja'),
    unit('Cebollitas o Palomitas', 'Sonidos-02', 150000, 'paca x50 cajitas', 50, 5000, 'La diversión de toda la familia.', 'cada cajita'),
    unit('Mecha Mini Fo', 'Sonidos-04', 40000, 'paca x40 cajitas', 40, 2000, 'Poquita plata, buena ganancia.', 'cada cajita'),
    unit('Rosita China Craqueante', 'Sonidos-06', 60000, 'paca x12 sachets', 12, 8000, 'Gira, suena y alegra la calle.', 'cada sachet'),
    unit('Martinicas', 'Sonidos-12', 30000, 'paca x4 hojas', 4, 10000, 'Cada hoja trae 150.', 'cada hoja'),
    unit('Barril Cracker', 'Sonidos-13', 35000, 'paca x6', 6, 8000, 'Pequeño pero muy sonador.'),
    unit('Totes', 'Sonidos-08', 40000, 'paca x100', 100, 500, 'El clásico de siempre.'),
    unit('4 Golpes', 'Sonidos-01', 45000, 'paquete x20 por 6', None, 4000, 'Cuatro golpes de pura emoción.'),
]
SONIDO_EXTRA = [('Mega Pop cebollitas (24x12x20)', 82500, 5000)]

LUCES = [
    unit('Volcán No. 7 Premium', 'Volcanes-04', 300000, 'paca x12', 12, 35000, 'El volcán más vistoso de la lista.'),
    unit('Volcán Brillante', 'Volcanes-02', 72000, 'paca x12', 12, 10000, 'Brilla bonito y deja buena plata.'),
    unit('Volcán No. 4', 'Volcanes-03', 72000, 'paca x12', 12, 8000, 'Colores para alegrar la noche.'),
    unit('Volcancito', 'Volcanes-01', 15000, 'bolsa x10', 10, 3000, 'Pequeñito y facilito de vender.'),
    unit('Chispitas', 'Chispitas-01', 20000, 'caja x60 (x12 c/u)', None, 3000, 'Luz para las fotos de diciembre.', 'cada paquete'),
]
LUCES_EXTRA_UNIT = [('Vela Cracker 15 tiros (paca x12)', 75000, 10000, 12), ('Vela Cracker 20 tiros', 45000, 12000, None),
                    ('Vela Cracker 25 tiros', 50000, 14000, None), ('Vela Cracker 30 tiros', 72000, 15000, None),
                    ('Misil 25 tiros', 40000, 12000, None)]

VOLADORES = [
    neg('Viaje a Marte', 'Voladores-01', 100000, 'paca x10', 'Diez voladores que suben alto.'),
    neg('Volador 5 tiros + 1 bomba', 'Voladores-04', 50000, 'caja x6', 'Cinco tiros y cierra con bomba.'),
    neg('Cohete Lunar', 'Voladores-02', 60000, 'paca x12 bolsitas', 'Viene en bolsitas, listo para vender.'),
    neg('Volador importado 1 golpe', 'Voladores-06', 50000, 'paca x12', 'El volador de toda la vida.'),
    neg('Misil 100 tiros', 'Voladores-05', 35000, 'c/u', '100 tiros de luces en una caja.'),
]
VOL_EXTRA = [('Bazuca de Luces 888 (8x1)', 300000)]

def gain(p):
    if p['k'] != 'unit' or not p['n']:
        return None
    cost = p['price'] / p['n']
    return p['sell'] - cost, p['sell'] * p['n'] - p['price']

# ---------------- ICONS ----------------
def ic(path, size=40, color='currentColor', sw=2.2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'
I = {
 'pick': '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
 'video': '<rect x="2" y="5" width="14" height="14" rx="2"/><path d="m22 8-6 4 6 4z"/>',
 'money': '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>',
 'box': '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
 'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M8 7h8M8 11h6"/>',
 'hand': '<path d="M12 21s-7-4.4-9.3-9A5 5 0 0 1 12 6a5 5 0 0 1 9.3 6c-2.3 4.6-9.3 9-9.3 9z"/>',
 'gift': '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v9H5v-9"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 0 1 0 5"/>',
 'star': '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
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
 'calc': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15h.01M8 19h8"/>',
 'check': '<path d="M20 6 9 17l-5-5"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
}

# ---------------- COMPONENTS ----------------
TOTAL = 18
def header(label, n, dark):
    return f'''<div class="hdr"><img class="mini-logo" src="{W}Logo-01.png"><div class="hdr-lbl">{label}</div></div>
<div class="ftr"><span>Macías Pirotecnia <b>|</b> Celebra cada momento.</span><a href="{WA}" class="ftr-wa">{ic(I['chat'],12)} Pide por WhatsApp</a><span class="pg">{n:02d}</span></div>'''

def page(n, theme, label, body, extra_cls=''):
    return f'<section class="page {theme} {extra_cls}">{header(label, n, theme!="cream")}{body}</section>'

def card(p, size='m'):
    g = gain(p)
    img = f'<div class="stage"><img src="{W}{p["img"]}.jpg"></div>'
    if p['k'] == 'neg':
        prices = f'''<div class="prices"><div><small>Precio por mayor</small><b>{m(p["price"])}</b><em>{p["ul"]}</em></div>
<div><small>Precio de venta</small><b class="negb">Negociable</b><em>tú pones el precio</em></div></div>
<div class="gain neg"><span>Tú decides</span> cuánto ganas</div>'''
    else:
        if g:
            per, tot = g
            if per == int(per):
                gtxt = f'<div class="gain"><span>Ganas {m(per)}</span> por {p["sl"]}</div><div class="gain2">¡{m(tot)} por toda la paca!</div>'
            else:
                gtxt = f'<div class="gain"><span>Ganas {m(tot)}</span> por paca</div><div class="gain2">Más de $2.100 por cada uno</div>'
        else:
            gtxt = f'<div class="gain"><span>Ganas $[&nbsp;&nbsp;&nbsp;]</span> por {p["sl"]}</div><div class="gain2">Pregúntanos por WhatsApp</div>'
        prices = f'''<div class="prices"><div><small>Precio por mayor</small><b>{m(p["price"])}</b><em>{p["pl"]}</em></div>
<div><small>Vende {p["sl"]} a</small><b>{m(p["sell"])}</b><em>precio sugerido</em></div></div>{gtxt}'''
    return f'<div class="card {size}">{img}<div class="info"><h3>{p["name"]}</h3><p class="line">{p["line"]}</p>{prices}</div></div>'

def grid(items, cols, size='m', cell=''):
    return f'<div class="grid c{cols}">' + ''.join(card(p, size) for p in items) + cell + '</div>'

def cat_head(kicker, title, sub):
    return f'<div class="cat-head"><div class="kicker">{kicker}</div><h2>{title}</h2><p>{sub}</p></div>'

pages = []
# 1 PORTADA
pages.append(f'''<section class="page dark cover">
<div class="cover-bg" style="background-image:url('{W}Fotos-03.jpg')"></div>
<div class="cover-glow"></div>
<img class="cover-logo" src="{W}Logo-01.png">
<div class="cover-kicker">Catálogo para emprendedores · Diciembre 2026</div>
<h1 class="cover-title">EMPRENDE<br><span>CON MACÍAS</span></h1>
<div class="cover-hero"><div class="red-block"></div><img src="{W}Torta-11.png"></div>
<div class="cover-phrase">Este diciembre,<br><span>la plata la ganas tú.</span></div>
<div class="cover-badge"><small>Empieza con</small><b>$100.000</b></div>
<div class="cover-foot">Valledupar · Más de 10 años celebrando contigo<br><b>Macías Pirotecnia | Celebra cada momento.</b></div>
</section>''')

# 2 HISTORIA
pages.append(page(2, 'cream', 'Tu historia', f'''
<div class="story">
 <div class="story-photo"><div class="red-block tall"></div><img src="{W}Fotos-01.jpg"></div>
 <div class="story-text">
  <div class="kicker">Seamos sinceros</div>
  <h2>Cada diciembre<br>pasa lo mismo.</h2>
  <p class="big">La plata de la ropita del 24 y del 31… <b>se embolata.</b></p>
  <p>Llegan las fiestas, los gastos suben y el bolsillo no alcanza.</p>
  <div class="divider"></div>
  <p class="big">Pero hay algo que <b>nunca falta</b> en diciembre:</p>
  <div class="story-pop">LA PÓLVORA</div>
  <p>Todos la buscan. Todos la compran.<br><b>¿Y si esta vez se la vendes tú?</b></p>
 </div>
</div>
<div class="story-band"><b>No necesitas local ni saber de negocios.</b> Puedes vender desde tu casa, con tu celular. Nosotros te enseñamos.</div>
'''))

# 3 CÓMO FUNCIONA
steps = [('pick', 'Eliges tus productos', 'Miras este catálogo y escoges lo que quieres vender. Empiezas desde $100.000.'),
         ('video', 'Recibes videos y catálogo', 'Te damos videos con la marca Macías y un catálogo para que publiques en tus estados y redes.'),
         ('money', 'Vendes y ganas', 'Publicas, tus clientes te escriben, vendes… ¡y la ganancia es toda tuya!')]
st = ''.join(f'<div class="step"><div class="step-num">{i+1}</div><div class="step-ic">{ic(I[k],46)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (k, t, d) in enumerate(steps))
pages.append(page(3, 'dark', 'Cómo funciona', f'''
{cat_head('Así de fácil', 'Cómo funciona', 'Solo 3 pasos. Si sabes usar WhatsApp, sabes hacer esto.')}
<div class="steps">{st}</div>
<div class="quote-gold">“Tú pones las ganas.<br>Macías pone el producto.”</div>
'''))

# 4 QUÉ RECIBES
rec = [('box', 'Productos de calidad', 'Pólvora que la gente ya conoce y pide, a precio de mayorista.'),
       ('video', 'Videos con la marca Macías', 'Videos listos para subir a tus estados de WhatsApp y redes.'),
       ('book', 'Catálogo para vender', 'Para que tus clientes vean todo y escojan rápido.'),
       ('hand', 'Acompañamiento paso a paso', 'No te dejamos solo. Te ayudamos desde tu primer pedido.')]
rc = ''.join(f'<div class="rec"><div class="rec-ic">{ic(I[k],34)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in rec)
pages.append(page(4, 'cream', 'Qué recibes', f'''
{cat_head('Todo lo que te llevas', 'Qué recibes', 'No solo compras pólvora. Te llevas un negocio listo para arrancar.')}
<div class="rec-grid">{rc}</div>
<div class="rec-photo"><div class="red-block wide"></div><img src="{W}Fotos-02.jpg"></div>
'''))

# 5-7 TORTAS
pages.append(page(5, 'dark', 'Tortas pirotécnicas', f'''
{cat_head('Categoría 1', 'Tortas pirotécnicas', 'Las reinas del 24 y del 31. Tú pones el precio de venta y decides tu ganancia.')}
{grid(TORTAS[0:4], 2, 'l')}'''))
pages.append(page(6, 'cream', 'Tortas pirotécnicas', f'''{grid(TORTAS[4:10], 2, 's')}'''))
extra = ''.join(f'<li><span>{n}</span><b>{m(p)}</b></li>' for n, p in TORTAS_EXTRA)
pages.append(page(7, 'dark', 'Tortas pirotécnicas', f'''{grid(TORTAS[10:14], 2, 'm')}
<div class="extra"><h4>También tenemos <small>(pídenos la foto por WhatsApp)</small></h4><ul>{extra}</ul><p>Precio de venta: <b>negociable</b>. Tú decides tu ganancia.</p></div>'''))

# 8-9 SONIDO
pages.append(page(8, 'cream', 'Sonido y explosión', f'''
{cat_head('Categoría 2', 'Sonido y explosión', 'Lo que más se mueve en la cuadra. Compras la paca y vendes por unidad.')}
{grid(SONIDO[0:4], 2, 'l')}'''))
mp = SONIDO_EXTRA[0]
pages.append(page(9, 'dark', 'Sonido y explosión', f'''{grid(SONIDO[4:9], 3, 'xs', f'<div class="xcell"><h4>También tenemos</h4><ul><li>{mp[0]}<b>{m(mp[1])} · vende c/u a {m(mp[2])}</b></li></ul><p style="margin-top:3mm">Pídenos la foto y te contamos la ganancia.</p><a class="xbtn" href="{WA}">Pedir por WhatsApp</a></div>')}'''))

# 10 LUCES Y VOLCANES
ex = ''
for n_, pp, s_, c_ in LUCES_EXTRA_UNIT:
    gtxt = f'ganas {m(s_ - pp / c_)} c/u' if c_ else 'ganancia $[&nbsp;&nbsp;]'
    ex += f'<li>{n_}<b>{m(pp)} → c/u a {m(s_)} · {gtxt}</b></li>'
pages.append(page(10, 'cream', 'Bengalas, luces y volcanes', f'''
{cat_head('Categoría 3', 'Luces y volcanes', 'Brillan bonito, no asustan y son perfectos para las fotos en familia.')}
{grid(LUCES, 3, 'xs', f'<div class="xcell"><h4>Más luces</h4><ul>{ex}<li>{VOL_EXTRA[0][0]}<b>{m(VOL_EXTRA[0][1])} · venta negociable</b></li></ul></div>')}'''))

# 11 VOLADORES
pages.append(page(11, 'dark', 'Voladores y misiles', f'''
{cat_head('Categoría 4', 'Voladores y misiles', 'Suben, suenan y llenan el cielo. Tú pones el precio de venta.')}
{grid(VOLADORES, 3, 'xs', f'<div class="xcell"><h4>{VOL_EXTRA[0][0]}</h4><p>Por mayor: <b>{m(VOL_EXTRA[0][1])}</b><br>Precio de venta: <b>negociable</b></p><p style="margin-top:3mm">¿No ves un producto aquí? <b>Escríbenos.</b> Te mandamos la foto y el precio.</p><a class="xbtn" href="{WA}">Pedir por WhatsApp</a></div>')}'''))

# 12 MÁS VENDIDOS
best = [SONIDO[0], SONIDO[1], LUCES[0], SONIDO[2]]
bc = ''
for i, p in enumerate(best):
    per, tot = gain(p)
    bc += f'''<div class="best"><div class="best-rank">#{i+1}</div><div class="stage"><img src="{W}{p["img"]}.jpg"></div>
<h3>{p["name"]}</h3><div class="best-g"><small>Ganas</small><b>{m(per)}</b><small>por {p["sl"]}</small></div><div class="best-t">{m(tot)} por paca</div></div>'''
pages.append(page(12, 'red', 'Los más vendidos', f'''
<div class="cat-head center"><div class="kicker">Lo que más sale</div><h2>Los más vendidos</h2><p>Si no sabes por dónde empezar, empieza por aquí.</p></div>
<div class="best-grid">{bc}</div>
<div class="fire-line">{ic(I['star'],18)} Fáciles de vender · Buena ganancia · Los clientes los piden {ic(I['star'],18)}</div>'''))

# 13 KITS
kits = [
 ('Kit Arranque', 'Para empezar sin miedo', [(SONIDO[0], 1), (SONIDO[3], 1), (LUCES[3], 1), (SONIDO[5], 1)]),
 ('Kit Pro', 'Para los que van en serio', [(SONIDO[2], 1), (LUCES[2], 1), (LUCES[1], 1), ('vela', 1), (SONIDO[0], 1)]),
 ('Kit Jefe', 'Para mandar en diciembre', [(SONIDO[1], 1), (SONIDO[2], 1), (LUCES[0], 1), (SONIDO[4], 1), ('vela', 1)]),
]
VELA = dict(name='Vela Cracker 15 tiros', price=75000, n=12, sell=10000, pl='paca x12')
kh = ''
for i, (kn, ks, items) in enumerate(kits):
    inv = venta = 0; lis = ''
    for it, q in items:
        p = VELA if it == 'vela' else it
        inv += p['price']; venta += p['sell'] * p['n']
        lis += f'<li>{ic(I["check"],14)} 1 {p["pl"].split(" ")[0]} de {p["name"]}</li>'
    tag = '<div class="kit-tag">¡Incluye bono de bienvenida!</div>' if inv >= 750000 else ''
    kh += f'''<div class="kit k{i}">{tag}<div class="kit-top"><h3>{kn}</h3><p>{ks}</p></div><ul>{lis}</ul>
<div class="kit-nums"><div><small>Inviertes</small><b>{m(inv)}</b></div><div><small>Vendes</small><b>{m(venta)}</b></div></div>
<div class="kit-gain"><small>Tu ganancia</small><b>{m(venta - inv)}</b></div></div>'''
pages.append(page(13, 'cream', 'Kits armados', f'''
{cat_head('Combos listos', 'Kits armados', 'No pienses mucho: escoge tu kit, pídelo por WhatsApp y empieza a vender.')}
<div class="kits">{kh}</div>
<p class="fine">Ganancia calculada vendiendo todo al precio sugerido de la lista de precios Macías.</p>
<div class="band"><img src="{W}Fotos-02.jpg"><div><h3>¿Quieres otro combo?</h3><p>Dinos cuánta plata quieres invertir y te ayudamos a escoger los productos. Recuerda: <b>desde $750.000</b> te llevas el bono de bienvenida.</p></div></div>'''))

# 14 PROPUESTAS: ESCALERA + BONOS
lad = [('$100.000', 'Empiezas tu negocio', 'Productos + videos con la marca Macías + acompañamiento.', 'box'),
       ('$750.000', 'Bono de bienvenida', 'Con tu primer pedido desde $750.000 te damos un regalo.', 'gift'),
       ('Más de $1.200.000', 'Tu propio catálogo', 'Un catálogo personalizado con el logo de Macías y todos tus productos, más los mensajes listos para WhatsApp. Sin precios, para que tú pongas los tuyos.', 'book'),
       ('$[        ]', 'Descuento extra', 'Descuento de [   ]% en tu pedido.', 'tag'),
       ('$[        ]', 'Envío gratis', 'Te llevamos el pedido sin costo.', 'truck')]
lh = ''.join(f'<div class="rung r{i}"><div class="rung-ic">{ic(I[k],28)}</div><div class="rung-amt"><small>Desde</small>{a}</div><div class="rung-txt"><h3>{t}</h3><p>{d}</p></div></div>' for i, (a, t, d, k) in enumerate(lad))
pages.append(page(14, 'dark', 'Propuestas irresistibles', f'''
{cat_head('Entre más compras, más ganas', 'La escalera de beneficios', 'Cada escalón te da algo más. ¿Hasta dónde quieres subir?')}
<div class="ladder">{lh}</div>
<div class="urgent">{ic(I['clock'],30)}<div><b>Precios especiales hasta el [&nbsp;&nbsp;&nbsp;] de diciembre.</b><span>Después de esa fecha, los precios pueden cambiar. ¡No lo dejes para después!</span></div></div>'''))

# 15 CALCULADORA + GUIA + MENSAJES
calc_items = [SONIDO[0], SONIDO[1], LUCES[1], LUCES[0]]
ch = ''
for p in calc_items:
    per, tot = gain(p)
    ch += f'<div class="calc-row"><span>Si vendes <b>10</b> {p["name"]}</span><i></i><b class="cg">ganas {m(per*10)}</b></div>'
msgs = ['🎆 ¡Llegó la pólvora de diciembre! Tortas, volcanes y más. Escríbeme y te mando fotos y precios. 🔥',
        '✨ Este 24 y 31 celebra en grande. Tengo productos Macías listos para entregar. ¡Pide el tuyo antes de que se acaben!',
        '🎇 ¿Ya tienes la pólvora para la noche buena? Te la llevo. Pregúntame sin compromiso. 📲']
mh = ''.join(f'<div class="msg">{x}</div>' for x in msgs)
pages.append(page(15, 'cream', 'Herramientas de regalo', f'''
<div class="two">
 <div class="calc"><div class="calc-head">{ic(I['calc'],30)}<h2>Calculadora<br>sencilla</h2></div>{ch}
 <p class="fine">Con los precios sugeridos de este catálogo.</p></div>
 <div class="gifts">
  <div class="kicker">De regalo para ti</div>
  <h2>Guía de ventas<br>+ mensajes listos</h2>
  <p>Te regalamos una guía fácil para vender y mensajes listos para tus <b>estados de WhatsApp</b>. Solo copias, pegas y publicas.</p>
  <div class="msgs"><div class="msgs-title">{ic(I['chat'],16)} Así se ven tus mensajes:</div>{mh}</div>
 </div>
</div>
<div class="cta-band"><div><h3>Ya hiciste las cuentas. Ahora te toca a ti.</h3><p>Escríbenos: <b>“Quiero emprender con Macías”</b></p></div><a href="{WA}">Ir a WhatsApp</a></div>'''))

# 16 POLITICAS
pol = [('money', 'Empieza desde $100.000', 'Tu primer pedido puede ser desde $100.000. Así empiezas tranquilo.'),
       ('video', 'Videos solo para clientes Macías', 'Los videos con la marca Macías se entregan únicamente a quienes compran sus productos en Macías. Si los productos no se compran con nosotros, no se entregan los videos.'),
       ('shield', 'Cuida la marca', 'Los videos solo se usan para vender productos comprados en Macías. No se pueden editar ni quitarles la marca.'),
       ('money', 'Pagos', '[  Escribe aquí cómo se paga: efectivo, transferencia, Nequi…  ]'),
       ('truck', 'Entregas', '[  Escribe aquí cómo y cuándo se entregan los pedidos  ]'),
       ('doc', 'Cambios', '[  Escribe aquí la política de cambios  ]')]
ph = ''.join(f'<div class="pol"><div class="pol-ic">{ic(I[k],26)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for k, t, d in pol)
pages.append(page(16, 'dark', 'Políticas', f'''
{cat_head('Reglas claras, negocio tranquilo', 'Políticas de Emprende con Macías', 'Así trabajamos juntos, para que a ti y a nosotros nos vaya bien.')}
<div class="pols">{ph}</div>'''))

# 17 VENTA RESPONSABLE
vr = [('id', 'No vendas a menores de edad', 'La pólvora es solo para adultos. Si tienes duda, pide la cédula.'),
      ('drop', 'Guarda bien tus productos', 'En un lugar seco, fresco y seguro, lejos del fuego y de los niños.'),
      ('doc', 'Consulta los permisos', 'Pregunta qué permisos necesitas para vender en tu barrio o municipio.'),
      ('talk', 'Enseña a usarlos', 'Explícale a tu cliente cómo usar cada producto. Un cliente feliz vuelve.')]
vh = ''.join(f'<div class="vr"><div class="vr-ic">{ic(I[k],34)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in vr)
pages.append(page(17, 'cream', 'Venta responsable', f'''
<div class="vr-banner" style="background-image:url('{W}Fotos-03.jpg')"><div><div class="kicker">Vender bien es vender seguro</div><h2>Venta responsable</h2></div></div>
<p class="vr-intro">Un buen negocio cuida a sus clientes. Con estos 4 consejos, tu diciembre será alegre <b>y seguro</b>.</p>
<div class="vr-grid">{vh}</div>'''))

# 18 CONTRAPORTADA
pages.append(f'''<section class="page dark back">
<div class="cover-bg" style="background-image:url('{W}Fotos-03.jpg');opacity:.55"></div><div class="cover-glow"></div>
<img class="back-logo" src="{W}Logo-01.png">
<div class="back-kicker">¿Listo para tu primer pedido?</div>
<h1 class="back-title">ESCRÍBENOS<br>AL <span>WHATSAPP</span></h1>
<div class="back-say">y dinos:</div>
<a class="back-cta" href="{WA}">“Quiero emprender con Macías”</a>
<div class="contacts">
 <a href="{WA}" class="ct"><img src="{W}qr-wa.png"><div>{ic(I['chat'],20)}<b>WhatsApp</b><span>Toca o escanea</span></div></a>
 <a href="{IG}" class="ct"><img src="{W}qr-ig.png"><div>{ic(I['ig'],20)}<b>Instagram</b><span>@pirotecniamacias__</span></div></a>
 <a href="{MAPS}" class="ct"><img src="{W}qr-maps.png"><div>{ic(I['pin'],20)}<b>Ubicación</b><span>Valledupar, Cesar</span></div></a>
</div>
<div class="back-close">Macías Pirotecnia <span>|</span> Celebra cada momento.</div>
</section>''')

CSS = open(os.path.join(os.path.dirname(__file__), 'style.css')).read().replace('{F}', F)
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Emprende con Macías</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(S + '/catalogo.html', 'w').write(html)
print(len(pages), 'pages')
