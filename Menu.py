#!/usr/bin/python

import Blackjack
import FizzBuzz
import os


class Menu:
    menu_actions = {}

    def __init__(self):
        os.system('clear')

        print("""Welcome to the Games menu!\n
        Please choose the game you wish to start:
        1. Blackjack
        2. FizzBuzz
        \n0. Quit""".replace("  ", ""))
        self.choice = raw_input(">>  ")
        if self.choice == '1':
            Blackjack.Blackjack()
        elif self.choice == '2':
            FizzBuzz.FizzBuzz()
        elif self.choice == '0':
            print("Exiting menu...")
            exit()
        else:
            print("You did not choose wisely.\nExiting...")
            exit()


Menu()
