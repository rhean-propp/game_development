# Author: Rhean Propp
# Date: February 15th, 2022
# Desc: Serialize Game Data | Save States, Inventory, Character Name

import pickle

# Global Variable Declaration
inv_dict = {'Crumpled Note':1}                      # User Inventory
inventory_file = ""

def create_inv(inventory_file):       # Creates initial user inventory file.
    inventory_file = inventory_file
    
    outfile = open(inventory_file, 'wb')
    pickle.dump(inv_dict, outfile)
    outfile.close()

def save_inv():                             # Enters new dictionary parameter | Pickles Data
    global inv_dict
    
    outfile = open(inventory_file, 'wb')
    pickle.dump(inv_dict)
    outfile.close()
    
def load_inv(inventory_file, name):               # Loads and prints pickled inventory data.
    global inv_dict
    
    infile = open(inventory_file, 'rb')             # Open binary file
    inv_dict = pickle.load(infile)                  # Load dictionary
    print(f"{name}'s Inventory:\n".format(name))
    for key, value in list(inv_dict.items()):       # Iterate through dictionary.
        print(f"{key}\n".format(key))               # Print key value.
    infile.close()                                  # Close file
    