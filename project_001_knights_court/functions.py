# Author: Rhean Propp
# Date: January 28, 2022
# Desc: Genral functions that do not call other functions are placed in this file.

import sys                  # Used for delay_print()
import random               # Used for delay_print()
from time import sleep      # Used for delay_print()

def delay_print(string):                        # Prints strings character by character.
    for character in string:                    # Cycle through each character
        sys.stdout.write(character)             # Write the character to the CMD line.
        if character == '.':                    # If a period is encountered.
            sleep(random.uniform(1.5, 1.9))     # Pause for a random time between 1.5 and 1.9 seconds
        if character == ',':                    # If a comma is encountered
            sleep(random.uniform(0.3, 0.5))     # Pause for a random time between 0.3 and 0.5 seconds
        sys.stdout.flush()                      # Flush the character from stdout.
        sleep(random.uniform(0.02, 0.07))       # Adjusts overall typing speed.

def help():                                     # Display's a list of commands the user can use.
    print("\nCommand List:\n\t\t\t\t\t\t|")
    print("\thelp\t\t\t\t\t| Lists commands user can use.\n\t\t\t\t\t\t|")
    print("\tinv\t\t\t\t\t| Displays user's inventory.\n\t\t\t\t\t\t|")
    print("\tsave\t\t\t\t\t| Saves the game from the last checkpoint.\n\t\t\t\t\t\t|")
    print("\tuse <item>\t\t\t\t| Uses an item from the user's inventory.\n\t\t\t\t\t\t|")
    print("\tmove <direction>\t\t\t| Move character in specific direction.\n\t\t\t\t\t\t|")
    print("\tattack <creature/object> with <item>\t| Attack creature/object with item from user inventory.\n\t\t\t\t\t\t|")
    print("\tread <object>\t\t\t\t| Reads an object if the object can be read.\n\t\t\t\t\t\t|")
