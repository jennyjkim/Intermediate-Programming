#### THE ONE IM WORKING ON
import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special



# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
balls = set()
cycle_count = 0
selected_object = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls, selected_object
    running     = False
    cycle_count = 0
    balls       = set()
    selected_object = None


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, running
    if running:
        update_all()
        running = False
    else:
        running = True
        update_all()
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected_object
    selected_object = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if selected_object == None:
        pass
    elif selected_object == 'Remove':
        clicked_ball = find(lambda all_balls: all_balls.contains((x, y)))
        for each in clicked_ball:
            balls.remove(each)
    else:
        balls.add(eval(str(selected_object) + '(' + str(x) + ',' + str(y) + ')'))
        
#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = set()
    for each in balls:
        if p(each):
            result.add(each)
    return result


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in balls.copy():
            b.update(model)


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
