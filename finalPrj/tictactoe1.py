from random import randint
import recognizeAudio

a = {}				#Creating and initializing the grid
for i in range(0, 9):
  a[i] = '_';

combs=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #List of all winning combinations

def drawGrid():
  for i in range(0,3):
    print '|',
    print a[i],
  print '|'
  for i in range(3,6):
    print '|',
    print a[i],
  print '|'
  for i in range(6,9):
    print '|',
    print a[i],
  print '|'		#Draws the grid

def chkCorner():
  if a[0] == 'X' and a[8] == '_':
    return 8
  if a[2] == 'X' and a[6] == '_':
    return 6
  if a[8] == 'X' and a[0] == '_':
    return 0
  if a[6] == 'X' and a[2] == '_':
    return 2
  return -1	#Checks if corner is occupied by opponent. Returns the other corner.

def gridComplete():
  for i in range(0,9):
    if a[i] == '_':
      return 0
  return 1	#Checks if grid is complete

def win():
  for comb in combs:
    if a[comb[0]] == a[comb[1]] == a[comb[2]] =='X':
      return 'X'
    elif a[comb[0]] == a[comb[1]] == a[comb[2]] == 'O':
      return 'O'
  return 0; #Check if someone has won.

def oneLeft():
  for comb in combs:
    if a[comb[0]] == a[comb[1]] == '_' and a[comb[2]] == 'O': #returns two open spaces in a line; useful when blocking forks
      return [comb[0], comb[1]]
    elif a[comb[0]] == a[comb[2]] == '_' and a[comb[1]] == 'O':
      return [comb[0], comb[2]]
    elif a[comb[2]] == a[comb[1]] == '_' and a[comb[0]] == 'O':
      return [comb[2], comb[1]]		#Checks if a row/column/diagonal has one space taken and two empty spaces. Returns the two empty spaces

def twoLeft(): 			#Checks if a row/column/diagonal has two spaces taken and one empty space. Returns the empty space
  for comb in combs:
    if a[comb[0]] == a[comb[1]] and a[comb[2]] == '_':
      if a[comb[0]] == 'O':
        return [comb[2], 'O']
      elif a[comb[0]] == 'X':
        return [comb[2], 'X']
    elif a[comb[1]] == a[comb[2]] and a[comb[0]] == '_':
      if a[comb[1]] == 'O':
        return [comb[0], 'O']
      elif a[comb[1]] == 'X':
        return [comb[0], 'X']
    elif a[comb[2]] == a[comb[0]] and a[comb[1]] == '_':
      if a[comb[2]] == 'O':
        return [comb[1], 'O']
      elif a[comb[2]] == 'X':
        return [comb[1], 'X']
  return [-1, '_']

def usrTurn():			#Function that executes a user's turn
  flag = 0
  n1 = -99
  while(flag==0): 
    while (n1<0):
      n1 = recognizeAudio.getMove()#raw_input("Player 1\n >")
    if a[n1] == '_':
      flag = 1
  a[n1] = 'X'

def cpuTurn():			#Function that executes a CPU's turn. This is where the priority list is.
  flag = 0
  print("CPU's turn")
  if(twoLeft()[1] == 'O'):		#Priority one- Complete your line
    a[twoLeft()[0]] = 'O'
    return
  elif(twoLeft()[1] == 'X'):		#Priority two - Block the opponent's line
    a[twoLeft()[0]] = 'O'
    return
  elif oneLeft():					#Priority three - Block fork by creating an opportunity
    a[oneLeft()[0]] = 'O'
  elif a[4] == '_':					#Priority four - Get the center
    a[4] = 'O'
    return
  elif chkCorner()!=-1:			#Priority five - Get the opposite end	
    a[chkCorner()] = 'O'
  else:							#Priority six - Whatever. I don't care
    for i in range(0,9):
      if a[i] == '_':
        a[i] = 'O'
        break

def main():
  c = 0					
  while(not(c =='Y') and not(c =='N')):
    c = raw_input("Press 'Y' if you want to start, 'N' if you don't.\n >")
  while(gridComplete()==0):
    if c=='Y':
      usrTurn()
    elif c=='N':
      cpuTurn()
    drawGrid()
    if(win()!=0):
      break
    flag = 0
    if(gridComplete() == 1):
      break
    if c=='Y':
      cpuTurn()
    elif c=='N':
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

main()
