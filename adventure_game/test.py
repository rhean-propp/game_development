from print_func import *             # General functions that do not call other functions.
from data_serialization import *    # Saves game state, inventory and username
from map import *
from items import *

# External Library Imports
from time import sleep              # Timed messages
from threading import Thread

inv_dict = {}

crumpled_note = CrumpledNote()
rusty_key = RustyKey()
torch = Torch()
potion = Potion()

add_inv_item(inv_dict, crumpled_note, 1)
add_inv_item(inv_dict, rusty_key, 1)

print(inv_dict)

delete_inv_item(inv_dict, rusty_key)

print(inv_dict)