# Testing Co-ordinate system.

# Ideas:
# 1. 3D Linked List
# 2. xyz co-ordinates
# 3. Array referrence with parent and child subclasses

# Working with 2D linked lists.
# We'll make a grid, and a player entity. Then move the player around the grid borders.
# Initial grid should be 3x3 so the player has 9 different spaces to move.

# Working with xyz co-ordinate system.
# We'll create a list of possible co-ordinates with a 3 dimensional list.
# A testing area will be a 5x5 cube. 3x3 spaces which the player can move within, with the outer edge being NULL.



# Print Output
#print(coordinates)

# Movement Testing:
#player_location = (0,0,0)
#print(player_location)

class Map():             # Parent Class
    def __str__(self):
        return self
    
class Room(Map):
    def __init__(self, name, description, index, aN, aS, aW, aE):
        self.name = name
        self.description = description
        self.index = index
        
        self.north = aN
        self.south = aS
        self.west = aW
        self.east = aE
        
    def getN():
        return north
    
    def setN(aN):
        north = aN
    
    def getS():
        return south
    
    def setS(aS):
        south = aS
        
    def getE():
        return east
    
    def setE(aE):
        east = aE
        
    def getW():
        return west
    
    def setW(aW):
        west = aW
    
    def __str__(self):
        return f"\nName: {self.name}\nDescription: {self.description}\nIndex: {self.index}\n"
    
class Player(Map):
    def __init__(self):
        return self
    
    def get_location():
        print("Print Index[x] for room # player is in.\n")
    
    # def get_name():
    
    # def get_description():
    
    # def set_description():

rock = Rock()       # Object creation. This is our newly created rock.
weapon = Weapon(rock)

print(weapon)
