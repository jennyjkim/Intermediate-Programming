# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import randrange
import random


class Floater(Prey):
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self,x,y,self.radius*2,self.radius*2, 1 ,5) 
        self.randomize_angle()
    
    def update(self, model):
        x = randrange(1, 11)
        if x in [1, 2, 3]:
            new_speed = self.get_speed() + random.uniform(-.5, .5)
            self.set_angle(self.get_angle() + random.uniform(-.5, .5))
            if 3 <= new_speed <= 7:
                self.set_speed(new_speed)
        self.move()
        
    def display(self,canvas):
        self.ufo = PhotoImage(file='ufo.gif')
        canvas.create_image(self.get_location(), image= self.ufo)