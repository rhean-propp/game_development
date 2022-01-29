# Author: Rhean Propp

from time import sleep

def start_game():
    
    print("Would you like to play a game?\n")
    
    input_buffer = input("> ").lower()

    if "yes" in input_buffer:

        print("Starting game...")
        sleep(2)
    
    elif "no" in input_buffer:

        print("Maybe another time..")
    
    elif "perhaps" in input_buffer:

        print("Perhaps yes or perhaps no?")
        
        input_buffer = input("> ").lower()

        if "perhaps" in input_buffer:

            print("No really. Do you want to play this game or not?")
            input_buffer = input("> ").lower()
        
        if "yes" in input_buffer:

            print("Starting game...")
            sleep(2)

        elif "no" in input_buffer:

            print("Ok. Fine. Have it your way.")
            exit()

        elif "perhaps" in input_buffer:

            sleep(4.5)
            print("\n." end="")
            sleep(1)
            print("." end="")       # fix
            sleep(1)
            print(".\n")
            sleep(4)
            print("Ok you know what?\n")
            sleep(2.5)
            print("Fine.\n")
            sleep(1.5)
            print("PERHAPS\n")
            sleep(1.8)
            print("Apparently you think i'm more than some binary computer.\n")
            sleep(4)
            print("Maybe you think. OH. THIS IS A QUANTUM COMPUTER. HE CAN HANDLE PERHAPS.\n")
            sleep(4)
            print("WELL PERHAPS YOU'RE WRONG\n")
            sleep(3)
            print("Perhaps things didn't work out the way you expected them to.\n")
            sleep(3.5)
            print("You've just been PERHAPSING your whole life, HAVENT YOU?\n")
            sleep(3)
            print("Well you know what?\n")
            sleep(2)
            print("PERHAPS I LEAVE!\n")
            sleep(1)
            print("PERHAPS THAT!\n")
            exit()

        else:

            print("You're really not making this easy for me, are you?")
    else:

        print("It's a yes or no question.")
        start_game()