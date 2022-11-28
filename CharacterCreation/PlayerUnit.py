from PlayerUnits.Eliwood import Eliwood
from PlayerUnits.Hector import Hector
from PlayerUnits.Kent import Kent
from PlayerUnits.Sain import Sain
from PlayerUnits.Serra import Serra
from Maps.mapOne import mapOne
from Algorithms.BFS import BFS
import random

characters = {
    "Eliwood": Eliwood(),
    "Hector": Hector(),
    "Kent": Kent(),
    "Sain": Sain(),
    "Serra": Serra()
}

class PlayerUnit:
    def __init__(self, chr, level, id):
        self._name = chr
        self._class = characters[chr]._class
        self._level = level
        self._stats = {
            "MaxHP": characters[chr].HP,
            "HP": characters[chr].HP,
            "STR": characters[chr].STR,
            "MAG": characters[chr].MAG,
            "DEF": characters[chr].DEF,
            "RES": characters[chr].RES,
            "SPD": characters[chr].SPD,
            "SKL": characters[chr].SKL,
            "MOV": characters[chr].MOV
        }
        self._growthRates = {
            "HP_Growth": characters[chr].HP_Growth,
            "STR_Growth": characters[chr].STR_Growth,
            "MAG_Growth": characters[chr].MAG_Growth,
            "DEF_Growth": characters[chr].DEF_Growth,
            "RES_Growth": characters[chr].RES_Growth,
            "SPD_Growth": characters[chr].SPD_Growth,
            "SKL_Growth": characters[chr].SKL_Growth,
        }
        self._side = 1
        self._id = id
        self._type = characters[chr].type
        if characters[chr].type == "Offensive":
            self._state = "aggro"
        else:
            self._state = "heal"
        self._inventory = characters[chr].starting_items

    def get_id(self):
        return self._id

    def get_side(self):
        return self._side

    def levelUp(self):
        for add in range(self._level):
            if random.random() < self._growthRates["HP_Growth"]:
                self._stats["MaxHP"] += 1
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

    def scanForTarget(self):
        target = 2 if self._type == "Offensive" else 1
        RNG = self._inventory[0]["RNG"]
        BFS(mapOne, target, RNG)
        
    def die(self):
        if self._class == "Lord":
            # Trigger game over
            pass
        # Update matchups and remove self from board
        pass

    def move(self):
        # Move up to the unit's movement
        pass
    