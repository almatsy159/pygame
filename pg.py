import pygame as pg
# for connexion of character and to get data ...
#import mysql.connector as mc
#import sys

class Vector:
    def __init__(self,x=0,y=0,z=0,t=0,s=0):
        self.x = x
        self.y = y
        self.z = z
        
        
        self.t = t
        self.s = s
        

class Pos():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pos = (self.x,self.x)
        
    def draw(self,screen,s=3):
        pg.draw.line(screen,"white",(self.x-s,self.y-s),(self.x+s,self.y+s))
        pg.draw.line(screen,"black",(self.x+s,self.y-s),(self.x+s,self.y-s))
        
        

def f_osef():
    print("f_osef running")
    return "f_osef"



default_output = ""

x = pg.init()
screen = pg.display.set_mode((0,0))

#bg_img = pg.image.load("./img/bg.jpg").convert()
char_png = pg.image.load("./img/perso.png").convert()

w_pix = screen.get_width()
h_pix = screen.get_height()

u_x=19
u_y=19

w_cell = w_pix // u_x
h_cell = h_pix // u_y
print(h_cell,w_cell)
w_game = w_cell * u_x
h_game = h_cell * u_y

x_rest = w_pix - w_cell * u_x
#print(x_rest)
y_rest = h_pix - h_cell * u_y
#print(y_rest)

class Perso(pg.sprite.Sprite):
    def __init__(self,x=100,y=100):
        super().__init__()
        self.name = None
        self.x = x 
        self.y = y
        self.body_part = []
        self.force = 10
        self.vita = 10
        self.endurance = 10
        self.magie = 10
        self.mana = 10
        self.rect = pg.Rect(self.x-10,self.y-10,20,20)
    
    def draw(self,screen):
        pg.draw.circle(screen,"red",(self.x,self.y),10)
        pg.draw.rect(screen,"red",(self.rect),2)
        
    def mk_rect(self):
        self.rect = pg.Rect(self.x-10,self.y-10,20,20)
        
    def move(self,d_x=0,d_y=0):
        # dt ?
        self.x += d_x 
        self.y += d_y       
        self.mk_rect()
        
