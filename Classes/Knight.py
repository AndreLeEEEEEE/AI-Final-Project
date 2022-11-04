from Items.Weapons.Lance import Lance

class Knight:
    def __init__(self):
        self.name = "Knight"
        self.HP = 17
        self.STR = 5
        self.MAG = 0
        self.DEF = 9
        self.RES = 0
        self.SPD = 0
        self.SKL = 2
        self.MOV = 4
        self.HP_Growth = 0.80
        self.STR_Growth = 0.40
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.28
        self.RES_Growth = 0.20
        self.SPD_Growth = 0.15
        self.SKL_Growth = 0.30
        self.starting_items = [Lance]
