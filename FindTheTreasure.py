import random, os


class FindTheTreasure:
    treasureXPos = treasureYPos = playerXPos = playerYPos = distance = 0
    treasurePos = []
    playerPos = []
    gameComplete = False
    welcomeMessage = """You have awoken in a groggy haze. Your memory is patchy, but you definitely remember seeing some treasure somewhere around here before you passed out...
   Try typing "north", "south", "east" or "west" to look for your treasure!""".replace("   ", "")
    exitMessage = "You have found the treasure!"

    def __init__(self, boardXSize, boardYSize):
        os.system('clear')
        print(self.welcomeMessage)
        self.treasureXPos = random.randint(0, boardXSize)
        self.treasureYPos = random.randint(0, boardYSize)
        self.treasurePos = [self.treasureXPos, self.treasureYPos]
        self.generatePlayerPosition(boardXSize, boardYSize)
        while not self.gameComplete:
            self.playGame(self.treasurePos, self.playerPos)
        print(self.exitMessage)
        play_again = raw_input("Play again? (y/n)\n >>  ").lower()
        if play_again == "y":
            FindTheTreasure(boardXSize, boardYSize)
        else:
            from Menu import Menu
            Menu()

    def generatePlayerPosition(self, boardXSize, boardYSize):
        self.playerXPos = random.randint(0, boardXSize)
        self.playerYPos = random.randint(0, boardYSize)
        self.playerPos = [self.playerXPos, self.playerYPos]
        if self.playerPos == self.treasurePos:
            self.generatePlayerPosition(boardXSize, boardYSize)
        else:
            pass

    def playGame(self, treasurePos, playerPos):
        self.calcDistanceFromTreasure()
        print("You are %fm away from the treasure!" % self.distance)
        playerMovement = raw_input(">> ")
        self.movePlayer(playerMovement)
        if playerPos == treasurePos:
            self.gameComplete = True
        else:
            pass

    def movePlayer(self, inputDir):
        if inputDir.lower() == "north":
            self.playerPos[0] += 1
        elif inputDir.lower() == "south":
            self.playerPos[0] -= 1
        elif inputDir.lower() == "east":
            self.playerPos[1] += 1
        elif inputDir.lower() == "west":
            self.playerPos[1] -= 1
        else:
            pass

    def calcDistanceFromTreasure(self):
        if self.playerPos[0] == self.treasurePos[0]:
            self.distance = float(abs(self.playerPos[1] - self.treasurePos[1]))
        elif self.playerPos[1] == self.treasurePos[1]:
            self.distance = float(abs(self.playerPos[0] - self.treasurePos[0]))
        else:
            from math import sqrt
            self.distance = float(sqrt(((self.treasurePos[0] - self.playerPos[0]) * (self.treasurePos[0] - self.playerPos[0])) + ((self.treasurePos[1] - self.playerPos[1]) * (self.treasurePos[1] - self.playerPos[1]))))
