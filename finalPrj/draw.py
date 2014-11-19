from myro import *
import movement

#draw 0
def draw_O(lr):
    time_O_right = 5.04335
    time_O_left = 5.04335
    if(lr=="left"):
        while timeRemaining(time_O_left):
            motors(-.27, 1.0)
    if(lr=="right"):
        while timeRemaining(time_O_right):
            motors(1.0, -.27)


def draw_O_top(lr):
    forward(1, 0.32)
    draw_O(lr)
    backward(1, 0.42)
    stop()

def draw_O_bottom(lr):
    backward(1, 0.32)
    draw_O(lr)
    forward(1, 0.42)
    stop()

def draw_O_at(ud,lr):
  if ud == "up":
    draw_O_top(lr)
  else:
    draw_O_bottom(lr)

# draw straight line
#use c=1, d=-1 or vise versa
# 45 degree turn = 0.438
# 90 degree turn = 0.835
# 180 degree turn = 1.6478
# 360 degree turn = 3.2835
#at full speed for all times

#accepts up, down, left and right

def draw_l_at(ud, lr):
    
    time_45_right = 0.835
    time_45_left = 0.835
    time_diagonal_box = 0.82
    motor_speed = 0.5

    if (ud=="up" and lr=="right"):
        movement.threesixty(motor_speed, -1*motor_speed, time_45_right)#right turn
        forward(time_diagonal_box)
        wait(.2)
        backward(time_diagonal_box)
        movement.threesixty(-1*motor_speed, motor_speed, time_45_left)#left turn

    if (ud=="up" and lr=="left"):
        movement.threesixty(-1*motor_speed, motor_speed, time_45_left)#left turn
        forward(time_diagonal_box)
        wait(.2)
        backward(time_diagonal_box)
        movement.threesixty(motor_speed, -1*motor_speed, time_45_right)#right turn

    if (ud=="down" and lr=="right"):
        movement.threesixty(-1*motor_speed, motor_speed, time_45_left)#left turn
        backward(time_diagonal_box)
        wait(.2)
        forward(time_diagonal_box)
        movement.threesixty(motor_speed, -1*motor_speed, time_45_right)#right turn

    if (ud=="down" and lr=="left"):
        movement.threesixty(motor_speed, -1*motor_speed, time_45_right)#right turn
        backward(time_diagonal_box)
        wait(.2)
        forward(time_diagonal_box)
        movement.threesixty(-1*motor_speed, motor_speed, time_45_left)#left turn
    
   
