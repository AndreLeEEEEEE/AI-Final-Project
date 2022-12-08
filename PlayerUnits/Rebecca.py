from Items.Weapons.Bow import Bow
from Items.Miscellaneous.Vulnerary import Vulnerary

class Rebecca:
    def __init__(self):
        self._class = "Archer"
        self.starting_items = [Bow, Vulnerary]
        self.HP = 17
        self.STR = 4
        self.MAG = 0
        self.DEF = 3
        self.RES = 1
        self.SPD = 6
        self.SKL = 5
        self.MOV = 5
        self.HP_Growth = 0.60
        self.STR_Growth = 0.40
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.15
        self.RES_Growth = 0.30
        self.SPD_Growth = 0.60
        self.SKL_Growth = 0.50
        self.type = "Offensive"
