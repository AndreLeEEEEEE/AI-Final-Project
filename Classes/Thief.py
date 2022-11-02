from ..CharacterCreation.EnemyUnit import EnemyUnit

class Thief(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Thief"

    def setTraits(self):
        self._stats["HP"] = 16
        self._stats["STR"] = 3
        self._stats["DEF"] = 2
        self._stats["RES"] = 0
        self._stats["SPD"] = 9
        self._stats["SKL"] = 1
        self._stats["MOV"] = 6

        self._growthRates["HP_Growth"] = 0.50
        self._growthRates["STR_Growth"] = 0.05
        self._growthRates["DEF_Growth"] = 0.05
        self._growthRates["RES_Growth"] = 0.25
        self._growthRates["SPD_Growth"] = 0.40
        self._growthRates["SKL_Growth"] = 0.45