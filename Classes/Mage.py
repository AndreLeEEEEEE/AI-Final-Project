from ..CharacterCreation.EnemyUnit import EnemyUnit

class Mage(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Mage"

    def setTraits(self):
        self._stats["HP"] = 16
        self._stats["MAG"] = 1
        self._stats["DEF"] = 3
        self._stats["RES"] = 3
        self._stats["SPD"] = 3
        self._stats["SKL"] = 2
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.55
        self._growthRates["MAG_Growth"] = 0.55
        self._growthRates["DEF_Growth"] = 0.05
        self._growthRates["RES_Growth"] = 0.30
        self._growthRates["SPD_Growth"] = 0.35
        self._growthRates["SKL_Growth"] = 0.40
