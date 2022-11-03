from Weapon import Weapon

class Tome(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Tome"
        self.MT = 5
        self.HIT = 0.90
        self.RNG = (1, 2)