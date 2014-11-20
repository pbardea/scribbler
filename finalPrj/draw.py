from myro import *
import movement

#draw 0
def draw_O(lr):
    time_O_right = 9.9
    time_O_left = 9.9
    if(lr=="left"):
        wait(0.2)
        while timeRemaining(time_O_left):
            motors(-.135, 0.5)
        wait(0.2)
        while timeRemaining(0.07):
            motors(0,-0.05)
        wait(0.2)
    if(lr=="right"):
        wait(0.2)
        while timeRemaining(time_O_right):
            motors(0.5, -.135)
        wait(0.2)
        while timeRemaining(0.05):
            motors(-0.05,0)
        wait(0.2)


def draw_O_top(lr):
    time_box_fwd = 1.57
    time_box_back = 1.6
    motor_speed_lateral = 0.5

    forward(motor_speed_lateral, time_box_fwd/2)
    wait(0.2)
    draw_O(lr)
    wait(0.2)
    backward(motor_speed_lateral, time_box_back/2)
    stop()

def draw_O_bottom(lr):
    time_box_fwd = 1.57
    time_box_back = 1.6
    motor_speed_lateral = 0.5

    backward(motor_speed_lateral, time_box_back/2)
    wait(0.2)
    draw_O(lr)
    wait(0.2)
    forward(motor_speed_lateral, time_box_fwd/2)
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
    
    time_45_right = 2.95/2
    time_45_left = 3.04/2
    time_diagonal_box = 1.57
    motor_speed_turn = 0.3
    motor_speed_lateral = 0.5

    if (ud=="up" and lr=="right"):
        movement.threesixty(motor_speed_turn, -1*motor_speed_turn, time_45_right)#right turn
        forward(motor_speed_lateral,time_diagonal_box)
        wait(.2)
        backward(motor_speed_lateral,time_diagonal_box)
        movement.threesixty(-1*motor_speed_turn, motor_speed_turn, time_45_left)#left turn

    if (ud=="up" and lr=="left"):
        movement.threesixty(-1*motor_speed_turn, motor_speed_turn, time_45_left)#left turn
        forward(motor_speed_lateral,time_diagonal_box)
        wait(.2)
        backward(motor_speed_lateral,time_diagonal_box)
        movement.threesixty(motor_speed_turn, -1*motor_speed_turn, time_45_right)#right turn

    if (ud=="down" and lr=="right"):
        movement.threesixty(-1*motor_speed_turn, motor_speed_turn, time_45_left)#left turn
        backward(motor_speed_lateral,time_diagonal_box)
        wait(.2)
        forward(motor_speed_lateral,time_diagonal_box)
        movement.threesixty(motor_speed_turn, -1*motor_speed_turn, time_45_right)#right turn

    if (ud=="down" and lr=="left"):
        movement.threesixty(motor_speed_turn, -1*motor_speed_turn, time_45_right)#right turn
        backward(motor_speed_lateral,time_diagonal_box)
        wait(.2)
        forward(motor_speed_lateral,time_diagonal_box)
        movement.threesixty(-1*motor_speed_turn, motor_speed_turn, time_45_left)#left turn
    
   
