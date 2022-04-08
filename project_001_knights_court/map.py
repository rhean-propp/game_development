
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

# Player Subclass
class Player:
    def __init__(self, name, description):
        self.name = name                    # Player Name
        self.description = description      # Player Description




# To Do:
# ========================
# How do I tie the co-ordinate system to individual rooms?
    # Do I reference rooms by the coords?
    # Does room know what rooms it's touching?
# How many rooms do I want to generate?
    # Should the generation be 2 dimensional?
    # How do I associate the room name with the coordinates? 
    

