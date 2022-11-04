from Items.Weapons.Lance import Lance
from Items.Weapons.Sword import Sword

class Sain:
    def __init__(self):
        self._class = "Cavalier"
        self.starting_items = [Lance(), Sword()]
        self.HP = 19
        self.STR = 8
        self.MAG = 0
        self.DEF = 6
        self.RES = 0
        self.SPD = 6
        self.SKL = 4
        self.MOV = 7
        self.HP_Growth = 0.80
        self.STR_Growth = 0.60
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.20
        self.RES_Growth = 0.20
        self.SPD_Growth = 0.40
        self.SKL_Growth = 0.35
