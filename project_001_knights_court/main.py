# ============================ #
# Author: Rhean Propp          #
# Date: January 28, 2022       #
# Desc: Primary Game Functions #
# ============================ #

from functions import *             # General functions that do not call other functions.
from data_serialization import *    # Saves game state, inventory and username
from time import sleep              # Timed messages
import threading                    # Used for Oxygen Clock in Chapter_01       # Is this actually used?
from threading import Thread

# ============================================================================================================================================


# GLOBAL VARIABLES


# ============================================================================================================================================

# General Purpose Variables
user_name = ""                  # Name of the character the user is playing.
input_buffer = ""               # User input is stored here.
inventory_file = ""             # Stores <user_name>_inventory. Used for file creation.

# General Responses | user_input()
input_positive = ["yes", "ye", "yup", "ya", "yeah", "yep", "perhaps yes", "yus", "sure", "bet", "fo sho", "fo shizzle", "yesh", "yas", "okay", "ok", "yessir"]
input_negative = ["no", "nope", "nah", "no way", "perhaps no", "naw", "hell nah", "nein", "hell no", "nay", "hell no", "nah brah", "nae"]
input_undecided = ["perhaps", "maybe", "perchance", "conceivably", "possibly", "mayhaps", "mebbeh", "persnaps"]

# Directional movements | user_input()
input_forward = ["forward", "north", "n"]
input_backward = ["backward", "back", "south", "s"]
input_right = ["right", "east", "e"]
input_left = ["left", "west", "w"]
input_up = ["up", "upward", "upwards", "u"]
input_down = ["down", "downward", "downwards", "d"]
input_direction = [input_forward, input_backward, input_right, input_left, input_up, input_down]

# Movement Types | user_input()
input_swim = ["swim"]
input_climb = ["climb"]
input_walk = ["walk", "step"]
input_run = ["run", "dash", "sprint"]
input_jump = ["jump", "hop", "leap", "vault"]
input_move = ["swim", "climb", "walk", "step", "run", "dash", "sprint", "jump", "hop", "leap", "vault"]
# If we make input_move a list of lists, does it break everything?

# Universal commands | user_input()
input_inventory = ["inventory", "inv", "i"]
input_shorthand = ["shorthand", "short"]
input_help_guide = ["help", "halp", "h"]        # Need to update this changed list with the function
input_move_guide = ["move"]                     # Need to update this changed list with the function | Do not call it input_move
input_save = ["save game", "save"]
input_load = ["load game", "load"]

# Player commands for interaction | user_input()
input_examine = ["examine", "look at", "look", "view", "probe"]

# ============================================================================================================================================


# PRIMARY FUNCTIONS


# ============================================================================================================================================

def clear_buffer():         # Clears the input_buffer global variable.
    global input_buffer     # Tells the function to use the global variable.
    input_buffer = ""       # Sets the variable to an empty string.

def user_input():           # Primary Parser. Returns sanitized input.
    
    # Get User Input | Lowercase | Store
    buffer = input("> ").lower()               
    
    # ======================================================== #
    # Directional Movement Commands
    # ======================================================== #
    
    movement_command = False    # Flag
    
    # Check if buffer is a movement command:
    for movement_type in input_move:                                #
        if movement_type in buffer and movement_command == False:   # 
            movement_command = True                                 # Set flag to true.
    
    # If the buffer is a movement Command, sanitize command:
    if movement_command == True:
        for movement_type in input_move:
            for list in input_direction:
                for direction in list:
                    if buffer == f"{movement_type} {direction}":
                        buffer = movement_check(movement_type, direction)
    
    # ======================================================== #
    # Help Menu Commands
    # ======================================================== #
    
    # Help Commands
    elif buffer in input_help_guide:                             
        buffer = "help"
        help()                  # See functions.py
    
    # Move Command List
    elif buffer in input_move_guide:          
        buffer = "move"
        move_player()           # See functions.py
    
    # Shorthand Command List
    elif buffer in input_shorthand:     
        buffer = "shorthand"
        short_hand_commands()   # See functions.py
        
    # ======================================================== #
    # System Commands
    # ======================================================== #                                    
    
    # Save Player's Game | data_serialization.py | Unfinished
    elif buffer in input_save:  
        if inventory_file == "":
            delay_print("\nThe inventory cannot be saved until you create your character.\n")
        else:
            buffer = "save"                    
            save_inv()                         
            #add save game
            
    # ======================================================== #
    # Polar Response Commands
    # ======================================================== #
    
    # Yes | Positive Response
    elif buffer in input_positive:      
        buffer = "yes"          
    
    # No | Negative Response
    elif buffer in input_negative:      
        buffer = "no"           
    
    # Maybe | Uncertain Response
    elif buffer in input_undecided:     
        buffer = "perhaps"  
        
    # ======================================================== #
    # Player/World Interaction Commands
    # ======================================================== #
    
    # List Player Inventory
    elif buffer in input_inventory:
        if inventory_file == "":
            delay_print("\nThe inventory cannot be loaded until you create your character.\n")
        else:
            buffer = "inventory"                                                    
            load_inv(inventory_file, user_name)
    
    # Item Use | Unfinished
    elif "use" in buffer:               
        return buffer
    
    # ======================================================== #
    # Invalid Input
    # ======================================================== #
    
    # Undefined Response
    else:
        delay_print('\nThis is not a valid input. Type "help" or "h" if you are stuck.\n')
    
    return buffer

