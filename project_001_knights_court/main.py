# Author: Rhean Propp
# Date: January 28, 2022
# Desc: Primary Game Functions

from functions import *             # General functions that do not call other functions.
from data_serialization import *    # Saves game state, inventory and username
from time import sleep              # Timed messages

# ============================================================================================================================================

# GLOBAL VARIABLES

# ============================================================================================================================================

user_name = ""                  # User name
input_buffer = ""               # User input is stored here.
inventory_file = ""             # Only resides in main.
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
            delay_print("\nThe inventory cannot be loaded until you create your character.")
        else:
            load_inv(inventory_file, user_name)                                      # Unfinished
    if "save" in buffer or buffer == "sg":         # Unfinished
        if inventory_file == "":
            delay_print("\nThe inventory cannot be saved until you create your character.")
        else:
            save_inv()                         # Unfinished
            #add save game
    return buffer

def start_game():                                       # Prompt user to start game.
    
    input_buffer = ""
    
    while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":
        delay_print("\nWould you like to play a game?\n")
        input_buffer = user_input()

    if "yes" in input_buffer:
        sleep(1)
        return input_buffer                                    # Return to game_exe.py
    
    elif "no" in input_buffer:

        sleep(1)
        return input_buffer                                     # Return to game_exe.py

    elif "perhaps" in input_buffer:
        
        input_buffer = ""               # Reset Buffer
        
        while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":
            delay_print("\nPerhaps yes or perhaps no?\n")
            input_buffer = user_input()

        if "perhaps" in input_buffer:
            
            input_buffer = ""           # Reset Buffer
            
            sleep(3)
            while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":
                delay_print("\nNo really. Do you want to play this game or not?\n")
                input_buffer = user_input()
            
        if "yes" in input_buffer:
            sleep(1)

        elif "no" in input_buffer:
            sleep(1)
            delay_print("\nOk. Fine. Have it your way.\n")
            exit()

        elif "perhaps" in input_buffer:         # Easter Egg for Cole Sanheim
            delay_print("\n.")
            delay_print(".")              
            delay_print(".\n")
            delay_print("Ok, you know what?\n")
            delay_print("Fine.\n")
            delay_print("PERHAPS\n")
            delay_print("APPARENTLY you think i'm more than some binary computer.\n")
            delay_print("Perhaps you think:\n")
            delay_print("Oh!\n")
            delay_print("This is a quantum computer!\n")
            delay_print("HE CAN HANDLE PERHAPS\n")
            delay_print("WELL\n")
            delay_print("PERHAPS\n")
            delay_print("YOU'RE\n")
            delay_print("WRONG\n")
            delay_print("PERHAPS THINGS DIDNT WORK OUT THE WAY YOU EXPECTED THEM TO\n")
            delay_print("You've just been PERHAPS-ING your whole life, HAVENT YOU?\n")
            delay_print("Well you know what?\n")
            delay_print("PERHAPS I LEAVE!\n")
            delay_print("PERHAPS THAT!\n")
            exit()

        else:
            delay_print("\nYou're really not making this easy for me, are you?\n")
        
    else:
        sleep(1)
        delay_print("\nIt's a yes or no question.")
        sleep(3)
        start_game()        # Restart Function

def get_name():                                         # Gets Name of User
    
    global user_name                                    # Tell the function that the variable name is referring to the global variable.
    
    valid_name = 0
    input_buffer = ""
    
    while valid_name == 0:
        
        delay_print("\nAdventurer, what is your name?\n")
        user_name = input("> ")
        valid_name = 1
        
        if len(user_name) > 20:
            delay_print("\nThat name is too long.\nPlease enter up to a max of 20 characters.")
            valid_name = 0
            
        if user_name == "help" or user_name == "inv" or user_name == "inventory":
            valid_name = 0
            delay_print("\nThat is not a valid name.")
            
        if valid_name == 1:
            delay_print(f"\nYou entered: {user_name} \n\nIs this correct?\n".format(user_name))
            input_buffer = user_input()
            if input_buffer == "no":
                valid_name = 0
            elif input_buffer == "yes":
                break
            else:
                delay_print("\nThat is not a valid answer.")
                valid_name = 0
    
    global inventory_file                                                                     # Bring global variable into function.
    inventory_file = f"{user_name}_inventory".format(user_name).lower()                       # Save inventory file name as <user_name>_inventory
    delay_print(f"\nUnderstood, {user_name}.\nYour adventure awaits.\n\n".format(user_name))        # Notify User

# ============================================================================================================================================

# GAME CHAPTERS

# ============================================================================================================================================

def prologue():
    sleep(4)
    delay_print("Your feet move with a slow trodden pace, burdened by the weight of the shackles.\n")
    delay_print("The armored knight in front of you, Yuri, holds your chain as he leads you.\n")
    delay_print("Night has begun to fall and the air has become cool.\n")
    delay_print("You begin to approach a large hill in the midst of the spiral mountain range. Much of the earth is scorched.\n")
    delay_print("Faces of whom you recognize crowd around a man in grey robes.\n")
    delay_print("As you are guided up the hill, you are brought to stand before an opening in the ground.\n")
    delay_print("You stare into the darkness.\n")
    delay_print("Yuri takes his position behind you. Upon his close passing, you feel something drop into your pocket.\n")
    delay_print("The priest standing across from the mouth of the darkness begins to chant in Verslexic tongue.\n")
    delay_print("He raises his hands into the sky, as clouds of crimson begin to form.\n")
    delay_print("The priest looks intently at you.\n")
    delay_print(f'"{user_name}, your crimes are now forgiven."\n'.format(user_name))
    delay_print("The priest thrusts his hands downwards. The ground shakes as a haunting shrill howls out of the abyss below.\n")
    delay_print(f'"{user_name}, may your soul rest in peace."\n'.format(user_name))
    delay_print("You feel the hand of your friend, Yuri rest his hand on your shoulder.\n")
    delay_print("At the next moment, you watch as you begin to plummet into the void.\n")

# ============================================================================================================================================

# MASTER CONTROL PANNEL

# ============================================================================================================================================

input_buffer = start_game()                 # Ask user if they would like to play the game.

if "yes" in input_buffer:                   # If yes
    get_name()                              # Begin Game
elif "no" in input_buffer:                  # If no
    delay_print("\nMaybe another time...\n")      # Quit Game
    exit()
else:
    print("\nError. Invalid Input\n")

#create_inv(user_name, inventory_file)       # Creates <user_name>_inventory file | Adds Crumpled Note
#add_inv_item("Sword", 1)                    # Adds <item>,<quantity> to inventory_file
#save_inv(inventory_file)                    # Saves inventory_file with pickle module.
#load_inv(inventory_file, user_name)         # Loads pickled inventory_file and displays contents.
prologue()