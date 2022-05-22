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
    
    
### Test Code
# ===========================

class Item:
    def __init__(self):
        raise NotImplementedError("Do not create raw Item objects.\n")
    
    def __str__(self):
        return self.keyword        # When the object is called, (printed), the name of the object is displayed.

class CrumpledNote(Item):
    def __init__(self):
        self.name = "Crumpled Note"
        self.keyword = "crumpled_note"
        self.description = f"I know this wasn't what you wanted.\nI didn't want this either.\nI pray you make your return.\n\n~Yuri"

class RustyKey(Item):
    def __init__(self):
        self.name = "Rusty Key"
        self.keyword = "rusty_key"
        self.description = "A worn out skeleton key often carried by jailers.\n"
        
class Torch(Item):
    def __init__(self):
        self.name = "Torch"
        self.keyword = "torch"
        self.description = "A wooden stick wrapped in an oil soaked rag."

'''
# Debugging Code. Delete Once Solved

crumpled_note = CrumpledNote()
rusty_key = RustyKey()
torch = Torch()

inv_dict = {crumpled_note:1, rusty_key:1}                  # User Inventory
inventory_file = "test_inventory"
player_name = "test"

create_inv(inventory_file, inv_dict)
load_inv(inventory_file, inv_dict, player_name)
delete_inv_item(inv_dict, rusty_key)
save_inv(inventory_file, inv_dict)
load_inv(inventory_file, inv_dict, player_name)
add_inv_item(inv_dict, torch, 1)
save_inv(inventory_file, inv_dict)
load_inv(inventory_file, inv_dict, player_name)

'''