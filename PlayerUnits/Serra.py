from ..CharacterCreation.PlayerUnit import PlayerUnit
from ..Items.Weapons.Stave import Stave
from ..Items.Miscellaneous.Vulnerary import Vulnerary


class Serra(PlayerUnit):
    def __init__(self):
        PlayerUnit.__init__(self)
        self._class = "Cleric"
        self.starting_items = [Stave(), Vulnerary()]

    def setTraits(self):
        self._stats["HP"] = 17
        self._stats["STR"] = 2
        self._stats["DEF"] = 2
        self._stats["RES"] = 5
        self._stats["SPD"] = 8
        self._stats["SKL"] = 5
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.50
        self._growthRates["STR_Growth"] = 0.50
        self._growthRates["DEF_Growth"] = 0.15
        self._growthRates["RES_Growth"] = 0.55
        self._growthRates["SPD_Growth"] = 0.40
        self._growthRates["SKL_Growth"] = 0.30
