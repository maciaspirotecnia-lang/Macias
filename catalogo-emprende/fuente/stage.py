import sys, glob, os
from PIL import Image, ImageDraw, ImageFilter, ImageChops
S=sys.argv[1]; OUT=S+'/web3/'
KEYS=['Sonidos-01','Sonidos-02','Sonidos-03','Sonidos-04','Sonidos-05','Sonidos-06','Sonidos-08','Sonidos-12','Sonidos-13',
 'Volcanes-01','Volcanes-02','Volcanes-03','Volcanes-04','Chispitas-01',
 'Torta-01','Torta-02','Torta-03','Torta-04','Torta-05','Torta-06','Torta-08','Torta-09','Torta-10','Torta-11','Torta-12','Torta-13','Torta-14',
 'Voladores-01','Voladores-02','Voladores-04','Voladores-05','Voladores-06']
BG={'l':(241,224,220),'d':(75,0,0)}
def kill_white(im):
    rgb=im.convert('RGB'); w,h=rgb.size
    mark=(255,0,255)
    pts=[(x,0) for x in range(0,w,7)]+[(x,h-1) for x in range(0,w,7)]+[(0,y) for y in range(0,h,7)]+[(w-1,y) for y in range(0,h,7)]
    for p in pts:
        r,g,b=rgb.getpixel(p)
        if min(r,g,b)>215: ImageDraw.floodfill(rgb,p,mark,thresh=38)
    a=Image.new('L',(w,h),255); px=rgb.load(); pa=a.load()
    for y in range(h):
        for x in range(w):
            if px[x,y]==mark: pa[x,y]=0
    a=a.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
    out=im.convert('RGBA'); out.putalpha(ImageChops.multiply(a,im.convert('RGBA').split()[3])); return out
C=640
for k in KEYS:
    im=Image.open(f'{S}/img/{k}.png').convert('RGBA')
    if k in ('Torta-08','Volcanes-03'): im=kill_white(im)
    im=im.crop(im.getbbox())
    box=int(C*.80); s=min(box/im.width, box/im.height); im=im.resize((max(1,int(im.width*s)),max(1,int(im.height*s))),Image.LANCZOS)
    x=(C-im.width)//2; y=int(C*.90)-im.height
    for v,col in BG.items():
        can=Image.new('RGB',(C,C),col)
        # floor shadow
        sh=Image.new('L',(C,C),0); d=ImageDraw.Draw(sh)
        ew=int(im.width*.85); d.ellipse([C//2-ew//2,int(C*.90)-12,C//2+ew//2,int(C*.90)+12],fill=150 if v=='l' else 200)
        sh=sh.filter(ImageFilter.GaussianBlur(14))
        # drop shadow from alpha
        ds=Image.new('L',(C,C),0); ds.paste(im.split()[3],(x+6,y+14)); ds=ds.filter(ImageFilter.GaussianBlur(16)).point(lambda p:int(p*(.30 if v=='l' else .55)))
        shadow=ImageChops.lighter(sh,ds)
        dark=Image.new('RGB',(C,C),(40,10,8) if v=='l' else (8,0,0))
        can=Image.composite(dark,can,shadow)
        can.paste(im,(x,y),im)
        can.save(f'{OUT}{k}_{v}.jpg',quality=80)
print('ok')
