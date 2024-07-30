import math
from array import array 
import numpy as np
from datetime import date 
class Boid:
    def __init__(self, position: tuple, vitesse: tuple):
        self.x, self.y = position
        self.vx, self.vy = vitesse
    def __repr__(self) -> str:
        return f"Boid({self.x}, {self.y}, {self.vx}, {self.vy}"
    
    def module_vitesse(self) ->float:
        return f"{math.sqrt(self.vx**2 + self.vy**2)}"
    def avance(self):
        self.x += format(self.vx, '.3f')
        self.y += format(self.vy, '.03f') 
        return self
    def __str__(self)-> str:
        return f"the fastest of our program {Boid.module_vitesse(self)}"

class Boid1:
    taille = 300
    count = 0
    def __init__(self, position = None, vitesse = None):
        self.x = (position
                  if position is not None
                  else np.random.uniform(-Boid1.taille, Boid1.taille,2)
                  )
        self.dx = (
            vitesse if vitesse is not None 
            else np.random.uniform(-5,5,2)
        )
        Boid1.count +=1
    def __del__(self):
        Boid1.count -=1
    def __repr__(self) -> str:
        return f"Boid({format(self.x, '0.4f')}, {format(self.dx, '.4f')} on {Boid1.count}"
    def __str__(self) -> str:
        return f'Boid({self.x}, {self.dx}) on {Boid1.count}'
class A:
    count = 0
    def __init__(self):
        self.count += 1
        A.count += 1

    def __str__(self):
        return f"A() a {self.count} sur {A.count}"

class Boid2:
    taille = 300
    count = 0
    dvitesse = 0
    def __init__(self, position = None, vitesse = None):
        self.x = (position
                  if position is not None
                  else np.random.uniform(-Boid2.taille, Boid2.taille,2)
                  )
        self.dx = (
            vitesse if vitesse is not None 
            else np.random.uniform(-5,5,2)
        )
        Boid1.count +=1
    
    def __del__(self):
        Boid2.count -=1
    def __str__(self): 
        return f"Boid2({self.x.round(2)}, {self.dx.round(2)})"
    
    def avance(self):
        self.x += self.dx
        return self 
    
    @property
    def vitesse(self): 
        return self.dx 
    @vitesse.setter
    def vitesse(self, value: list):
        self.dx = self.dx*value
        
###%%%%%%%%%%%%%%%%%%%%%###
#b1 = Boid2()
#print(b1.__str__())
#########%%%%%%%%%%%%%%%%########
class vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __iter__(self):
        return (i for i in (self.x, self.y))
    def __str__(self):
        return str(tuple(self))
    def __repr__(self) -> str:
        return "le format binaire est " + format(self.x ,'b')+ " and " + format(self.y, 'b')
    
class Person: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    @classmethod
    def klasmethod(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)
        
    def display(self):
        print(self.name +" have "+ str(self.age))

####### #######################
p1 = Person('ben',23)
p1.display()
p2 = Person.klasmethod('ben', 2000)
p2.display()
###########################
class Polygone:
    def aire(self)-> float: 
        ...
    def __repr__(self) -> str:
        return f"c'est un polygone d'aire {Polygone.aire(self): 0.04f}"
    
class Triangle(Polygone):
    def __init__(self, p1, p2, p3):
        self.v1 = p2 -p1 
        self.v2 = p3 - p1
    
    def aire(self):
        ...



