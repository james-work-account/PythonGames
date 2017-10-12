#!/usr/bin/python

import os


class Menu:
    menu_actions = {}

    def __init__(self):
        os.system('clear')

        print "Welcome to the Games menu!\n"
        print "Please choose the game you wish to start:"
        print "1. Blackjack"
        print "2. FizzBuzz"
        print "\n0. Quit"
        self.choice = raw_input(" >>  ")
        if self.choice == '1':
            print "Choice: 1"
            from Blackjack import Blackjack
            Blackjack()
        elif self.choice == '2':
            print "Choice: 2"
            from FizzBuzz import FizzBuzz
            FizzBuzz()
        elif self.choice == '0':
            print "Exiting menu..."
            exit()
        else:
            print "You did not choose wisely.\nExiting..."
            exit()


Menu()
