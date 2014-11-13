"""
Used to read in speech input and convert it to a action represented by numeric output.
"""
import speech_recognition as sr #import the speech recognition module

#global thesaurus
thesaurus = {'top':['top','up','upper','highest','uppermost','zenith','climax','above'], 'bottom':['bottom','down','base','lowest','floor','bottommost','below','under','underneath'],'left':['left','leftmost'],'right':['right','rightmost'],'middle':['middle','between'],'centre':['centre'],'bot':{'robot','bot','theo','mario'}}

def getAudio(tries):
    # r = sr.Recognizer(language = "en-US", key = "AIzaSyC0BY4MvU0DNvVkRuK0r9uSHtcl_SPdylI")
    triesThreshold = 2
    r = sr.Recognizer() #initialize the recognizer
    audioStr  = "Nothing yet..."
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

def convertCoord(cartesian):
    arrayCoord = -1;
    for i in range(-1,2):
        for j in range(-1,2):
            if (cartesian[0] == i and cartesian[1] == j):
                i+=1
                j+=1
                j = 2-j
                arrayCoord = j*3+i%3
    return arrayCoord

def wordToInt(word):
  convert = ['zero','one','two','three','four','five','six','seven','eight','nine']
  #array serach function

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
        vertical += lastInt
      elif word in thesaurus['bottom']:
        vertical -= lastInt
      elif word in thesaurus['left']:
        horizontal -= lastInt
      elif word in thesaurus['right']:
        horizontal += lastInt
  return [horizontal,vertical]


def getMove(spoken,botPos):
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
        elif word == thesaurus['centre']:
            vertical = 0
            horizontal = 0
        elif word in thesaurus['bot']:
            print "Calling relative motion"
            newPos = relativeMotion(spoken,[-0.5,0.5]) 
            horizontal = newPos[0]
            vertical = newPos[1]
            break
        print word, horizontal, vertical
    return [horizontal,vertical]
    
spoken = getAudio(0)
# spoken = raw_input(":")
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
print getMove(spoken,[-1,1])
