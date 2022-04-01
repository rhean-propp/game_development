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
    # Class Variables:
    # Class Variable #1
    
    def __init__(self, name, description, index, aN, aS, aW, aE):       # Variables passed when declaring object.
        
        # Instance Variables:
        self.name = name                    # Room Name
        self.description = description      # Room description
        self.index = index                  # Index of room
        
        self.north = aN                     # Index of adjacent room north.
        self.south = aS                     # Index of adjacent room south.
        self.west = aW                      # Index of adjacent room west.
        self.east = aE                      # Index of adjacent room east.
    
    def __str__(self):
        return f"\nName: {self.name}\nDescription: {self.description}\nIndex: {self.index}\n"
    
class Player(Map):
    def __init__(self):
        return self
    
    def get_location():
        print("Print Index[x] for room # player is in.\n")
    
#print(weapon)

# When I instantiate a room object, I need to know what rooms are connected to it.
# N/S/E/W should point to an index number, that index number referrs to the instance of the room.
# 

room_0 = Room("The Pit\n", "A cold and dark room.\n", 0, 1, 2, 3, 4)
room_1 = Room("Ice Cave\n", "Cold pillars of ice cover the walls.\n", 1, 5, 0, -1, -1)