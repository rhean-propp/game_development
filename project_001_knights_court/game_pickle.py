# Author: Rhean Propp
# Date: February 15th, 2022
# Purpose: This file is used for pickling and un-pickling data. Data involving the user's name, inventory and save state is handled here.

import pickle
from game_functions import *

# Global Variable Declaration
inventory_file = ""             # Stores the name of the inventory file. Updated in get_name()
inventory_file_name = 0         # Notes if the inventory_file has been properly named or not.

def get_name():                                         # Gets Name of User
    
    valid_name = 0
    input_buffer = ""
    
    while valid_name == 0:
        
        print("\nAdventurer, what is your name?\n")
        name = input("> ")
        valid_name = 1
        
        if len(name) > 20:
            print("\nThat name is too long.\nPlease enter up to a max of 20 characters.")
            valid_name = 0
            
        if name == "help" or name == "inv" or name == "inventory":
            valid_name = 0
            print("\nThat is not a valid name.")
            
        if valid_name == 1:
            print("\nYou entered: {user_name} \n\nIs this correct?\n".format(user_name = name))
            input_buffer = user_input()
            if input_buffer == "no":
                valid_name = 0
    
    global inventory_file
    inventory_file = "{user_name}_inventory".format(user_name = name)
    print("\nUnderstood, {user_name}\nYour adventure awaits...\n".format(user_name = name))
    print("\n")
    
    return name

def inventory():                                        # Displays user's inventory
    print("\nInventory:\n")

def save_inv():
    inv_dict = {'Crumpled Note':1}                      # User Inventory
    
    outfile = open(inventory_file, 'wb')
    pickle.dump(inv_dict)
    outfile.close()
    
def load_inv():
    print("Hello world")
    infile = open(inventory_file, 'rb')
    