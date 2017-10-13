import random


class Blackjack:

    WelcomeMessage = "Welcome to Blackjack!"
    playerOneNumber = 0
    playerTwoNumber = 0

    def __init__(self):
        print(self.WelcomeMessage)
        self.playOne()

        while (self.playerOneNumber <= self.playerTwoNumber <= 21):
            raise NotImplemented


    def playOne(self):
        playerOneInput = raw_input("Player 1, your number is %d. Save your number? y/n > " % self.playerOneNumber).lower()
        if playerOneInput == "y":
            print("Number saved: %d" % self.playerOneNumber)
            self.playTwo()
        else:
            self.playerOneNumber += random.randint(1, 10)
            if not self.check21(self.playerOneNumber):
                self.playOne()
            else:
                print("Your number is %d, which is greater than 21!" % self.playerOneNumber)
                self.playTwo()
            
    def playTwo(self):
        playerTwoInput = raw_input("Player 2, your number is %d. Save your number? y/n > " % self.playerTwoNumber).lower()
        if playerTwoInput == "y":
            print("Number saved: %d" % self.playerTwoNumber)
            self.calcWinner()
        else:
            self.playerTwoNumber += random.randint(1, 10)
            if not self.check21(self.playerTwoNumber):
                self.playTwo()
            else:
                print("Your number is %d, which is greater than 21!" % self.playerTwoNumber)
                self.calcWinner()
    
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
        print("Thank you for playing!")
        play_again = raw_input("Play again? (y/n)\n >>  ").lower()
        if (play_again == "y"):
            Blackjack()
        else:
            from Menu import Menu
            Menu()

    def check21(self, inputNumber):
        if inputNumber > 21:
            return True
        else:
            return False
