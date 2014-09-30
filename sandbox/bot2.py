from myro import *

'''
step 1: approach box and turn right 90 deg when close
'''

init("/dev/tty.IPRE6-185826-DevB")

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
    forward(0.4,1)
    cleared = checkClear()
    if cleared:
      forward(0)
    else:
      rightTurn()
  return counter

def clearLast(cycles):
  for i in range(cycles):
    forward(0.4,1)
  rightTurn()
  forward(0.4,5)
  

approachBox()
count = clearSide()
if getObstacle(0) > 500:
  rightTurn()
  forward(0.4,0.6)
  leftTurn()
forward(0.4,2)
clearSide()
if getObstacle(0) > 500:
  rightTurn()
  forward(0.4,0.6)
  leftTurn()
clearLast(count)
