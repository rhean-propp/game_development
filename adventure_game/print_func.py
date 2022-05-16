# ================================================================================ #
# Author: Rhean Propp                                                              #
# Date: January 28, 2022                                                           #
# Desc: Genral functions that do not call other functions are placed in this file. #
# ================================================================================ #

import sys                  # Used for delay_print()
import random               # Used for delay_print()
from time import sleep      # Used for delay_print()

# ============================== #
# General Purpose Game Functions #
# ============================== #

def delay_print(string):                        # Prints strings character by character.
    for character in string:                    # Cycle through each character
        sys.stdout.write(character)             # Write the character to the CMD line.
        if character == '.':                    # If a period is encountered.
            sleep(0.6)                          # Pause for a random time between 1.5 and 1.9 seconds
        if character == ',':                    # If a comma is encountered
            sleep(0.3)                          # Pause for a random time between 0.3 and 0.5 seconds
        sys.stdout.flush()                      # Flush the character from stdout.
        sleep(random.uniform(0.02, 0.07))       # Adjusts overall typing speed.

def game_over():                                # Displays Game over ASCII art and quits program.
    
    print('\n  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  \n ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒\n▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒\n░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  \n░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒\n ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░\n  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░\n░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ \n      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     \n                                                     ░                   \n')
    sys.exit()

# =================== #
# Help Menu Functions #
# =================== #

def help():                                     # Display's a list of commands the user can use.
    print("\n[-----------------]\n  System Commands\n[-----------------]\n\t\t\t\t\t|")
    print("\thelp\t\t\t\t| Displays general help menu.\n\t\t\t\t\t|")
    print("\thelp move\t\t\t\t| Displays movement help menu.\n\t\t\t\t\t|")
    print("\tshorthand\t\t\t| Displays shorthand help menu.\n\t\t\t\t\t|")
    print("\tsave\t\t\t\t| Saves the game from the last checkpoint.\n\t\t\t\t\t|")
    #print("\tload\t\t\t\t\t| Loads the game from the last checkpoint.\n\t\t\t\t\t\t|")
    print("\tquit\t\t\t\t| Quits the game.\n\t\t\t\t\t|")
    print("\nPress enter to continue...")
    input()
    
    print("[-----------------]\n  Player Commands\n[-----------------]\n\t\t\t\t\t|")
    print("\tinv\t\t\t\t| Displays user's inventory.\n\t\t\t\t\t|")
    print("\t<veb> <noun>\t\t\t| Performs a player action.\n\t\t\t\t\t|")
    print("\nPress enter to continue...")
    input()

def move_player():
    print("\n[------------------------]\n  Moving Within the Game\n[------------------------]\n\n\t\t\t|")
    print("\twalk\t\t| north, south, east, west\n\t\t\t|")
    print("\trun\t\t| north, south, east, west\n\t\t\t|")
    print("\tswim\t\t| north, south, east, west, up, down\n\t\t\t|")
    print("\tjump\t\t| over, on\n\t\t\t|")
    print("\tclimb\t\t| up, down, left, right\n\t\t\t|")        # You should not be able to climb north, south, east or west. Add this functionality into the parser.
    
def short_hand_commands():
    print("\n[-------------------------]\n  Short Hand Command List\n[-------------------------]\n")
    print("\t  |\n\tN | Move player north\n\t  |")
    print("\tS | Move player south\n\t  |")
    print("\tE | Move player east\n\t  |")
    print("\tW | Move player west\n\t  |")
    print("\tU | Move player up\n\t  |")
    print("\tD | Move player down\n\t  |\n")
    print("\t  |\n\th | Displays help menu\n\t  |")
    print("\ti | Displays player inventory\n\t  |")
    print("\ty | Yes. Confirmation Response\n\t  |")
    print("\tn | No. Rejection response\n\t  |")
    
# =============================== #
# Game Chapter Specific Functions #
# =============================== #
    
def prologue(player_name):
    delay_print("\nYour feet drag along the ground, burdened by the weight of the chains that bound you.\n")
    delay_print("The paladin in front of you, Yuri, escorts you to the ceremony.\n")
    delay_print("Night has begun to fall. The air is cool.\n")
    delay_print("You begin to approach a ceremonial crater in the midst of the looming mountain range.\n")
    delay_print("Jagged formations of black-stone pierce into the sky.\n")
    delay_print("A light fog engulfs the floor of the scorched earthen crater.\n")
    delay_print("The presence of the soul eater grows stronger as you approach the ceremonial steps.\n")
    delay_print("You can begin to hear the solemn verses of the ceremony.\n")
    delay_print("It is a beautiful, yet haunting song.\n")
    delay_print("You see the sullen faces of friends and family chanting the burial song around the belt of the enidra.\n")
    delay_print("Upon your approach, you are guided to the black-stone plate overlooking the enidra.\n")
    delay_print("You stare into the abyss as the fog falls into the darkness.\n")
    delay_print("Yuri brings you to the plate. You kneel upon the edge of the void.\n")
    delay_print("Upon his passing, you feel something drop into your pocket.\n")
    delay_print("The priest, a grey robed man, begins the ritual.\n")
    delay_print("He raises his hands into the sky, as dark clouds begin to form.\n")
    delay_print("The gaze of the Enidra pierces into your soul.\n")
    delay_print("As you look up, you can see the somber faces of the choir.\n")
    delay_print(f'"{player_name}, your crimes are now forgiven."\n')
    delay_print("The priest thrusts his hands downwards.\n")
    delay_print("The ground shakes as howls of lost souls wail from the abyss below.\n")
    delay_print(f'"May the Enidra have mercy on our souls."\n')
    delay_print("You feel the hand of your friend, Yuri, rest his hand on your shoulder.\n")
    delay_print("At the next moment, you watch as you are pushed into the abyss below.\n")