# ============================ #
# Author: Rhean Propp          #
# Date: January 28, 2022       #
# Desc: Primary Game Functions #
# ============================ #

# Local Imports
from posixpath import split
from print_func import *             # General functions that do not call other functions.
from data_serialization import *    # Saves game state, inventory and username
from map import *
#from global_variables import *      # Global variables.
#from game_boot import prologue

# External Library Imports
from time import sleep              # Timed messages
#import threading                    # Used for Oxygen Clock in Chapter_01       # Is this actually used?
from threading import Thread

# ============================================================================================================================================ #


# GLOBAL VARIABLES


# ============================================================================================================================================ #

# General Purpose Variables
user_name = ""                  # Name of the character the user is playing.
inventory_file = ""             # Stores <user_name>_inventory. Used for file creation.
player_character = None         # Stores player object. | Location of player.

input_buffer = ""               # User input is stored here.

# General Responses | user_input()
input_positive = ["yes", "y", "ye", "yup", "ya", "yeah", "yep", "perhaps yes", "yus", "sure", "bet", "fo sho", "mmm", "fo shizzle", "yesh", "yas", "okay", "ok", "yessir"]
input_negative = ["no", "n","nope", "nah", "no way", "perhaps no", "naw", "hell nah", "nein", "hell no", "nay", "hell no", "nah brah", "nae"]
input_undecided = ["perhaps", "maybe", "perchance", "conceivably", "possibly", "mayhaps", "mebbeh", "persnaps"]

# Directional movements | user_input()
input_north = ["north", "N"]
input_south = ["south", "S"]
input_east = ["east", "E"]
input_west = ["west", "W"]
input_up = ["up", "upward", "upwards", "U"]
input_down = ["down", "downward", "downwards", "D"]
input_direction = [input_north, input_south, input_east, input_west, input_up, input_down]

# Movement Types | user_input()
input_swim = ["swim"]
input_climb = ["climb"]
input_walk = ["walk", "step"]
input_run = ["run", "dash", "sprint"]
input_jump = ["jump", "hop", "leap", "vault"]
input_move = ["swim", "climb", "walk", "step", "run", "dash", "sprint", "jump", "hop", "leap", "vault"]
# If we make input_move a list of lists, does it break everything?

# Action Types | user_input()
input_use = ["use", "grab", "take", "hold", "drop", "throw", "give", "place"]
input_look = ["look", "examine", "view", "inspect"]
input_interact = ["light", "swing"]

# Items & Weapons | user_input()
input_items = ["rusty_key"]
input_weapons = ["rock", "rusty_sword", "dagger"]

# Universal commands | user_input()
input_inventory = ["inventory", "inv", "i"]
input_shorthand = ["shorthand", "short"]
input_help_guide = ["help", "halp", "h"]             # Need to update this changed list with the function
input_move_guide = ["help move"]                     # Need to update this changed list with the function | Do not call it input_move
input_save = ["save game", "save"]
input_load = ["load game", "load"]
input_quit = ["quit game", "quit", "q"]

# Adverb List for parser | user_input
input_adverb = [input_positive, input_negative, input_undecided, input_direction]   # 2D/3D list. Input Direction is already a list of lists.

# Verb List for Parser | user_input()
input_verb = [input_use, input_look, input_interact, input_move]

# Noun List for parser | user_input()
input_noun = [input_items, input_weapons]

# Function Specific Variables
play_game = False                   # Flag | Used to check if user selected yes when wanting to play a game.

# Puzzle Flags | All variables must be serialized.
room0_oxygen_solved = False 

# ============================================================================================================================================ #


# PRIMARY FUNCTIONS


# ============================================================================================================================================ #

def clear_buffer():         # Clears the input_buffer global variable.
    global input_buffer     # Tells the function to use the global variable.
    input_buffer = ""       # Sets the variable to an empty string.

