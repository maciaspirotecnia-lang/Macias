import sys, os
S = sys.argv[1]
W = S + '/web3/'
F = S + '/fonts/'
WA = 'https://wa.me/message/LAS2WAECZZRSK1'
IG = 'https://www.instagram.com/pirotecniamacias__'
MAPS = 'https://maps.app.goo.gl/aJCDFC2kRHKGPqhB8'
FECHA = '4 de diciembre'

def m(n):
    return '$' + f'{int(round(n)):,}'.replace(',', '.')

# ---------------- PRODUCTOS (misma información de la versión 2) ----------------
def neg(name, img, price, ul, line, tag=None):
    return dict(k='neg', name=name, img=img, price=price, ul=ul, line=line, tag=tag)
def unit(name, img, price, pl, n, sell, line, sl='cada uno', tag=None):
    return dict(k='unit', name=name, img=img, price=price, pl=pl, n=n, sell=sell, line=line, sl=sl, tag=tag)

TAG_TOP = ('MÁS VENDIDO', 'gold')
TAG_WIN = ('MÁS GANANCIA', 'red')
TAG_START = ('IDEAL PARA EMPEZAR', 'cream')
TAG_BIG = ('PARA GANAR EN GRANDE', 'gold')

TOTES = unit('Totes', 'Sonidos-08', 40000, 'paca x100', 100, 500, 'El que más se lleva la gente.', tag=TAG_TOP)
METRA = unit('Metralleta 16 tiros', 'Sonidos-05', 40000, 'paca x40', 40, 3000, 'Barata, rápida y se vende sola.', tag=TAG_START)
TRUENO = unit('Mini Trueno', 'Sonidos-03', 230000, 'paca x50 cajas', 50, 8000, 'El sonido que todos piden.', 'cada caja', tag=TAG_WIN)
CEBO = unit('Cebollitas o Palomitas', 'Sonidos-02', 150000, 'paca x50 cajitas', 50, 5000, 'Diversión para toda la familia.', 'cada cajita')
MECHA = unit('Mecha Mini Fo', 'Sonidos-04', 40000, 'paca x40 cajitas', 40, 2000, 'Poquita plata, buena ganancia.', 'cada cajita', tag=TAG_START)
ROSITA = unit('Rosita China Craqueante', 'Sonidos-06', 60000, 'paca x12 sachets', 12, 8000, 'Gira, suena y alegra la calle.', 'cada sachet')
MARTI = unit('Martinicas', 'Sonidos-12', 30000, 'paca x4 hojas', 4, 10000, 'Cada hoja trae 150.', 'cada hoja')
BARRIL = unit('Barril Cracker', 'Sonidos-13', 35000, 'paca x6', 6, 8000, 'Pequeño pero muy sonador.')
GOLPES = neg('4 Golpes', 'Sonidos-01', 45000, 'paquete x20 por 6', 'Cuatro golpes de pura emoción.')

V7 = unit('Volcán No. 7 Premium', 'Volcanes-04', 300000, 'paca x12', 12, 35000, 'El volcán más vistoso de la lista.', tag=TAG_WIN)
VBRI = unit('Volcán Brillante', 'Volcanes-02', 72000, 'paca x12', 12, 10000, 'Brilla bonito y deja buena plata.')
V4 = unit('Volcán No. 4', 'Volcanes-03', 72000, 'paca x12', 12, 8000, 'Colores para alegrar la noche.')
VCITO = unit('Volcancito', 'Volcanes-01', 15000, 'bolsa x10', 10, 3000, 'Pequeñito y facilito de vender.', tag=TAG_START)
CHISP = unit('Chispitas', 'Chispitas-01', 20000, 'paca x12 cajitas', 12, 3000, 'Luz para las fotos de diciembre.', 'cada cajita')
VELA = dict(name='Vela Cracker 15 tiros', price=75000, n=12, sell=10000, pl='paca x12', img=None)
LUCES_EXTRA = [('Vela Cracker 15 tiros · paca x12', f'{m(75000)} · vende a {m(10000)} · ganas {m(10000-75000/12)} c/u'),
               ('Vela Cracker 20 · 25 · 30 tiros', f'{m(45000)} · {m(50000)} · {m(72000)}'),
               ('Misil 25 tiros', f'{m(40000)}'),
               ('Bazuca de Luces 888 (8x1)', f'{m(300000)}')]

