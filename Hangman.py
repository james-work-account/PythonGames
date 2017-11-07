class Hangman(object):
    input_letter = ""
    word_to_guess = ""
    word_to_guess_char_list = []
    DICTIONARY = "wordlist.txt"
    FILE = open(DICTIONARY, "r")
    list_of_words = []
    mutable_hidden_word = []
    count = 0
    game_complete = False
    wrong_guesses = []
    number_of_guesses = 0
    HANGED_MAN = {
        0: "     \n    |      \n    |      \n    |      \n    |       \n    |      \n    |\n____|________\n",
        1: "     _______\n    |      \n    |      \n    |      \n    |       \n    |      \n    |\n____|________\n",
        2: "     _______\n    |/      \n    |      \n    |      \n    |       \n    |      \n    |\n____|________\n",
        3: "     _______\n    |/      |\n    |      \n    |      \n    |       \n    |      \n    |\n____|________\n",
        4: "     _______\n    |/      |\n    |      (_)\n    |      \n    |       \n    |      \n    |\n____|________\n",
        5: "     _______\n    |/      |\n    |      (_)\n    |       |\n    |       |\n    |      \n    |\n____|________\n",
        6: "     _______\n    |/      |\n    |      (_)\n    |      \\|\n    |       |\n    |      \n    |\n____|________\n",
        7: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      \n    |\n____|________\n",
        8: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      / \n    |\n____|________\n",
        9: "     _______\n    |/      |\n    |      (_)\n    |      \\|/\n    |       |\n    |      / \\\n    |\n____|________\n"
    }

    def __init__(self):
        print "Welcome to Hangman!"
        self.reset_all()
        self.add_words_to_list()
        self.get_random_word(self.list_of_words, self.read_word_list_length(self.DICTIONARY))
        self.FILE.close()
        self.create_hidden_word(self.word_to_guess)
        while not self.game_complete:
            self.play_game()
        play_again = raw_input("Play again? (y/n)\n> ").lower()
        if play_again == "y":
            Hangman()


    # SETUP FUNCTIONS
    def reset_all(self):
        self.word_to_guess = ""
        self.wrong_guesses = []
        self.mutable_hidden_word = []
        self.game_complete = False
        self.count = 0
        self.word_to_guess_char_list = []
        self.number_of_guesses = 0
        self.input_letter = ""


    def add_words_to_list(self):
        if not self.list_of_words:
            for line in self.FILE:
                self.list_of_words.append(line)


    @staticmethod
    def read_word_list_length(fileName):
        with open(fileName) as f:
            i = -1
            for i, l in enumerate(f, 1):
                pass
        return i


    def get_random_word(self, listOfWords, wordListLength):
        from random import randint
        randomWord = randint(0, wordListLength-1)
        self.word_to_guess = listOfWords[randomWord].replace("\n", "")


    def create_hidden_word(self, wordToHide):
        for char in range(0, len(wordToHide)):
            self.mutable_hidden_word.append("_")


    # GAMEPLAY FUNCTIONS
    def play_game(self):
        if "_" in self.mutable_hidden_word:
            self.print_hanged_man()
            self.print_hidden_word()
            self.print_wrong_guesses()
            self.take_player_guess()
            self.check_player_guess(self.input_letter)
            self.number_of_guesses += 1
            if self.count == 9:
                print "You lose!"
                print "Correct word: " + self.word_to_guess
                self.game_complete = True
        else:
            self.print_hanged_man()
            self.print_hidden_word()
            print "Congratulations, you win! Your word was \"%s\". Tt took you %d guesses to win."\
                  % (self.word_to_guess, self.number_of_guesses)
            self.game_complete = True


    def take_player_guess(self):
        player_input = raw_input("\nInput a letter: >>  ")
        if len(player_input) > 1:
            self.take_player_guess()
        else:
            self.input_letter = player_input


    def check_player_guess(self, guess):
        if guess not in self.word_to_guess:
            self.count += 1
            self.wrong_guesses.append(guess)
        else:
            for letter in range(0, len(self.word_to_guess)):
                if self.word_to_guess[letter] == guess:
                    self.mutable_hidden_word[letter] = guess

    def print_hidden_word(self):
        print " ".join(self.mutable_hidden_word)


    def print_wrong_guesses(self):
        if not self.wrong_guesses == []:
            print "Wrong guesses: " + ", ".join(self.wrong_guesses)


    def print_hanged_man(self):
        try:
            print self.HANGED_MAN[self.count]
        except KeyError:
            print "Dictionary key is invalid!"
