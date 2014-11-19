from random import randint
from myro import *
import wav
import recognizeAudio
import draw
import movement

debug = False

board = {}				#Creating and initializing the grid
for i in range(0, 9):
  board[i] = '_'

combs=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #List of all winning combinations

def drawGrid():
  for i in range(0,3):
    print '|',
    print board[i],
  print '|'
  for i in range(3,6):
    print '|',
    print board[i],
  print '|'
  for i in range(6,9):
    print '|',
    print board[i],
  print '|'		#Draws the grid

def chkCorner():
  if board[0] == 'X' and board[8] == '_':
    return 8
  if board[2] == 'X' and board[6] == '_':
    return 6
  if board[8] == 'X' and board[0] == '_':
    return 0
  if board[6] == 'X' and board[2] == '_':
    return 2
  return -1	#Checks if corner is occupied by opponent. Returns the other corner.

def gridComplete():
  for i in range(0,9):
    if board[i] == '_':
      return 0
  return 1	#Checks if grid is complete

def win():
  for comb in combs:
    if board[comb[0]] == board[comb[1]] == board[comb[2]] =='X':
      return 'X'
    elif board[comb[0]] == board[comb[1]] == board[comb[2]] == 'O':
      return 'O'
  return 0; #Check if someone has won.

def oneLeft():
  for comb in combs:
    if board[comb[0]] == board[comb[1]] == '_' and board[comb[2]] == 'O': #returns two open spaces in a line; useful when blocking forks
      return [comb[0], comb[1]]
    elif board[comb[0]] == board[comb[2]] == '_' and board[comb[1]] == 'O':
      return [comb[0], comb[2]]
    elif board[comb[2]] == board[comb[1]] == '_' and board[comb[0]] == 'O':
      return [comb[2], comb[1]]		#Checks if a row/column/diagonal has one space taken and two empty spaces. Returns the two empty spaces

def twoLeft(): 			#Checks if a row/column/diagonal has two spaces taken and one empty space. Returns the empty space
  for comb in combs:
    if board[comb[0]] == board[comb[1]] and board[comb[2]] == '_':
      if board[comb[0]] == 'O':
        return [comb[2], 'O']
      elif board[comb[0]] == 'X':
        return [comb[2], 'X']
    elif board[comb[1]] == board[comb[2]] and board[comb[0]] == '_':
      if board[comb[1]] == 'O':
        return [comb[0], 'O']
      elif board[comb[1]] == 'X':
        return [comb[0], 'X']
    elif board[comb[2]] == board[comb[0]] and board[comb[1]] == '_':
      if board[comb[2]] == 'O':
        return [comb[1], 'O']
      elif board[comb[2]] == 'X':
        return [comb[1], 'X']
  return [-1, '_']

def arrToCart(arr):
  hor  = arr%3-1
  vert = -(arr/3)+1
  return [hor,vert]

def usrTurn(botPos):			#Function that executes a user's turn
  print "botpos 89",botPos
  flag = 0
  while(flag==0): 
    n1 = recognizeAudio.getMove()#input("Player 1\n >")
    if n1 >= 0 and n1 <= 8 and board[n1] == '_':
      flag = 1
  if (not debug):
    botPos = movement.play(botPos,arrToCart(n1),'l')
  board[n1] = 'X'
  return botPos
    


def cpuTurn(diff,botPos):			#Function that executes a CPU's turn. This is where the priority list is.
  flag = 0
  print "Start botpos",botPos
  print("CPU's turn")
  if diff == 'H':
    if(twoLeft()[1] == 'O'):		#Priority one- Complete your line
      if (not debug):
        botPos = movement.play(botPos,arrToCart(twoLeft()[0]),'O')
      board[twoLeft()[0]] = 'O'
      return
    elif(twoLeft()[1] == 'X'):		#Priority two - Block the opponent's line
      if (not debug):
        botPos = movement.play(botPos,arrToCart(twoLeft()[0]),'O')
      board[twoLeft()[0]] = 'O'
      return
    elif oneLeft():					#Priority three - Block fork by creating an opportunity
      if (not debug):
        botPos = movement.play(botPos,arrToCart(oneLeft()[0]),'O')
      board[oneLeft()[0]] = 'O'
    elif board[4] == '_':					#Priority four - Get the center
      if (not debug):
        botPos = movement.play(botPos,arrToCart(4),'O')
      board[4] = 'O'
      return
    elif chkCorner()!=-1:			#Priority five - Get the opposite end	
      if (not debug):
        botPos = movement.play(botPos,arrToCart(chkCorner()),'O')
      board[chkCorner()] = 'O'
    else:							#Priority six - Whatever. I don't care
      for i in range(0,9):
        if board[i] == '_':
          if (not debug):
            botPos = movement.play(botPos,arrToCart(i),'O')
          board[i] = 'O'
          break
  elif diff == 'M':
    if(twoLeft()[1] == 'O'):    #Priority one- Complete your line
      if (not debug):
        botPos = movement.play(botPos,arrToCart(twoLeft()[0]),'O')
      board[twoLeft()[0]] = 'O'
      return
    elif(twoLeft()[1] == 'X'):    #Priority two - Block the opponent's line
      if (not debug):
        botPos = movement.play(botPos,arrToCart(twoLeft()[0]),'O')
      board[twoLeft()[0]] = 'O'
      return
    else:             #Priority six - Whatever. I don't care
      for i in range(0,9):
        if board[i] == '_':
          if (not debug):
            botPos = movement.play(botPos,arrToCart(i),'O')
          board[i] = 'O'
          break
  elif diff == 'E':
    flag = 0
    while flag == 0:
      i = randint(0,8)
      if(board[i] == '_'):
        if (not debug):
        	botPos = movement.play(botPos,arrToCart(i),'O')
        board[i] = 'O'
        flag = 1
  return botPos

def run():
  usrStart = 0					
  diff = ''
  botPos = 1
  #wav.playMusic('')
  while(not(usrStart =='Y') and not(usrStart =='N')):
    speak("Press 'Y' if you want to start, 'N' if you don't.")
    usrStart = raw_input(" >")
  while not(diff == 'E' or diff == 'M' or diff == 'H'):
    speak("Enter the difficulty level. (E/M/H)")
    diff = raw_input(" >")
  while(gridComplete()==0):
    if usrStart=='Y':
      botPos = usrTurn(botPos)
    elif usrStart=='N':
      botPos = cpuTurn(diff,botPos)
    drawGrid()
    if(win()!=0):
      break
    flag = 0
    if(gridComplete() == 1):
      break
    if usrStart=='Y':
      botPos =cpuTurn(diff,botPos)
    elif usrStart=='N':
      botPos = usrTurn(botPos)
    drawGrid()
    if(win()!=0):
      break
    print "botpos main",botPos

  if win() == 'X':
    speak("Player 1 wins")
  elif win() == 'O':
    speak("Player 2 wins")
  else:
    speak("It's a draw")
    #Main function
