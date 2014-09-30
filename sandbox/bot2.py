from myro import *

init("/dev/tty.IPRE6-185826-DevB")
increment = [0.4,1] #set increment speed, time (between checks)

'''
todo:
  calibrate 90 degree turns
  what if box isn't perpendicular
  make corners tighter
  RELIABLE
  multiple object detection
'''


def rightTurnAngle(angle):
  turnRight(0.3,3.0/90*angle)

def rightTurn():
  turnRight(0.3,2.9)

def leftTurn():
  turnLeft(0.3,2.9)


def approachBox():
  obs = False
  forward(0.4)  
  dataCounter = 0

  while(not obs):
    data = getObstacle()
    if data[1] > 1050:
      dataCounter += 1
    else:
      dataCounter = 0

    if dataCounter > 2:
      obs = True

  forward(0)
  rightTurn()

def checkClear():
  leftTurn()
  if getObstacle(1) > 800:
    return False
  else:
    return True


def clearSide():
  counter = 0
  cleared = False
  while (not cleared):
    counter += 1
    forward(increment[0],increment[1])
    cleared = checkClear()
    if cleared:
      forward(0)
    else:
      rightTurn()
  return counter

def clearLastSide(cycles):
  for i in range(cycles):
    forward(increment[0],increment[1])
  rightTurn()
  forward(0.4,5)
  

def boost(threshold):#this function gives it a little boost if the left sensor exceeds a certain threshold
  if getObstacle(0) > threshold:#this adds a little boost if an obstacle is detected by the left sensor.
    rightTurn()
    forward(0.4,0.6)#amount of boost
    leftTurn()

approachBox()
count = clearSide()
boost(400)
forward(0.4,2)#you know that you have to go forward at least the length of the robot, so no point in keep checking
clearSide()
boost(400)
clearLastSide(count)
