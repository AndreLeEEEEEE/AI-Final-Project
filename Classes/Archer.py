from Items.Weapons.Bow import Bow

class Archer:
    def __init__(self):
        self.name = "Archer"
        self.HP = 18
        self.STR = 4
        self.MAG = 0
        self.DEF = 3
        self.RES = 0
        self.SPD = 3
        self.SKL = 3
        self.MOV = 5
        self.HP_Growth = 0.70
        self.STR_Growth = 0.35
        self.DEF_Growth = 0.15
        self.RES_Growth = 0.10
        self.SPD_Growth = 0.32
        self.SKL_Growth = 0.40
        self.starting_items = [Bow]
