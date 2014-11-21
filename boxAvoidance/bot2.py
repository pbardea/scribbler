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
    forward(0.5,1)
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

def rightTurn(time):
  turnRight(0.4,time)

def leftTurn(time):
  turnLeft(0.4,time)


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
  rightTurn(1.9)
  
def checkClear(direction):
 if direction==0:
  leftTurn(1.907)
  obs = getAvgOb(1,5)
  rightTurn(1.9)
  if  obs > 900:
    return False
  else:
    return True
 else:
  rightTurn(1.9)
  obs = getAvgOb(1,5)
  leftTurn(1.862)
  if  obs > 900:
    return False
  else:
    return True

def findEdge(direction):
  counter = 0.0
  foundBox = False
  while (not foundBox):
    counter -= 0.5
    forward(-increment[0],increment[1]/2)
    foundBox = not checkClear(direction)
  return counter

def clearSide(direction):
  counter = 0.0
  cleared = False
  while (not cleared):
    counter += 1
    forward(increment[0],increment[1])
    cleared = checkClear(direction)
    if cleared:
      counter += findEdge(direction)
      forward(-0.3,back)
      if direction==0:
        smoothTurn(.2,.625,4.2)
      else:
        smoothTurn(.625,.2,4.2)#####TODO
  return counter

def clearLastSide(cycles,direction):
  forward(increment[0],increment[1]*cycles-back)
  if direction==0:
      rightTurn(1.9)
  else:
      leftTurn(1.907)
  
def setUpPerp():
    direction = 0
    leftTurnAngle(20)
    measure1 = getAvgOb(1,20)
    rightTurnAngle(40)
    measure2 = getAvgOb(1,20)
    leftTurnAngle(20)
    print str(measure1)+" "+str(measure2)
    if abs(measure1-measure2)<100:
        forward(0.5,0.8)
        rightTurnAngle(90)
        return 2
    elif measure1<measure2:
        #forward(0.5,0.7)
        leftTurnAngle(45)
        return 1
    else:
        #forward(0.5,0.7)
        rightTurnAngle(45)
        return 0
    

#STARTS HERE
def box():
  
  forward2(0.3)
  
  direction = setUpPerp()
  count = clearSide(direction%2)
  clearSide(direction%2)
  if direction==0:
      rightTurnAngle(135)
  elif direction==1:
      leftTurnAngle(135)
  elif direction==2:
      clearLastSide(count,direction%2)
  forward(0.5,2)  
box()

