from Items.Weapons.Stave import Stave
from Items.Miscellaneous.Vulnerary import Vulnerary

class Serra:
    def __init__(self):
        self._class = "Cleric"
        self.starting_items = [Stave(), Vulnerary()]
        self.HP = 17
        self.STR = 0
        self.MAG = 2
        self.DEF = 2
        self.RES = 5
        self.SPD = 8
        self.SKL = 5
        self.MOV = 5
        self.HP_Growth = 0.50
        self.STR_Growth = 0.0
        self.MAG_Growth = 0.50
        self.DEF_Growth = 0.15
        self.RES_Growth = 0.55
        self.SPD_Growth = 0.40
        self.SKL_Growth = 0.30
