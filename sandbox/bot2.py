#from myro import *

#init("com7")
increment = [0.3,1.2] #set increment speed, time (between checks)
clearCorner = [0.3,2.6]
back = 2

'''
todo:
  calibrate 90 degree turns
  what if box isn't perpendicular
  make corners tighter
  RELIABLE
  multiple object detection
'''

def forward2(speed):
    average=getAvgOb(1,10);
    threshold=1070
    distance=0
    while(True):
        average = getAvgOb(1,10)
        #average = averagetAvgOb(1,1)/10 + average*9/10
        print average
        if(average>threshold):
            print "Breaking"
            break
        forward(speed,0.3)
        distance += 0.3;
    return distance

def getAvgOb(obs, num):
    total = 0.0;
    for i in range (0,num):
        total += getObstacle(obs);
    total = total/num;
    return total;

def smoothLeft(ltSpd, rtSpd, time):
  while timeRemaining(time):
    motors(ltSpd,rtSpd)
  stop()

def rightTurnAngle(angle):
  turnRight(0.3,3.0/90*angle)

def rightTurn():
  turnRight(0.4,1.9)

def leftTurn():
  turnLeft(0.4,1.9)


def approachBox():
  obs = False
  forward(0.4)  
  dataCounter = 0
  avg = 0

  while(not obs):
    data = getObstacle()
    avg = (avg*9+data[1])/10

    if avg > 960:
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
  if getObstacle(2) > 900:
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
      forward(-0.3,back)
      smoothLeft(.2,.6,4)
    else:
      rightTurn()
  return counter

def clearLastSide(cycles):
  for i in range(cycles):
      forward(increment[0],increment[1])
  forward(-0.3,back)
  rightTurn()
  forward(0.4,5)
  


#STARTS HERE
forward2(0.5)
forward(0.5,0.8)
rightTurn()
count = clearSide()
clearSide()
clearLastSide(count)
