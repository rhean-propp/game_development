
# Map Parent Class
class Map:        
    def __init__(self):
        raise NotImplementedError("Do not create raw Map objects.\n")
    
    def __str__(self):
        return self.name

# Room Subclass
class Room(Map):
    
    NOEXIT = False  # Do I define this here? How do I pass this when creating the object?
    
    def __init__(self, name, description, coordinates, aN, aS, aW, aE):
        
        # Name / Description:
        self.name = name                    # Room Name
        self.description = description      # Room description
        
        # Object Room Coordinates
        self.coordinates = coordinates      # Location of room on grid. (x,y,z)
        
        # Adjacent Room Coordinates:
        self.north = aN                     # Index of adjacent room north.
        self.south = aS                     # Index of adjacent room south.
        self.west = aW                      # Index of adjacent room west.
        self.east = aE                      # Index of adjacent room east.

# Player Subclass
class Player(Map):
    def __init__(self, name, description):
        self.name = name                    # Player Name
        self.description = description      # Player Description
    
    def set_room(self, coordinates):        # Do I need this function?
        self.coordinates = coordinates      # Should this be a class variable?
    
    def get_room(self):                     # Do I need this function?
        return self.coordinates
    
    # Need a function if player moves (n,s,e,w), that value passed from created room object is the value for the room coordinate.

room_0 = Room("Cave\n", "\Dark and cold.\n", (0,0,0), (0,1,0), (0,-1,0), (-1,0,0), (1,0,0))

# x = horizontal x
# y = horizontal y
# z = vertical z

print(room_0.north)