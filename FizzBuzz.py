class FizzBuzz():
    WelcomeMessage = "Welcome to FizzBuzz!"

    def __init__(self):
        print(self.WelcomeMessage)
        self.FizzBuzz(range(0, int(raw_input("What is the highest number?\n> "))),
                      self.CSLToArray(raw_input("What words to replace? (comma separated)\n> "), "str"),
                      self.CSLToArray(raw_input("What numbers to replace? (comma separated)\n> "), "int"))

    def CSLToArray(self, CSL, type):
        splitted = CSL.split(",")
        output = []
        if type == "str":
            for word in splitted:
                output.append(str(word))
        elif type == "int":
            for num in splitted:
                output.append(int(num))
        return output

    def FizzBuzz(self, range, strings, rules):
        for i in range:
            outputString = "[%s] " % str(i)
            for rule in rules:
                if i % rule == 0:
                    outputString += strings[rules.index(rule)]
            print(outputString)


FizzBuzz()
