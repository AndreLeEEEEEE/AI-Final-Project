from Items.Weapons.Axe import Axe

class Pirate:
    def __init__(self):
        self.name = "Pirate"
        self.HP = 19
        self.STR = 4
        self.MAG = 0
        self.DEF = 3
        self.RES = 0
        self.SPD = 6
        self.SKL = 2
        self.MOV = 5
        self.HP_Growth = 0.75
        self.STR_Growth = 0.50
        self.DEF_Growth = 0.10
        self.RES_Growth = 0.13
        self.SPD_Growth = 0.25
        self.SKL_Growth = 0.35
        self.starting_items = [Axe]
