#from main import player_name

# ========================== #
# Weapons                    #
# ========================== #

class Weapon:        
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.\n")
    
    def __str__(self):
        return self.name        # When the object is called, (printed), the name of the object is displayed.

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A rock like object that remarkably resembles a rock.\n"

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small knife that does not resemble a rock.\n"

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "An arm's length blade rusted and chipped from the years of wear.\n"
        
# ========================== #
# Items                      #
# ========================== #

# inv_dict = {'Crumpled Note':1, 'Rusty Key':1}                  # User Inventory

class Item:
    def __init__(self):
        raise NotImplementedError("Do not create raw Item objects.\n")
    
    def __str__(self):
        return self.name        # When the object is called, (printed), the name of the object is displayed.
    
class CrumpledNote(Item):
    def __init__(self):
        self.name = "Crumpled Note"
        self.keyword = "crumpled_note"
        self.description = f"I know this wasn't what you wanted.\nI didn't want this either.\nI pray you make your return.\n\n~Yuri"

class RustyKey(Item):
    def __init__(self):
        self.name = "Rusty Key"
        self.keyword = "rusty_key"
        self.description = "A worn out skeleton key often carried by jailers.\n"
        
class Torch(Item):
    def __init__(self):
        self.name = "Torch"
        self.keyword = "torch"
        self.description = "A wooden stick wrapped in an oil soaked rag."
        
class Potion(Item):
    def __init__(self):
        self.name = "Potion"
        self.keyword = "potion"
        self.description = "An apothecary jar filled with a mysterious red liquid."