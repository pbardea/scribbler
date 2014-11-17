from random import randint
import recognizeAudio
import draw
import movement

board = {}				#Creating and initializing the grid
for i in range(0, 9):
  board[i] = '_';

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

def usrTurn():			#Function that executes a user's turn
  flag = 0
  while(flag==0): 
    n1 = recognizeAudio.getMove()#input("Player 1\n >")
    if n1 >= 0 and n1 <= 8 and board[n1] == '_':
      flag = 1
  board[n1] = 'X'
  movement.play(arrToCart(n1),'l')


def cpuTurn():			#Function that executes a CPU's turn. This is where the priority list is.
  flag = 0
  print("CPU's turn")
  if(twoLeft()[1] == 'O'):		#Priority one- Complete your line
    board[twoLeft()[0]] = 'O'
    movement.play(arrToCart(twoLeft()[0]),'O')
    return
  elif(twoLeft()[1] == 'X'):		#Priority two - Block the opponent's line
    board[twoLeft()[0]] = 'O'
    movement.play(arrToCart(twoLeft()[0]),'O')
    return
  elif oneLeft():					#Priority three - Block fork by creating an opportunity
    board[oneLeft()[0]] = 'O'
    movement.play(arrToCart(oneLeft()[0]),'O')
  elif board[4] == '_':					#Priority four - Get the center
    board[4] = 'O'
    movement.play(arrToCart(4),'O')
    return
  elif chkCorner()!=-1:			#Priority five - Get the opposite end	
    board[chkCorner()] = 'O'
    movement.play(arrToCart(chkCorner()),'O')
  else:							#Priority six - Whatever. I don't care
    for i in range(0,9):
      if board[i] == '_':
        board[i] = 'O'
        movement.play(arrToCart(i),'O')
        break

def run():
  usrStart = 0					
  while(not(usrStart =='Y') and not(usrStart =='N')):
    usrStart = raw_input("Press 'Y' if you want to start, 'N' if you don't.\n >")
  while(gridComplete()==0):
    if usrStart=='Y':
      usrTurn()
    elif usrStart=='N':
      cpuTurn()
    drawGrid()
    if(win()!=0):
      break
    flag = 0
    if(gridComplete() == 1):
      break
    if usrStart=='Y':
      cpuTurn()
    elif usrStart=='N':
      usrTurn()
    drawGrid()
    if(win()!=0):
      break

  if win() == 'X':
    print "Player 1 wins"
  elif win() == 'O':
    print "Player 2 wins"
  else:
    print "It's a draw"				#Main function
