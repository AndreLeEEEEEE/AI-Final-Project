from PlayerUnits.Eliwood import Eliwood
from PlayerUnits.Hector import Hector
from PlayerUnits.Kent import Kent
from PlayerUnits.Sain import Sain
from PlayerUnits.Serra import Serra
from Maps.testMapTwo import testMapTwo as levelMap
from Algorithms.BFS import *
from Algorithms.Astar import moveTowardsTarget
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
        # self._state handled here
        if characters[chr].type == "Offensive":
            self._state = "aggro"
        else:
            self._state = "heal"
        self._weapon = characters[chr].starting_items[0]
        self._item = characters[chr].starting_items[0]
        self._tile = (0, 0)

    def get_id(self):
        return self._id

    def get_side(self):
        return self._side

    def getTile(self):
        return self._tile

    def setTile(self, tile: tuple):
        self._tile = tile

    def getSpd(self):
        return self._stats["SPD"]

    def getDR(self, damageType):
        if damageType == "STR": return self._stats["DEF"]
        elif damageType == "MAG": return self._stats["RES"]

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
            self._state = "retreat"
            # Insert code to move away from enemy
            # Use healing item if still available
            if self._item["Uses"] > 0:
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
        result = BFS(levelMap, self._tile, target, self._weapon["RNG"], self._side)
        if result:
            moveTowardsTarget(levelMap, self._tile, target, self._stats["MOV"])
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
        if random.randrange(1, 101) < self.calculateAccuracy(unitTarget):
            heal = False if self._weapon["offense"] else True
            if unitTarget.takeDMG(attack, self._weapon["type"], heal):
                # Stop combat if the target dies
                return
        # Counterattack
        # Only triggers if the target unit can counter attack
        # Support units cannot defend themselves
        if unitTarget.getType() == "Support": return
        # Units ranges have to be equal to counterattack
        if set(unitTarget.getRng()) & set(self.getRng()):
            if random.randrange(1, 101) < unitTarget.calculateAccuracy(self):
                heal = False if unitTarget._weapon["offense"] else True
                if self.takeDMG(unitTarget.calculateAttack(), unitTarget._weapon["type"], heal):
                    # Stop combat if the unit dies
                    return
        # Follow-up attack
        if spdDiff >= 4:
            if random.randrange(1, 101) < self.calculateAccuracy(unitTarget):
                heal = False if self._weapon["offense"] else True
                if unitTarget.takeDMG(attack, self._weapon["type"], heal):
                    # Stop combat if the target dies
                    return

    def calculateAttack(self):
        """Get the attack value."""
        attack: int = self._weapon["MT"]
        if self._weapon["type"] == "STR": attack += self._stats["STR"]
        elif self._weapon["type"] == "MAG": attack += self._stats["MAG"]
        # If weapon is a stave
        if not self._weapon["offense"]: attack *= -1

        return attack

    def calculateHit(self, unitTarget):
        """Determine if the attack lands"""
        accuracy = self.calculateAccuracy(unitTarget)

    def calculateAccuracy(self, unitTarget):
        """Get the attack accuracy."""
        hitRate: int = (self._stats["SKL"] * 2) + self._weapon["HIT"]
        evade: int = unitTarget.getSpd()

        return hitRate - evade

    def takeDMG(self, DMG, damageType, heal):
        """Handle taking damage."""
        if heal:
            self._stats["HP"] -= DMG
            # Prevent excess HP via healing
            if self._stats["HP"] > self._stats["MaxHP"]:
                self._stats["HP"] = self._stats["MaxHP"]
            return True
        else:
            if damageType == "STR":
                mitigate = DMG - self._stats["DEF"]
                if mitigate >= 0:
                    self._stats["HP"] -= mitigate
            elif damageType == "MAG":
                mitigate = DMG - self._stats["RES"]
                if mitigate >= 0:
                    self._stats["HP"] -= mitigate
            if self._stats["HP"] <= 0:
                return self.die(self)
        
        return False
        
    def die(self):
        i, j = self._tile
        levelMap[i][j] = '_'

        return True
        
