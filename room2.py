import pygame as pg


def mkl(l=10,val=0):
    res = []
    for i in range(l):
        res.append(val)
        
def mkm(le,la,val):
    res = []
    for i in range(le):
        res.append(mkl(la,val))
        
    return res

map0 =[[1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1]]

class RayCast:
    def __init__(self,game):
        self.game = game
        

class Frame(pg.sprite.Sprite):
    
    def __init__(self,x=100,y=100,w=1700,h=800,color="grey"):
        super().__init__()
        #self.u_x = 1
        #self.u_y = 1
        self.x=x
        self.y=y
        self.w = w
        self.h = h
        self.cg = self.x + self.w/2,self.y + self.h/2
        self.color = color
        self.img()
        #self.items = []
        self.group = pg.sprite.Group()
        
    def img(self):
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.cg
        #self.rect.center = self.cg.pos
        #self.rect = pg.Rect(self.x,self.y,self.w,self.h)
        
        
    def add_item(self,item):
        #self.items.append(item)
        
        item.x = self.x + item.x
        item.y = self.y + item.y
        item.img()
        #item.ima
        #print(f"adding {item} in self.groups")
        self.group.add(item)
        #print(self.group)
        

    def draw(self,screen):
        pg.draw.rect(screen,self.color,self.rect,2)
        #print("drawing frame")
        #for i in self.items:
            #i.u_x = self.u_x
            #i.u_y = self.u_y
        #   i.draw(screen)
        #pg.display.flip()
        self.group.draw(screen)
        
class Map:
    def __init__(self,map):
        self.map = {}
        for i in range(len(map)):
            for j in range(len(map[i])):
                self.map[i,j] = map[i][j]
                
                

        
        

pg.init()
screen = pg.display.set_mode((0,0))
h,w = res = screen.get_size()
frame = Frame()

running = True
event = True

while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
    
    if event:
        
        frame.draw(screen)
        pg.display.update()
    event = False
    
pg.quit()