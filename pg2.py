import pygame as pg
from glob import glob
#print(help(pg.sprite.Group))

class Couple:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pos = self.get_pos()
        
    def get_pos(self):
        return (self.x,self.y)

map = [[0,0,0,0,0,1],[0,0,0,0,1,1]]

imgs_p = glob("img/*.jpg") + glob("img/*.png")
imgs = []
#print(imgs)
for i in imgs_p:
    surf = pg.image.load(i)
    imgs.append(surf)
    


class Case(pg.sprite.Sprite):
    def __init__(self,pos,contain={},color="blue",unit=50,uy=None):
        self.map = map
        self.x,self.y = self.pos = pos
        self.contain = contain
        self.color = color
        self.ux = unit
        if uy == None:
            self.uy = unit
        
        
    def add_element(self,elem):
        self.contain[elem.name] = elem  
        
class Map:
    def __init__(self,map):
        self.map = map
        self.dic = {}
        for r in range(len(map)):
            for c in range(len(map[r])):
                #print(c)
                if c == 0:
                    color = "black"
                else :
                    color = "white"
                    
                self.dic[(c,r)] = Case((c,r),color="red")
    
    def __repr__(self):
        res = ""
        for i in self.map:
            res += f"{str(i)}\n"
        return res
            
map1 = Map(map)
print(map1)
            

class Perso(pg.sprite.Sprite):
    def __init__(self,name,pos=(0,0),u=50,color="purple"):
        self.x,self.y = self.pos = pos
        self.name = name
        self.u = u
        self.color = color
        self.img()
        
    def img(self):
        self.image = pg.Surface((self.u,self.u))
        self.image.fill(self.color)
        
    def draw(self,surface):
        pg.draw.rect(surface)
        
p1 = Perso("alma",(300,300))
        
class Game_screen(pg.sprite.Sprite):
    
    def __init__(self,screen,scene):
        self.screen = screen
        self.scene = scene
        self.group = pg.sprite.Group()
        
    
    def add_item(self,item=None):
        if item == None:
            item = Frame(self)
        self.group.add(item)
        self.scene.add(item)
        
    def draw(self):
        for s in self.scene.group:
            if s in self.group:
                s.draw(self.screen)
    
    def remove_item(self,item):
        self.group.remove(item)
        
    
    def blit(self,img,pos=(0,0)):
        self.screen.blit(img,pos)

