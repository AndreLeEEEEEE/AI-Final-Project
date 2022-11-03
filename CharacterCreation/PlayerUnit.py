from PlayerUnits.Eliwood import Eliwood
from PlayerUnits.Hector import Hector
from PlayerUnits.Kent import Kent
from PlayerUnits.Sain import Sain
from PlayerUnits.Serra import Serra
import random

class PlayerUnit:
    def __init__(self):
        self._class = ""
        self._level = 10
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
            if random.random() < self._growthRates["HP_Growth"]:
                self._stats["HP"] += 1
            if random.random() < self._growthRates["STR_Growth"]:
                self._stats["STR"] += 1
            if random.random() < self._growthRates["MAG_Growth"]:
                self._stats["MAG"] += 1
            if random.random() < self._growthRates["DEF_Growth"]:
                self._stats["DEF"] += 1
            if random.random() < self._growthRates["RES_Growth"]:
                self._stats["RES"] += 1
            if random.random() < self._growthRates["SPD_Growth"]:
                self._stats["SPD"] += 1
            if random.random() < self._growthRates["SKL_Growth"]:
                self._stats["SKL"] += 1 
        
    def attack(self, offStat, wpnMT):
        return self._stats[offStat] + wpnMT

    def takeDMG(self, DMG):
        self._stats["HP"] -= DMG
        if self._stats["HP"] <= 0:
            self.die(self)

    def die(self):
        # Update matchups and remove self from board
        pass