def user_input():           # Primary Parser. Returns sanitized input.
    
    # Get User Input | Lowercase | Store
    buffer = input("> ").lower()               
    
    # Speech Flags for adverb/verb/noun handler
    is_adverb = False
    is_verb = False
    is_noun = False
    
    # ======================================================== #
    # Directional Movement Commands
    # ======================================================== #
    
    movement_command = False    # Flag | Wow great comment. Whats the flag for?
    
    # Pseudo Code
        # Split user input. It should be indicated to the user that commands involve <verb> <noun>
            # Send verb to verb checker.
            # Send noun to noun checker.
        # Check if first word user entered was a verb.
            # If verb, validate command.
            # If not verb, print error for user.
        # Check if second word user enetered was a noun.
            # If noun, validate command.
            # If not noun, print error for user.
            
    # ======================================================== #
    # Adverb / Verb / Noun Error Handler
    # ======================================================== #
    
    # Sample Pseudo Code
    split_input = buffer.split(" ")
    
    if len(split_input) == 1:
        adverb = split_input[0]

        for list in input_adverb:
            for item in list:                   # Checking 2D List
                for value in item:              # Checking 3D List
                    if adverb == value:         # If in 3D List
                        is_adverb = True
                        print("Adverb found")
                    else:
                        pass
                if adverb == item:              # If in 2D List
                    is_adverb = True
                    print("Adverb found")
                else:
                    pass
        # Check if adverb in adverb list.
            # If not in list, print error.
            # If in list, proceed.
        
        print("Adverb: " + adverb)
        pass
        # Single word command
        # Should either be polar word or noun
    elif len(split_input) == 2:
        
        # Define Verb & Noun
        verb = split_input[0]
        noun = split_input[1]
        
        # Check Verb
        for list in input_verb:
            for item in list:
                if verb == item:
                    is_verb = True
                    print("Verb found")
                else:
                    pass
        
        # Check Noun
        for list in input_noun:
            for item in list:
                if noun == item:
                    is_noun = True
                    print("Noun found")
                else:
                    pass
        
        # Debugging
        print("Verb: " + verb)
        print("Noun: " + noun)
        
        # Objects that have long names should be have an underscore attached.
            # e.g. rusty_key, flaming_sword, glowing_apple
    else:
        print("\n[Input Error] The command you entered was too long. Commands should be either 1 or 2 words.\n")
        
    # How do I do an error handler for the noun/verb/adverb checker?
        # If it is marked as true and the others are false, there could be false positives.
            # How do I correctly write the program so there are no false positives?
    
    # ======================================================== #
    # Player Movement Error Handler
    # ======================================================== #
    
    # Check if buffer is a movement command:
    for movement_type in input_move:                                #
        if movement_type in buffer and movement_command == False:   # 
            movement_command = True                                 # Set flag to true
    
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
        buffer = "help move"
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
    
    # Quit Game
    elif buffer in input_quit:
        buffer = "q"
        print("Warning: If you quit without saving, progress may be lost.\nDo you still wish to quit?\n")
        buffer = user_input()
        if buffer == "yes":
            delay_print("Exiting game...")
            exit()
        else:
            delay_print("Resuming game...\n")
            
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
        # Check for object to be used here.        
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
        if direction in input_north:
            delay_print(f"You cannot {movement_type} {direction}.\n")
        elif direction in input_south:
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
        delay_print("\nWould you like to play a game? [yes/no]\n")                                   
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
    global player_character
    
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
        if user_name in input_inventory or user_name in input_help_guide or user_name in input_verb or user_name in input_save or user_name in input_load:
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
    player_character = Player(user_name, "A royal knight.", 0)                  # Create Player Object.
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
player_death = False

def countdown_event():                  # Countdown Clock for Oxygen Puzzle | Credit to Austin L. Howard for this threading solution.
    global countdown_running
    global room0_oxygen_solved
    
    # Loop Until: 120 Seconds Have Passed
    for i in range(120, 0, -1):          # Count for 10 seconds.
        
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
        room0_oxygen_solved = True
        # Add game_over() function call here

def question():                         # Prompts User Repeatedly | Credit to Austin L. Howard for this threading solution.
    
    global input_buffer                 
    global exit_event                   # Used to define when to stop
    global countdown_running            # Used as a stop flag for question_thread
    global play_game                    # Used in Game Loop
    
    player_restrained = True            # Checks if the player is still in shackles
    clear_buffer()
    
    # Loop For: 120 Second Countdown
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
            elif "use rusty key on shackles" in input_buffer or "use rusty key on shackle" in input_buffer:
                player_restrained = False
                delay_print("\nAs you feel in your pocket, you find a rusty key.\nYou twist the key into the lock.\nThe key snaps as the lock releases.\nKicking your feet, you knock off the chains that bound you.\n")
            
            # If Player Restrained:
            elif "swim" in input_buffer and player_restrained == True:
                delay_print("\nYou attempt to kick your feet, but you are still bound by the shackles that hold you.\nYou make no progress.\n")
            
            # If Player Unrestrained:
            elif player_restrained == False: # If the player is not bound by the shackles and tries to swim:
                
                # If Correct Answer:
                if input_buffer == "swim up": # If input_buffer == "swim up"
                    exit_event = True                       # Sets Exit Event for countdown_event() | Marker for correct answer
                    play_game = True
                
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
    delay_print("At the next moment, you watch as you are pushed into the abyss below.\n")