def movement_check(movement_type, direction):   # Ensures Player Cannot Move Invalidly
    
    # Walking Check
    if movement_type in input_walk:
        if direction in input_up:
            delay_print(f"You cannot {movement_type} {direction}.\n")
        elif direction in input_down:
            delay_print(f"You cannot {movement_type} {direction}.\n")
        else:
            return f"{movement_type} {direction}"
    
    # Running Check
    elif movement_type in input_run:
        if direction in input_up:
            delay_print(f"You cannot {movement_type} {direction}.\n")
        elif direction in input_down:
            delay_print(f"You cannot {movement_type} {direction}.\n")
        else:
            return f"{movement_type} {direction}"

    # Climbing Check
    elif movement_type in input_climb:
        if direction in input_forward:
            delay_print(f"You cannot {movement_type} {direction}.\n")
        elif direction in input_backward:
            delay_print(f"You cannot {movement_type} {direction}.\n")
        else:
            return f"{movement_type} {direction}"
    
    # Valid Command        
    else:
        return f"{movement_type} {direction}"

def start_game():           # Prompt user to start game.
    
    global input_buffer     
    clear_buffer()          
    
    # Loop Until: Yes, No, Maybe
    while input_buffer not in input_positive and input_buffer not in input_negative and input_buffer not in input_undecided:
        delay_print("\nWould you like to play a game?\n")                                   
        input_buffer = user_input()                                                         
    
    # If Positive:
    if input_buffer in input_positive:                                                      
        sleep(1)                                                                            
        return input_buffer  
    
    # If Negative:
    elif input_buffer in input_negative:                                                              
        sleep(1)                                                                            
        return input_buffer                                                                 
    
    # If Undecided #1:
    elif input_buffer in input_undecided:                                                         
        
        input_buffer = ""       # Reset Buffer | Change to clear_buffer() and test.
        
        # Loop Until: Yes, No, Maybe
        while input_buffer not in input_positive and input_buffer not in input_negative and input_buffer not in input_undecided:         
            delay_print("\nPerhaps yes or perhaps no?\n")                                           
            input_buffer = user_input()                                                             
        
        # If Undecided #2:
        if input_buffer in input_undecided:                                                               
            
            input_buffer = ""   # Reset Buffer | Change to clear_buffer() and test.                                                                                        
            sleep(3)                                                                                
            
            # Loop Until: Yes, No, Maybe
            while input_buffer not in input_positive and input_buffer not in input_negative and input_buffer not in input_undecided:     
                delay_print("\nNo really. Do you want to play this game or not?\n")                 
                input_buffer = user_input()                                                         
        
        # If Positive:
        if input_buffer in input_positive:                                                          
            sleep(1)                                                                                
            return input_buffer                                                                     
        
        # If Negative:
        elif input_buffer in input_negative:                                                        
            sleep(1)                                                                                
            delay_print("\nOk. Fine. Have it your way.\n")                                           
            exit()                                                                                  
        
        # If Undecided #3:
        elif input_buffer in input_undecided:   # Easter Egg for Cole Sanheim
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
            exit()                                                                                  
        
        # If Invalid Response:
        else:                                                                                       
            delay_print("\nYou're really not making this easy for me, are you?\n")                  
    
    # If Invalid Response:
    else:                                                                                           
        sleep(1)                                                                                    
        delay_print("\nIt's a yes or no question.")                                                 
        sleep(3)                                                                                    
        start_game()                                                                                

