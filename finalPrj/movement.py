##2|3
##_|_
##1|4
##
###use cartesian plane for dictionary
###
from myro import *
import draw

curPos = 1
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
    time_box = 1.62
    motor_speed = 0.5
    if(ud=="up"):
        forward(motor_speed, time_box)
    if(ud=="down"):
        backward(motor_speed, time_box)

def getPos(): #returns current position of the robot
    return grid_position[curPos]

def horizontal_movement(lr): #moves left or right by 1 cell
    time_90 = 1.6478
    time_box = 1.62
    motor_speed = 0.5
    if(lr=="right"):
        threesixty(motor_speed, -1*motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_90)
        wait(.2)
        threesixty(-1*motor_speed, motor_speed, time_90)
    if(lr=="left"):
        threesixty(-1*motor_speed, motor_speed, time_90)
        wait(.2)
        forward(motor_speed, time_90)
        wait(.2)
        threesixty(motor_speed, -1*motor_speed, time_90)
def safeRemove(a,x):
  if x in a:
    a.remove(x)
  return a

def play(destination, element): #move to right corner and play, destination is in cart form
  cartPos = grid_position[curPos]
  valid = [1,2,3,4]
  if destination[0] >= 0:
    valid = safeRemove(valid,1)
    valid = safeRemove(valid,2)
  if destination[0] == -1:
    valid = safeRemove(valid,3)
    valid = safeRemove(valid,4)
  if destination[1] >= 0:
    valid = safeRemove(valid,1)
    valid = safeRemove(valid,4)
  if destination[1] == -1:
    valid = safeRemove(valid,2)
    valid = safeRemove(valid,3)
  if destination[0] == destination[1] and destination[0] == 0:
    valid = [1]
  navCorner(curPos,valid[0])
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
    draw.draw_O_at(ud,lr)
  else:
    draw.draw_l_at(ud,lr)

def navCorner(position, destination):#moves from position to destination

#straight lines between positions
    
    if (position == 1 and destination == 2):
        vertical_movement("up")
    if (position == 4 and destination == 3):
        vertical_movement("up")
    if (position == 2 and destination == 1):
        vertical_movement("down")
    if (position == 3 and destination == 4):
        vertical_movement("down")
    if (position == 1 and destination == 4):
        horizontal_movement("right")
    if (position == 2 and destination == 3):
        horizontal_movement("right")
    if (position == 4 and destination == 1):
        horizontal_movement("left")
    if (position == 3 and destination == 2):
        horizontal_movement("left")
        
#diagonals between positions

    if (position == 1 and destination == 3):
        vertical_movement("up")
        horizontal_movement("right")
    if (position == 2 and destination == 4):
        horizontal_movement("right")
        vertical_movement("down")
    if (position == 3 and destination == 1):
        vertical_movement("down")
        horizontal_movement("left")
    if (position == 4 and destination == 2):
        horizontal_movement("left")
        vertical_movement("up")

    curPos = destination