def oxygen_puzzle():
    global input_buffer
    global oxy_solved
    
    # Begin Drowning Puzzle
    delay_print("\nThe air slices your skin as it rushes past your face.\n")
    delay_print("Weightless; you plummet.\n")
    delay_print("Death knocking at the door.\n")
    delay_print("A loud crash echoes into your ears.\n")
    delay_print("The cold rush of liquid races past your body.\n")
    delay_print("You open your eyes and come to your senses.\n")
    delay_print("You are submerged, with little breath to spare.\n")
    
    
    # Drowning Puzzle | Credit to Austin L. Howard for the solution.
    question_thread = Thread(target=question)           # Associate question() function with thread.
    question_thread.daemon = True                       # Daemon Thread ensures question_thread ends when its parent thread (countdown_thread) ends.
    countdown_thread = Thread(target=countdown_event)   # Associate countdown_event() function with thread.
    countdown_thread.start()                            # Start oxygen countdown
    question_thread.start()                             # Prompt user until oxygen countdown ends.
    countdown_thread.join()                             # Waits for countdown_thread to finish before proceeding in chapter_01()
    
    if player_death == True:
        game_over()
    elif player_death == False:
        oxy_solved = True
    
    # Exit function here if condition is true.

def room_0():
    
    global player_character
    
    delay_print('\nWith little air left to spare, you swim to the surface.\nYou take a gasp of air as you begin to take in your surroundings.\n')
    delay_print("\nPillars of blackstone rise 60ft to the celing of this grand grotto.\n")
    delay_print("Looking upwards through the brick layed shaft, you can see the small dot of light from the top of the crater.\n")
    delay_print("You tread water in a pool with a diamater of no more than 50ft.\n")
    delay_print("On each of the four sides of the pool, there are statues of two claw formed hands stretched upwards.\n")
    delay_print("The grotto is too dark to see much of anything else.\n")
    
    while True:
        delay_print("What do you do?\n")
        input_buffer = user_input()
        
        for string in input_north:
            if string in str(input_buffer):
                player_character = Player(user_name, "A royal knight.", 1)                  # Create Player Object.


# ============================================================================================================================================


# MASTER CONTROL PANNEL


# ============================================================================================================================================

# Game Loop
while True:
    
    # Game Startup Functions
    if play_game == False:
        
        input_buffer = start_game()                     # Ask user if they would like to play the game.
        
        if input_buffer in input_positive:              # If yes
            play_game = True                            # Flag | Runs at game startup.
            get_name()                                  # Begin Game
            create_inv(inventory_file)                  # Creates user's binary inventory file | <user_name>_inventory
        elif input_buffer in input_negative:            # If no
            delay_print("\nMaybe another time.\n")      # Quit Game
            exit()
        else:
            print("\nError. Invalid Input\n")
    
        # Prompt Tutorial
        clear_buffer()
        while input_buffer not in input_negative and input_buffer not in input_positive:        # Check for tutorial flag here.
            delay_print("Would you like to learn how to play the game?\n")
            input_buffer = user_input()
            if input_buffer in input_positive:
                tutorial()
                # Put Tutorial Flag Here | This data needs to be serialized and referenced through serialization.
            elif input_buffer in input_undecided:
                delay_print("\nIf you are unsure, it is a wise idea to run through the tutorial. Don't worry, it's quick.\n")
            else: 
                pass
        
        # Prompt Prologue
        clear_buffer()
        while input_buffer not in input_negative and input_buffer not in input_positive:
            delay_print("\nWould you like to read the prologue?\n")
            input_buffer = user_input()
            if input_buffer in input_positive:
                prologue()
            elif input_buffer in input_undecided:
                delay_print("\nThe prologue is about a 5 minute read. If you like to play games for the story, it is recommended.\n")
            else: 
                continue
    
    # Room 0 Functions
    elif player_character.index == 0:
        
        # Call Oxygen Puzzle
        if room0_oxygen_solved == False:
            oxygen_puzzle()
        
        # Second puzzle.    
        room_0()
        
        # If player moves to new room:
            # Change player_character.index to new room number.o
            
            
    # Room 1 Functions
    elif player_character.index == 1:
        print("Index 1")
    elif player_character.index == 2:
        print("Index 2")
    elif player_character.index == 3:
        print("Index 3")
    else:
        print("Error: Player index out of bounds.\n")
        

#game_over()
#create_inv(user_name, inventory_file)       # Creates <user_name>_inventory file | Adds Crumpled Note
#add_inv_item("Sword", 1)                    # Adds <item>,<quantity> to inventory_file
#save_inv(inventory_file)                    # Saves inventory_file with pickle module.
#load_inv(inventory_file, user_name)         # Loads pickled inventory_file and displays contents.