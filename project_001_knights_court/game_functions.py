# Author: Rhean Propp

from time import sleep

def help():
    print("\nCommand List:\n\n\thelp\t\t\t\t| Lists commands user can use\n\t\t\t\t\t|\n\tuse <item>\t\t\t| Uses an item from the user's inventory\n\t\t\t\t\t|\n\tinv\t\t\t\t| Displays user's inventory\n\t\t\t\t\t|\n\tmove <direction>\t\t| Move character in specific direction.\n\t\t\t\t\t|\n\tattack <object> with <item>\t| Attack creature/object with item from user inventory\n\t\t\t\t\t|\n")

def start_game():       # Prompt user to start game.
    
    print("\nWould you like to play a game?\n")
    
    input_buffer = input("> ").lower()

    if "yes" in input_buffer:
        sleep(1)
        print("\nStarting game...\n")
        sleep(2)
        # Add call to begin game.
    
    elif "no" in input_buffer:

        sleep(1)
        print("\nMaybe another time..")
    
    elif "perhaps" in input_buffer:

        sleep(3)
        print("\nPerhaps yes or perhaps no?\n")
        
        input_buffer = input("> ").lower()

        if "perhaps" in input_buffer:
            
            sleep(3)

            print("\nNo really. Do you want to play this game or not?\n")
            input_buffer = input("> ").lower()
        
        if "yes" in input_buffer:

            sleep(1)
            print("\nStarting game...\n")
            sleep(2)
            # Add call to begin game

        elif "no" in input_buffer:

            sleep(1)
            print("\nOk. Fine. Have it your way.\n")
            exit()

        elif "perhaps" in input_buffer:

            sleep(3)
            print("\n.", end="", flush=True)
            sleep(0.15)
            print(".", end="", flush=True)       # fix
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