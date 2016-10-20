# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self,x,y,self.radius*2, self.radius*2) 
        
    
    def update(self, model):
        eaten_prey = set()
        all_prey = model.find(lambda x: isinstance(x, Prey))
        for prey in all_prey:
            position = prey.get_location()
            if self.contains(position):
                eaten_prey.add(prey)
                model.remove(prey)
        return eaten_prey
                
    
    def contains(self, xy):
        return self.distance(xy) < (self.get_dimension()[1])/2
        
                
    def display(self,canvas):
        canvas.create_oval(self._x - self._width/2      , self._y - self._height/2,
                                self._x + self._width/2, self._y + self._height/2,
                                fill='black')
        
        
        
        