from Classes.Archer import Archer
from Classes.Brigand import Brigand
from Classes.Cavalier import Cavalier
from Classes.Cleric import Cleric
from Classes.Fighter import Fighter
from Classes.Knight import Knight
from Classes.Mage import Mage
from Classes.Mercenary import Mercenary
from Classes.Monk import Monk
from Classes.Myrmidon import Myrmidon
from Classes.Pirate import Pirate
from Classes.Soldier import Soldier
from Classes.Thief import Thief
from Classes.Troubadour import Troubadour
import random

class EnemyUnit:
    def __init__(self, level):
        self._level = level

        randomInt = random.randrange(14)
        self._class = ""
        if randomInt == 0:
            self._class = Archer()
        elif randomInt == 1:
            self._class = Brigand()
        elif randomInt == 1:
            self._class = Cavalier()
        elif randomInt == 1:
            self._class = Cleric()
        elif randomInt == 1:
            self._class = Fighter()
        elif randomInt == 1:
            self._class = Knight()
        elif randomInt == 1:
            self._class = Mage()
        elif randomInt == 1:
            self._class = Mercenary()
        elif randomInt == 1:
            self._class = Monk()
        elif randomInt == 1:
            self._class = Myrmidon()
        elif randomInt == 1:
            self._class = Pirate()
        elif randomInt == 1:
            self._class = Soldier()
        elif randomInt == 1:
            self._class = Thief()
        else:
            self._class = Troubadour()

        self._stats = {
            "HP": self._class.HP,
            "STR": self._class.STR,
            "MAG": self._class.MAG,
            "DEF": self._class.DEF,
            "RES": self._class.RES,
            "SPD": self._class.SPD,
            "SKL": self._class.SKL,
            "MOV": self._class.MOV
        }
        self._growthRates = {
            "HP_Growth": self._class.HP,
            "STR_Growth": self._class.STR,
            "MAG_Growth": self._class.MAG,
            "DEF_Growth": self._class.DEF,
            "RES_Growth": self._class.RES,
            "SPD_Growth": self._class.SPD,
            "SKL_Growth": self._class.SKL,
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

    def move(self):
        # Move up to the unit's movement
        pass
    