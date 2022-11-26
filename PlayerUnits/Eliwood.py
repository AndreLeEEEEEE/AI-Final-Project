from Items.Weapons.Rapier import Rapier
from Items.Miscellaneous.Vulnerary import Vulnerary

class Eliwood:
    def __init__(self):
        self._class = "Lord"
        self.starting_items = [Rapier, Vulnerary]
        self.HP = 18
        self.STR = 5
        self.MAG = 0
        self.DEF = 5
        self.RES = 0
        self.SPD = 7
        self.SKL = 5
        self.MOV = 5
        self.HP_Growth = 0.80
        self.STR_Growth = 0.45
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.30
        self.RES_Growth = 0.35
        self.SPD_Growth = 0.40
        self.SKL_Growth = 0.50
        self.type = "Offensive"
