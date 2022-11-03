from ..CharacterCreation.PlayerUnit import PlayerUnit
from ..Items.Weapons.Wolf_Beil import Wolf_Beil
from ..Items.Miscellaneous.Vulnerary import Vulnerary

class Hector(PlayerUnit):
    def __init__(self):
        PlayerUnit.__init__(self)
        self._class = "Lord"
        self.starting_items = [Wolf_Beil(), Vulnerary()]

    def setTraits(self):
        self._stats["HP"] = 19
        self._stats["STR"] = 7
        self._stats["DEF"] = 8
        self._stats["RES"] = 0
        self._stats["SPD"] = 5
        self._stats["SKL"] = 4
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.80
        self._growthRates["STR_Growth"] = 0.45
        self._growthRates["DEF_Growth"] = 0.30
        self._growthRates["RES_Growth"] = 0.35
        self._growthRates["SPD_Growth"] = 0.40
        self._growthRates["SKL_Growth"] = 0.50
