from myro import *

init("/dev/tty.IPRE6-185826-DevB")

obs = False
forward(0.5)  

while(not obs):
  data = getObstacle()
  if data[1] > 1200:
    obs = True

forward(0)
