# Author: Rhean Propp
# Date: February 15th, 2022
# Desc: Serialize Game Data | Save States, Inventory, Character Name

import pickle

# Global Variable Declaration
inventory_file = ""             # Stores the name of the inventory file. Updated in get_name()
inventory_file_name = 0         # Notes if the inventory_file has been properly named or not.

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
    