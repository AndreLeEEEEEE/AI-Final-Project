from Weapon import Weapon

class Lance(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Lance"
        self.MT = 7
        self.HIT = 0.80
        self.RNG = 1