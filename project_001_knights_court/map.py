# ================================================================================ #
# Author: Rhean Propp                                                              #
# Date: April 9th, 2022                                                            #
# Desc: Room and player classes for movement within the game.                      #
# ================================================================================ #

# Global Variables
NOEXIT = -1  # Indicates there is no exit at the specified n/s/e/w direction. 
map = []     # Contains all room objects | Rooms are referrenced by array index.

# Room Class | Template for creating room objects.
class Room:
    def __init__(self, name, description, index, aN, aS, aW, aE):
        
        # Name / Description:
        self.name = name                    # Room Name
        self.description = description      # Room description
        self.index = index
        
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
class Player:
    def __init__(self, name, description, index):
        self.name = name                    # Player Name
        self.description = description      # Player Description
        self.index = index                  # Player Location
        
map.append(Room("Troll Room", "A dank room that smells of troll.", 0, NOEXIT, 1, NOEXIT, 2))               # Connected to Room 1 and Room 2
map.append(Room("Forest", "A leafy woodland", 1, 0, NOEXIT, NOEXIT, 3))                                    # Connected to Room 0 and Room 3
map.append(Room("Cave", "A dismal cave with walls covered in luminous moss", 2, NOEXIT, 3, 0, NOEXIT))     # Connected to Room 3 and Room 0
map.append(Room("Dungeon", "A nasty, dark cell", 3, 2, NOEXIT, 1, NOEXIT))                                 # Connected to Room 2 and Room 1

# Print Out All Room Objects
'''
x = 0
while x < len(map):
    print(map[x].__str__())
    x+=1
'''
# To Do:
# ======
# Create testing area for the player to move around in.

while True:
    print("What room # do you want to move to?\n")
    test_input = input("> ")
    print(test_input)

    if  "0" in test_input:
        player_character = Player("Xenquish", "A royal knight.", 0)
    
    if "1" in test_input:
        player_character = Player("Xenquish", "A royal knight.", 1)
        
    if "2" in test_input:
        player_character = Player("Xenquish", "A royal knight.", 2)
        
    if "3" in test_input:
        player_character = Player("Xenquish", "A royal knight.", 3)
        
    #print(xenquish)
    print(map[player_character.index].name)
