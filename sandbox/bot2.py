from myro import *

init("com7")
increment = [0.3,1.2] #set increment speed, time (between checks)
clearCorner = [0.3,2.6]

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
  turnRight(0.2,4.48)

def leftTurn():
  turnLeft(0.2,4.52)


def approachBox():
  obs = False
  forward(0.4)  
  dataCounter = 0
  avg = 0

  while(not obs):
    data = getObstacle()
    avg = (avg*9+data[1])/10

    if avg > 800:
      obs = True

    # if data[1] > 1100:
    #   dataCounter += 1
    # else:
    #   dataCounter = 0

    # if dataCounter > 9:
    #   obs = True

  forward(0)
  rightTurn()

def checkClear():
  leftTurn()
  if getObstacle(0) > 1000:
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
      rightTurn()
      forward(clearCorner[0],clearCorner[1])
      leftTurn()
    else:
      rightTurn()
  return counter

def clearLastSide(cycles):
  forward(clearCorner[0],clearCorner[1])
  for i in range(cycles):
    forward(increment[0],increment[1])
  rightTurn()
  forward(0.4,5)
  


#STARTS HERE
approachBox()
count = clearSide()
forward(0.4,2)#you know that you have to go forward at least the length of the robot, so no point in keep checking
clearSide()
forward(0.4,0.4)#make sure you have enough room to turn right at the end
clearLastSide(count)
