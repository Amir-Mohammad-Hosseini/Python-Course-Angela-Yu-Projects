Link : 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

code : 

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    
def move_up():
    turn_left()
    while(wall_on_right()):
        move()
def move_right():
    turn_around()
    move()

def move_down():
    turn_around()
    while(front_is_clear()):
        move()

def go_ahead():
    move_up()
    move_right()
    move_down()
    turn_left()

while not at_goal():
    if(front_is_clear()):
        move()
    elif(wall_in_front()):
        go_ahead()