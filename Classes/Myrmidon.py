from ..CharacterCreation.EnemyUnit import EnemyUnit

class Myrmidon(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Myrmidon"

    def setTraits(self):
        self._stats["HP"] = 16
        self._stats["STR"] = 4
        self._stats["DEF"] = 2
        self._stats["RES"] = 0
        self._stats["SPD"] = 9
        self._stats["SKL"] = 9
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.70
        self._growthRates["STR_Growth"] = 0.35
        self._growthRates["DEF_Growth"] = 0.15
        self._growthRates["RES_Growth"] = 0.20
        self._growthRates["SPD_Growth"] = 0.40
        self._growthRates["SKL_Growth"] = 0.40
