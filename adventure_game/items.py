# ========================== #
# Weapons                    #
# ========================== #

class Weapon:        
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.\n")
    
    def __str__(self):
        return self.name

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

class Item:
    def __init__(self):
        raise NotImplementedError("Do not create raw Item objects.\n")
    
    def __str__(self):
        return self.name

class RustyKey(Item):
    def __init__(self):
        self.name = "Rusty Key"
        self.description = "A worn out skeleton key often carried by jailers.\n"