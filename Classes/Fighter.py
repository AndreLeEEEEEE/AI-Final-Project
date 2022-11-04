from Items.Weapons.Axe import Axe

class Fighter:
    def __init__(self):
        self.name = "Fighter"
        self.HP = 20
        self.STR = 5
        self.MAG = 0
        self.DEF = 2
        self.RES = 0
        self.SPD = 4
        self.SKL = 2
        self.MOV = 5
        self.HP_Growth = 0.85
        self.STR_Growth = 0.55
        self.DEF_Growth = 0.15
        self.RES_Growth = 0.10
        self.SPD_Growth = 0.30
        self.SKL_Growth = 0.20
        self.starting_items = [Axe]
