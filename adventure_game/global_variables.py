# ============================ #
# Author: Rhean Propp          #
# Date: April 20th, 2022       #
# Desc: All Global Variables   #
# ============================ #
'''
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
input_forward = ["forward", "north", "N"]
input_backward = ["backward", "back", "south", "S"]
input_right = ["right", "east", "E"]
input_left = ["left", "west", "W"]
input_up = ["up", "upward", "upwards", "U"]
input_down = ["down", "downward", "downwards", "D"]
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
input_quit = ["quit game", "quit", "q"]

# Player commands for interaction | user_input()
input_examine = ["examine", "look at", "look", "view", "probe"]

# Function Specific Variables
play_game = False                   # Flag | Used to check if user selected yes when wanting to play a game.s
'''