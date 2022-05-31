# ============================ #
# Author: Rhean Propp          #
# Date: January 28, 2022       #
# Desc: Primary Game Functions #
# ============================ #

# ============================================================================================================================================ #


# IMPORTS


# ============================================================================================================================================ #

# Local Imports
from print_func import *             # General functions that do not call other functions.
from data_serialization import *    # Saves game state, inventory and username
from map import *
from items import *

# External Library Imports
from time import sleep              # Timed messages
from threading import Thread

# ============================================================================================================================================ #


# GLOBAL VARIABLES


# ============================================================================================================================================ #

# General Purpose Variables
player_name = ""                # Name of the character the user is playing.
player_character = None         # Stores player object. | Location of player.

# User Input
input_buffer = ""               # User input is stored here.

# Serialized Data
inventory_file = ""                                            # Stores <player_name>_inventory. Used for file creation.

# Item Object Creation
crumpled_note = CrumpledNote()
rusty_key = RustyKey()
torch = Torch()
potion = Potion()

input_items = [crumpled_note, rusty_key, torch, potion] 
input_objects = ["wood", "torch"]

inv_dict = {crumpled_note:1, rusty_key:1}

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
input_help_move = ["move"]                           # Used to prevent an error being thrown from the user_input() parser when using the command "help move"
input_move_guide = ["help move"]                     # Need to update this changed list with the function | Do not call it input_move
input_save = ["save game", "save"]
input_load = ["load game", "load"]
input_quit = ["quit game", "quit", "q"]

# Adverb List for parser | user_input
input_adverb = [input_positive, input_negative, input_undecided, input_direction, input_inventory, input_look]   # 2D/3D list. Input Direction is already a list of lists.

# Verb List for Parser | user_input()
input_verb = [input_use, input_look, input_interact, input_move]

