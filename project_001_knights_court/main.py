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
#inventory_file_name = 0         # Notes if the inventory_file has been properly named or not. # Might be unused.

# ============================================================================================================================================

# PRIMARY FUNCTIONS

# ============================================================================================================================================

def user_input():                                       # Primary Parser. Must be in main.
    buffer = input("> ").lower()                        # Get input | Sanitize | Store
    if buffer == "help" or buffer == "h":                          
        buffer == "help"
        help()          
    if buffer == "inventory" or buffer == "inv" or buffer == "i":
        if inventory_file == "":
            delay_print("\nThe inventory cannot be loaded until you create your character.")
        else:
            buffer == "inventory"
            load_inv(inventory_file, user_name)                                      # Unfinished
    if buffer == "save" or buffer == "sg":         # Unfinished
        if inventory_file == "":
            delay_print("\nThe inventory cannot be saved until you create your character.")
        else:
            buffer == "save"
            save_inv()                         # Unfinished
            #add save game
    if buffer == "yes" or buffer == "ye" or buffer == "y" or buffer == "perhaps yes" or buffer == "yeah" or buffer == "yus" or buffer == "yup" or buffer == "fo sho" or buffer == "sure" or buffer == "bet" or buffer == "fo shizzle":         # Allows short-handing Consider Adding. Does it Simplify the code?
        buffer = "yes"          # Shorthand
    if buffer == "no" or buffer == "nah" or buffer == "n" or buffer == "perhaps no" or buffer == "naw":          # Allows short-handing
        buffer = "no"           # Shorthand 
    if buffer == "perhaps" or buffer == "p" or buffer == "maybe" or buffer == "m" or buffer == "i don't know" or buffer == "i dont know" or buffer == "idk":
        buffer == "perhaps"     # Shorthand
    return buffer

def start_game():                                       # Prompt user to start game.
    input_buffer = ""
    while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":     # Loop until yes, no or perhaps is said.
        delay_print("\nWould you like to play a game?\n")                                   # Prompt user
        input_buffer = user_input()                                                         # Get input
    if "yes" in input_buffer:                                                               # If yes
        sleep(1)                                                                            # Sleep
        return input_buffer                                                                 # Return to master control panel
    elif "no" in input_buffer:                                                              # If no
        sleep(1)                                                                            # Sleep
        return input_buffer                                                                 # Return to master control panel
    elif "perhaps" in input_buffer:                                                         # If perhaps
        input_buffer = ""                                                                   # Reset Buffer
        while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":         # Loop until yes, no or perhaps is said
            delay_print("\nPerhaps yes or perhaps no?\n")                                           # Prompt user
            input_buffer = user_input()                                                             # Get input
        if "perhaps" in input_buffer:                                                               # If perhaps
            input_buffer = ""                                                                       # Reset Buffer                               
            sleep(3)                                                                                # Sleep
            while input_buffer != "yes" and input_buffer != "no" and input_buffer != "perhaps":     # Loop until yes, not or perhaps is said
                delay_print("\nNo really. Do you want to play this game or not?\n")                 # Prompt user
                input_buffer = user_input()                                                         # Get input
        if "yes" in input_buffer or input_buffer == "perhaps yes":                                  # If yes
            sleep(1)                                                                                # Sleep
            return input_buffer                                                                     # Return to master control panel
        elif "no" in input_buffer or input_buffer == "perhaps no":                                  # If no
            sleep(1)                                                                                # Sleep
            delay_print("\nOk. Fine. Have it your way.\n")                                          # 
            exit()                                                                                  # Exit game
        elif "perhaps" in input_buffer:                                                             # Easter Egg for Cole Sanheim
            delay_print("\n.")                                                                      # 
            delay_print(".")                                                                        #
            delay_print(".\n")                                                                      #
            delay_print("Ok, you know what?\n")                                                     #
            delay_print("Fine.\n")                                                                  #
            delay_print("PERHAPS\n")                                                                #   
            delay_print("APPARENTLY you think i'm more than some binary computer.\n")               #
            delay_print("Perhaps you think:\n")                                                     #
            delay_print("Oh!\n")                                                                    #
            delay_print("This is a quantum computer!\n")                                            #
            delay_print("HE CAN HANDLE PERHAPS\n")                                                  #
            delay_print("WELL\n")                                                                   #
            delay_print("PERHAPS\n")                                                                #
            delay_print("YOU'RE\n")                                                                 #
            delay_print("WRONG\n")                                                                  #
            delay_print("PERHAPS THINGS DIDNT WORK OUT THE WAY YOU EXPECTED THEM TO\n")             #
            delay_print("You've just been PERHAPS-ING your whole life, HAVENT YOU?\n")              #
            delay_print("Well you know what?\n")                                                    #
            delay_print("PERHAPS I LEAVE!\n")                                                       #
            delay_print("PERHAPS THAT!\n")                                                          #
            exit()                                                                                  # Exit game
        else:                                                                                       # Catch-all statement for previous if/else logic
            delay_print("\nYou're really not making this easy for me, are you?\n")                  #
    else:                                                                                           # If user inputs an invalid response
        sleep(1)                                                                                    # Sleep
        delay_print("\nIt's a yes or no question.")                                                 # Inform
        sleep(3)                                                                                    # Sleep
        start_game()                                                                                # Restart Function

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
    global inventory_file                                                                       # Bring global variable into function.
    inventory_file = f"{user_name}_inventory".format(user_name).lower()                         # Save inventory file name as <user_name>_inventory
    delay_print(f"\nUnderstood, {user_name}.\nYour adventure awaits.\n\n".format(user_name))    # Notify User
    
