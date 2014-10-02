from myro import *

init("com7")

def leftTurnAngle(angle):
	turnLeft(0.3,3.0/90*angle)

leftTurnAngle(90)