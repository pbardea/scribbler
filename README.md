Tic Tac Toe with Scribbler
=========

Final project located in finalPrj directory

*Installation of Speech Recognition Library*
- Install Speech Recognition module using:
    pip install SpeechRecognition
- Install PyAudio from: http://people.csail.mit.edu/hubert/pyaudio/
- Install FLAC tools from: https://xiph.org/flac/download.html
- Also required to install myro to run on scribbler robot

*Summary*
Play tic tac toe with the scribbler robot via voice input.

To make a move, simply state where on the board you want to go (eg 'top left'), or you can give it a position relative to the robot (eg above and to the right of the robot). You can also make your move a full sentence and the robot will understand you, and if you say more than one command it will take the last one you said. The robot can be addressed as 'bot', 'robot', 'Mario' and 'Theo'. If you want a break, when giving your command, say that you want to hear some music and the Mario theme song will play.

*Difficulties*
Easy = random moves

Medium = will try to block you if you can win, but won't try to win

Hard = will try to win and will block you