TORTAS = [
    neg('Torta Británica 15 tiros', 'Torta-01', 120000, 'c/u', 'Pequeña, bonita y fácil de vender.'),
    neg('Torta de 16 tiros 0,8"', 'Torta-02', 50000, 'c/u', 'La más económica para empezar.', TAG_START),
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
RITMO = neg('Torta Ritmo de la Noche 100 tiros', 'Torta-13', 980000, 'caja x4', 'Viene en caja de 4: rinde para vender.', TAG_BIG)
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
 'quote': '<path d="M3 21c3 0 7-1 7-8V5H3v8h4c0 4-2 5-4 5zM14 21c3 0 7-1 7-8V5h-7v8h4c0 4-2 5-4 5z"/>',
}
WA_ICON = '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'

# ---------------- COMPONENTES ----------------
def chrome(label, n):
    return f'''<div class="hdr"><img class="mini-logo" src="{W}Logo-01.png"><div class="hdr-lbl"><i></i>{label}</div></div>
<div class="ftr"><span class="ftr-close">Macías Pirotecnia <b>|</b> Celebra cada momento.</span><a class="wa-btn" href="{WA}">{WA_ICON} Pide por WhatsApp</a><span class="pg">{n:02d}</span></div>'''

def page(n, theme, label, body):
    return f'<section class="page {theme}">{chrome(label, n)}{body}</section>'

def tag_html(p):
    t = p.get('tag')
    return f'<span class="tag t-{t[1]}">{t[0]}</span>' if t else ''

def ganancia(p):
    """Bloque de ganancia: lo más grande de la tarjeta."""
    if p['k'] == 'neg':
        return '<div class="win neg"><small>Tu ganancia</small><b>Tú decides</b><em>Tú pones el precio de venta</em></div>'
    per, tot = gain(p)
    if per == int(per):
        return f'<div class="win"><small>Ganas</small><b>{m(per)}</b><em>por {p["sl"]}<br><strong>{m(tot)} la paca</strong></em></div>'
    return f'<div class="win"><small>Ganas</small><b>{m(tot)}</b><em>por paca<br><strong>más de {m(int(per // 100) * 100)} c/u</strong></em></div>'

def precios(p):
    unit_lbl = p['ul'] if p['k'] == 'neg' else p['pl']
    sell = '<span class="soft">Venta: negociable</span>' if p['k'] == 'neg' else f'Lo vendes a <b>{m(p["sell"])}</b> {p["sl"]}'
    return f'<div class="price"><span>Por mayor</span><b>{m(p["price"])}</b><em>{unit_lbl}</em></div><div class="sell">{sell}</div>'

def card_v(p, v):  # vertical: 4 por página
    return f'''<div class="cv"><div class="stage s-{v}"><img src="{W}{p["img"]}_{v}.jpg">{tag_html(p)}</div>
<div class="cv-body">{ganancia(p)}<h3>{p["name"]}</h3>{precios(p)}</div></div>'''

def card_h(p, v):  # horizontal: 6 por página
    return f'''<div class="ch"><div class="stage s-{v}"><img src="{W}{p["img"]}_{v}.jpg">{tag_html(p)}</div>
<div class="ch-body">{ganancia(p)}<h3>{p["name"]}</h3>{precios(p)}</div></div>'''

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
N = [0]
def nxt():
    N[0] += 1
    return N[0]

# 1 PORTADA (emoción)
nxt()
pages.append(f'''<section class="page cover">
<div class="cv-photo" style="background-image:url('{W}cover.jpg')"></div>
<img class="cv-logo" src="{W}Logo-01.png">
<div class="cv-band">
 <div class="cv-kicker">Catálogo para emprendedores · Diciembre 2026</div>
 <h1>EMPRENDE CON <span>MACÍAS</span></h1>
 <p class="cv-phrase">Este diciembre, <b>la plata la ganas tú.</b></p>
 <div class="cv-meta">
  <div><b>Inversión</b>desde $100.000</div>
  <div><b>Precios especiales</b>hasta el {FECHA}</div>
  <div><b>Valledupar</b>más de 10 años</div>
 </div>
</div>
<div class="cv-strip">Macías Pirotecnia <span>|</span> Celebra cada momento.</div>
</section>''')

