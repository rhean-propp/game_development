# Author: Rhean Propp
# Date: January 28, 2022
# Desc: Genral functions that do not call other functions are placed in this file.

def help():                                             # Display's a list of commands the user can use.
    print("\nCommand List:\n\t\t\t\t\t\t|")
    print("\thelp\t\t\t\t\t| Lists commands user can use.\n\t\t\t\t\t\t|")
    print("\tinv\t\t\t\t\t| Displays user's inventory.\n\t\t\t\t\t\t|")
    print("\tsave\t\t\t\t\t| Saves the game from the last checkpoint.\n\t\t\t\t\t\t|")
    print("\tuse <item>\t\t\t\t| Uses an item from the user's inventory.\n\t\t\t\t\t\t|")
    print("\tmove <direction>\t\t\t| Move character in specific direction.\n\t\t\t\t\t\t|")
    print("\tattack <creature/object> with <item>\t| Attack creature/object with item from user inventory.\n\t\t\t\t\t\t|")
    print("\tread <object>\t\t\t\t| Reads an object if the object can be read.\n\t\t\t\t\t\t|")