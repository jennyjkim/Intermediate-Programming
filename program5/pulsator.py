# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter_constant = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.count = 0
        
    def update(self, model):
        eaten_objects = Black_Hole.update(self, model)
        self.count += 1
        if len(eaten_objects) > 0:
            self.count = 0
            self.change_dimension(len(eaten_objects), len(eaten_objects))
        if self.count == self.counter_constant:
            self.count = 0
            self.change_dimension(-1, -1)
        if self.get_dimension() == (0, 0):
                model.remove(self)
                
            