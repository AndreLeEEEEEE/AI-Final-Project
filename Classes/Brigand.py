from Items.Weapons.Axe import Axe

class Brigand:
    def __init__(self):
        self.name = "Brigand"
        self.HP = 20
        self.STR = 5
        self.MAG = 0
        self.DEF = 3
        self.RES = 0
        self.SPD = 5
        self.SKL = 1
        self.MOV = 5
        self.HP_Growth = 0.82
        self.STR_Growth = 0.50
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.10
        self.RES_Growth = 0.13
        self.SPD_Growth = 0.20
        self.SKL_Growth = 0.30
        self.starting_items = [Axe]
