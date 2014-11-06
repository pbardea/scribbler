import speech_recognition as sr #import the speech recognition module

def getTextInput():

def getAudio():
    # r = sr.Recognizer(language = "en-US", key = "AIzaSyC0BY4MvU0DNvVkRuK0r9uSHtcl_SPdylI")
    r = sr.Recognizer() #initialize the recognizer
    audioStr = "Nothing yet..."
    with sr.Microphone() as source: #Take the microphone as the audio source
        audio = r.listen(source) #listen until the first pause

    try:
        audioStr  = r.recognize(audio) #store audio in audioStr
    except LookupError: #can't understand audio
        # audioStr = "Could not understand audio"
        audioStr = raw_input("Could not understand audio, please enter your command: ")

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

def getMove(spoken,botPos):
    vertical = -99
    horizontal = -99
    spoken = spoken.rstrip().split()
    topSyn = ['top','up','upper','highest','uppermost','zenith','climax']
    botSyn = ['bottom','down','base','lowest','floor','bottommost']
    leftSyn = ['left','leftmost']
    rightSyn = ['right','rightmost']
    for i in range(len(spoken)):
        word = spoken[i]
        if word in topSyn:
            vertical = 1
        elif word in botSyn:
            vertical = -1
        elif ((word == 'middle') or (word == 'between')) and horizontal != -99:
            vertical = 0
        elif word in leftSyn:
            horizontal = -1
        elif word in rightSyn:
            horizontal = 1
        elif ((word == 'middle') or (word == 'between')) and vertical != -99:
            horizontal = 0
        elif (word == 'centre'):
            vertical = 0
            horizontal = 0
        elif (word == 'middle') or (word == 'between'):
            vertical = 0
    return [horizontal,vertical]
    
spoken = getAudio()
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
print getMove(spoken,[)
