def forward2(speed,threshold):
    average=getAvgOb(1,10)
    distance=0
    while(True):
        average = getAvgOb(1,10)
        #average = averagetAvgOb(1,1)/10 + average*9/10
        #print average
        if(average>threshold):
            #print "Breaking"
            break
        forward(speed,0.3)
        distance += 0.3;
    return distance

def turnRightA(angle):
    turnRight(0.3,3.0/90*angle)

def turnLeftA(angle):
    turnLeft(0.3,3.0/90*angle)

def getAvgOb(obs, num):
    total = 0.0;
    for i in range (0,num):
        total += getObstacle(obs);
    total = total/num;
    return total;

def findClosestAngle():
    dist2=0;
    dist1=0;
    for i in range (0,10):
        dist2=getAvgOb(1,20);
        print "is "+str(dist2)+"<"+str(dist1)+"?";
        if(dist2<dist1):
            break;
            print "Break at "+str(i);
        dist1=dist2;
        rightTurnAngle(9);

def verifyClose():
    average0=0;
    average1=0;
    average2=0;
    for i in range(0,20):
        average0 += getObstacle(0)/20;
        average1 += getObstacle(1)/20;
        average2 += getObstacle(2)/20;
    print str(average0)+", "+str(average1);
    if(average0>1020 and average1>1080):
        print "Hello??";
        return True;
    return False;
def box():
    for i in range(0,4):
        forward2(0.5);
        forward(0,0.5);
        backward(1,1);
#box()

#while(not verifyClose()):
#    forward(0.05,0.5);

#forward(0.2,0.4)
def test():
    for i in range(0,1):
        forward2();
        forward(0.5,0.55);
        forward(0,1);
        forward(-1,1.5);
        forward(0,1);
        
#findClosestAngle();

#while True:
#    print str(getAvgOb(0,50))+" "+str(getAvgOb(1,50))+" "+str(getAvgOb(2,50))

def firstEdge():
    count = 0;
    stage=0;
    while True:
        leftTurnAngle(18);
        count+=1
        ir = getIR()
        if(stage==0 and ir[1]==0):
            print("Found box at: "+str(count*4.5))
            break;
            stage+=1
        if(stage==1 and ir[0]==1):
            print("Stopped at: "+str(count*4.5))
            break;
        count+=1
    forward(0)

def zig():
    forward2(0.5);
    x=0.0
    y=0.0
    while(True):
        rightTurnAngle(90);
        x+=0.8
        forward(0.3,0.8);
        leftTurnAngle(90);
        y+=forward2(0.3);
    #rightTurnAngle(90);


#zig();

def fRightTurn():
    forward2(0.5)
    forward(0.4,0.2)
    obs=0;

def test2():
    obs = 0.0
    left = []
    right = []
    centre = []
    for j in range(45):
        obs = getAvgOb(1,10)
        left.append(getAvgOb(0,20))
        centre.append(getAvgOb(1,20))
        right.append(getAvgOb(2,20))
        forward(0.2,0.4)
    for i in left:
        print i
    print ""
    for i in centre:
        print i
    print ""
    for i in right:
        print i


def test3():
    obs = 0.0
    leftIr = []
    rightIr = []
    left = []
    right = []
    centre = []
    angle = 10
    for j in range(360/angle):
        obs = getAvgOb(1,10)
        left.append(getAvgOb(0,20))
        centre.append(getAvgOb(1,20))
        right.append(getAvgOb(2,20))
        rightTurnAngle(angle)
    print "Left"
    for i in left:
        print i
    print "Centre"
    for i in centre:
        print i
    print "Right"
    for i in right:
        print i
    print "IR LEFT"
    for i in leftIr:
        print i
    print "IR Right"
    for i in rightIr:
        print i

def test4():
    angle = 5
    obs = 1
    counter1 = 0
    counter2 = 0
    while(obs):       
        data = getAvgOb(1,20)
        print data
        #if data[0] < 500 and data[1] < 500 and data[2] < 400:
        if data < 500:
            obs = 0
            print "First stop at "+str(angle*counter1)
        else:
            rightTurnAngle(angle)
        counter1 += 1


        
    leftTurnAngle(counter1*angle)
    obs = 1
    while(obs):
        data = getAvgOb(1,20)
        print data
       # if data[0] < 500 and data[1] < 500 and data[2] < 400:
        if data < 500:
            obs = 0
            print "Second stop at "+str(angle*counter2)
        else:
            leftTurnAngle(angle)
        counter2 += 1

    rightTurnAngle(counter2*angle)
    if counter1 < counter2:
        rightTurnAngle(counter1*angle+10)
    else:
        leftTurnAngle(counter2*angle+10)
   
    
#test4()

threshold = 300;
sensor = 0
def findLeftEdgeFluke():
    turn = -30#########
    turnLeftA(30)##########
    a = getAvgOb(sensor,10)
    if a<threshold:
        for i in range(0,3):
            turn-=5
            turnLeftA(5)
            a = getAvgOb(sensor,10)
            if  a>threshold:
                break
    else:
        while a>threshold:
            turn+=5
            turnRightA(5)
            a = getAvgOb(sensor,10)
    return turn

def findLeftEdgeIR():
    turn = -45
    turnLeftA(45)
    if getIR(0)==1:
        for i in range(0,5):
            if getIR(0)==0:
                break;
            turnLeftA(2)
            turn-=2
    else:
        while getIR(0)==0:
            turnRightA(2)
            turn+=2
    return turn

def doBox():
    forward2(0.5,1000)#base approach of box
    forward(0.25,2)#extra forward boost
    lastTurn=0
    thisTurn=0
    counter=0
    turnLeftA(90)
    while True:
        thisTurn = findLeftEdgeIR()
        print thisTurn
        turnRightA(45)########
        forward(-0.5,0.5)
        lastTurn=thisTurn
doBox();

def calibrate():
    while True:
        print getAvgOb(0,10)

#calibrate()

print "DONE";
