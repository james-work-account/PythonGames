# Games Repo

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b37e5ebc0e6344e1a16e9e235c2113a6)](https://www.codacy.com/app/james-work-account/PythonGames?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=james-work-account/PythonGames&amp;utm_campaign=Badge_Grade)

### Info

This is a repo documenting various mini games I make while teaching myself Python.

Current game options:

* Blackjack
* FizzBuzz
* Find The Treasure
* Hangman


### Running

To run, first install Python and then enter `python Menu.py` in the terminal.

### Footnotes

##### - Blackjack

A simplified two-player game based on Blackjack. Each player has to
choose whether they want to gamble and receive a random number between
1 and 10 until they either go over 21 or decide they are happy with
their number. The closest to 21 wins.

##### - FizzBuzz

A condense version of the popular FizzBuzz coding challenge. The player
chooses the upper limit, which words will be used to replace the numbers,
and which numbers will be replaced. The full list (between 0 and the
chosen upper limit) is then printed.

##### - Find The Treasure

A game wherein the player has to type in one cardinal direction at a time
to move closer and closer to the treasure. The player and the treasure
are placed randomly on a "board" (choosing the size of the board to be added
in a later iteration). The player will never be placed in the same position
as the treasure.

##### - Hangman

A word is randomly chosen from a word list, and the player has to guess the word. For
each incorrect guess, another piece of a hanged man is drawn until the hanged man is complete
and the game is lost.

### TODO

* Add option to play with custom board size for Find The Treasure from menu
* ~~Remove games referencing the parent class (Menu) when going back to the
main menu~~
* Make sure games conform to pep8 naming standards
* **More games!!**
