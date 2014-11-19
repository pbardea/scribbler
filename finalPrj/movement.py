##2|3
##_|_ ##1|4
##
###use cartesian plane for dictionary
###
from myro import *
import draw

grid_position = {1: [-0.5, -0.5], 2: [-0.5, 0.5], 3: [0.5, 0.5], 4: [0.5, -0.5]}


#use c=1, d=-1 or vise versa
# 45 degree turn = 0.438
# 90 degree turn = 0.835
# 180 degree turn = 1.6478
# 360 degree turn = 3.2835
def threesixty(c, d, t):
    while timeRemaining(t):
        motors(c, d)
    stop()


def vertical_movement(ud):#move up or down by a cell
    time_box_fwd = 1.57
    time_box_back = 1.6
    motor_speed_lateral = 0.5
    motor_speed_turn = 0.3
    if(ud=="up"):
        forward(motor_speed_lateral, time_box_fwd)
    if(ud=="down"):
        backward(motor_speed_lateral, time_box_back)

# def getPos(curPos): #returns current position of the robot
#     return grid_position[curPos]

def horizontal_movement(lr): #moves left or right by 1 cell
    time_90_right = 3.04 #time for motors to turn right
    time_90_left = 3.05 #time for motors to turnn left
    time_box_fwd = 1.57
    time_box_back = 1.6
    motor_speed_turn = 0.3
    motor_speed_lateral = 0.5
    if(lr=="right"):
        threesixty(motor_speed_turn, -1*motor_speed_turn, time_90_left)#right turn
        wait(.2)
        forward(motor_speed_lateral, time_box_fwd)
        wait(.2)
        threesixty(-1*motor_speed_turn, motor_speed_turn, time_90_right)#left turn
    if(lr=="left"):
        threesixty(-1*motor_speed_turn, motor_speed_turn, time_90_right)#left turn
        wait(.2)
        forward(motor_speed_lateral, time_box_fwd)
        wait(.2)
        threesixty(motor_speed_turn, -1*motor_speed_turn, time_90_left)#right turn

def safeRemove(a,x):
  if x in a:
    a.remove(x)
  return a

def play(curPos,destination, element): #move to right corner and play, destination is in cart form
  print "curPos",curPos
  cartPos = grid_position[curPos]#of robot
  valid = [1,2,3,4]
  if destination[0] == 1:
    valid = safeRemove(valid,1)
    valid = safeRemove(valid,2)
  elif destination[0] == -1:
    valid = safeRemove(valid,3)
    valid = safeRemove(valid,4)
  if destination[1] == 1:
    valid = safeRemove(valid,1)
    valid = safeRemove(valid,4)
  elif destination[1] == -1:
    valid = safeRemove(valid,2)
    valid = safeRemove(valid,3)
  if curPos in valid:
    valid = [curPos]
  print "cartPos: ",cartPos,"valid",valid,"curpos",curPos,"destination",destination
  navCorner(curPos,valid[0])#both in arr form
  curPos = valid[0] #valid 
  if (not curPos):
    print "NOT CUR POS!cartPos: ",cartPos,"valid",valid,"curpos",curPos,"destination",destination
  cartPos = grid_position[curPos]
  print "cartPos: ",cartPos, "destination:",destination,"curpos",curPos
  ud = "up"
  lr = "left"
  if destination[0] < cartPos[0]:
    lr = "left"
  else:
    lr = "right"
  if destination[1] < cartPos[1]:
    ud = "down"
  else:
    ud = "up"
  if element == "O":
    print "O",ud,lr
    draw.draw_O_at(ud,lr)
  else:
    print "l",ud,lr
    draw.draw_l_at(ud,lr)
  return curPos

def navCorner(position, destination):#moves from position to destination

#straight lines between positions
    print "move from ",position," to ",destination

    
    if (position == 1 and destination == 2):
        print "move up"
        vertical_movement("up")
    if (position == 4 and destination == 3):
        print "move up"
        vertical_movement("up")
    if (position == 2 and destination == 1):
        print "move down"
        vertical_movement("down")
    if (position == 3 and destination == 4):
        print "move down"
        vertical_movement("down")
    if (position == 1 and destination == 4):
        print "move right"
        horizontal_movement("right")
    if (position == 2 and destination == 3):
        print "move right"
        horizontal_movement("right")
    if (position == 4 and destination == 1):
        print "move left"
        horizontal_movement("left")
    if (position == 3 and destination == 2):
        print "move left"
        horizontal_movement("left")
        
#diagonals between positions

    if (position == 1 and destination == 3):
        print "move up"
        vertical_movement("up")
        print "move right"
        horizontal_movement("right")
    if (position == 2 and destination == 4):
        print "move right"
        horizontal_movement("right")
        print "move down"
        vertical_movement("down")
    if (position == 3 and destination == 1):
        print "move down"
        vertical_movement("down")
        print "move left"
        horizontal_movement("left")
    if (position == 4 and destination == 2):
        print "move left"
        horizontal_movement("left")
        print "move up"
        vertical_movement("up")
