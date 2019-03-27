from Constants import *
from text import Text


class Menu(object):
    def __init__(self):
        self.titleText = Text("font/ARCADE_R.TTF", 70, 'PacMan', YELLOW, 255, 125)
        self.titleText1 = Text("font/ARCADE_R.TTF", 25, 'Press P to play', YELLOW, 320, 215)
        self.titleText2 = Text("font/ARCADE_R.TTF", 25, 'Press H to see high scores', YELLOW, 240, 615)

        self.titleBlinky = Text("font/ARCADE_R.TTF", 50, 'Blinky', WHITE, 350, 475)
        self.titleInkey = Text("font/ARCADE_R.TTF", 50, 'Inkey', WHITE, 370, 475)
        self.titlePinky = Text("font/ARCADE_R.TTF", 50, 'Pinky', WHITE, 370, 475)
        self.titleClyde = Text("font/ARCADE_R.TTF", 50, 'Clyde', WHITE, 370, 475)

        self.hsText = Text("font/ARCADE_R.TTF", 60, 'High Scores', YELLOW, 200, 125)
        self.hsText1 = Text("font/ARCADE_R.TTF", 25, 'Press "ESC" to go back', YELLOW, 230, 615)
        self.hsInGame = Text("font/ARCADE_R.TTF", 20, 'Score: ', YELLOW, 695, 65)
        self.levelText = Text("font/ARCADE_R.TTF", 20, 'Level: ', YELLOW, 90, 65)
        self.loseText = Text("font/ARCADE_R.TTF", 70, 'GAME OVER', YELLOW, 255, 125)

        self.mainScreen = True
        self.highScore = False
        self.startGame = False
        self.gameOver = False
