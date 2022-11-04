from Items.Weapons.Tome import Tome

class Mage:
    def __init__(self):
        self.name = "Mage"
        self.HP = 16
        self.STR = 0
        self.MAG = 1
        self.DEF = 3
        self.RES = 3
        self.SPD = 3
        self.SKL = 2
        self.MOV = 5
        self.HP_Growth = 0.55
        self.STR_Growth = 0.0
        self.MAG_Growth = 0.55
        self.DEF_Growth = 0.05
        self.RES_Growth = 0.30
        self.SPD_Growth = 0.35
        self.SKL_Growth = 0.40
        self.starting_items = [Tome]
        