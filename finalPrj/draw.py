from myro import *

#draw 0
def draw_O(lr):
    time_O = 5.04335
    if(lr=="left"):
        while timeRemaining(time_O):
            motors(-.27, 1.0)
    if(lr=="right"):
        while timeRemaining(time_O):
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

def draw_l(ud):#it's a little L not a one
    
    time_90 = 1.6478
    time_box = 1.62
    motor_speed = 0.5
        
    if(ud=="up"):
        threesixty(-1*motor_speed, motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_box)
        wait(.2)
        backward(motor_speed, time_box)
        wait(.2)
        threesixty(motor_speed, -1*motor_speed, time_90)
    if(ud=="down"):
        threesixty(motor_speed, -1*motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_box)
        wait(.2)
        backward(motor_speed, time_box)
        wait(.2)
        threesixty(-1*motor_speed, motor_speed, time_90)

def draw_l_at(ud, lr):
    
    time_90 = 1.65
    time_half_box = 0.82
    motor_speed = 0.5
    
    threesixty(motor_speed, -1*motor_speed, time_90)
    wait(.2)
    if (lr=="left"):
        backward(motor_speed, time_half_box)
        wait(.2)
        draw_l(ud)
        forward(motor_speed, time_half_box)
    elif (lr=="right"):
        forward(motor_speed, time_half_box)
        wait(.2)
        draw_l(ud)
        backward(motor_speed, time_half_box)
    wait(.2)
    threesixty(-1*motor_speed, motor_speed, time_90-0.1)

