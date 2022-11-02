from ..CharacterCreation.EnemyUnit import EnemyUnit

class Monk(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Monk"

    def setTraits(self):
        self._stats["HP"] = 18
        self._stats["MAG"] = 1
        self._stats["DEF"] = 1
        self._stats["RES"] = 5
        self._stats["SPD"] = 2
        self._stats["SKL"] = 1
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.50
        self._growthRates["MAG_Growth"] = 0.30
        self._growthRates["DEF_Growth"] = 0.08
        self._growthRates["RES_Growth"] = 0.40
        self._growthRates["SPD_Growth"] = 0.32
        self._growthRates["SKL_Growth"] = 0.35