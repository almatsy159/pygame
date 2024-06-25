

"""
    
    i am in the midlle of a room 
    
"""
class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self,v):
        x = self.x + v.x
        y = self.y+v.y
        z = self.z + v.z
        return Vector(x,y,z)
    
class Point:
    def __init__(self,x=0,y=0,z=0,t=0):
        
        self.x = x
        self.y = y
        self.z = z
        self.t = t
    
    def delta(self,p):
        x = self.x - p.x
        y = self.y - p.y
        z = self.z - p.z
        return Vector()
        

origin = Point(0,0,0)
i = Point(1,0,0)
j = Point(0,1,0)
k = Point(0,0,1)


class Segment:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.v = self.a.delta(self.b)
        




    
class Personnage:
    def __init__(self,e=100,f=50,v=50):
            
        self.energie = e
        self.force = f
        self.vitesse = v
        
