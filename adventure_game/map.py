# ================================================================================ #
# Author: Rhean Propp                                                              #
# Date: April 9th, 2022                                                            #
# Desc: Room and player classes for movement within the game.                      #
# ================================================================================ #

# Global Variables
NOEXIT = -1  # Indicates there is no exit at the specified n/s/e/w direction. 
map = []     # Contains all room objects | Rooms are referrenced by array index.

class Thing:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return self.name    # When the object is called, (printed), the name given to that object is displayed.

# Room Class | Template for creating room objects.
class Room(Thing):
    def __init__(self, name, description, aN, aS, aW, aE, hint=""):
        
        # Name / Description:
        super().__init__(name, description)           # Inherits properties from Thing class.
        #self.index = index                  # Is this used? Refer to map[] index instead?
        
        # Define Exit Points | Values indicate list index for "map" list
        self.north_exit = aN
        self.south_exit = aS
        self.west_exit = aW
        self.east_exit = aE
    
    def __repr__(self):                 # Dunder method for devleopers.
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.north_exit}, {self.south_exit}, {self.west_exit}, {self.east_exit})'
    
    def __str__(self):                  # Dunder method for users.
        return f'------------------------------------------------------------------------\n\nName:\t\t{self.name}\nDescription:\t{self.description}\nRoom Number:\t{self.index}\nExits:\n\tNorth: {self.north_exit}\n\tSouth: {self.south_exit}\n\tWest: {self.west_exit}\n\tEast: {self.east_exit}\n'

# Player Class
class Player(Thing):
    def __init__(self, name, description, index):
        super().__init__(name, description)                   # Inherits properties from Thing class.
        #self.name = name                    # Player Name
        #self.description = description      # Player Description
        self.index = index                  # Player Location
        
# Room Creation & Appending to the Map List        
map.append(Room("Void's End", "A dark hemisphere filled with 4 statues surrounding a pool of dark liquid in the center.", NOEXIT, 1, NOEXIT, 2))               
map.append(Room("Forest", "A leafy woodland", 0, NOEXIT, NOEXIT, 3))                                    
map.append(Room("Cave", "A dismal cave with walls covered in luminous moss", NOEXIT, 3, 0, NOEXIT))     
map.append(Room("Dungeon", "A nasty, dark cell", 2, NOEXIT, 1, NOEXIT))                            

# Debugging | Print Out All Room Objects
'''
x = 0
while x < len(map):
    print(map[x].__str__())
    x+=1
'''