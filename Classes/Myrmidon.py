from Items.Weapons.Sword import Sword

class Myrmidon:
    def __init__(self):
        self.name = "Myrmidon"
        self.HP = 16
        self.STR = 4
        self.MAG = 0
        self.DEF = 2
        self.RES = 0
        self.SPD = 9
        self.SKL = 9
        self.MOV = 5
        self.HP_Growth = 0.70
        self.STR_Growth = 0.35
        self.DEF_Growth = 0.15
        self.RES_Growth = 0.20
        self.SPD_Growth = 0.40
        self.SKL_Growth = 0.40
        self.starting_items = [Sword]
