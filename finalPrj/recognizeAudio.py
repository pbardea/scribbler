import speech_recognition as sr #import the speech recognition module

def getAudio():
    # r = sr.Recognizer(language = "en-US", key = "AIzaSyC0BY4MvU0DNvVkRuK0r9uSHtcl_SPdylI")
    r = sr.Recognizer() #initialize the recognizer
    audioStr = "Nothing yet..."
    with sr.Microphone() as source: #Take the microphone as the audio source
        audio = r.listen(source) #listen until the first pause

    try:
        audioStr  = r.recognize(audio) #store audio in audioStr
    except LookupError: #can't understand audio
        audioStr = "Could not understand audio"

    return audioStr

def decypherAudio(spoken):
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
        elif (word == 'center'):
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
print decypherAudio(spoken)