# Noun List for parser | user_input()
input_noun = [input_items, input_weapons, input_help_move, input_items, input_objects]

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
    
    movement_command = False    # Flag | Wow great comment. Whats the flag for?
            
    # ======================================================== #
    # Adverb / Verb / Noun Error Handler
    # ======================================================== #
    
    split_input = buffer.split(" ")             # Splits user input into a list of seperate words.
    
    # If single word input:
    if len(split_input) == 1:
        
        # Define local variables
        adverb = split_input[0]

        # Check if adverb exists.
        for list in input_adverb:
            for item in list:                   # Checking 2D List
                for value in item:              # Checking 3D List
                    if adverb == value:         # If in 3D List
                        is_adverb = True
                    else:
                        pass
                if adverb == item:              # If in 2D List
                    is_adverb = True
                else:
                    pass
                
        # Single word error handler:
        if is_adverb == True:
            pass
            #print("Valid command.")
        elif is_adverb == False and adverb is not None:
            print(f"\n[Input Error] Command: <{split_input[0]}> is not a valid adverb.")

    # If two word input:
    elif len(split_input) == 2:
        
        # Define local variables:
        verb = split_input[0]
        noun = split_input[1]
        adverb = split_input[1]
        
        # Check if verb exists:
        for list in input_verb:
            for item in list:
                if verb == item:
                    is_verb = True
                else:
                    pass
        
        # Check if noun exists:
        for list in input_noun:
            for item in list:
                if noun == item:
                    is_noun = True
                else:
                    pass
        
        # Check if adverb exists.
        for list in input_adverb:
            for item in list:                   # Checking 2D List
                for value in item:              # Checking 3D List
                    if adverb == value:         # If in 3D List
                        is_adverb = True
                    else:
                        pass
                if adverb == item:              # If in 2D List
                    is_adverb = True
                else:
                    pass
        
        # Error handling two word commands:
        if is_verb == True and is_adverb == True or is_noun == True: # If verb = True AND adverb = True OR noun = True
            pass
            #print("Valid command.")
        elif is_adverb == False and is_noun == False:
            print(f"\n[Input Error] Second argument in command: <{split_input[0]}> <{split_input[1]}> is not a valid adverb or noun.\n")
        elif is_verb == False and is_noun == True or is_adverb == True:
            print(f"\n[Input Error] First argument in command: <{split_input[0]}> <{split_input[1]}> is not a valid verb.\n")
        else:
            print(f"[Input Error] Unknown command entry.")
        
    else:
        print("\n[Input Error] The command you entered was too long. Commands should be either 1 or 2 words.\n")
    
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
            save_inv(inventory_file, inv_dict)                         
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
            load_inv(inventory_file, inv_dict, player_name)
    
    # Item Use | Unfinished
    elif "use" in buffer:        
        # Check for object to be used here.        
        return buffer
    
    # ======================================================== #
    # Invalid Input
    # ======================================================== #
    
    # Undefined Response
    else:
        pass
        #delay_print('\nThis is not a valid input. Type "help" or "h" if you are stuck.\n')
    
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
    global player_name                                    
    global input_buffer
    global inventory_file
    global player_character
    
    valid_name = 0  # Flag | Change to Boolean True/False for Clarity
    clear_buffer()
    
    # Loop Until: Name is Valid
    while valid_name == 0:
        delay_print("\nAdventurer, what is your name?\n")
        player_name = input("> ")
        valid_name = 1
        
        # If Name > 20 Characters:
        if len(player_name) > 20:
            delay_print("\nThat name is too long.\nPlease enter up to a max of 20 characters.")
            valid_name = 0
        
        # If Name is a System Command:
        if player_name in input_inventory or player_name in input_help_guide or player_name in input_verb or player_name in input_save or player_name in input_load:
            valid_name = 0
            delay_print("\nThat is not a valid name.")
            # This will need to be updated as system commands are added.
        
        # Check if User Entered Name Correctly:
        if valid_name == 1:
            delay_print(f"\nYou entered: {player_name} \n\nIs this correct?\n")
            input_buffer = user_input()
            if input_buffer in input_negative:
                valid_name = 0
            elif input_buffer in input_positive:
                break
            else:
                delay_print("\nThat is not a valid answer.")
                valid_name = 0
                
    # Create Inventory File Based on Player's Name:
    inventory_file = f"{player_name.lower()}_inventory"                        # Save inventory file name as <player_name>_inventory
    player_character = Player(player_name, "A royal knight.", 0)                  # Create Player Object.
    delay_print(f"\nUnderstood, {player_name}.\nYour adventure awaits.\n\n")
    
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
        return                          # Return back to function call.
    
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
            if input_buffer == "use key":                
                delay_print("\nuse <what object?>\n")
                continue
            
            # If Correct Answer:
            elif "use rusty_key" in input_buffer:
                player_restrained = False
                delete_inv_item(inv_dict, rusty_key)
                save_inv(inventory_file, inv_dict)
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

def oxygen_puzzle():
    global input_buffer
    global oxy_solved
    
    # Begin Drowning Puzzle
    delay_print("\nThe air rushes past your face.\n")
    delay_print("Weightless; you plummet.\n")
    delay_print("A loud crash echoes into your ears.\n")
    delay_print("The cold rush of liquid races past your body.\n")
    delay_print("You open your eyes and come to your senses.\n")
    
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

