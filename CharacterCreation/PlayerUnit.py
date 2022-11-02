import random

class PlayerUnit:
    def __init__(self, _class, _level, _baseStats, _growthRates):
        self._class = _class
        self._level = _level
        self._HP = _baseStats.HP
        self._STR = _baseStats.STR
        self._MAG = _baseStats.MAG
        self._DEF = _baseStats.DEF
        self._RES = _baseStats.RES
        self._SPD = _baseStats.SPD
        self._SKL = _baseStats.SKL
        self.HP_Growth = _growthRates.HP_Growth
        self.STR_Growth = _growthRates.STR_Growth
        self.MAG_Growth = _growthRates.MAG_Growth
        self.DEF_Growth = _growthRates.DEF_Growth
        self.RES_Growth = _growthRates.RES_Growth
        self.SPD_Growth = _growthRates.SPD_Growth
        self.SKL_Growth = _growthRates.SKL_Growth

    def levelUp(self):
        for add in range(self._level):
            if random.random() < self.HP_Growth:
                self._HP += 1
            if random.random() < self.STR_Growth:
                self._STR += 1
            if random.random() < self.MAG_Growth:
                self._MAG += 1
            if random.random() < self.DEF_Growth:
                self._DEF += 1
            if random.random() < self.RES_Growth:
                self._RES += 1
            if random.random() < self.SPD_Growth:
                self._SPD += 1
            if random.random() < self.SKL_Growth:
                self._SKL += 1 
        
    