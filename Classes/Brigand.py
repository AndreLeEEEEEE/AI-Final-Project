from ..CharacterCreation.EnemyUnit import EnemyUnit

class Brigand(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Brigand"

    def setTraits(self):
        self._stats["HP"] = 20
        self._stats["STR"] = 5
        self._stats["DEF"] = 3
        self._stats["RES"] = 0
        self._stats["SPD"] = 5
        self._stats["SKL"] = 1
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.82
        self._growthRates["STR_Growth"] = 0.50
        self._growthRates["DEF_Growth"] = 0.10
        self._growthRates["RES_Growth"] = 0.13
        self._growthRates["SPD_Growth"] = 0.20
        self._growthRates["SKL_Growth"] = 0.30