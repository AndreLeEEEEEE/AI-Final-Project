from ..CharacterCreation.EnemyUnit import EnemyUnit

class Cavalier(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Cavalier"

    def setTraits(self):
        self._stats["HP"] = 20
        self._stats["STR"] = 5
        self._stats["DEF"] = 6
        self._stats["RES"] = 0
        self._stats["SPD"] = 5
        self._stats["SKL"] = 2
        self._stats["MOV"] = 7

        self._growthRates["HP_Growth"] = 0.75
        self._growthRates["STR_Growth"] = 0.35
        self._growthRates["DEF_Growth"] = 0.15
        self._growthRates["RES_Growth"] = 0.12
        self._growthRates["SPD_Growth"] = 0.28
        self._growthRates["SKL_Growth"] = 0.40
