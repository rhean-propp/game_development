
# Global Variables
NOEXIT = -1  # Value for n/s/e/w directions. 
map = []     # Contains all room objects | Rooms are referrenced by array index.

# Room Subclass
class Room:
    def __init__(self, name, description, aN, aS, aW, aE):
        
        # Name / Description:
        self.name = name                    # Room Name
        self.description = description      # Room description
        
        # Define Exit Points | Values indicate list index for "map" list
        self.north_exit = aN
        self.south_exit = aS
        self.west_exit = aW
        self.east_exit = aE
    
    def __repr__(self):                 # Dunder method for devleopers.
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.north_exit}, {self.south_exit}, {self.west_exit}, {self.east_exit})'
    
    def __str__(self):                  # Dunder method for users.
        return f'{self.name}\n\t{self.description}\n\tNorth Exit: {self.north_exit}\n\tSouth Exit: {self.south_exit}\n\tWest Exit: {self.west_exit}\n\tEast Exit: {self.east_exit}'

# Player Subclass
class Player:
    def __init__(self, name, description):
        self.name = name                    # Player Name
        self.description = description      # Player Description
        
map.append(Room("Troll Room", "A dank room that smells of troll.", NOEXIT, 1, NOEXIT, 2))               # Connected to Room 1 and Room 2
map.append(Room("Forest", "A leafy woodland", 0, NOEXIT, NOEXIT, 3))                                    # Connected to Room 0 and Room 3
map.append(Room("Cave", "A dismal cave with walls covered in luminous moss", NOEXIT, 3, 0, NOEXIT))     # Connected to Room 3 and Room 0
map.append(Room("Dungeon", "A nasty, dark cell", 2, NOEXIT, 1, NOEXIT))                                 # Connected to Room 2 and Room 1

print(str(map.__str__()))

# To Do:
# ========================
# How do I tie the co-ordinate system to individual rooms?
    # Do I reference rooms by the coords?
    # Does room know what rooms it's touching?
# How many rooms do I want to generate?
    # Should the generation be 2 dimensional?
    # How do I associate the room name with the coordinates? 
    

