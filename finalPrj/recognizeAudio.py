"""
Used to read in speech input and convert it to a action represented by numeric output.
"""
import speech_recognition as sr #import the speech recognition module
text_debug = False

#global thesaurus
thesaurus = {'top':['top','up','upper','highest','uppermost','zenith','climax','above'], 'bottom':['bottom','down','base','lowest','floor','bottommost','below','under','underneath'],'left':['left','leftmost'],'right':['right','rightmost'],'middle':['middle','between'],'centre':['centre','center'],'bot':['robot','bot','theo','mario']}



def getAudio(tries):
    # r = sr.Recognizer(language = "en-US", key = "AIzaSyC0BY4MvU0DNvVkRuK0r9uSHtcl_SPdylI")
    triesThreshold = 2
    r = sr.Recognizer() #initialize the recognizer
    audioStr  = "Nothing yet..."
    raw_input("Press enter when you are ready to give a command.") #waits until user is ready. user presses entre to indicate that they are ready to start speaking
    print "Listening..."
    with sr.Microphone() as source: #Take the microphone as the audio source
        audio = r.listen(source) #listen until the first pause

    r.pause_threshold = 0.8
    r.energy_threshold = 200

    try:
        audioStr  = r.recognize(audio) #store audio in audioStr
    except LookupError: #can't understand audio
        if tries < triesThreshold:
            print "Sorry, didn't catch that. Please try again."
            audioStr = getAudio(tries+1)
        else:
            audioStr = raw_input("Could not understand audio, please enter your command: ")
        # audioStr = "Could not understand audio"

    return audioStr

def convertCartToArr(cartesian):
    arrayCoord = -1;
    if -99 in cartesian:
      return -1
    for i in range(-1,2):
        for j in range(-1,2):
            if (cartesian[0] == i and cartesian[1] == j):
                i+=1
                j+=1
                j = 2-j
                arrayCoord = j*3+i%3
    return arrayCoord

def wordToInt(word):
  convert = [['zero','none','nada'],['one','once','singular'],['two','twice','double']]
  for i in range(len(convert)):
    if word in convert[i]:
      return i

def relativeMotion(statement, botPos):#if a robot keyword is triggered, the last 10 words is passed back for decomposition
  #define botPos as a cartesian system with the bottom left corner of the centre cell as 0,0. Assuming staying on corners of centre cell
  horizontal = botPos[0]
  vertical = botPos[1]
  lastInt = 1 #default, so if user says 'left', it will move one left of the robot by deafult
  for word in statement:
    if wordToInt(word) >= 0: #then a number was spoken
      lastInt = wordToInt(word)
    else: #process as a word
      if word in thesaurus['top']:
        if lastInt == 1:
          vertical += 0.5
        else:
          vertical += 1.5
        lastInt = 1
      elif word in thesaurus['bottom']:
        if lastInt == 1:
          vertical -= 0.5
        else:
          vertical -= 1.5
        lastInt = 1
      elif word in thesaurus['left']:
        if lastInt == 1:
          horizontal -= 0.5
        else:
          horizontal -= 1.5
        lastInt = 1
      elif word in thesaurus['right']:
        if lastInt == 1:
          horizontal += 0.5
        else:
          horizontal += 1.5
        lastInt = 1
  if horizontal == -99 or vertical == -99:
    print horizontal, vertical, "line 76"
    return getMove()
  else:
    print botPos[0], botPos[1], horizontal, vertical, "all good!"
    return [horizontal,vertical]


def interpret(spoken,botPos):
    vertical = -99
    horizontal = -99
    spoken = spoken.lower().rstrip().split()
    for i in range(len(spoken)):
        word = spoken[i]
        if word in thesaurus['top']:
            vertical = 1
        elif word in thesaurus['bottom']:
            vertical = -1
        elif word in thesaurus['middle'] and horizontal != -99:
            vertical = 0
        elif word in thesaurus['left']:
            horizontal = -1
        elif word in thesaurus['right']:
            horizontal = 1
        elif word in thesaurus['middle'] and vertical != -99:
            horizontal = 0
        elif word in thesaurus['middle']:
            vertical = 0
        elif word in thesaurus['centre']:
            vertical = 0
            horizontal = 0
        elif word in thesaurus['bot']:
            print "Calling relative motion"
            newPos = relativeMotion(spoken,[-0.5,0.5]) 
            horizontal = newPos[0]
            vertical = newPos[1]
            return convertCartToArr([horizontal,vertical])
        print word, horizontal, vertical
    return convertCartToArr([horizontal,vertical])
    
def getMove():
  if (text_debug):
    spoken = raw_input(":")
  else:
    spoken = getAudio(0)
  print spoken
  print """   
               _________________
               |     |    |    |
               |-1,1 | 0,1|1,1 |
               -----------------
               |     |    |    |
               |-1,0 | 0,0|1,0 |
               -----------------
               |     |    |    |
               |-1,-1|0,-1|1,-1|
               ----------------
  """
  return interpret(spoken,[-1,1])