# 2 HISTORIA (emoción)
pages.append(page(nxt(), 'cream', 'Tu historia', f'''
<div class="st-photo"><img src="{W}Fotos-03.jpg"></div>
<div class="kicker">Seamos sinceros</div>
<h2 class="big dark-t">Cada diciembre pasa lo mismo.</h2>
<p class="lead">La plata de la ropita del 24 y del 31… <b>se embolata.</b></p>
<p class="body">Llegan las fiestas, los gastos suben y el bolsillo no alcanza.</p>
<div class="st-turn">
 <p>Pero hay algo que <b>nunca falta</b> en diciembre:</p>
 <div class="st-big">LA PÓLVORA</div>
 <p>Todos la buscan. Todos la compran. <b>¿Y si esta vez se la vendes tú?</b></p>
</div>
'''))

# 3 CONFIANZA
pages.append(page(nxt(), 'dark', 'Confianza', f'''
<div class="kicker">Por qué confiar en Macías</div>
<div class="tr-hero"><div class="tr-num">+10</div><div><h2>AÑOS EN<br><span>VALLEDUPAR</span></h2><p>Más de 10 años celebrando contigo. Sabemos lo que la gente compra en diciembre.</p></div></div>
<div class="tr-obj"><h3>“Pero yo no sé de negocios…”</h3><p>Tranquilo, no tienes que saber. Tú vendes y nosotros te acompañamos paso a paso.</p></div>
<div class="tr-test">
 <div class="tr-q">{ic(I['quote'],34,1.4)}</div>
 <div class="tr-ph">[TESTIMONIO]</div>
 <p class="tr-hint">Aquí va la experiencia real de un aliado Macías.</p>
 <div class="tr-who">— [Nombre del aliado] · [Barrio]</div>
</div>
'''))

# 4 CÓMO FUNCIONA (confianza)
steps = [('pick', 'Eliges tus productos', 'Miras este catálogo y escoges lo que quieres vender. Empiezas desde $100.000.'),
         ('video', 'Recibes videos y catálogo', 'Te damos videos con la marca Macías y un catálogo para tus estados y redes.'),
         ('money', 'Vendes y ganas', 'Publicas, tus clientes te escriben, vendes… y la ganancia es toda tuya.')]
