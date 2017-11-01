class FizzBuzz(object):
    WelcomeMessage = "Welcome to FizzBuzz!"

    def __init__(self):
        print(self.WelcomeMessage)
        self.FizzBuzz(range(0, int(raw_input("What is the highest number?\n> "))),
                      self.CSLToArray(raw_input("What words to replace? (comma separated)\n> "), "str"),
                      self.CSLToArray(raw_input("What numbers to replace? (comma separated)\n> "), "int"))
        play_again = raw_input("Play again? (y/n)\n> ").lower()
        if play_again == "y": FizzBuzz()

    @staticmethod
    def CSLToArray(CSL, inputType):
        splitted = CSL.split(",")
        output = []
        if inputType == "str":
            for word in splitted:
                output.append(str(word))
        elif inputType == "int":
            for num in splitted:
                output.append(int(num))
        return output

    @staticmethod
    def FizzBuzz(inputRange, strings, rules):
        for i in inputRange:
            outputString = "[%s] " % str(i)
            for rule in rules:
                if i % rule == 0:
                    outputString += strings[rules.index(rule)]
            print(outputString)
