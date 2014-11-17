#use c=1, d=-1 or vise versa
# 45 degree turn = 0.438
# 90 degree turn = 0.835
# 180 degree turn = 1.6478
# 360 degree turn = 3.2835
#at full speed for all times

def draw_l(ud):#it's a little L not a one
    if(lr=="up"):
        threesixty(-1, 1, 0.835)
        wait(.2)
        forward(1, 0.81)
        wait(.2)
        backward(1, 0.81)
        wait(.2)
        threesixty(1, -1, 0.835)
        wait(.2)
    if(lr=="down"):
        threesixty(1, -1, 0.835)
        wait(.2)
        forward(1, 0.81)
        wait(.2)
        backward(1, 0.81)
        wait(.2)
        threesixty(-1, 1, 0.835)
        wait(.2)

def draw_l_left_and_right(ud, lr):
    threesixty(1, -1, 0.835)
    wait(.2)
    if (lr=="left"):
        backward(1, 0.405)
        wait(.2)
        draw_l(ud)
        forward(1, 0.405)
    elif (lr=="right"):
        forward(1, 0.405)
        wait(.2)
        draw_l(ud)
        backward(1, 0.405)
    wait(.2)
    threesixty(-1, 1, 0.835)

##everything here is for going to the right so far
##both of these are the same!
