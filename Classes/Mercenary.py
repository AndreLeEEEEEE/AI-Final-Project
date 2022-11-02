from ..CharacterCreation.EnemyUnit import EnemyUnit

class Mercenary(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Mercenary"

    def setTraits(self):
        self._stats["HP"] = 18
        self._stats["STR"] = 4
        self._stats["DEF"] = 4
        self._stats["RES"] = 0
        self._stats["SPD"] = 8
        self._stats["SKL"] = 8
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.80
        self._growthRates["STR_Growth"] = 0.40
        self._growthRates["DEF_Growth"] = 0.18
        self._growthRates["RES_Growth"] = 0.20
        self._growthRates["SPD_Growth"] = 0.32
        self._growthRates["SKL_Growth"] = 0.40
