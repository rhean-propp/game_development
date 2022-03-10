# ================================================================== #
# Author: Rhean Propp                                                #
# Date: February 15th, 2022                                          #
# Desc: Serialize Game Data | Save States, Inventory, Character Name #
# ================================================================== #

import pickle

# Global Variable Declaration
inv_dict = {'Crumpled Note':1, 'Rusty Key':1}                  # User Inventory

def create_inv(inventory_file):      # Creates initial user inventory file.
    outfile = open(inventory_file, 'wb')        # Create <user_name>_inventory file and open it in binary writing mode.
    pickle.dump(inv_dict, outfile)              # Write (pickle) the user's inventory into the file.
    outfile.close()                             # Close the file.

def save_inv(inventory_file):                   # Updates user_inventory | Pickles Data    
    outfile = open(inventory_file, 'wb')        # Open <user_name>_inventory file.
    pickle.dump(inv_dict, outfile)              # Input data from item dictionary into <user_name>_inventory file.
    outfile.close()                             # Close file.
    
def load_inv(inventory_file, user_name):                        # Loads user_inventory & prints to screen.
    infile = open(inventory_file, 'rb')                         # Open binary file
    inv_dict = pickle.load(infile)                              # Load dictionary
    print(f"{user_name}'s Inventory:\n".format(user_name))      # Prints <user_name>'s Inventory Title
    for key, value in inv_dict.items():                         # Iterate through dictionary.
        print(f"\t{value} | {key}".format(value, key))          # Print value and key.c
    print("")                                                   # Print newline.
    infile.close()                                              # Close file
    
def add_inv_item(item, quantity):           # Adds item to user's inventory.
    inv_dict.update({item:quantity})        # Updates dictionary with new entry.
    # Note                                  # The inventory must be saved with save_inv() to make the changes persistent.