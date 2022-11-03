from Weapon import Weapon

class Bow(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Bow"
        self.MT = 6
        self.HIT = 0.85
        self.RNG = 2