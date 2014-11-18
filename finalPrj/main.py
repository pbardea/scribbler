import draw
import movement
import recognizeAudio
import tictactoe
debug = True

if (not debug):
  from myro import *
  init("/dev/tty.IPRE6-185826-DevB")

tictactoe.run()
