# ================================================================== #
# Author: Rhean Propp                                                #
# Date: February 15th, 2022                                          #
# Desc: Serialize Game Data | Save States, Inventory, Character Name #
# ================================================================== #

import pickle

# Global Variable Declaration
#inv_dict = {'Crumpled Note':1, 'Rusty Key':1}                  # User Inventory

# Creates initial user inventory file.
def create_inv(inventory_file, inv_dict):
    outfile = open(inventory_file, 'wb')        # Create <player_name>_inventory file and open it in binary writing mode.
    pickle.dump(inv_dict, outfile)              # Write (pickle) the user's inventory into the file.
    outfile.close()                             # Close the file.

# Updates user_inventory | Pickles Data
def save_inv(inventory_file, inv_dict):                       
    outfile = open(inventory_file, 'wb')        # Open <player_name>_inventory file.
    pickle.dump(inv_dict, outfile)              # Input data from item dictionary into <player_name>_inventory file.
    outfile.close()                             # Close file.

# Loads user_inventory & prints to screen.
def load_inv(inventory_file, inv_dict, player_name):                        
    infile = open(inventory_file, 'rb')                         # Open binary file
    inv_dict = pickle.load(infile)                              # Load dictionary
    print(f"\n{player_name}'s Inventory:\n")                      # Prints <player_name>'s Inventory Title
    for key, value in inv_dict.items():                         # Iterate through dictionary.
        print(f"\t{value} | {key}")                             # Print value and key.c
    print("")                                                   # Print newline.
    infile.close()                                              # Close file
    
# Adds item to players's inventory.
def add_inv_item(inv_dict, item, quantity):           
    inv_dict.update({item:quantity})        # Updates dictionary with new entry.
    # Note                                  # The inventory must be saved with save_inv() to make the changes persistent.

# Removes an item from player's inventory.
def delete_inv_item(inv_dict, item):                  
    del inv_dict[item]                      # Look for the key in the dictionary and delete that entry.