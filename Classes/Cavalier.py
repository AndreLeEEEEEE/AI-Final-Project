from Items.Weapons.Lance import Lance

class Cavalier:
    def __init__(self):
        self.name = "Cavalier"
        self.HP = 20
        self.STR = 5
        self.MAG = 0
        self.DEF = 6
        self.RES = 0
        self.SPD = 5
        self.SKL = 2
        self.MOV = 7
        self.HP_Growth = 0.75
        self.STR_Growth = 0.35
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.15
        self.RES_Growth = 0.12
        self.SPD_Growth = 0.28
        self.SKL_Growth = 0.40
        self.starting_items = [Lance]