def get_name():             # Gets Name of User
    
    # Bring Global Variables Into Function:
    global user_name                                    
    global input_buffer
    global inventory_file
    
    valid_name = 0  # Flag | Change to Boolean True/False for Clarity
    clear_buffer()
    
    # Loop Until: Name is Valid
    while valid_name == 0:
        delay_print("\nAdventurer, what is your name?\n")
        user_name = input("> ")
        valid_name = 1
        
        # If Name > 20 Characters:
        if len(user_name) > 20:
            delay_print("\nThat name is too long.\nPlease enter up to a max of 20 characters.")
            valid_name = 0
        
        # If Name is a System Command:
        if user_name in input_inventory or user_name in input_help_guide or user_name in input_examine or user_name in input_save or user_name in input_load:
            valid_name = 0
            delay_print("\nThat is not a valid name.")
            # This will need to be updated as system commands are added.
        
        # Check if User Entered Name Correctly:
        if valid_name == 1:
            delay_print(f"\nYou entered: {user_name} \n\nIs this correct?\n")
            input_buffer = user_input()
            if input_buffer in input_negative:
                valid_name = 0
            elif input_buffer in input_positive:
                break
            else:
                delay_print("\nThat is not a valid answer.")
                valid_name = 0
                
    # Create Inventory File Based on Player's Name:
    inventory_file = f"{user_name.lower()}_inventory"                        # Save inventory file name as <user_name>_inventory
    delay_print(f"\nUnderstood, {user_name}.\nYour adventure awaits.\n\n")
    
def tutorial():             # Tutorial for Player
    delay_print("\nWelcome to <insert_game_name_here>. This is a text adventure.\n")
    
    # Add the name of the game here: ^^^
    # Once the name of the game has been decided.
    
    delay_print("The idea of the game is to progress through the story by solving puzzle rooms.\n")
    delay_print("There is no 2D or 3D display. Everything in this game is described to you, while you play the game in your head.\n")
    delay_print("You may find it helpful to have a piece of pen and paper handy when solving certain puzzles.\n")
    delay_print('If you are ever stuck, you can type "help" or "h" to get a list of commands you can use to interact with the world.\n')
    delay_print("Give it a try now.\n")
    
    input_buffer = user_input()
    
    # Loop Until: User Types "help" or "h"
    while input_buffer not in input_help_guide:
        delay_print('You inputted the incorrect command. Try typing "help" or "h" for short.\n')
        input_buffer = user_input()
        
    sleep(5)
    
    delay_print('Great job. Anytime you see a ">" symbol, you can type "help" or "h" to bring up the help menu again.\n')
    delay_print("This is all you need to begin your adventure.\n")
    delay_print("We hope you enjoy your journey, traveler.\n\n")

# ============================================================================================================================================


# GAME CHAPTER SPECIFIC FUNCTIONS


# ============================================================================================================================================

exit_event = False                      # This boolean variable is used to check if the user inputted the correct answer.
oxygen_remaining = [0]                  # Keeps track of remaining time left before function ends.
countdown_running = True

def countdown_event():                  # Countdown Clock for Oxygen Puzzle | Credit to Austin L. Howard for this threading solution.
    global countdown_running
    
    # Loop Until: 60 Seconds Have Passed
    for i in range(60, 0, -1):          # Count for 10 seconds.
        
        # If Player is Correct:
        if exit_event is True:          # If user is correct.
            break                       # Break out of loop. Resume function.
        
        oxygen_remaining[0] = i         # Stores current countdown value.
        for i in range(10):             # 0.1 * 10 iterations = 1 second sleep
            sleep(0.1)                  # Sleep 1/10th of a second.
            
            # If Player is Correct:
            if exit_event is True:      # Check if the exit_event is set every 1/10th of a second.
                break                   # If exit is set, break out of loop, resume function.
    
    # If Player Succeeded:
    if oxygen_remaining[0] > 1:         # If user suceeded with oxygen remaining:
        countdown_running = False
        return                          # Return back to chapter_01()
    
    # If Player Failed:
    else:                               # If user failed: 
        countdown_running = False
        print("\b\b\r", end="")
        delay_print("As you struggle to make your way out of the water, your chest gives weigh.\nYou open your mouth, gasping for air, as water rushes into your lungs.\nYou have perished. Game over.\n") 
        sys.exit()

