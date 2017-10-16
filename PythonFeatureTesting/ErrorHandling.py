class ErrorHandling:
    def __init__(self):
        try:
            print(int("this will not work"))
        except ValueError:
            print("string to int error caught!")

        try:
            print(int("this will not work"))
        except TypeError:
            print("this code will never run")
        except NotImplementedError:
            print("neither will this")
        except:
            print("general error case hit!")

        try:
            int(3)
        except:
            print("the try case will pass")
        else:
            print("here, the try case passes")

        try:
            raise Exception("eggs", "bacon")
        except Exception as breakfast:
            print(type(breakfast))
            print(breakfast.args)
            ingredient_1, ingredient_2 = breakfast.args
            print("ingredients of breakfast are %s and %s" % (ingredient_1, ingredient_2))



ErrorHandling()
