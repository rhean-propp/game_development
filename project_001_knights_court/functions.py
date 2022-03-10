# ================================================================================ #
# Author: Rhean Propp                                                              #
# Date: January 28, 2022                                                           #
# Desc: Genral functions that do not call other functions are placed in this file. #
# ================================================================================ #

import sys                  # Used for delay_print()
import random               # Used for delay_print()
from time import sleep      # Used for delay_print()

def delay_print(string):                        # Prints strings character by character.
    for character in string:                    # Cycle through each character
        sys.stdout.write(character)             # Write the character to the CMD line.
        if character == '.':                    # If a period is encountered.
            sleep(0.6)                          # Pause for a random time between 1.5 and 1.9 seconds
        if character == ',':                    # If a comma is encountered
            sleep(0.3)                          # Pause for a random time between 0.3 and 0.5 seconds
        sys.stdout.flush()                      # Flush the character from stdout.
        sleep(random.uniform(0.02, 0.07))       # Adjusts overall typing speed.

def help():                                     # Display's a list of commands the user can use.
    print("\n---------------\n Command List:\n---------------\n\t\t\t\t\t\t|")
    print("\thelp\t\t\t\t\t| Lists commands user can use.\n\t\t\t\t\t\t|")
    print("\tinv\t\t\t\t\t| Displays user's inventory.\n\t\t\t\t\t\t|")
    print("\tsave\t\t\t\t\t| Saves the game from the last checkpoint.\n\t\t\t\t\t\t|")
    print("\tuse <item>\t\t\t\t| Uses an item from the user's inventory.\n\t\t\t\t\t\t|")
    print("\tmove\t\t\t\t\t| Displays movement help menu.\n\t\t\t\t\t\t|")
    print("\tattack <creature/object> with <item>\t| Attack creature/object with item from user inventory.\n\t\t\t\t\t\t|")
    print("\texamine <object>\t\t\t| Examines an object if the object can be examined.\n\t\t\t\t\t\t|\n")

def move_player():
    print("\n-------------------------\n Moving Within the Game:\n-------------------------\n")
    print("\twalk\t\t| forward, right, backward, left, north, east, south, west\n\t\t\t|")
    print("\trun\t\t| forward, right, backward, left, north, east, south, west\n\t\t\t|")
    print("\tjump\t\t| over, on\n\t\t\t|")
    print("\tclimb\t\t| up, down, left, right, east, west\n\t\t\t|")
    print("\tswim\t\t| up, down, forward, backward, left, right, north, east, south, west\n\t\t\t|")
    
def short_hand_commands():
    print("\n-------------------------\n Short Hand Command List:\n-------------------------\n")
    print("\t  |\n\tn | Moves player north/forward\n\t  |")
    print("\te | Moves player east/right\n\t  |")
    print("\ts | Moves player south/backward\n\t  |")
    print("\tw | Moves player west/left\n\t  |")
    print("\td | Moves player downwards\n\t  |")
    print("\tu | Moves player updwards\n\t  |")
    print("\ti | Displays player inventory\n\t  |")
    print("\th | Displays help menu\n\t  |")