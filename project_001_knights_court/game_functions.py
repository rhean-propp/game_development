# Author: Rhean Propp
# Date: January 28, 2022

from game_pickle import *
from game_chapters import *
from game_pickle import *

from time import sleep      # Timed messages


def help():                                             # Display's a list of commands the user can use.
    print("\nCommand List:\n\n\thelp\t\t\t\t| Lists commands user can use\n\t\t\t\t\t|\n\tuse <item>\t\t\t| Uses an item from the user's inventory\n\t\t\t\t\t|\n\tinv\t\t\t\t| Displays user's inventory\n\t\t\t\t\t|\n\tmove <direction>\t\t| Move character in specific direction.\n\t\t\t\t\t|\n\tattack <object> with <item>\t| Attack creature/object with item from user inventory\n\t\t\t\t\t|") 

def user_input():                                       # Grab input from user.
    buffer = input("> ").lower()                        # Store user input into buffer
    if "help" in buffer or buffer == "h":                          
        help()          
    if "inv" in buffer or buffer == "i" or buffer == "inventory":
        inventory()                  
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

        elif "perhaps" in input_buffer:

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
        start_game()
