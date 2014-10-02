from myro import *

init("com7")

def leftTurnAngle(angle):
	turnLeft(0.3,3.0/90*angle)

def smoothLeft(ltSpd, rtSpd, time):
  while timeRemaining(time):
    motors(ltSpd,rtSpd)
  stop()

leftTurnAngle(90)
