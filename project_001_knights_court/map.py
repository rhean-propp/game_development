

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

#room_0 = Room("Cave\n", "\Dark and cold.\n", (0,0,0), (0,1,0), (0,-1,0), (-1,0,0), (1,0,0))

# x = horizontal x
# y = horizontal y
# z = vertical z

# [x,y,z]
cube3d = [[
            [[0,0,0], [1,0,0], [2,0,0]],
            [[0,1,0], [1,1,0], [2,1,0]],
            [[0,2,0], [1,2,0], [2,2,0]],
        
        ],[
            
            [[0,0,1], [1,0,1], [2,0,1]],
            [[0,1,1], [1,1,1], [2,1,1]],
            [[0,2,1], [1,2,1], [2,2,1]],
            
        ],[                 
            
            [[0,0,2], [1,0,2], [2,0,2]],
            [[0,1,2], [1,1,2], [2,1,2]],
            [[0,2,2], [1,2,2], [2,2,2]],
         ]]

#print(cube3d) #[z][y][x]
#print("\n")

# Testing a 3D 3x3x3 cube
'''
x = 0
y = 0
z = 0

while x < 3:
    x += 1
    while y < 3:
        y += 1
        while z < 3:
            z += 1
            mytuple = (x,y,z)
            print(mytuple)
'''
                
# Credit to Austin L. Howard for this generation code:
game_map_side_length = 3   
game_map_list = [[[0 for z in range(game_map_side_length)] for y in range(game_map_side_length)] for x in range(game_map_side_length)]

for x in range(len(game_map_list)):
    for y in range(len(game_map_list[0])):
        for z in range(len(game_map_list[0][0])):
            game_map_list[x][y][z] = [x+1, y+1, z+1]
            
print(game_map_list)