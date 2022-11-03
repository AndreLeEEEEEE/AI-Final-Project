from ..CharacterCreation.PlayerUnit import PlayerUnit
from ..Items.Weapons.Lance import Lance
from ..Items.Weapons.Sword import Sword


class Kent(PlayerUnit):
    def __init__(self):
        PlayerUnit.__init__(self)
        self._class = "Cavalier"
        self.starting_items = [Lance(), Sword()]

    def setTraits(self):
        self._stats["HP"] = 20
        self._stats["STR"] = 6
        self._stats["DEF"] = 5
        self._stats["RES"] = 1
        self._stats["SPD"] = 7
        self._stats["SKL"] = 6
        self._stats["MOV"] = 5

        self._growthRates["HP_Growth"] = 0.85
        self._growthRates["STR_Growth"] = 0.40
        self._growthRates["DEF_Growth"] = 0.25
        self._growthRates["RES_Growth"] = 0.25
        self._growthRates["SPD_Growth"] = 0.45
        self._growthRates["SKL_Growth"] = 0.50
