import pygame as pg

pg.init()
screen = pg.display.set_mode((0,0))
w,h = res = screen.get_width(),screen.get_height()

ux = 50
uy = 50
uz = 0
pi = 3.14



poid = 80
taille = 180
rpt = poid/taille
print(rpt)



class Point:
    def __init__(self,x=0,y=0,z=0,color="black",dec=5):
        self.x =  x
        self.y =  y
        self.z = z
        self.pos = (x,y)
        self.color = color
        self.dec = dec
        
    def draw(self,screen):
        s0 = (self.x-self.dec,self.y-self.dec)
        e0 = (self.x+self.dec,self.y+self.dec)
        s1 = (self.x-self.dec,self.y+self.dec)
        e1 = (self.x+self.dec,self.y-self.dec)
        pg.draw.line(screen,self.color,s0,e0)
        pg.draw.line(screen,self.color,s1,e1)
        
class Line:
    def __init__(self,a,b,color="red"):
        self.a = a
        self.b = b
        self.dx = self.a.x - self.b.x
        self.dy = self.b.y - self.b.y
        #self.k = self.dx / self.dy
        self.color = color
    
    def draw(self,screen):
        pg.draw.line(screen,self.color,self.a.pos,self.b.pos) 
        

class Frame:
    def __init__(self,x=0,y=0,w=1,h=1,color="white"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.cg = Point(self.x+self.w//2,self.y+self.h//2)
        self.elements = []
        self.img()
        
    def img(self):
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.cg.x,self.cg.y

    def draw(self,screen):
        pg.draw.rect(screen,self.color,self.rect)
        

class Angle:
    def __init__(self,value=0,rad=True):
        self.rad = True
        self.val = value
        
    
    def modulo(self):
        if self.value == 0:
            return 0
        if self.rad == True:
            k = pi
        else:
            k = 180
        
            
            
        
    
        

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

f0 = Frame(0,0,w,h)
origin = Point(f0.cg.x,f0.cg.y)
A = Point(f0.cg.x+ux,f0.cg.y)
B = Point(f0.cg.x,f0.cg.y-uy)
Aorigine = Line(A,origin)

running = True
something = True

while running:
    for e in pg.event.get():
        if e:
            print(e)
            something = True
            if e.type == pg.QUIT :
                running = False
    if something:
        f0.draw(screen)
        origin.draw(screen)
        A.draw(screen)
        B.draw(screen)
        Aorigine.draw(screen)
        pg.display.flip()
    something = False

pg.quit()