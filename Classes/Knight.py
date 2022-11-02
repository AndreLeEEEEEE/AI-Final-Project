from ..CharacterCreation.EnemyUnit import EnemyUnit

class Knight(EnemyUnit):
    def __init__(self):
        EnemyUnit.__init__(self)
        self._class = "Knight"
        
    def setTraits(self):
        self._stats["HP"] = 17
        self._stats["STR"] = 5
        self._stats["DEF"] = 9
        self._stats["RES"] = 0
        self._stats["SPD"] = 0
        self._stats["SKL"] = 2
        self._stats["MOV"] = 4

        self._growthRates["HP_Growth"] = 0.80
        self._growthRates["STR_Growth"] = 0.40
        self._growthRates["DEF_Growth"] = 0.28
        self._growthRates["RES_Growth"] = 0.20
        self._growthRates["SPD_Growth"] = 0.15
        self._growthRates["SKL_Growth"] = 0.30