st = ''.join(f'<div class="step"><div class="step-num">0{i+1}</div><div class="step-ic">{ic(I[k],30)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (k, t, d) in enumerate(steps))
pages.append(page(nxt(), 'cream', 'Cómo funciona', f'''
<div class="kicker">Así de fácil</div><h2 class="big dark-t">Cómo funciona</h2>
<p class="sub">Solo 3 pasos. Si sabes usar WhatsApp, sabes hacer esto.</p>
<div class="steps">{st}</div>
<div class="quote">“Tú pones las ganas.<br><span>Macías pone el producto.”</span></div>
'''))

# 5 QUÉ RECIBES (confianza)
rec = [('box', 'Productos de calidad', 'Pólvora que la gente ya conoce y pide, a precio de mayorista.'),
       ('video', 'Videos con la marca Macías', 'Listos para subir a tus estados de WhatsApp y redes.'),
       ('book', 'Catálogo para vender', 'Para que tus clientes vean todo y escojan rápido.'),
       ('hand', 'Acompañamiento paso a paso', 'No te dejamos solo. Te ayudamos desde tu primer pedido.')]
rc = ''.join(f'<div class="rec"><div class="rec-ic">{ic(I[k],26)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in rec)
pages.append(page(nxt(), 'dark', 'Qué recibes', f'''
<div class="rc-photo"><div class="blk"></div><img src="{W}Fotos-02.jpg"></div>
<div class="kicker">Todo lo que te llevas</div><h2 class="big">Qué recibes</h2>
<p class="sub">No solo compras pólvora. Te llevas un negocio listo para arrancar.</p>
<div class="rec-grid">{rc}</div>
'''))

# 6 SONIDO 1 — LOS MÁS VENDIDOS
pages.append(page(nxt(), 'cream', 'Sonido y explosión', f'''
{opener('01', 'Los más vendidos', 'Sonido y explosión: lo que más se lleva la gente. Compras la paca y vendes por unidad.')}
{grid_v([TOTES, METRA, TRUENO, CEBO], 'l')}'''))

# 7 SONIDO 2
pages.append(page(nxt(), 'dark', 'Sonido y explosión', f'''
{mini_head('Más sonido y explosión', 'Pacas baratas que se venden por unidad.')}
{grid_h([MECHA, ROSITA, MARTI, BARRIL, GOLPES], 'd', xcell('También tenemos', [('Mega Pop cebollitas (24x12x20)', f'{m(82500)} · venta negociable')]), cls=' mh')}'''))

# 8 LUCES
pages.append(page(nxt(), 'cream', 'Luces y volcanes', f'''
{opener('02', 'Luces y volcanes', 'Brillan bonito, no asustan y son perfectos para las fotos en familia.')}
{grid_h([V7, VBRI, V4, VCITO, CHISP], 'l', xcell('Más luces', LUCES_EXTRA, '<p class="xnote">Venta negociable, menos la vela de 15.</p>'))}'''))

# 9-11 TORTAS
pages.append(page(nxt(), 'dark', 'Tortas pirotécnicas', f'''
{opener('03', 'Tortas pirotécnicas', 'Las reinas del 24 y del 31. Tú pones el precio de venta y decides tu ganancia.')}
{grid_h(TORTAS[0:6], 'd')}'''))
pages.append(page(nxt(), 'cream', 'Tortas pirotécnicas', f'''
{mini_head('Más tortas', 'Para la noche buena y el año nuevo.')}
{grid_h(TORTAS[6:12], 'l', cls=' mh')}'''))
ex = ''.join(f'<li><span>{n}</span><b>{m(p)}</b></li>' for n, p in TORTAS_EXTRA)
pages.append(page(nxt(), 'dark', 'Tortas pirotécnicas', f'''
{mini_head('La torta estrella', 'Para los que quieren ganar en grande.')}
<div class="feat"><div class="stage s-d"><img src="{W}{RITMO["img"]}_d.jpg">{tag_html(RITMO)}</div>
<div class="feat-body">{ganancia(RITMO)}<h3>{RITMO["name"]}</h3><p class="fline">{RITMO["line"]}</p>{precios(RITMO)}</div></div>
<div class="two-cells">
 <div class="xcell"><h4>También tenemos</h4><ul class="rows">{ex}</ul><p class="xnote">Venta negociable. Pídenos la foto.</p></div>
 <div class="help"><div class="help-q">?</div><h3>¿No sabes cuál torta escoger?</h3><p>Escríbenos y te ayudamos a elegir las que mejor se venden en tu barrio.</p></div>
</div>'''))

# 12 VOLADORES
pages.append(page(nxt(), 'cream', 'Voladores y misiles', f'''
{opener('04', 'Voladores y misiles', 'Suben, suenan y llenan el cielo. Tú pones el precio de venta.')}
{grid_h(VOLADORES, 'l', '<div class="xcell"><h4>¿No ves un producto?</h4><p class="xp">Escríbenos y te mandamos la foto y el precio.</p></div>')}'''))

# 13 GANANCIA — LOS QUE MÁS PLATA TE DEJAN
rank = sorted([TRUENO, V7, CEBO, METRA, VBRI, MECHA], key=lambda p: -gain(p)[1])
rk = ''
for i, p in enumerate(rank):
    per, tot = gain(p)
    rk += f'''<div class="rk"><div class="rk-n">0{i+1}</div><img src="{W}{p["img"]}_d.jpg"><div class="rk-t"><span>Si vendes 1 {p["pl"].split(" ")[0]} de</span><b>{p["name"]}</b><em>Inviertes {m(p["price"])}</em></div><div class="rk-g"><small>Ganas</small><b>{m(tot)}</b></div></div>'''
pages.append(page(nxt(), 'dark', 'Tu ganancia', f'''
<div class="kicker">Haz la cuenta</div><h2 class="big">Los que más plata <span class="gold-t">te dejan</span></h2>
<p class="sub">Mira cuánto te puede quedar en el bolsillo con cada paca.</p>
<div class="ranking">{rk}</div>
<div class="calc-box"><p>Si vendes <b>3 pacas de Metralleta</b>, inviertes {m(120000)}…</p><div>y te quedan <span>{m(240000)}</span> de ganancia.</div></div>
<p class="fine">Cuentas hechas vendiendo toda la paca al precio sugerido de este catálogo.</p>'''))

# 14 KITS
kits = [('Kit Arranque', 'Para empezar sin miedo', [METRA, MECHA, VCITO, TOTES]),
        ('Kit Pro', 'Para los que van en serio', [CEBO, V4, VBRI, VELA, METRA]),
        ('Kit Jefe', 'Para mandar en diciembre', [TRUENO, CEBO, V7, ROSITA, VELA])]
kh = ''
for i, (kn, ks, items) in enumerate(kits):
    inv = sum(p['price'] for p in items); venta = sum(p['sell'] * p['n'] for p in items)
    thumbs = ''.join(f'<img src="{W}{p["img"]}_l.jpg">' for p in items if p.get('img'))[:2000]
    lis = ''.join(f'<li>{ic(I["check"],13,2)} 1 {p["pl"].split(" ")[0]} de {p["name"]}</li>' for p in items)
    bono = '<div class="kit-bono">+ Bono de bienvenida</div>' if inv >= 750000 else ''
    kh += f'''<div class="kit k{i}"><div class="kit-top"><h3>{kn}</h3><p>{ks}</p></div><div class="kit-th">{thumbs}</div>
<div class="kit-gain"><small>Tu ganancia</small><b>{m(venta - inv)}</b></div>
<div class="kit-nums"><div><small>Inviertes</small><b>{m(inv)}</b></div><div><small>Vendes</small><b>{m(venta)}</b></div></div>
<ul>{lis}</ul>{bono}</div>'''
pages.append(page(nxt(), 'cream', 'Kits armados', f'''
<div class="kicker">Combos listos</div><h2 class="big dark-t">Kits armados</h2>
<p class="sub">No pienses mucho: escoge tu kit, pídelo por WhatsApp y empieza a vender.</p>
<div class="kits">{kh}</div>
<p class="fine">Ganancia calculada vendiendo todo al precio sugerido de este catálogo.</p>
<div class="band"><h3>¿Quieres otro combo?</h3><p>Dinos cuánta plata quieres invertir y te ayudamos a escoger. Desde <b>$750.000</b> te llevas el bono de bienvenida.</p></div>'''))

# 15 ESCALERA (oferta)
lad = [('Desde', '$100.000', 'Empiezas tu negocio', 'Productos + videos con la marca Macías + acompañamiento.', 'box'),
       ('Desde', '$750.000', 'Bono de bienvenida', 'Con tu primer pedido desde $750.000 te damos un regalo.', 'gift'),
       ('Compras', 'Más de $1.200.000', 'Tu propio catálogo', 'Un catálogo con el logo de Macías y tus productos, sin precios para que pongas los tuyos. Más los mensajes listos para WhatsApp.', 'book'),
       ('Desde', '$[        ]', 'Descuento extra', 'Descuento de [   ]% en tu pedido.', 'tag'),
       ('Desde', '$[        ]', 'Envío gratis', 'Te llevamos el pedido sin costo.', 'truck')]
lh = ''.join(f'<div class="rung r{i}"><div class="rung-ic">{ic(I[k],24)}</div><div class="rung-amt"><small>{s}</small>{a}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (s, a, t, d, k) in enumerate(lad))
pages.append(page(nxt(), 'dark', 'Beneficios', f'''
<div class="kicker">Entre más compras, más ganas</div><h2 class="big">Escalera de beneficios</h2>
<p class="sub">Cada escalón te da algo más. ¿Hasta dónde quieres subir?</p>
<div class="ladder">{lh}</div>
<div class="urgent">{ic(I['clock'],30)}<div><b>Precios especiales hasta el {FECHA}.</b><span>Después de esa fecha los precios pueden cambiar.</span></div></div>'''))

# 16 REGALOS (oferta)
msgs = ['🎆 ¡Llegó la pólvora de diciembre! Totes, volcanes, tortas y más. Escríbeme y te mando fotos y precios. 🔥',
        '✨ Este 24 y 31 celebra en grande. Tengo productos Macías listos para entregar. ¡Pide el tuyo antes de que se acaben!',
        '🎇 ¿Ya tienes la pólvora para la noche buena? Te la llevo. Pregúntame sin compromiso. 📲']
mh = ''.join(f'<div class="msg">{x}</div>' for x in msgs)
pages.append(page(nxt(), 'cream', 'De regalo', f'''
<div class="kicker">De regalo para ti</div><h2 class="big dark-t">Te lo damos listo</h2>
<p class="sub">Con tu pedido te regalamos una <b>guía de ventas</b> y <b>mensajes listos</b> para tus estados de WhatsApp. Solo copias, pegas y publicas.</p>
<div class="gift-row">
 <div class="gift"><div class="rec-ic">{ic(I['book'],26)}</div><h3>Guía de ventas</h3><p>Pasos fáciles para vender más rápido.</p></div>
 <div class="gift"><div class="rec-ic">{ic(I['chat'],26)}</div><h3>Mensajes listos</h3><p>Para tus estados de WhatsApp.</p></div>
 <div class="gift"><div class="rec-ic">{ic(I['video'],26)}</div><h3>Videos Macías</h3><p>Con la marca, listos para subir.</p></div>
</div>
<div class="msgs"><div class="msgs-title">{ic(I['chat'],16,2)} Así se ven tus mensajes</div>{mh}</div>'''))

# 17 POLÍTICAS
pol = [('money', 'Empieza desde $100.000', 'Tu primer pedido puede ser desde $100.000. Así empiezas tranquilo.'),
       ('key', 'Pagos', 'Pagas por llave o en efectivo. Fácil y rápido.'),
       ('video', 'Videos solo para clientes Macías', 'Los videos con la marca Macías se entregan únicamente a quienes compran sus productos en Macías. Si los productos no se compran con nosotros, no se entregan los videos.'),
       ('shield', 'Cuida la marca', 'Los videos solo se usan para vender productos comprados en Macías. No se pueden editar ni quitarles la marca.'),
       ('eye', 'Revisa tu pedido', 'Al recibir, revisa bien todos tus productos antes de irte.'),
       ('doc', 'Sin devoluciones', 'No se hacen devoluciones. Por eso es importante revisar todo al recibir.')]
ph = ''.join(f'<div class="pol"><div class="pol-ic">{ic(I[k],22)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for k, t, d in pol)
pages.append(page(nxt(), 'dark', 'Políticas', f'''
<div class="kicker">Reglas claras, negocio tranquilo</div><h2 class="big">Nuestras políticas</h2>
<p class="sub">Así trabajamos juntos, para que a ti y a nosotros nos vaya bien.</p>
<div class="pols">{ph}</div>'''))

# 18 VENTA RESPONSABLE
vr = [('id', 'No vendas a menores de edad', 'La pólvora es solo para adultos. Si tienes duda, pide la cédula.'),
      ('drop', 'Guarda bien tus productos', 'En un lugar seco, fresco y seguro, lejos del fuego y de los niños.'),
      ('doc', 'Consulta los permisos', 'Pregunta qué permisos necesitas para vender en tu barrio o municipio.'),
      ('talk', 'Enseña a usarlos', 'Explícale a tu cliente cómo usar cada producto. Un cliente feliz vuelve.')]
vh = ''.join(f'<div class="vr"><div class="rec-ic">{ic(I[k],26)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in vr)
pages.append(page(nxt(), 'cream', 'Venta responsable', f'''
<div class="kicker">Vender bien es vender seguro</div><h2 class="big dark-t">Venta responsable</h2>
<p class="sub">Un buen negocio cuida a sus clientes. Con estos 4 consejos, tu diciembre será alegre <b>y seguro</b>.</p>
<div class="vr-grid">{vh}</div>
<div class="vr-photo"><img src="{W}Fotos-03.jpg"></div>'''))

# 19 CONTRAPORTADA — una sola instrucción
nxt()
pages.append(f'''<section class="page back">
<div class="bk-bg" style="background-image:url('{W}Fotos-03.jpg')"></div>
<img class="bk-logo" src="{W}Logo-01.png">
<div class="bk-kicker">¿Listo para ganar este diciembre?</div>
<h1>TU NEGOCIO<br><span>EMPIEZA HOY</span></h1>
<p class="bk-step">Toca el botón y escríbenos:<br><b>“Quiero emprender con Macías”</b></p>
<a class="bk-btn" href="{WA}">{WA_ICON.replace('width="13" height="13"','width="30" height="30"')} ESCRÍBENOS AL WHATSAPP</a>
<div class="bk-links"><a href="{IG}">{ic(I['ig'],18,2)} @pirotecniamacias__</a><a href="{MAPS}">{ic(I['pin'],18,2)} Valledupar, Cesar · Ver en el mapa</a></div>
<div class="bk-close">Macías Pirotecnia <span>|</span> Celebra cada momento.</div>
</section>''')

CSS = open(os.path.join(os.path.dirname(__file__), 'style3.css')).read().replace('{F}', F)
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Emprende con Macías</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(S + '/catalogo3.html', 'w').write(html)
print(len(pages), 'pages')
