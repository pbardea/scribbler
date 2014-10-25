#from myro import *

#init("com7")
increment = [0.3,1.2] ##set increment speed, time (between checks)
back = 1

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
    threshold=900
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
    forward(0.5,0.7)
    return distance

def getAvgOb(obs, num):
    total = 0.0;
    for i in range (0,num):
        total += getObstacle(obs);
    total = total/num;
    return total;

def smoothTurn(ltSpd, rtSpd, time):
  while timeRemaining(time):
    motors(ltSpd,rtSpd)
  stop()

def rightTurnAngle(angle):
  turnRight(0.3,3.0/90*angle)

def leftTurnAngle(angle):
  turnLeft(0.3,3.01/90*angle)

def rightTurn():
  turnRight(0.4,1.9)

def leftTurn():
  turnLeft(0.4,1.907)


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

def checkClearLeft():
  leftTurn()
  obs = getAvgOb(1,5)
  rightTurn()
  if  obs > 900:
    return False
  else:
    return True
  
def checkClearRight():
  rightTurn()
  obs = getAvgOb(1,5)
  leftTurn()
  if  obs > 900:
    return False
  else:
    return True

def findEdge():
  counter = 0.0
  foundBox = False
  while (not foundBox):
    counter -= 0.5
    forward(-increment[0],increment[1]/2)
    foundBox = not checkClearLeft()
  return counter

def clearSide(direction):
  counter = 0.0
  cleared = False
  while (not cleared):
    counter += 1
    forward(increment[0],increment[1])
    cleared = checkClearLeft()
    if cleared:
      counter += findEdge()
      forward(-0.3,back)
      if direction==0:
        smoothTurn(.2,.625,4.2)
      else:
        smoothTurn(.625,.2,4.2)#####TODO
  return counter

def clearLastSide(cycles,direction):
  forward(increment[0],increment[1]*cycles-back)
  if direction==0:
      rightTurn()
  else:
      leftTurn()
  forward(0.5,2)
  
def setUpPerp():
    direction = 0
    #leftTurnAngle(20)
    measure1 = getAvgOb(1,10)
    #rightTurnAngle(40)
    measure2 = getAvgOb(1,10)+250
    #leftTurnAngle(20)
    print str(measure1)+" "+str(measure2)
    #if abs(measure1-measure2)<200:
    forward(0.5,0.8)
    rightTurnAngle(90)
    #elif measure1<measure2:
    #    forward(0.5,0.7)
    #    leftTurnAngle(45)
    #    return 1
    #else:
    #    forward(0.5,0.7)
    #    rightTurnAngle(45)
    return 0
    

#STARTS HERE
def box():
  
  forward2(0.3)
  
  direction = setUpPerp()
  count = clearSide(direction%2)
  clearSide(direction%2)
  clearLastSide(count,direction%2)
box()

