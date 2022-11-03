from Weapon import Weapon

class Stave(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = "Stave"
        self.MT = 10
        self.HIT = 1.0
        self.RNG = 1
        self.offence = False