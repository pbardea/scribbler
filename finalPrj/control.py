import recognizeAudio

command = ""
while (command != "done"):
    command =recognizeAudio.getAudio()
    print command
