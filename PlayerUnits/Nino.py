from Items.Weapons.Tome import Tome
from Items.Miscellaneous.Vulnerary import Vulnerary

class Nino:
    def __init__(self):
        self._class = "Mage"
        self.starting_items = [Tome, Vulnerary]
        self.HP = 19
        self.STR = 0
        self.MAG = 7
        self.DEF = 4
        self.RES = 7
        self.SPD = 11
        self.SKL = 8
        self.MOV = 5
        self.HP_Growth = 0.55
        self.STR_Growth = 0.0
        self.MAG_Growth = 0.50
        self.DEF_Growth = 0.15
        self.RES_Growth = 0.50
        self.SPD_Growth = 0.60
        self.SKL_Growth = 0.55
        self.type = "Offensive"
