# Author: Rhean Propp
# Date: January 28, 2022
# Desc: Primary Game Functions

from functions import *             # General functions that do not call other functions.
from data_serialization import *    # Saves game state, inventory and username
from time import sleep              # Timed messages

# ============================================================================================================================================

# GLOBAL VARIABLES

# ============================================================================================================================================

user_name = ""                  # Name of the character the user is playing.
input_buffer = ""               # User input is stored here.
inventory_file = ""             # Stores <user_name>_inventory. Used for file creation.

# General user_input() responses:
input_positive = ["yes", "ye", "y", "yup", "ya", "yeah", "yep", "perhaps yes", "yus", "sure", "bet", "fo sho", "fo shizzle", "yesh", "yas", "okay", "ok", "yessir"]
input_negative = ["no", "n", "nope", "nah", "no way", "perhaps no", "naw", "hell nah", "nein", "hell no", "nay", "hell no", "nah brah", "nae"]
input_undecided = ["perhaps", "maybe", "perchance", "conceivably", "possibly", "mayhaps", "mebbeh", "persnaps"]
input_inventory = ["inventory", "inv", "i"]
input_examine = ["examine", "look at", "view", "probe"]
input_help = ["help", "h", "halp", "give me a hand here"]
input_save = ["save game", "save", "s"]
input_load = ["load game", "load", "l"]

# ============================================================================================================================================

# PRIMARY FUNCTIONS

# ============================================================================================================================================

def clear_buffer():         # Clears the input_buffer global variable.
    global input_buffer     # Tells the function to use the global variable.
    input_buffer = ""       # Sets the variable to an empty string.

def user_input():                                       # Primary Parser. Must be in main.
    buffer = input("> ").lower()                        # Get input | Sanitize | Store
    if buffer in input_help:                          
        buffer == "help"
        help()          
    elif buffer in input_inventory:
        if inventory_file == "":
            delay_print("\nThe inventory cannot be loaded until you create your character.")
        else:
            buffer == "inventory"                                                    # Why is this here and what is it doing?
            load_inv(inventory_file, user_name)                                      # Unfinished
    elif buffer in input_save:         # Unfinished
        if inventory_file == "":
            delay_print("\nThe inventory cannot be saved until you create your character.")
        else:
            buffer == "save"                   # Why is this here and what is it doing?
            save_inv()                         # Unfinished
            #add save game
    elif buffer in input_positive:         # Allows short-handing Consider Adding. Does it Simplify the code?
        buffer = "yes"          # Shorthand
    elif buffer in input_negative:          # Allows short-handing
        buffer = "no"           # Shorthand 
    elif buffer in input_undecided:
        buffer == "perhaps"     # Shorthand
    else:
        delay_print('\nThis is not a valid input. Type "help" or "h" if you are stuck.\n')
    return buffer

def start_game():                                       # Prompt user to start game.
    global input_buffer     # Allow the function access to the global variable.
    clear_buffer()          # Reset the buffer before beginning the program.
    while input_buffer not in input_positive and input_buffer not in input_negative and input_buffer not in input_undecided:     # Loop until yes, no or perhaps is said.
        delay_print("\nWould you like to play a game?\n")                                   # Prompt user
        input_buffer = user_input()                                                         # Get input
    if input_buffer in input_positive:                                                               # If yes
        sleep(1)                                                                            # Sleep
        return input_buffer                                                                 # Return to master control panel
    elif input_buffer in input_negative:                                                              # If no
        sleep(1)                                                                            # Sleep
        return input_buffer                                                                 # Return to master control panel
    elif input_buffer in input_undecided:                                                         # If perhaps
        input_buffer = ""                                                                   # Reset Buffer
        while input_buffer not in input_positive and input_buffer not in input_negative and input_buffer not in input_undecided:         # Loop until yes, no or perhaps is said
            delay_print("\nPerhaps yes or perhaps no?\n")                                           # Prompt user
            input_buffer = user_input()                                                             # Get input
        if input_buffer in input_undecided:                                                               # If perhaps
            input_buffer = ""                                                                       # Reset Buffer                               
            sleep(3)                                                                                # Sleep
            while input_buffer not in input_positive and input_buffer not in input_negative and input_buffer not in input_undecided:     # Loop until yes, not or perhaps is said
                delay_print("\nNo really. Do you want to play this game or not?\n")                 # Prompt user
                input_buffer = user_input()                                                         # Get input
        if input_buffer in input_positive:                                                          # If yes
            sleep(1)                                                                                # Sleep
            return input_buffer                                                                     # Return to master control panel
        elif input_buffer in input_negative:                                                        # If no
            sleep(1)                                                                                # Sleep
            delay_print("\nOk. Fine. Have it your way.\n")                                          # 
            exit()                                                                                  # Exit game
        elif input_buffer in input_undecided:                                                       # Easter Egg for Cole Sanheim
            delay_print("\n.")                                                                      
            delay_print(".")                                                                        
            delay_print(".\n")                                                                      
            delay_print("Ok, you know what?\n")                                                     
            delay_print("Fine.\n")                                                                  
            delay_print("PERHAPS.\n")                                                                 
            delay_print("APPARENTLY you think i'm more than some binary computer.\n")               
            delay_print("Perhaps you think:\n")                                                     
            delay_print("Oh!\n")                                                                    
            delay_print("This is a quantum computer!\n")                                            
            delay_print("HE CAN HANDLE PERHAPS.\n")                                                  
            delay_print("WELL\n")                                                                   
            delay_print("PERHAPS\n")                                                                
            delay_print("YOU'RE\n")                                                                 
            delay_print("WRONG\n")                                                                  
            delay_print("PERHAPS THINGS DIDNT WORK OUT THE WAY YOU EXPECTED THEM TO.\n")             
            delay_print("You've just been PERHAPS-ING your whole life, HAVENT YOU?\n")              
            delay_print("Well you know what?\n")                                                    
            delay_print("PERHAPS I LEAVE!\n")                                                       
            delay_print("PERHAPS THAT!\n")                                                          
            exit()                                                                                  # Exit game
        else:                                                                                       # Catch-all statement for previous if/else logic
            delay_print("\nYou're really not making this easy for me, are you?\n")                  
    else:                                                                                           # If user inputs an invalid response
        sleep(1)                                                                                    # Sleep
        delay_print("\nIt's a yes or no question.")                                                 # Inform
        sleep(3)                                                                                    # Sleep
        start_game()                                                                                # Restart Function