def question():                         # Prompts User Repeatedly | Credit to Austin L. Howard for this threading solution.
    
    global input_buffer                 
    global exit_event                   # Used to define when to stop
    global countdown_running            # Used as a stop flag for question_thread
    
    player_restrained = True            # Checks if the player is still in shackles
    clear_buffer()
    
    # Loop For: 60 Second Countdown
    while countdown_running == True:                                     # Indefinitely Loop
        
        # If Player has not Solved Puzzle Yet:
        if exit_event is False:                     
            delay_print("You are drowning. What do you do?\n")
            input_buffer = user_input()             
        
        # If Near Correct Answer:
        if input_buffer == "use key" or input_buffer == "use key on shackles":                
            delay_print("\nuse <what object?> on <what object?>\n")
            continue
        
        # If Correct Answer:
        elif "use rusty key on shackles" in input_buffer:
            player_restrained = False
            delay_print("\nAs you feel in your pocket, you find a rusty key.\nYou twist the key into the lock.\nThe key snaps as the lock releases.\nKicking your feet, you knock off the chains that bound you.\n")
        
        # If Player Restrained:
        elif "swim" in input_buffer and player_restrained == True:
            delay_print("\nYou attempt to kick your feet, but you are still bound by the shackles that hold you.\nYou make no progress.\n")
        
        # If Player Unrestrained:
        elif player_restrained == False and input_swim in input_buffer: # If the player is not bound by the shackles and tries to swim:
            
            # If Correct Answer:
            if input_buffer == "swim up": # If input_buffer == "swim up"
                exit_event = True                       # Sets Exit Event for countdown_event() | Marker for correct answer
            
            # If Movement Down:
            elif input_buffer == "swim down":
                delay_print("\nThe darkness grows as the faint light above you begins to dim.\n")
            
            # If movement Left, Right, Forward, Backward:
            else:
                delay_print("\nYour hands press up against a cold stone wall. Moss and algae fill the cracks and crevasis of the black-stone bricks.\n")
        
        # If System Command Called:
        elif input_buffer in input_help_guide or input_buffer in input_inventory:     # If help or inv are called:
            continue                                                            # Print normally
        
        # If invalid input:
        else:                                                                   # Catch all | If incorrect answer:
            continue                                                            # Error handling is passed to user_input() for wrong answers
    

# ============================================================================================================================================


# GAME CHAPTERS


# ============================================================================================================================================

def prologue():
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
    delay_print(f'"{user_name}, your crimes are now forgiven."\n')
    delay_print("The priest thrusts his hands downwards.\n")
    delay_print("The ground shakes as howls of lost souls wail from the abyss below.\n")
    delay_print(f'"May the Enidra have mercy on our souls."\n')
    delay_print("You feel the hand of your friend, Yuri, rest his hand on your shoulder.\n")
    delay_print("At the next moment, you watch you are pushed into the abyss below.\n")


def chapter_01():
    global input_buffer
    
    delay_print("\nThe air slices your skin as it rushes past your face.\n")
    delay_print("Weightless; you plummet.\n")
    delay_print("Death knocking at the door.\n")
    delay_print("A loud crash echoes into your ears.\n")
    delay_print("The cold rush of liquid races past your body.\n")
    delay_print("You open your eyes and come to your senses.\n")
    delay_print("You are submerged, with little breath to spare.\n")
    delay_print("You are about to drown, what do you do?\n")
    input_buffer = user_input()
    
    # Oxygen Puzzle | Credit to Austin L. Howard for the solution.
    question_thread = Thread(target=question)           # Associate question() function with thread.
    question_thread.daemon = True
    countdown_thread = Thread(target=countdown_event)   # Associate countdown_event() function with thread.
    countdown_thread.start()                            # Start oxygen countdown
    question_thread.start()                             # Prompt user until oxygen countdown ends.
    countdown_thread.join()                             # Waits for countdown_thread to finish before proceeding in chapter_01()
    
    delay_print('\nWith little air left to spare, you swim to the surface.\nYou take a gasp of air as you begin to take in your surroundings.\n')
    delay_print("\nPillars of blackstone rise 60ft to the celing of this grand grotto.\n")
    delay_print("Looking upwards through the brick layed shaft, you can see the small dot of light from the top of the crater.\n")
    delay_print("You tread water in a pool with a diamater of no more than 50ft.\n")
    delay_print("On each of the four sides of the pool, there are statues of two claw formed hands stretched upwards.\n")
    delay_print("The grotto is too dark to see much of anything else.\n")