class Scene(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.group = pg.sprite.Group()
        self.types = []
        self.dic = {}

    def add(self,item):
        self.group.add(item)
        if type(item) not in self.types:
            self.types.append(type(item))
        #self.dic[item] = item.visibility
        # sprite may have one !
            
    
    def do(self):
        for t in self.types:
            for e in self.group:
                if t == type(e):
                    """
                    case
                        t is Frame 
                        print(t)
                    case t is Dialog
                    """
                    pass
                
    def get2(self,t):
        res = []
        for i in self.group :
            if type(i) == t:
                res.append(i)
        return res
    
    def draw(self,gamescreen):
        screen = gamescreen.screen
        group =  gamescreen.group 
        for s in self.group:
            if s in group:
                s.draw(screen)
                
    
    def remove_item(self,item):
        self.group.remove(item)


def qit(frame):
    frame.master.remove_item(frame)

class Frame(pg.sprite.Sprite):
    
    def __init__(self,master,x=100,y=100,w=500,h=500,color="grey",vis=True,border=1):
        super().__init__()
        self.master = master
        self.visibility = True
        
        #self.u_x = 1
        #self.u_y = 1
        self.x=x
        self.y=y
        self.w = w
        self.h = h
        self.cg = Couple(self.x + self.w/2,self.y + self.h/2)
        self.color = color
        self.img()
        #self.items = []
        self.border = border
        self.group = pg.sprite.Group()
        #self.all_frame()
        self.running = False
        
        
        
    def img(self):
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        #self.rect.center = self.cg.pos
        #self.rect = pg.Rect(self.x,self.y,self.w,self.h)
        
    def all_frame(self):
        #print(self.group)
        self.b_quit = Button(self,self.x,self.y,50,50,qit)
        self.add_item(self.b_quit)
        #print(self.group)
        
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
        pg.draw.rect(screen,self.color,self.rect,self.border)
        #print("drawing frame")
        #for i in self.items:
            #i.u_x = self.u_x
            #i.u_y = self.u_y
        #   i.draw(screen)
        #pg.display.flip()
        #print(self.group)
        self.group.draw(screen)
        
    def remove_item(self,item):
        self.group.remove(item)

class Button(pg.sprite.Sprite):
    def __init__(self,master=None,x=150,y=250,w=10,h=10,f=None,color="red"):
        super().__init__()
        self.master= master
        self.x =  x
        self.y = y
        self.w = w
        self.h = h
        self.f = f
        self.color = color
        self.img()
        #self.rect = pg.Rect(self.x,self.y,self.w,self.h)
    
    def img(self):
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        
    def draw(self,screen):
        #print("drawing button")
        #print(self.x,self.y)
        pg.draw.rect(screen,self.color,self.rect)
        #pg.display.flip()

class Grid(pg.sprite.Sprite):
    def __init__(self,master,x=1000,y=1000,u=50):
        # screen.w ?
        super().__init__()
        self.master = master
        self.y=y
        self.u=u
        self.x = x
        #print(self.u)
        #self.img()
        
    #def img(self):
    #   self.image = pg.Surface((self.x,self.y)) 
    #    self.rect = self.image.get_rect()
    def draw_vert(self):
        for i in range(int(self.x//self.u+1)):
            pg.draw.line(self.master.image,"black",(self.u*i,0),(self.u*i,self.y))
    
    def draw_hort(self):
        for j in range(int(self.y//self.u+1)):
            pg.draw.line(self.master.image,"black",(0,self.u*j),(self.x,self.u*j))   
        
    def draw(self):
        
        for i in range(int(self.x//self.u+1)):
            pg.draw.line(self.master.image,"black",(self.u*i,0),(self.u*i,self.y))
            
        for j in range(int(self.y//self.u+1)):
            pg.draw.line(self.master.image,"black",(0,self.u*j),(self.x,self.u*j))               


def create_frame(master,x,y,w,h):
    res = Frame(master,x,y,w,h)
    return res
"""
def event_handler(event):
    res = ""
    match type(event):
        case pg.QUIT:
            print("quiting")
    
    res = eval(res)
"""            
            
def event_scene(scene,pos):
    for e in scene.group:
        if e.rect.collidepoint(pos):
            if type(e) is Frame:
                for el in e.group:
                    #print(f"{e} => {el} collided at pos {pge.pos}!")
                    #print(el)
                    if type(el) is Button:
                        #print("button clicked")
                        el.f(e)
        #gs1.update()        

def main():
    
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((0,0))
    w = screen.get_width()
    h = screen.get_height()
    res = (h,w)
    scene = Scene()
    gs1 = Game_screen(screen,scene)
    print(res)
    
    # game
    f0 = Frame(gs1,800,400,1600,800)
    gs1.add_item(f0)
    
    f00 = Frame(f0,0,0,w=800,h=400,color="green")
    grid00 = Grid(f00,800,400)
    f0.add_item(f00)
    
    f0l = Frame(f0,-600,0,400,400,"red")
    grid0l = Grid(f0l,400,400)
    f0r = Frame(f0,600,0,400,400,"blue")
    grid0r = Grid(f0r,400,400)
    
    f0t = Frame(f0,0,-300,800,200,"lightgreen")
    grid0t = Grid(f0t,800,400)
    f0d = Frame(f0,0,300,800,200,"darkgreen")
    grid0d = Grid(f0d,800,400)
    
    f0lt = Frame(f0,-600,-300,400,200,"crimson")
    f0ld = Frame(f0,600,300,400,200,"darkblue")
    
    f0rt = Frame(f0,600,-300,400,200,"lightblue")
    f0rd = Frame(f0,-600,300,400,200,"darkred")
    
    f0.add_item(f0l)
    f0.add_item(f0t)
    f0.add_item(f0r)
    f0.add_item(f0d)
    
    f0.add_item(f0ld)
    f0.add_item(f0lt)
    f0.add_item(f0rt)
    f0.add_item(f0rd)

    
    
    
    # map
    f1 = Frame(gs1,1600+190,800+140,380,280)
    gs1.add_item(f1)
    f11 = Frame(f1,0,0,380,280)
    f1.add_item(f11)
    gridmap= Grid(f11,380,280,20)
    
    # perso
    f2 = Frame(gs1,1600+190,400,380,800)
    gs1.add_item(f2)
    
    f20 = Frame(f2,0,-200,380,400,"brown")
    f21 = Frame(f2,0,200,380,400,'white')
    f2.add_item(f20)
    f2.add_item(f21)
    
    # interaction
    f3 = Frame(gs1,0+800,800+140,1600,280)
    gs1.add_item(f3)
    
    f4 = Frame(f3,-400,0,800,280)
    f3.add_item(f4)
    f5 = Frame(f3,400,0,800,280,"blue")
    f3.add_item(f5)
    
    def fct1(master):
        print(master)
        f = Frame(master,400,400,500,500,"pink",border=0)
        master.master.add_item(f)
        #print("frame_added")

        
    
    b0 = Button(f3,400,50,50,50,fct1)
    f3.add_item(b0)
    b1 = Button(f3,300,50,50,50,fct1)
    f3.add_item(b1)
    
    b2 = Button(f3,200,50,50,50,fct1)
    f3.add_item(b2)
    
    b3 = Button(f3,100,50,50,50,fct1)
    f3.add_item(b3)
    
    b4 = Button(f3,700,50,50,50,fct1)
    f3.add_item(b4)
    
    b5 = Button(f3,600,50,50,50,fct1)
    f3.add_item(b5)
    
    b6 = Button(f3,500,50,50,50,fct1)
    f3.add_item(b6)
    
    
    
    
    
    """
    dic_btn_int = {}
    index_c = [-2,-1,0,1,2]
    index_r = [-1,1]
    lst_f = [f1]
    
    for i in range(len(index_c)):
        for j in range(len(index_r)):
            b = Button(f0,200+index_c[i]*100,50*index_r[j],50,50)
            name = f"b{i}{j}"
            dic_btn_int[name] = b
            f3.add_item(dic_btn_int[name])
    """
    
    
    
    running = True
    pg_event = False
    custom_event = True
    changed = True
    last_clicked_frame = None
    first = True
    count = 0
    implemented = [pg.K_a,pg.K_z,pg.K_e,pg.K_s]

    while running == True:
        img_count = 0
        count += 1
        for pge in pg.event.get():
            if pge :
                #print(pge)
                changed = True
                pg_event == True
                if pge.type == pg.QUIT:
                    running = False
                    
                if pge.type == pg.MOUSEBUTTONDOWN:
                    for e in scene.group:
                        if e.rect.collidepoint(pge.pos):
                            if type(e) is Frame:
                                for el in e.group:
                                    #print(f"{e} => {el} collided at pos {pge.pos}!")
                                    #print(el)
                                    if type(el) is Button and el.rect.collidepoint(pge.pos):
                                        #print("button clicked")
                                        #last_clicked_frame = e
                                        #print(e)
                                        el.f(e)
                if pge.type == pg.KEYDOWN:
                    print(pge)
                    if pge.key in implemented:
                        print("is implemented !")
    
        #gs1.update()
        if changed or first:
            #scene.update()
            scene.draw(gs1)
            
            pos_img = (500,500)
            gs1.blit(imgs[0],pos_img)
            pos_img = (0,500)
            gs1.blit(imgs[1],pos_img)
            pos_img = (500,0)
            gs1.blit(imgs[2],pos_img)
            pos_img = (200,300)
            gs1.blit(imgs[3],pos_img)
            pos_img = (800,1000)
            gs1.blit(imgs[4],pos_img)
            
                
            grid00.draw()
            grid0l.draw_hort()
            grid0r.draw_hort()
            grid0d.draw_vert()
            grid0t.draw_vert()
            gridmap.draw()
            #gs1.draw()
            pg.display.flip()
        
        changed = False 
        clock.tick(26) 
        
        if first == True:
            first = False
        #for ce in custom_event:
        #custom_event = True
        """
        if count > 100:
            print(count)
            changed = True
            img_count +=1
            count = 0
        pg.display.update()
        """
    pg.quit()


if __name__=="__main__" :
    custom_event = []
    main()
