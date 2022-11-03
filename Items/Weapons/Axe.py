from Weapon import Weapon

class Axe(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Axe"
        self.MT = 8
        self.HIT = 0.75
        self.RNG = 1