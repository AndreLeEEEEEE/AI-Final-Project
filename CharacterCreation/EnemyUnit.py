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
from Maps.testMapTwo import testMapTwo as levelMap
from Algorithms.BFS import BFS
from Algorithms.Astar import moveTowardsTarget
import random

class EnemyUnit:
    def __init__(self, level, id, boss=False):
        self._class = ""
        self._boss = boss
        # Set unit level and random class
        if boss:
            self._level = level + 2
            randomInt = random.randrange(12)
            if randomInt == 0:
                self._class = Archer()
            elif randomInt == 1:
                self._class = Brigand()
            elif randomInt == 2:
                self._class = Cavalier()
            elif randomInt == 3:
                self._class = Fighter()
            elif randomInt == 4:
                self._class = Knight()
            elif randomInt == 5:
                self._class = Mage()
            elif randomInt == 6:
                self._class = Mercenary()
            elif randomInt == 7:
                self._class = Monk()
            elif randomInt == 8:
                self._class = Myrmidon()
            elif randomInt == 9:
                self._class = Pirate()
            elif randomInt == 10:
                self._class = Soldier()
            else:
                self._class = Thief()
        else:
            self._level = level
            randomInt = random.randrange(14)
            if randomInt == 0:
                self._class = Archer()
            elif randomInt == 1:
                self._class = Brigand()
            elif randomInt == 2:
                self._class = Cavalier()
            elif randomInt == 3:
                self._class = Cleric()
            elif randomInt == 4:
                self._class = Fighter()
            elif randomInt == 5:
                self._class = Knight()
            elif randomInt == 6:
                self._class = Mage()
            elif randomInt == 7:
                self._class = Mercenary()
            elif randomInt == 8:
                self._class = Monk()
            elif randomInt == 9:
                self._class = Myrmidon()
            elif randomInt == 10:
                self._class = Pirate()
            elif randomInt == 11:
                self._class = Soldier()
            elif randomInt == 12:
                self._class = Thief()
            else:
                self._class = Troubadour()
        # String name of class
        self._name = self._class.name
        self._stats = {
            "MaxHP": self._class.HP,
            "HP": self._class.HP,
            "STR": self._class.STR,
            "MAG": self._class.MAG,
            "DEF": self._class.DEF,
            "RES": self._class.RES,
            "SPD": self._class.SPD,
            "SKL": self._class.SKL,
            "MOV": self._class.MOV
        }
        # Set boss movement
        if boss:
            self._stats["MOV"] = 0
        self._growthRates = {
            "HP_Growth": self._class.HP_Growth,
            "STR_Growth": self._class.STR_Growth,
            "MAG_Growth": self._class.MAG_Growth,
            "DEF_Growth": self._class.DEF_Growth,
            "RES_Growth": self._class.RES_Growth,
            "SPD_Growth": self._class.SPD_Growth,
            "SKL_Growth": self._class.SKL_Growth,
        }
        self._side = 2
        self._id = id
        # self._type handled here
        if self._name == "Cleric" or self._name == "Troubadour":
            self._type = "Support"
        else:
            self._type = "Offensive"
        # Either passive or aggro
        self._state = "passive"
        self._weapon = self._class.starting_items[0]
        self._tile = (0, 0)

    def get_id(self):
        return self._id

    def get_side(self):
        return self._side

    def getTile(self):
        return self._tile
    
    def setTile(self, tile: tuple):
        self._tile = tile

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

    def startTurn(self): # Make separate versions for offense and support
        target = 1 if self._type == "Offensive" else 2
        if self._state == "passive": self.toBattleState(target)
        # If state is "aggro"
        else: self.moveToTarget(target)

    def toBattleState(self, target):
        result = BFS(levelMap, self._tile, target, self._weapon["RNG"], self._side)
        if type(result) != str:
            self._state = "aggro"
            self.moveToTarget(target)

    def moveToTarget(self, target):
        result = BFS(levelMap, self._tile, target, self._weapon["RNG"], self._side)
        if type(result) != str:
            moveTowardsTarget(levelMap, self._tile, target, self._stats["MOV"])

    def attack(self, offStat, wpnMT):
        return self._stats[offStat] + wpnMT

    def takeDMG(self, DMG):
        self._stats["HP"] -= DMG
        if self._stats["HP"] <= 0:
            self.die(self)
        
    def die(self):
        i, j = self._tile
        levelMap[i][j] = '_'

    