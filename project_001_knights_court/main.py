# Author: Rhean Propp
# Date: January 28, 2022
# Desc: Primary Game Functions

from functions import *             # General functions that do not call other functions.
from data_serialization import *    # Saves game state, inventory and username
from time import sleep              # Timed messages

# ============================================================================================================================================

# GLOBAL VARIABLES

# ============================================================================================================================================

name = ""                       # User name
input_buffer = ""               # User input is stored here.
inventory_file_name = 0         # Notes if the inventory_file has been properly named or not.

# ============================================================================================================================================

# PRIMARY FUNCTIONS

# ============================================================================================================================================

def user_input():                                       # Primary Parser. Must be in main.
    buffer = input("> ").lower()                        # Get input | Sanitize | Store
    if "help" in buffer or buffer == "h":                          
        help()          
    if "inv" in buffer or buffer == "i" or buffer == "inventory":
        if inventory_file == "":
            print("\nThe inventory cannot be loaded until you create your character.")
        else:
            load_inv(inventory_file, name)                                      # Unfinished
    if "save" in buffer or buffer == "sg":         # Unfinished
        if inventory_file == "":
            print("\nThe inventory cannot be saved until you create your character.")
        else:
            save_inv()                         # Unfinished
    return buffer

def start_game():                                       # Prompt user to start game.
    
    input_buffer = ""
    
    while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":
        print("\nWould you like to play a game?\n")
        input_buffer = user_input()

    if "yes" in input_buffer:
        sleep(1)
        print("\nStarting game...")
        sleep(2)
        return input_buffer                                    # Return to game_exe.py
    
    elif "no" in input_buffer:

        sleep(1)
        return input_buffer                                     # Return to game_exe.py

    elif "perhaps" in input_buffer:
        
        input_buffer = ""               # Reset Buffer
        
        while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":
            print("\nPerhaps yes or perhaps no?\n")
            input_buffer = user_input()

        if "perhaps" in input_buffer:
            
            input_buffer = ""           # Reset Buffer
            
            sleep(3)
            while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":
                print("\nNo really. Do you want to play this game or not?\n")
                input_buffer = user_input()
            
        if "yes" in input_buffer:
            sleep(1)
            print("\nStarting game...")
            sleep(2)

        elif "no" in input_buffer:
            sleep(1)
            print("\nOk. Fine. Have it your way.\n")
            exit()

        elif "perhaps" in input_buffer:         # Easter Egg for Cole Sanheim
            sleep(3)
            print("\n.", end="", flush=True)
            sleep(0.15)
            print(".", end="", flush=True)              
            sleep(0.15)
            print(".\n")
            sleep(4)
            print("Ok, you know what?\n")
            sleep(2.5)
            print("Fine.\n")
            sleep(1.8)
            print("PERHAPS\n")
            sleep(3.8)
            print("APPARENTLY you think i'm more than some binary computer.\n")
            sleep(4)
            print("Perhaps you think:\n")
            sleep(0.8)
            print("Oh!\n")
            sleep(1.6)
            print("This is a quantum computer!\n")
            sleep(1.7)
            print("HE CAN HANDLE PERHAPS\n")
            sleep(4)
            print("WELL\n")
            sleep(0.5)
            print("PERHAPS\n")
            sleep(0.5)
            print("YOU'RE\n")
            sleep(0.5)
            print("WRONG\n")
            sleep(3.4)
            print("PERHAPS THINGS DIDNT WORK OUT THE WAY YOU EXPECTED THEM TO\n")
            sleep(3.5)
            print("You've just been PERHAPS-ING your whole life, HAVENT YOU?\n")
            sleep(3)
            print("Well you know what?\n")
            sleep(2)
            print("PERHAPS I LEAVE!\n")
            sleep(1.5)
            print("PERHAPS THAT!\n")
            exit()

        else:
            print("\nYou're really not making this easy for me, are you?\n")
        
    else:
        sleep(1)
        print("\nIt's a yes or no question.")
        sleep(3)
        start_game()        # Restart Function

def get_name():                                         # Gets Name of User
    
    global name                                         # Tell the function that the variable name is referring to the global variable.
    
    valid_name = 0
    input_buffer = ""
    
    while valid_name == 0:
        
        print("\nAdventurer, what is your name?\n")
        name = input("> ")
        valid_name = 1
        
        if len(name) > 20:
            print("\nThat name is too long.\nPlease enter up to a max of 20 characters.")
            valid_name = 0
            
        if name == "help" or name == "inv" or name == "inventory":
            valid_name = 0
            print("\nThat is not a valid name.")
            
        if valid_name == 1:
            print("\nYou entered: {user_name} \n\nIs this correct?\n".format(user_name = name))
            input_buffer = user_input()
            if input_buffer == "no":
                valid_name = 0
            elif input_buffer == "yes":
                break
            else:
                print("\nThat is not a valid answer.")
                valid_name = 0
    
    global inventory_file                                                                           # Bring global variable into function.
    inventory_file = "{user_name}_inventory".format(user_name = name).lower()                       # Save inventory file name.
    print("\nUnderstood, {user_name}.\nYour adventure awaits...\n".format(user_name = name))        # Notify User

# ============================================================================================================================================

# MASTER CONTROL PANNEL

# ============================================================================================================================================

input_buffer = start_game()                 # Ask user if they would like to play the game.

if "yes" in input_buffer:                   # If yes
    get_name()                              # Begin Game
elif "no" in input_buffer:                  # If no
    print("\nMaybe another time...\n")      # Quit Game
    exit()
else:
    print("\nError. Invalid Input\n")

create_inv(inventory_file)
#load_inv(inventory_file, name)

# ============================================================================================================================================

# GAME CHAPTERS

# ============================================================================================================================================

def chapter_01():
     print("Chapter 01 - Shallows Isle")
     sleep(4)
     print("\nYou awake. The air is cold and damp. Upon their opening, your eyes are met with darkness...")
     sleep(3)
     print("\nWhat do you do?")