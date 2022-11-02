from ..CharacterCreation.EnemyUnit import EnemyUnit

class Soldier(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Soldier"

    def setTraits(self):
        self._stats["HP"] = 20
        self._stats["STR"] = 3
        self._stats["DEF"] = 0
        self._stats["RES"] = 0
        self._stats["SPD"] = 1
        self._stats["SKL"] = 0
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.80
        self._growthRates["STR_Growth"] = 0.50
        self._growthRates["DEF_Growth"] = 0.12
        self._growthRates["RES_Growth"] = 0.15
        self._growthRates["SPD_Growth"] = 0.20
        self._growthRates["SKL_Growth"] = 0.30