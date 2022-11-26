from Items.Weapons.Wolf_Beil import Wolf_Beil
from Items.Miscellaneous.Vulnerary import Vulnerary

class Hector:
    def __init__(self):
        self._class = "Lord"
        self.starting_items = [Wolf_Beil, Vulnerary]
        self.HP = 19
        self.STR = 7
        self.MAG = 0
        self.DEF = 8
        self.RES = 0
        self.SPD = 5
        self.SKL = 4
        self.MOV = 5
        self.HP_Growth = 0.90
        self.STR_Growth = 0.60
        self.MAG_Growth = 0.0
        self.DEF_Growth = 0.50
        self.RES_Growth = 0.25
        self.SPD_Growth = 0.35
        self.SKL_Growth = 0.45
        self.type = "Offensive"
        