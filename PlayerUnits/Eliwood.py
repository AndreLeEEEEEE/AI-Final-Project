from CharacterCreation.PlayerUnit import PlayerUnit
from Items.Weapons.Rapier import Rapier
from Items.Miscellaneous.Vulnerary import Vulnerary

class Eliwood(PlayerUnit):
    def __init__(self):
        PlayerUnit.__init__(self)
        self._class = "Lord"
        self.starting_items = [Rapier(), Vulnerary()]

    def setTraits(self):
        self._stats["HP"] = 18
        self._stats["STR"] = 5
        self._stats["DEF"] = 5
        self._stats["RES"] = 0
        self._stats["SPD"] = 7
        self._stats["SKL"] = 5
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.80
        self._growthRates["STR_Growth"] = 0.45
        self._growthRates["DEF_Growth"] = 0.30
        self._growthRates["RES_Growth"] = 0.35
        self._growthRates["SPD_Growth"] = 0.40
        self._growthRates["SKL_Growth"] = 0.50