# Chapter 01 Refactoring Into a Class
"""
class chapter_01:
    def __init__(self):
        pass
        
    def countdown_event():  # Used for oxygen_puzzle()
        global countdown_running
        
        # Loop Until: 60 Seconds Have Passed
        for i in range(60, 0, -1):          # Count for 10 seconds.
            
            # If Player is Correct:
            if exit_event is True:          # If user is correct.
                break                       # Break out of loop. Resume function.
            
            oxygen_remaining[0] = i         # Stores current countdown value.
            for i in range(10):             # 0.1 * 10 iterations = 1 second sleep
                sleep(0.1)                  # Sleep 1/10th of a second.
                
                # If Player is Correct:
                if exit_event is True:      # Check if the exit_event is set every 1/10th of a second.
                    break                   # If exit is set, break out of loop, resume function.
        
        # If Player Succeeded:
        if oxygen_remaining[0] > 1:         # If user suceeded with oxygen remaining:
            countdown_running = False
            return                          # Return back to chapter_01()
        
        # If Player Failed:
        else:                               # If user failed: 
            countdown_running = False
            print("\b\b\r", end="")
            delay_print("As you struggle to make your way out of the water, your chest gives weigh.\nYou open your mouth, gasping for air, as water rushes into your lungs.\nYou have perished. Game over.\n") 
            sys.exit()
   
    def question():         # Used for oxygen_puzzle()
        
        global input_buffer                 
        global exit_event                   # Used to define when to stop
        global countdown_running            # Used as a stop flag for question_thread
        
        player_restrained = True            # Checks if the player is still in shackles
        clear_buffer()
        
        # Loop For: 60 Second Countdown
        while countdown_running == True:                                     # Indefinitely Loop
            
            # If Player has not Solved Puzzle Yet:
            if exit_event is False:                     
                delay_print("You are drowning. What do you do?\n")
                input_buffer = user_input()             
            
            # If Near Correct Answer:
            if input_buffer == "use key" or input_buffer == "use key on shackles":                
                delay_print("\nuse <what object?> on <what object?>\n")
                continue
            
            # If Correct Answer:
            elif "use rusty key on shackles" in input_buffer:
                player_restrained = False
                delay_print("\nAs you feel in your pocket, you find a rusty key.\nYou twist the key into the lock.\nThe key snaps as the lock releases.\nKicking your feet, you knock off the chains that bound you.\n")
            
            # If Player Restrained:
            elif "swim" in input_buffer and player_restrained == True:
                delay_print("\nYou attempt to kick your feet, but you are still bound by the shackles that hold you.\nYou make no progress.\n")
            
            # If Player Unrestrained:
            elif player_restrained == False and input_swim in input_buffer: # If the player is not bound by the shackles and tries to swim:
                
                # If Correct Answer:
                if input_buffer == "swim up": # If input_buffer == "swim up"
                    exit_event = True                       # Sets Exit Event for countdown_event() | Marker for correct answer
                
                # If Movement Down:
                elif input_buffer == "swim down":
                    delay_print("\nThe darkness grows as the faint light above you begins to dim.\n")
                
                # If movement Left, Right, Forward, Backward:
                else:
                    delay_print("\nYour hands press up against a cold stone wall. Moss and algae fill the cracks and crevasis of the black-stone bricks.\n")
            
            # If System Command Called:
            elif input_buffer in input_help or input_buffer in input_inventory:     # If help or inv are called:
                continue                                                            # Print normally
            
            # If invalid input:
            else:                                                                   # Catch all | If incorrect answer:
                continue                                                            # Error handling is passed to user_input() for wrong answers
    
    def oxygen_puzzle():
        question_thread = Thread(target=question)           # Associate question() function with thread.
        question_thread.daemon = True
        countdown_thread = Thread(target=countdown_event)   # Associate countdown_event() function with thread.
        countdown_thread.start()                            # Start oxygen countdown
        question_thread.start()                             # Prompt user until oxygen countdown ends.
        countdown_thread.join()                             # Waits for countdown_thread to finish before proceeding in chapter_01()
"""
# ============================================================================================================================================


# MASTER CONTROL PANNEL


# ============================================================================================================================================

# Get Character Name | Create Save Files
'''
input_buffer = start_game()                     # Ask user if they would like to play the game.

if input_buffer in input_positive:              # If yes
    get_name()                                  # Begin Game
    create_inv(inventory_file)                  # Creates user's binary inventory file | <user_name>_inventory
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
'''
chapter_01()

#create_inv(user_name, inventory_file)       # Creates <user_name>_inventory file | Adds Crumpled Note
#add_inv_item("Sword", 1)                    # Adds <item>,<quantity> to inventory_file
#save_inv(inventory_file)                    # Saves inventory_file with pickle module.
#load_inv(inventory_file, user_name)         # Loads pickled inventory_file and displays contents.