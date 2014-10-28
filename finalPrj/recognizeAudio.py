import speech_recognition as sr #import the speech recognition module

def getAudio():
    r = sr.Recognizer() #initialize the recognizer
    with sr.Microphone() as source: #Take the microphone as the audio source
        audio = r.listen(source) #listen until the first pause

    try:
        audioStr  = r.recognize(audio) #store audio in audioStr
    except LookupError: #can't understand audio
        print("Could not understand audio")

getAudio()