def get_name():                                         # Gets Name of User
    global user_name                                    # Tell the function that the variable name is referring to the global variable.
    global input_buffer
    valid_name = 0
    clear_buffer()
    while valid_name == 0:
        delay_print("\nAdventurer, what is your name?\n")
        user_name = input("> ")
        valid_name = 1
        if len(user_name) > 20:
            delay_print("\nThat name is too long.\nPlease enter up to a max of 20 characters.")
            valid_name = 0
        if user_name in input_inventory or user_name in input_help or user_name in input_examine or user_name in input_save or user_name in input_load:       # Ensures username is not a command name.
            valid_name = 0
            delay_print("\nThat is not a valid name.")
        if valid_name == 1:
            delay_print(f"\nYou entered: {user_name} \n\nIs this correct?\n".format(user_name))
            input_buffer = user_input()
            if input_buffer in input_negative:
                valid_name = 0
            elif input_buffer in input_positive:
                break
            else:
                delay_print("\nThat is not a valid answer.")
                valid_name = 0
    global inventory_file                                                                       # Bring global variable into function.
    inventory_file = f"{user_name}_inventory".format(user_name).lower()                         # Save inventory file name as <user_name>_inventory
    delay_print(f"\nUnderstood, {user_name}.\nYour adventure awaits.\n\n".format(user_name))    # Notify User
    
def tutorial():
    delay_print("\nWelcome to <insert_game_name_here>. This is a text adventure.\n")            # Add game name.
    delay_print("The idea of the game is to progress through the story by solving puzzle rooms.\n")
    delay_print("There is no 2D or 3D display. Everything in this game is described to you, while you play the game in your head.\n")
    delay_print("You may find it helpful to have a piece of pen and paper handy when solving certain puzzles.\n")
    delay_print('If you are ever stuck, you can type "help" or "h" to get a list of commands you can use to interact with the world.\n')
    delay_print("Give it a try now.\n")
    input_buffer = user_input()
    while input_buffer not in input_help:
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

# Get Character Name | Create Save Files
input_buffer = start_game()                     # Ask user if they would like to play the game.

if input_buffer in input_positive:              # If yes
    get_name()                                  # Begin Game
    create_inv(inventory_file)
elif input_buffer in input_negative:            # If no
    delay_print("\nMaybe another time.\n")      # Quit Game
    exit()
else:
    print("\nError. Invalid Input\n")

# Prompt Tutorial
clear_buffer()
while input_buffer not in input_negative and input_buffer not in input_positive:
    delay_print("Would you like to learn how to play the game?\n")
    input_buffer = user_input()
    if input_buffer in input_positive:
        tutorial()
    elif input_buffer in input_undecided:
        delay_print("\nIf you are unsure, it is a wise idea to run through the tutorial. Don't worry, it's quick.\n")
    else: 
        pass

# Prompt Prologue
clear_buffer()
while input_buffer not in input_negative and input_buffer not in input_positive:
    delay_print("\nWould you like to skip the prologue?\n")
    input_buffer = user_input()
    if input_buffer in input_negative:
        prologue()
    elif input_buffer in input_undecided:
        delay_print("\nThe prologue is about a 5 minute read. If you like to play games for the story, it is recommended.\n")
    else: 
        continue

#create_inv(user_name, inventory_file)       # Creates <user_name>_inventory file | Adds Crumpled Note
#add_inv_item("Sword", 1)                    # Adds <item>,<quantity> to inventory_file
#save_inv(inventory_file)                    # Saves inventory_file with pickle module.
#load_inv(inventory_file, user_name)         # Loads pickled inventory_file and displays contents.