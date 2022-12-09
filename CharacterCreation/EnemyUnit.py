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
from Maps.testMapThree import testMapThree as levelMap
from Algorithms.BFS import *
from Algorithms.Astar import moveTowardsTarget
from Algorithms.Astar import manhattan_dist
from Algorithms.Translate import translate
from Results.Write import write
import random

class EnemyUnit:
    def __init__(self, level, boss=False):
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
        # self._type handled here
        if self._name == "Cleric" or self._name == "Troubadour":
            self._type = "Support"
        else:
            self._type = "Offensive"
        # Either passive or aggro
        self._state = "passive"
        self._weapon = self._class.starting_items[0]
        # Where the unit currently is
        self._tile = (0, 0)
        self._dead = False

    def get_side(self):
        return self._side

    def getTile(self):
        return self._tile
    
    def setTile(self, tile: tuple):
        self._tile = tile

    def getSpd(self):
        return self._stats["SPD"]

    def getRng(self):
        return self._weapon["RNG"]

    def getType(self):
        return self._type

    def getDead(self):
        return self._dead

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
        if self._type == "Offensive":
            # Stop this at MOV
            result = BFS(levelMap, self._tile, target,
                            self._weapon["RNG"], self._side, self._stats["MOV"])
        # If type is support
        else:
            result = BFS(levelMap, self._tile, target,
                            self._weapon["RNG"], self._side)
        if result:
            write(f"The {self._name} has aggroed")
            self._state = "aggro"
            self.moveToTarget(target)

    def moveToTarget(self, target):
        # Find tile from which a target can be interacted with
        result = BFS(levelMap, self._tile, target, self._weapon["RNG"], self._side)
        if result:
            # Move to that tile, may or may not reach tile
            newPosition = moveTowardsTarget(levelMap, self._tile, 
                                            result, self._stats["MOV"])

            write(f"{self._name} moved from {translate(self._tile)} to {translate(newPosition)}")
            levelMap[self._tile[0]][self._tile[1]] = '_'
            self.setTile(newPosition)
            levelMap[newPosition[0]][newPosition[1]] = self
            # Check if there's a target in range of this tile
            targetCoord = scan(levelMap, self._tile, self._tile,
                                target, self._weapon["RNG"], self._side)
            if targetCoord:
                i, j = targetCoord
                unitTarget = levelMap[i][j]
                self.attack(unitTarget)

    def attack(self, unitTarget):
        """Handle all rounds of combat and healing."""
        attack = self.calculateAttack()
        spdDiff = self._stats["SPD"] - unitTarget.getSpd()
        # Initial attack
        # Always triggers
        if self._type == "Offensive":
            write(f"The {self._name} attacks {unitTarget._name}")
        else:
            write(f"The {self._name} heals the {unitTarget._name}")
        if random.randrange(1, 101) < self.calculateAccuracy(unitTarget):
            heal = False if self._weapon["offense"] else True
            if unitTarget.takeDMG(attack, self._weapon["type"], heal):
                # Stop combat if the target dies
                return
        else: write(f"The {self._name}'s attack missed")
        # Counterattack
        # Support units cannot defend themselves
        # Don't trigger a counterattack when healing
        # Only triggers if the target unit can attack at the used RNG
        if (unitTarget.getType() == "Offensive" 
            and self._type == "Offensive"
            and set(unitTarget.getRng()) & set(self.getRngInUse(unitTarget))):
            write(f"{unitTarget._name} counterattacks")
            if random.randrange(1, 101) < unitTarget.calculateAccuracy(self):
                if self.takeDMG(unitTarget.calculateAttack(), unitTarget._weapon["type"], False):
                    # Stop combat if the unit dies
                    return
            else: write(f"{unitTarget._name}'s attack missed")
        # Follow-up attack
        # Do not make a follow-up attack for healing
        if spdDiff >= 4 and self._type == "Offensive":
            if random.randrange(1, 101) < self.calculateAccuracy(unitTarget):
                write(f"The {self._name} performs a follow-up attack")
                if unitTarget.takeDMG(attack, self._weapon["type"], False):
                    # Stop combat if the target dies
                    return
            else: write(f"The {self._name}'s attack missed")

    def calculateAttack(self):
        """Get the attack value."""
        attack: int = self._weapon["MT"]
        if self._weapon["type"] == "STR": attack += self._stats["STR"]
        elif self._weapon["type"] == "MAG": attack += self._stats["MAG"]

        return attack

    def calculateHit(self, unitTarget):
        """Determine if the attack lands"""
        accuracy = self.calculateAccuracy(unitTarget)

    def calculateAccuracy(self, unitTarget):
        """Get the attack accuracy."""
        hitRate: int = (self._stats["SKL"] * 2) + self._weapon["HIT"]
        evade: int = unitTarget.getSpd()

        return hitRate - evade

    def getRngInUse(self, unitTarget):
        return [manhattan_dist(self.getTile(), unitTarget.getTile())]

    def takeDMG(self, DMG, damageType, heal):
        """Handle taking damage."""
        if heal:
            self._stats["HP"] += DMG
            write(f"{DMG} health healed")
            # Prevent excess HP via healing
            if self._stats["HP"] > self._stats["MaxHP"]:
                self._stats["HP"] = self._stats["MaxHP"]
            return True
        else:
            if damageType == "STR":
                leftoverDMG = DMG - self._stats["DEF"]
                if leftoverDMG >= 0: self._stats["HP"] -= leftoverDMG
                else: leftoverDMG = 0
            elif damageType == "MAG":
                leftoverDMG = DMG - self._stats["RES"]
                if leftoverDMG >= 0: self._stats["HP"] -= leftoverDMG
                else: leftoverDMG = 0
            write(f"{leftoverDMG} damage done")
            if self._stats["HP"] <= 0:
                return self.die()
        
        return False
        
    def die(self):
        i, j = self._tile
        # Remove self from map
        levelMap[i][j] = '_'
        self._dead = True
        write(f"The {self._name} died")

        return True
