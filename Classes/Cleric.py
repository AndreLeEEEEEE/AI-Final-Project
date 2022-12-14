from Items.Weapons.Stave import Stave

class Cleric:
    def __init__(self):
        self.name = "Cleric"
        self.HP = 16
        self.STR = 0
        self.MAG = 1
        self.DEF = 0
        self.RES = 6
        self.SPD = 2
        self.SKL = 2
        self.MOV = 5
        self.HP_Growth = 0.50
        self.STR_Growth = 0.0
        self.MAG_Growth = 0.30
        self.DEF_Growth = 0.08
        self.RES_Growth = 0.50
        self.SPD_Growth = 0.32
        self.SKL_Growth = 0.35
        self.starting_items = [Stave]