def tutorial():
    global input_buffer
    delay_print("Would you like to learn how to play the game?\n")
    input_buffer = user_input()
    if input_buffer == "no":
        print("")
        return
    if input_buffer == "perhaps":
        delay_print("\nWell in that case, i'll choose for you.\n")
    delay_print("\nWelcome to <insert_game_name_here>. This is a text adventure.\n")            # Add game name.
    delay_print("The idea of the game is to progress through the story by solving puzzle rooms.\n")
    delay_print("There is no 2D or 3D display. Everything in this game is described to you, while you play the game in your head.\n")
    delay_print("You may find it helpful to have a piece of pen and paper handy when solving certain puzzles.\n")
    delay_print('If you are ever stuck, you can type "help" or "h" to get a list of commands you can use to interact with the world.\n')
    delay_print("Give it a try now.\n")
    input_buffer = user_input()
    while input_buffer != "help" and input_buffer != "h":
        delay_print('You inputted the incorrect command. Try typing "help" or "h" for short.\n')
        input_buffer = user_input()
    sleep(5)
    delay_print('Great job. Anytime you see a ">" symbol, you can type "help" or "h" to bring up the help menu again.\n')
    delay_print("This is all you need to begin your adventure.\n")
    delay_print("We hope you enjoy your journey, traveler.\n\n")
    
# ============================================================================================================================================

# GAME CHAPTERS

# ============================================================================================================================================

def prologue():
    global input_buffer
    delay_print("Would you like to skip the prologue?\n")
    input_buffer = user_input()
    if input_buffer == "yes":
        return
    if input_buffer == "perhaps":
        delay_print("\nGod damnit. Can't you just give me a yes or no answer?\n")
        prologue()
    if input_buffer == "no":
        sleep(2)
    delay_print("\nYour feet drag along the ground, burdened by the weight of the chains that bound you.\n")
    delay_print("The paladin in front of you, Yuri, escorts you to the ceremony.\n")
    delay_print("Night has begun to fall. The air is cool.\n")
    delay_print("You begin to approach a ceremonial crater in the midst of the Endera mountain range.\n")
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
    delay_print(f'"{user_name}, your crimes are now forgiven."\n'.format(user_name))
    delay_print("The priest thrusts his hands downwards.\n")
    delay_print("The ground shakes as howls of lost souls wail from the abyss below.\n")
    delay_print(f'"May the Enidra have mercy on our souls."\n'.format(user_name))
    delay_print("You feel the hand of your friend, Yuri, rest his hand on your shoulder.\n")
    delay_print("At the next moment, you watch you are pushed into the abyss below.\n")

# ============================================================================================================================================

# MASTER CONTROL PANNEL

# ============================================================================================================================================


input_buffer = start_game()                 # Ask user if they would like to play the game.
if "yes" in input_buffer:                   # If yes
    get_name()                              # Begin Game
    create_inv(user_name, inventory_file)
    tutorial()
    prologue()
elif "no" in input_buffer:                  # If no
    delay_print("\nMaybe another time...\n")      # Quit Game
    exit()
else:
    print("\nError. Invalid Input\n")
    


#create_inv(user_name, inventory_file)       # Creates <user_name>_inventory file | Adds Crumpled Note
#add_inv_item("Sword", 1)                    # Adds <item>,<quantity> to inventory_file
#save_inv(inventory_file)                    # Saves inventory_file with pickle module.
#load_inv(inventory_file, user_name)         # Loads pickled inventory_file and displays contents.