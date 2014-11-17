from myro import *

def draw_O(lr):
    time_O = 5.04335
    if(lr=="left"):
        while timeRemaining(time_O):
            motors(-.27, 1.0)
    if(lr=="right"):
        while timeRemaining(time_O):
            motors(1.0, -.27)


def draw_top(lr):
    forward(1, 0.32)
    draw_O(lr)
    backward(1, 0.42)
    stop()

def draw_bottom(lr):
    backward(1, 0.32)
    draw_O(lr)
    forward(1, 0.42)
    stop()


