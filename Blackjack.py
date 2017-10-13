import random


class Blackjack:

    WelcomeMessage = "Welcome to Blackjack!"
    ExitMessage = "Thank you for playing!"
    playerOneNumber = 0
    playerTwoNumber = 0
    playerXNumber = 0
    playerOneTurnOver = playerTwoTurnOver = False

    def __init__(self):
        print(self.WelcomeMessage)
        
        while self.playerOneTurnOver is False:
            self.playGame(1)
            
        while self.playerTwoTurnOver is False:
            self.playGame(2)
            
        self.calcWinner()
        print(self.ExitMessage)
        play_again = raw_input("Play again? (y/n)\n >>  ").lower()
        if play_again == "y":
            Blackjack()
        else:
            from Menu import Menu
            Menu()


    def playGame(self, playerNumber):
        self.setPlayerXValue(playerNumber)
        playerInput = raw_input("Player %d, your number is %d. Save your number? y/n > " % (playerNumber, self.playerXNumber)).lower()
        if playerInput == "y":
            self.setPlayerValue(playerNumber)
            print("Number saved: %d" % self.playerXNumber)
            if playerNumber == 1:
                self.playerOneTurnOver = True
            elif playerNumber == 2:
                self.playerTwoTurnOver = True
            else:
                print "ERROR"
                exit()
        else:
            self.playerXNumber += random.randint(1, 10)
            if playerNumber == 1:
                self.setPlayerValue(1)
                if self.check21(self.playerOneNumber):
                    self.playerOneTurnOver = True
            elif playerNumber == 2:
                self.setPlayerValue(2)
                if self.check21(self.playerTwoNumber):
                    self.playerTwoTurnOver = True

    def setPlayerXValue(self, playerNumber):
        if playerNumber == 1:
            self.playerXNumber = self.playerOneNumber
        elif playerNumber == 2:
            self.playerXNumber = self.playerTwoNumber
        else:
            print "ERROR"
            exit()

    def setPlayerValue(self, playerNumber):
        if playerNumber == 1:
            self.playerOneNumber = self.playerXNumber
        elif playerNumber == 2:
            self.playerTwoNumber = self.playerXNumber


    def calcWinner(self):
        if self.playerTwoNumber < self.playerOneNumber <= 21:
            print("Player 1 Wins!")
        elif self.playerOneNumber < self.playerTwoNumber <= 21:
            print("Player 2 Wins!")
        elif self.playerTwoNumber > 21 >= self.playerOneNumber:
            print("Player 1 Wins!")
        elif self.playerOneNumber > 21 >= self.playerTwoNumber:
            print("Player 2 Wins!")
        else:
            print("You both LOSE!")


    def check21(self, playerNumber):
        if playerNumber > 21:
            print("Your number is %d, which is greater than 21!" % playerNumber)
            return True
        else:
            return False
