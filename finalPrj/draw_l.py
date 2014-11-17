#use c=1, d=-1 or vise versa
# 45 degree turn = 0.438
# 90 degree turn = 0.835
# 180 degree turn = 1.6478
# 360 degree turn = 3.2835
#at full speed for all times

def draw_l(ud):#it's a little L not a one
    if(lr=="up"):
        time_90 = 1.6478
        time_box = 1.62
        motor_speed = 0.5
        threesixty(-1*motor_speed, motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_box)
        wait(.2)
        backward(motor_speed, time_box)
        wait(.2)
        threesixty(motor_speed, -1*motor_speed, time_90)
    if(lr=="down"):
        threesixty(motor_speed, -1*motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_box)
        wait(.2)
        backward(motor_speed, time_box)
        wait(.2)
        threesixty(-1*motor_speed, motor_speed, time_90)

def draw_l_left_and_right(ud, lr):
    time_90 = 1.6478
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
    threesixty(-1*motor_speed, motor_speed, time_90)

