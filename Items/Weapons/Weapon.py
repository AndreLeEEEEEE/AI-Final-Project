class Weapon:
    def __init__(self):
        self.name = ""
        self.MT = 0
        self.HIT = 0
        self.RNG = 0
        self.offence = True
        self.type = ""

    def getName(self):
        return self.name

    def getMT(self):
        return self.MT

    def getHIT(self):
        return self.HIT
        
    def getRNG(self):
        return self.RNG
