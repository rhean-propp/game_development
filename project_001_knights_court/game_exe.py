# Author: Rhean Propp
# Date: January 28, 2022
# Desc: Text Adventure Prototype
# Goal: The game should be fun in its first version of the prototype stage.

from game_functions import *

input_buffer = start_game()                 # Ask user if they would like to play the game.

if "yes" in input_buffer:                   # If yes
    chapter_01()                            # Begin Game
elif "no" in input_buffer:                  # If no
    print("\nThank you for playing.\n")     # Quit Game
    exit()
else:
    print("\nError. Invalid Input\n")