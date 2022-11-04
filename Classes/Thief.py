from Items.Weapons.Sword import Sword

class Thief:
    def __init__(self):
        self.name = "Thief"
        self.HP = 16
        self.STR = 3
        self.MAG = 0
        self.DEF = 2
        self.RES = 0
        self.SPD = 9
        self.SKL = 1
        self.MOV = 6
        self.HP_Growth = 0.50
        self.STR_Growth = 0.05
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.05
        self.RES_Growth = 0.25
        self.SPD_Growth = 0.40
        self.SKL_Growth = 0.45
        self.starting_items = [Sword]
