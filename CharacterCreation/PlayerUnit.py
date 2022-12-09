from PlayerUnits.Hector import Hector
from PlayerUnits.Kent import Kent
from PlayerUnits.Nino import Nino
from PlayerUnits.Rebecca import Rebecca
from PlayerUnits.Sain import Sain
from PlayerUnits.Serra import Serra
from Maps.testMapThree import testMapThree as levelMap
from Algorithms.BFS import *
from Algorithms.Astar import moveTowardsTarget
from Algorithms.Astar import manhattan_dist
from Algorithms.Translate import translate
from Results.Write import write
import random

characters = {
    "Hector": Hector(),
    "Kent": Kent(),
    "Nino": Nino(),
    "Rebecca": Rebecca(),
    "Sain": Sain(),
    "Serra": Serra(),
}

class PlayerUnit:
    def __init__(self, chr, level):
        self._name = chr
        # Is string
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
        self._type = characters[chr].type
        # self._state handled here
        if characters[chr].type == "Offensive":
            self._state = "aggro"
        else:
            self._state = "heal"
        self._weapon = characters[chr].starting_items[0]
        self._item = characters[chr].starting_items[1]
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

    def getClass(self):
        return self._class

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

    def startTurn(self):
        if self._stats["HP"] <= (self._stats["MaxHP"]/2):
            write(f"{self._name} is retreating")
            self._state = "retreat"
            # Fall back to retreat tile
            newPosition = moveTowardsTarget(levelMap, self._tile, 
                                            (6, 7), self._stats["MOV"])
            write(f"{self._name} moved from {translate(self._tile)} to {translate(newPosition)}")
            levelMap[self._tile[0]][self._tile[1]] = '_'
            self.setTile(newPosition)
            levelMap[newPosition[0]][newPosition[1]] = self
            # Use healing item if still available
            if self._item["Uses"] > 0:
                write(f"{self._name} used their vulnerary")
                self._stats["HP"] += self._item["HP"]
                # Don't go over the unit's max HP
                if self._stats["HP"] > self._stats["MaxHP"]:
                    self._stats["HP"] = self._stats["MaxHP"]
                self._item["Uses"] -=1
        elif self._type == "Offensive":
            self._state = "aggro"
            self.moveToTarget(2)
        # Type is support
        else:
            self._state = "heal"
            self.moveToTarget(1)

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
            write(f"{self._name} attacks the {unitTarget._name}")
        else:
            write(f"{self._name} heals {unitTarget._name}")
        if random.randrange(1, 101) < self.calculateAccuracy(unitTarget):
            heal = False if self._weapon["offense"] else True
            if unitTarget.takeDMG(attack, self._weapon["type"], heal):
                # Stop combat if the target dies
                return
        else: write(f"{self._name}'s attack missed")
        # Counterattack
        # Support units cannot defend themselves
        # Don't trigger a counterattack when healing
        # Only triggers if the target unit can attack at the used RNG
        if (unitTarget.getType() == "Offensive" 
            and self._type == "Offensive"
            and set(unitTarget.getRng()) & set(self.getRngInUse(unitTarget))):
            write(f"The {unitTarget._name} counterattacks")
            if random.randrange(1, 101) < unitTarget.calculateAccuracy(self):
                if self.takeDMG(unitTarget.calculateAttack(), unitTarget._weapon["type"], False):
                    # Stop combat if the unit dies
                    return
            else: write(f"The {unitTarget._name}'s attack missed")
        # Follow-up attack
        # Do not make a follow-up attack for healing
        if spdDiff >= 4 and self._type == "Offensive":
            if random.randrange(1, 101) < self.calculateAccuracy(unitTarget):
                write(f"{self._name} performs a follow-up attack")
                if unitTarget.takeDMG(attack, self._weapon["type"], False):
                    # Stop combat if the target dies
                    return
            else: write(f"{self._name}'s attack missed")

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
        write(f"{self._name} died")

        return True
        