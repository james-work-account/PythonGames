class CurlyBoyPrinter:
    WelcomeMessage = "How many Curly Boys?"

    def __init__(curlyBoy):
        print(curlyBoy.WelcomeMessage)
        curlyBoy.curlyBoyCount(input("> "))

    def curlyBoyCount(curlyBoy, curlyBoyNumber):
        print("{ " * curlyBoyNumber + "%d  C U R L Y  B O Y S" % curlyBoyNumber + " }" * curlyBoyNumber)


CurlyBoyPrinter()