def room_0_voids_end():
    
    global player_character
    global input_buffer
    
    delay_print('\nWith little air left to spare, you swim to the surface.\nYou take a gasp of air as you begin to take in your surroundings.\n')
    delay_print("You tread water in a pool with a diamater of no more than 50ft.\n")
    
    # These might need to be made global variables if the player returns to this room.
    intro_text = True
    secondary_text = False
    torch_lit = False
    
    while player_character.index == 0:      # Perhaps set to while true?
        
        #if "examine wood" in input_buffer or "look wood" in input_buffer:
        if "wood" in input_buffer:
            for item in input_look:             # This is such a stupid way of doing this. But for lack of a better idea at the time, this probably works.
                if item in input_buffer:        # Shoot me.
                    delay_print("This wooden object appears to be a torch.\n")
        elif "take torch" in input_buffer or "grab torch" in input_buffer or "take wood" in input_buffer or "grab wood" in input_buffer:
            delay_print("A torch has been added to your inventory!\n")
            add_inv_item(inv_dict, torch, 1)
            save_inv(inventory_file, inv_dict)
            #load_inv(inventory_file, inv_dict, player_name)                  # Testing Line Remove after use
        elif "use torch" in input_buffer or "light torch" in input_buffer:
            if torch in inv_dict:
                torch_lit = True
                secondary_text = True
                delay_print("You light the torch.\n")
                delay_print("The walls of the grotto flicker with a warm orange glow.\n")
            else:
                print("\nYou do not have a torch in your inventory.\n")
        elif any(observe in input_buffer for observe in input_look) and torch_lit == False:
            intro_text = True
        else:
            pass
        
        if intro_text == True:
            intro_text = False
            delay_print("\nYou have fallen into a large chasm. Sounds of dripping water can be heard echoing throughout the cave.\n")
            delay_print("It is to dark to see much of anything. However, you notice a small wood object.\n")

        if secondary_text == True:
            if any(observe in input_buffer for observe in input_look):
                secondary_text = False
                delay_print("\nYou have fallen into a grand grotto that engulfs a small pool of water in its center.\n")
                delay_print("Looking upwards, you can see a distant light coming from the opening of the chasm from which you fell.\n")
                delay_print("On each of the four sides of the pool, there are statues of opened handed angels peering upwards.\n")
        
        delay_print("What do you do?\n")
        input_buffer = user_input()
        
        # Allows User to exit in a certain direction.
        for string in input_north:
            if string in str(input_buffer):
                player_character = Player(player_name, "A royal knight.", 1)                  # Create Player Object.
        #for string in input_south:
        #    if string in str(input_buffer):
        #        player_character = Player(player_name, "A royal knight.", 2)


# ============================================================================================================================================


# MASTER CONTROL PANNEL


# ============================================================================================================================================

option = ""

# Game Loop
while True:
    while option != False:
        
        menu()
        option = int(input("\nEnter your selection: "))
        
        if option == 1:
            # Game Startup Functions
            if play_game == False:
        
                input_buffer = start_game()                     # Ask user if they would like to play the game.
            
            if input_buffer in input_positive:              # If yes
                play_game = True                            # Flag | Runs at game startup.
                get_name()                                  # Begin Game
                create_inv(inventory_file, inv_dict)                  # Creates user's binary inventory file | <player_name>_inventory
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
                    prologue(player_name)
                elif input_buffer in input_undecided:
                    delay_print("\nThe prologue is about a 5 minute read. If you like to play games for the story, it is recommended.\n")
                else: 
                    continue
        if option == 2:
            print("Option 2")
            option = False
        if option == 3:
            print("Option 3")
            option = False
        if option == 4:
            print("Option 4")
            option = False
        else:
            print("Invalid selection.")
            option = ""
            continue
    '''
    # Game Startup Functions
    if play_game == False:
        
        input_buffer = start_game()                     # Ask user if they would like to play the game.
        
        if input_buffer in input_positive:              # If yes
            play_game = True                            # Flag | Runs at game startup.
            get_name()                                  # Begin Game
            create_inv(inventory_file, inv_dict)                  # Creates user's binary inventory file | <player_name>_inventory
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
                prologue(player_name)
            elif input_buffer in input_undecided:
                delay_print("\nThe prologue is about a 5 minute read. If you like to play games for the story, it is recommended.\n")
            else: 
                continue
            '''
    
    # Room 0 Functions
    if player_character.index == 0:
        
        # Call Oxygen Puzzle
        if room0_oxygen_solved == False:
            oxygen_puzzle()
        
        # Second puzzle.    
        room_0_voids_end()
        
        # If player moves to new room:
            # Change player_character.index to new room number.
            
    # Room 1 Functions
    elif player_character.index == 1:
        print("Index 1")
        sleep(2)
    elif player_character.index == 2:
        print("Index 2")
        sleep(2)
    elif player_character.index == 3:
        print("Index 3")
        sleep(2)
    else:
        print("Error: Player index out of bounds.\n")