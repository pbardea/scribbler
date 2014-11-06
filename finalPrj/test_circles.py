#from myro import *
#init("com7")
#circle calibration
def circle_right():
    forward(1, 0.22)
    while timeRemaining(5.045335):
        motors(1.0, -.27)
    forward(1, 0.32)
    stop()

def circle_left():
    forward(1, 0.22)
    while timeRemaining(5.04335):
        motors(-.27, 1.0)
    forward(1, 0.32)
    stop()
#suggest a realigning def using the light sensors
#must cross a line before everymore

#forward(1, .57)
#^^^^^^^^^^^^^^^this is for one square
#distance across
