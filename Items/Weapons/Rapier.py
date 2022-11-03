from Weapon import Weapon

class Rapier(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Rapier"
        self.MT = 7
        self.HIT = 0.95
        self.RNG = 1