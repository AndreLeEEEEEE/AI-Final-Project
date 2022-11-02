from ..CharacterCreation.EnemyUnit import EnemyUnit

class Pirate(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Pirate"

    def setTraits(self):
        self._stats["HP"] = 19
        self._stats["STR"] = 4
        self._stats["DEF"] = 3
        self._stats["RES"] = 0
        self._stats["SPD"] = 6
        self._stats["SKL"] = 2
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.75
        self._growthRates["STR_Growth"] = 0.50
        self._growthRates["DEF_Growth"] = 0.10
        self._growthRates["RES_Growth"] = 0.13
        self._growthRates["SPD_Growth"] = 0.25
        self._growthRates["SKL_Growth"] = 0.35
