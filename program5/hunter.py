# A Hunter is both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    in_distance = 200
    
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, self.radius*2, self.radius*2, 1, 5)
        Pulsator.__init__(self, x, y)
        self.randomize_angle()
    
    def update(self, model):
        Pulsator.update(self, model)
        self.move()
        # finding prey
        all_prey = model.find(lambda x: isinstance(x, Prey))
        close_prey = []
        for prey in all_prey:
            position = prey.get_location()
            if self.distance(position) < self.in_distance:
                close_prey.append((self.distance(position), prey))
        if len(close_prey) != 0:
            prey_object = sorted(close_prey, key = lambda x: x[0])[0][1]
            px, py = prey_object.get_location()
            hx, hy = self.get_location()
            new_angle = atan2(py - hy, px - hx)
            self.set_angle(new_angle)
        
        
            
        
        
        
        
        
        
        
            
