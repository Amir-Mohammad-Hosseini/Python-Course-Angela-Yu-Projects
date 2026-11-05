Link :
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

code :

def turn_around():
    turn_left()
    turn_left()
    turn_left()

def move_up():
    move()
    turn_left()
    move()

def move_right():
    turn_around()
    move()

def move_down():
    turn_around()
    move()

def go_ahead():
    move_up()
    move_right()
    move_down()
    turn_left()
    
for step in range(0 , 6):
    go_ahead()