from ..CharacterCreation.EnemyUnit import EnemyUnit

class Troubadour(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Troubadour"

    def setTraits(self):
        self._stats["HP"] = 15
        self._stats["MAG"] = 1
        self._stats["DEF"] = 2
        self._stats["RES"] = 5
        self._stats["SPD"] = 3
        self._stats["SKL"] = 1
        self._stats["MOV"] = 7

        self._growthRates["HP_Growth"] = 0.50
        self._growthRates["MAG_Growth"] = 0.25
        self._growthRates["DEF_Growth"] = 0.12
        self._growthRates["RES_Growth"] = 0.40
        self._growthRates["SPD_Growth"] = 0.55
        self._growthRates["SKL_Growth"] = 0.35