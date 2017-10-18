import random, os


class FindTheTreasure:
    distance = 0
    treasurePos = []
    playerPos = []
    gameComplete = False
    welcomeMessage = "You have awoken in a groggy haze. Your memory is patchy, but you definitely remember seeing " \
                     "some treasure somewhere around here before you passed out...\nTry typing a direction (eg. " \
                     "north, s, w, east, south west, ne) to look for your treasure! \n"
    exitMessage = "You have found the treasure!"
    movementDirection = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    aliases = ["N,NORTH,UP", "E,EAST,RIGHT", "S,SOUTH,DOWN", "W,WEST,LEFT"]

    def __init__(self, boardXSize=10, boardYSize=10):
        os.system('clear')
        print(self.welcomeMessage)
        self.treasurePos = [random.randint(0, boardXSize), random.randint(0, boardYSize)]
        self.generatePlayerPosition(boardXSize, boardYSize)
        while not self.gameComplete:
            self.playGame(self.treasurePos, self.playerPos)
        print(self.exitMessage)
        play_again = raw_input("Play again? (y/n)\n >>  ").lower()
        if play_again == "y":
            FindTheTreasure(boardXSize, boardYSize)

    def generatePlayerPosition(self, boardXSize, boardYSize):
        self.playerPos = [random.randint(0, boardXSize), random.randint(0, boardYSize)]
        if self.playerPos == self.treasurePos:
            self.generatePlayerPosition(boardXSize, boardYSize)

    def playGame(self, treasurePos, playerPos):
        self.calcDistanceFromTreasure()
        print("You are %fm away from the treasure!" % self.distance)
        playerMovement = raw_input(">> ")
        self.movePlayer(playerMovement)
        if playerPos == treasurePos:
            self.gameComplete = True

    def movePlayer(self, inputDir):
        for direction in self.aliases:
            for alias in direction.split(","):
                if inputDir.lower() == alias.lower():
                    self.moveXY(self.movementDirection[self.aliases.index(direction)])

    def moveXY(self, moveDir):
        self.playerPos[0] += moveDir[0]
        self.playerPos[1] += moveDir[1]

    def calcDistanceFromTreasure(self):
        if self.playerPos[0] == self.treasurePos[0]:
            self.distance = float(abs(self.playerPos[1] - self.treasurePos[1]))
        elif self.playerPos[1] == self.treasurePos[1]:
            self.distance = float(abs(self.playerPos[0] - self.treasurePos[0]))
        else:
            from math import sqrt
            self.distance = float(sqrt(
                ((self.treasurePos[0] - self.playerPos[0]) * (self.treasurePos[0] - self.playerPos[0])) +
                ((self.treasurePos[1] - self.playerPos[1]) * (self.treasurePos[1] - self.playerPos[1]))))
            del sqrt
