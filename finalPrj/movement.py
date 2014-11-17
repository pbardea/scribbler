##2|3
##_|_
##1|4
##
###use cartesian plane for dictionary
###



def vertical_movement(ud):
    time_box = 1.62
    motor_speed = 0.5
    if(ud=="up"):
        forward(motor_speed, time_box)
    if(ud=="down"):
        backward(motor_speed, time_box)

def horizontal_movement(lr):
    time_90 = 1.6478
    time_box = 1.62
    motor_speed = 0.5
    if(lr=="right"):
        threesixty(motor_speed, -1*motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_90)
        wait(.2)
        threesixty(-1*motor_speed, motor_speed, time_90)
    if(lr=="left"):
        threesixty(-1*motor_speed, motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_90)
        wait(.2)
        threesixty(motor_speed, -1*motor_speed, time_90)

def movement(position, destination):
    grid_position = {1: {-0.5, -0.5}, 2: {-0.5, 0.5}, 3: {0.5, 0.5}, 4: {0.5, -0.5}}

#straight lines between positions
    
    if (position == 1 and destination == 2):
        vertical_movement("up")
    if (position == 4 and destination == 3):
        vertical_movement("up")
    if (position == 2 and destination == 1):
        vertical_movement("down")
    if (position == 3 and destination == 4):
        vertical_movement("down")
    if (position == 1 and destination == 4):
        horizontal_movement("right")
    if (position == 2 and destination == 3):
        horizontal_movement("right")
    if (position == 4 and destination == 1):
        horizontal_movement("left")
    if (position == 3 and destination == 2):
        horizontal_movement("left")
        
#diagonals between positions

    if (position == 1 and destination == 3):
        vertical_movement("up")
        horizontal_movement("right")
    if (position == 2 and destination == 4):
        horizontal_movement("right")
        vertical_movement("down")
    if (position == 3 and destination == 1):
        vertical_movement("down")
        horizontal_movement("left")
    if (position == 4 and destination == 2):
        horizontal_movement("left")
        vertical_position("up")
