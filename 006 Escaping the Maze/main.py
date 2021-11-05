def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
while not at_goal():
    while wall_on_right() and front_is_clear():
        move()
    while front_is_clear():
        move()
    if right_is_clear():
        turn_right()
    elif front_is_clear():
        move()        
    else:
        turn_left()