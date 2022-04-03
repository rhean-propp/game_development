

class Map:        
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        #raise NotImplementedError("Do not create raw Map objects.\n")
    
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead.\n")

# Room Subclass
class Room(Map):
    
    NOEXIT = False  # Do I define this here? How do I pass this when creating the object?
       
    def __init__(self, name, description, coordinates): #, aN, aS, aW, aE):
        
        # Name / Description:
        self.name = name                    # Room Name
        self.description = description      # Room description
        
        # Object Room Coordinates
        self.coordinates = coordinates      # Tuple Location of room on grid. (x,y,z)
        
        # Adjacent Room Coordinates:
        #self.north = aN                     # Index of adjacent room north.
        #self.south = aS                     # Index of adjacent room south.
        #self.west = aW                      # Index of adjacent room west.
        #self.east = aE                      # Index of adjacent room east.

# Player Subclass
class Player(Map):
    def __init__(self, name, description):
        self.name = name                    # Player Name
        self.description = description      # Player Description
        
        self.x = 0
        self.y = 0
        self.z = 0
        
    def move(self, dx, dy, dz):         # Modify Player Position
        self.x += dx                    # East / West
        self.y += dy                    # North / South
        self.z += dz                    # Up / Down
        
    def move_north(self):               # Y Axis Positive = North
        self.move(dx=0, dy=1, dz=0)
    
    def move_south(self):               # Y Axis Negative = South
        self.move(dx=0, dy=-1, dz=0)
    
    def move_east(self):                # X Axis Positive = East
        self.move(dx=1, dy=0, dz=0)
    
    def move_west(self):                # X Axis Negative = West
        self.move(dx=-1, dy=0, dz=0)
    
    def move_up(self):                  # Z Axis Positive = Up
        self.move(dx=0, dy=0, dz=1)
    
    def move_down(self):                # Z Axis Positive = Down
        self.move(dx=0, dy=0, dz=-1)
    
    # Need a function if player moves (n,s,e,w), that value passed from created room object is the value for the room coordinate.

room_0 = Room("Cave\n", "\Dark and cold.\n", (0,0,0), (0,1,0), (0,-1,0), (-1,0,0), (1,0,0))

# x = horizontal x
# y = horizontal y
# z = vertical z

print(room_0.north)