"""
def sprit(lst_img_path,screen,k=1):
    res = []
    for path in lst_img_path:
        tmp = pg.image.load(path).convert_alpha()
        w,h = int(tmp.get_width()/k),int(tmp.get_height()/k)
        tmp = pg.transform.scale(tmp,(w,h),screen)
        res.append(tmp)
    return tmp
"""
class Game_screen(pg.sprite.Sprite) :
    def __init__(self,screen,x,y,w,h,elem=[],color="pink",remain=50):
        
        super().__init__()
        #self.u_x = u_xself.draw_label(screen)
        #self.u_y = u_y
        
        # self.frame et self.grid
        self.remain = remain
        self.screen = screen
        self.elem = elem
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        
        self.elements = {}
        self.frames = []
        self.count_of_class = {}
        self.group = pg.sprite.Group()
        self.img()
        
    def img(self):
        self.outer_rect = pg.Rect(0,0,self.w,self.h)
        self.image = pg.Surface((self.w-2*self.remain,self.h-2*self.remain))
        self.image.fill(self.color)
        #self.rect = pg.Rect(self.x,self.y,self.w,self.h)
        self.rect = self.image.get_rect()
        self.rect.center= (self.w//2,self.h//2-self.remain/2)
        
        
        
    def old_draw(self,screen):
        pg.draw.rect(screen,self.color,self.rect)
        for e in self.elem:
            #e.u_x = self.u_x
            #e.u_y = self.u_y
            e.draw(screen)
        pg.display.flip()
        
    def add(self,elem):
        if type(elem) is Frame:
            self.frames.append(elem)
        if elem not in self.elements.keys():
            #self.elements[elem] = 0
            self.group.add(elem)
        if type(elem) not in self.count_of_class.keys():
            self.count_of_class[type(elem)] = 0
        
        #self.group.add(elem)
        
    def remove(self,elem):
        self.group.remove(elem)
        
    def draw_self(self,screen):
        pg.draw.rect(screen,"black",self.outer_rect)
        pg.draw.rect(screen,self.color,self.rect)
        
        
    def draw(self,screen):
        self.group.draw(screen)
        #print(f"{self.elements},\n{self.group}")
        for i in self.group:
            i.draw(screen)
        

class Area(pg.sprite.Sprite) : 
    def __init__(self,x=300,y=500,u=50,color="blue"):
        super().__init__()
        self.x = x
        self.y = y
        self.u = u
        self.rect=pg.Rect(self.x,self.y,self.x + self.u,self.y + self.u)
        self.color = color
        
    def chg_color(self,color="blue",changed=False):
        #print("color changed")
        default = color
        if self.color == default:
            self.color = "red"
        else :
            if changed :
                self.color == default
            
    def draw(self,screen):
        pg.draw.rect(screen,self.color,self.rect)
        #pg.display.flip()

class Frame(pg.sprite.Sprite):
    
    def __init__(self,master,x=100,y=100,w=500,h=500,color="grey"):
        super().__init__()
        self.master = master
        
        #self.u_x = 1
        #self.u_y = 1
        self.x=x
        self.y=y
        self.w = w
        self.h = h
        self.cg = Pos(self.x + self.w/2,self.y + self.h/2)
        self.color = color
        self.img()
        #self.items = []
        self.group = pg.sprite.Group()
        
    def img(self):
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
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
        #pg.draw.rect(screen,self.color,self.rect,2)
        #print("drawing frame")
        #for i in self.items:
            #i.u_x = self.u_x
            #i.u_y = self.u_y
        #   i.draw(screen)
        #pg.display.flip()
        self.group.draw(screen)
        
        
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


class ColorBar(pg.sprite.Sprite) :
    def __init__(self,x,y,label,val=0,max=10,color="red"):
        super().__init__()
        self.x = x
        self.y = y
        self.label = label
        self.val = val
        self.max = max
        self.ratio = self.val / self.max
        self.rect = pg.Rect(self.x,self.y,150,25)
        print(self.ratio)
        self.contour = pg.Rect(self.x+50,self.y,50,10)
        self.font = pg.font.Font(None,20)
        self.interieur_color = pg.Rect(self.x+1+50,self.y+1,50-self.ratio*self.val,7)
        self.interieur = pg.Rect(self.x+1+50,self.y+1,48,7)
        self.out_color = color
        if int(self.ratio*100) in range(0,25):
            self.color = "red"
        if int(self.ratio*100) in range(25,50):
            self.color = "orange"
        if int(self.ratio*100) in range(50,100):
            self.color = "green"
        else:
            self.color = "purple"
    
    def draw_label(self,screen):
        label_surface = self.font.render(self.label,True,self.out_color)
        screen.blit(label_surface,(self.x,self.y))
        
    def draw(self,screen):
        
        pg.draw.rect(screen,"lightgrey",self.rect)
        self.draw_label(screen)
        pg.draw.rect(screen,self.out_color,self.contour)
        pg.draw.rect(screen,"black",self.interieur)
        pg.draw.rect(screen,self.color,self.interieur_color)
        

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
    
    def draw(self):
        
        for i in range(int(self.x//self.u+1)):
            pg.draw.line(self.master.image,"black",(self.u*i,0),(self.u*i,self.y))
            
        for j in range(int(self.y//self.u+1)):
            pg.draw.line(self.master.image,"black",(0,self.u*j),(self.x,self.u*j))               
    
# to redo !!
#s
class Input:
    def __init__(self,x,y,h,w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

"""        
class Dialog(pg.sprite.Sprite):
    def __init__(self,master,x=0,y=0,w=100,h=100,ratio=0.33,default_text="|",color="black",border= 5,font_type=None,font_size=25) -> None:
        super().__init__()
        self.master = master
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.ratio = ratio
        self.default = default_text
        self.input_text = ""
        self.output_text = ""
        self.color = color
        self.border = border
        self.font_size = font_size
        self.font_type = font_type
        self.font = pg.font.Font(self.font_type,self.font_size)
        self.active = False
        self.img()
        
    def img(self):
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.input()
        self.output()
        
    def input(self):
        #self.input_img  = pg.Surface((int(self.w-self.border),int(self.h*(1-self.ratio)-self.border)))
        if self.input_text == "":
            self.input_text = self.default
        self.input_img = self.font.render(self.input_text,color="green")
        #self.input_img.blit(self.text_img)
        
    def output(self):
        self.output_img = pg.Surface((self.w+self.border))
    
    def add_to_output(self,res):
        self.output_text += res
        
        
    def clear_input(self):
        self.input_text = ""
        
    def chg_input_color(self):
        if self.active == True:
            self.input_color = "blue"
        else :
            self.input_color = self.color
    
    #def activate(self,pos):
    #    if pos colide input_rect
    
    def draw(self):
        self.chg_input_color()
"""      
        
        
class Dialog(pg.sprite.Sprite):
    
    def __init__(self,master,x,y,w=400,h=300,obj=None,text="|",color="green"):
        super().__init__()
        self.master = master
        self.obj = obj
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.text = text
        self.color = color
        self.font = pg.font.Font(None,26)
        self.input_text = ""
        self.input_color = self.color
        self.output_text = default_output
        self.active = False
        # frame
        
        self.img()
        
    def img(self):
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x+self.w//2,self.y+self.h//2)
        #self.rect = pg.Rect(self.x,self.y,self.w,self.h)
        self.input = pg.Rect(self.x+5,self.y+ 2*self.h//3,self.w-5,self.h//3-10)
        self.output = pg.Rect(self.x+5,self.y-10,self.w-10,2* self.h//3)
        self.draw(self.image)
        
        
    def input_blit(self,screen):
        
        text_input_surface = self.font.render(self.input_text,True,"black")
        screen.blit(text_input_surface,(self.input.x+5,self.input.y+5))

    def output_blit(self,screen):
        text_output_surface = self.font.render(self.output_text,True,"black")
        screen.blit(text_output_surface,(self.output.x+5,self.output.y+5))
        
    def add_to_output(self,res):
        self.output_text += res
        
        
    def clear_input(self):
        self.input_text = ""
        
    def chg_input_color(self):
        if self.active == True:
            self.input_color = "blue"
        else :
            self.input_color = self.color
        
    def draw(self,screen):
        #pg.draw.rect(screen,self.color,self.rect)
        self.chg_input_color()
        
        pg.draw.rect(screen,"white",self.output,2)
        pg.draw.rect(screen,self.input_color,self.input,5)
        self.input_blit(screen)
        self.output_blit(screen)
        
    def clicked(self):
        self.active = True

        #pg.display.flip()



class Articulation(pg.sprite.Sprite):
    def __init__(self,x,y,r=5,color="red"):
        self.r = r
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self,screen):
        pg.draw.circle(screen,self.color,(self.x,self.y),self.r,2)
        #pg.display.flip()
        
class Bones(pg.sprite.Sprite):
    def __init__(self,x,y,len):
        super().__init__()
        self.x = x
        self.y = y
        self.len = len
        
    def draw(self,screen):
        pg.draw.line(screen,"black",(self.x,self.y),(self.x+self.len,self.y))
        pg.draw.circle(screen,"black",(self.x,self.y),self.len,1)

class Body(pg.sprite.Sprite):
    def __init__(self,p,links=[]):
        self.perso = p
        self.links = links
    def draw(self,screen):
        c_x = w_pix//2
        c_y = h_pix//2
        pg.draw.line(screen,"black",(w_pix//2,250),(w_pix//2,400),2)
        pg.draw.line(screen,"black",(w_pix//2-50,250),(w_pix//2+50,250))
        pg.draw.line(screen,"black",(c_x-35,400),(c_x+35,400))
        #pg.display.flip()
        

class Arm:
    def __init__(self,p):
        self.p = p
    
    def draw(self):
        pass
class Hand:
    def __init__(self):
        pass
    
class Head:
    def __init__(self):
        pass

class Projectile(pg.sprite.Sprite):
    def __init__(self,caster,d=1):
        
        super().__init__()
        self.d = d
        self.caster = caster
        
    
    def draw(self,screen,vert=-1,hor=-1):
        
        dy = self.d * vert
        dx = self.d * hor
        pg.draw.circle(screen,"blue",(self.caster.x+dx,self.caster.y+dy),5)
        




g1 = Game_screen(screen,x_rest-1,y_rest-1,w_game,h_game)
g1.draw_self(screen)

f0 = Frame(g1,900,500,g1.w-g1.remain,g1.h-g1.remain)
g1.add(f0)
grid1=Grid(f0,x=w_pix,y=h_pix)
d1 = Dialog(f0,800,500)


# rename frame !

# f1 => character
f1 = Frame(g1,1600,360,400,700)
g1.add(f1)

# perso repr
f4 = Frame(f1,x=10,y=150,w=250,h=300,color="red")
f1.add_item(f4)
# stat repr
f5 = Frame(f1,x=10,y=-150,w=250,h=300,color="purple")
f1.add_item(f5)

#minimap
xf2 = 1600
yf2 = 850
wf2 = 360
hf2 = 300
ug2 = 25

f2 = Frame(g1,xf2,yf2,wf2,hf2,"blue")
g1.add(f2)
grid2 = Grid(f2,wf2,hf2,ug2)
grid2.draw()
#f2.add_item(grid2)


# btn bar
f3 = Frame(g1,600,900,800,100,"black")
g1.add(f3)



###

a1 = Area()
p1 = Perso()

#grid1.draw()

body1 = Body(p1)
art1 = Articulation(w_pix//2+50,250)
my_own_event = 1 # pg event custom here


c1 = ColorBar(f1.x+50,f1.y+100,"vita",7)
c2 = ColorBar(f1.x+50,f1.y+150,"mana",6,20,"blue")   
c3 = ColorBar(f1.x+50,f1.y+200,"rage",4,color="black") 
c4 = ColorBar(f1.x +50,f1.y+50,"label",5)
#f1.add_item(c4)
#g1.add(f1)
def open_dialog(frame,x=0,y=0,w=100,h=100):
    ftmp = Frame(frame,0,-300)
    d1 = Dialog(x,y,w,h)
    ftmp.add_item(d1)
    frame.add_item(ftmp)
    print(frame.group)

### 
b1 = Button(f3,f=lambda:open_dialog(f0),x=0,y=0,w=50,h=50)
f3.add_item(b1)
b2 = Button(None,color = "blue",x=100,y=700)
#f1.add_item(b1)
#f1.add_item(b2)d1


launched = True
clock = pg.time.Clock()
changed = True
first = True
created = False

def create_perso():
    return Perso()

while launched == True:
    flag_epg = False # ?
    flag_eg = False

    if not created:
        
        #p1 = Perso()
        p1 = create_perso()
        created = True
        

    for e in pg.event.get():
        #print(e)
        
        if e:
            if e.type == pg.MOUSEBUTTONDOWN:
                print(e)
                """
                if d1.input.collidepoint(e.pos):
                    d1.active = True
                else :
                    d1.active = False
                """
                print(g1.group)
                for el in g1.group:
                    if el.rect.collidepoint(e.pos):
                        if el is Dialog:
                            el.clicked()
                            print(f"{el} was clicked !")
            
                for f in g1.frames:
                
                    for i in f.group:
                        if i.rect.collidepoint(e.pos):
                            #print(f"{i} collided")
                            #print(type(i))
                            if type(i) is Button:
                                #print("button !!")
                                i.f()
                                #res.draw(g1.image)
                            if type(i) is Dialog:
                                if i.input.collidepoint(e.pos):
                                    i.active = True
                                else :
                                    i.active = False
                                if i.active == True:
                                    if e.key == pg.K_BACKSPACE:
                                        i.input_text = d1.input_text[:-1]
                                    elif e.key == pg.K_RETURN:
                                        i.add_to_output(d1.input_text)
                                        i.input_text = ""
                                    else :
                                        i.input_text += e.unicode
                
                                
                        
                if d1.active == True:
                    if e.key == pg.K_BACKSPACE:
                        d1.input_text = d1.input_text[:-1]
                    elif e.key == pg.K_RETURN:
                        d1.add_to_output(d1.input_text)
                        d1.input_text = ""
                    else :
                        d1.input_text += e.unicode
                
            
                    """                for elem in g1.elements:      
                    #if elem.rect.collidepoint(e.pos):
                    if elem is Button:
                            print("button colided !")
                            elem.f()
                    """
            changed = True
            flag_epg = True
            if e.type == pg.QUIT:
                launched = False
            if e.type == my_own_event:
                print("own event happened")
                # add or remove from g1 list
                # click on an item             
            if e.type == pg.KEYDOWN:
                print(e)
                """
                if e.key == pg.K_UP:
                    p1.move(0,-20)
                elif e.key == pg.K_DOWN:
                    p1.move(0,20)
                elif e.key == pg.K_LEFT:
                    p1.move(-20)
                #elif e.key == pg.K_RIGHT:
                #   p1.move(20)
                    
                elif e.key == pg.K_z:
                    p1.action()
                """
                        
            
                
            
    pressed = pg.key.get_pressed()
    tiping = False
    if pressed[pg.K_LCTRL]:
        print("tiping ...")
        tiping = True
    """
    key_shot = [pg.K_a,pg.K_z,pg.K_e,pg.K_s]
    if pressed[pg.K_a]:
        print("key a ! ")
        p1 = Projectile(p1,10)
    elif pressed[pg.K_z]:
        print("z")
    elif pressed[pg.K_e]:
        print("e")
    elif pressed[pg.K_s]:
        print("s")
    """
    if pressed[pg.K_RIGHT]:
        changed = True
        p1.move(20)
    if pressed[pg.K_DOWN]:
        changed=True
        p1.move(0,20)
    
    if pressed[pg.K_UP]:
        changed = True
        p1.move(0,-20)
    
    if pressed[pg.K_LEFT]:
        changed = True
        p1.move(-20)
        
    
    if p1.rect.colliderect(a1.rect):
        a1.chg_color()
    #print(a1.color)              
    
    #screen.blit(bg_img,(0,0))
    
    #for e in g1.elements:
    #    e.draw(screen)  
    #g1.draw(screen)
    #print(a1.color)
    
    if changed == True:
        g1.image.fill((255,255,255))
        # nafficher que les element de gamescreen qui ont changé
        g1.draw(screen)
        grid1.draw()
        
        #f1.draw(screen)
        b1.draw(screen)
        b2.draw(screen)
        #a1.draw(screen)
        art1.draw(screen)
        
        p1.draw(screen)
        c1.draw(screen)
        c2.draw(screen)
        c3.draw(screen)
        d1.draw(screen)
        pg.display.flip()
        
    changed = False
    clock.tick(26)

pg.quit()



