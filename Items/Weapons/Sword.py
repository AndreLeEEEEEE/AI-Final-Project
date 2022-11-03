from Weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Sword"
        self.MT = 5
        self.HIT = 0.90
        self.RNG = 1