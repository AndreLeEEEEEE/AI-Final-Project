from Items.Weapons.Tome import Tome

class Monk:
    def __init__(self):
        self.name = "Monk"
        self.HP = 18
        self.STR = 0
        self.MAG = 1
        self.DEF = 1
        self.RES = 5
        self.SPD = 2
        self.SKL = 1
        self.MOV = 5
        self.HP_Growth = 0.50
        self.MAG_Growth = 0.30
        self.DEF_Growth = 0.08
        self.RES_Growth = 0.40
        self.SPD_Growth = 0.32
        self.SKL_Growth = 0.35
        self.starting_items = [Tome]
