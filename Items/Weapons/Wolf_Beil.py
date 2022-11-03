from Weapon import Weapon

class Wolf_Beil(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Wolf Beil"
        self.MT = 10
        self.HIT = 0.75
        self.RNG = 1