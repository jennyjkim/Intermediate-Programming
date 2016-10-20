'''The Special class creates pink ball that changes colors randomly whenever it 
contains a Ball object.'''

import random
from prey import Prey
from ball import Ball
    
class Special(Prey):    
    radius = 8

    def __init__(self, x, y):
        Prey.__init__(self,x, y, 2 * self.radius, 2 * self.radius, 1 ,20)
        self.randomize_angle()
        self.colors = ['red', 'orange', 'pink', 'yellow', 'green', 'purple']
        self.current_color = 'pink'
        self.count = 0
 
     
    def update(self, model):
        self.move()
        all_s = model.find(lambda x: isinstance(x, Ball))
        for s in all_s:
            position = s.get_location()
            if self.contains(position):
                self.current_color=random.choice(self.colors)            
                 
 
    def display(self,canvas):
        canvas.create_oval(self._x - self.radius, self._y - self.radius,
                                self._x + self.radius, self._y + self.radius,
                                fill= self.current_color) 