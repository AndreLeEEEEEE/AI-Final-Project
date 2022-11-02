import random

class EnemyUnit:
    def __init__(self):
        self._level = 0
        self._stats = {
            "HP": 0,
            "STR": 0,
            "MAG": 0,
            "DEF": 0,
            "RES": 0,
            "SPD": 0,
            "SKL": 0,
            "MOV": 0
        }
        self._growthRates = {
            "HP_Growth": 0.0,
            "STR_Growth": 0.0,
            "MAG_Growth": 0.0,
            "DEF_Growth": 0.0,
            "RES_Growth": 0.0,
            "SPD_Growth": 0.0,
            "SKL_Growth": 0.0,
        }

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
        
    
