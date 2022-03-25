# Testing Co-ordinate system.

# Ideas:
# 1. 3D Linked List
# 2. xyz co-ordinates

# Working with 2D linked lists.
# We'll make a grid, and a player entity. Then move the player around the grid borders.
# Initial grid should be 3x3 so the player has 9 different spaces to move.

# Working with xyz co-ordinate system.
# We'll create a list of possible co-ordinates with a 3 dimensional list.
# A testing area will be a 5x5 cube. 3x3 spaces which the player can move within, with the outer edge being NULL.

# Co-Ordinate Generation:
from tkinter import N


coordinates = []

for x in range (-3, 3):             # East/West
    for y in range(-3, 3):          # North/South
        for z in range(-3, 3):      # Up/Down
            coordinates.append((x,y,z))

# Print Output
#print(coordinates)

# Movement Testing:
#player_location = (0,0,0)
#print(player_location)

class Weapon():             # Parent Class
    def __str__(self):
        return self
    
class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock. Suitable for bludgeoning."
        self.damage = 5
    
    def __str__(self):
        return f"\nName: {self.name}\nDescription: {self.description}\nDamage: {self.damage}\n"
    
    # def get_name():
    
    # def get_description():
    
    # def set_description():

rock = Rock()       # Object creation. This is our newly created rock.
weapon = Weapon(rock)

print(weapon)

