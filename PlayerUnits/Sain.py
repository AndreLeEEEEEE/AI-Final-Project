from ..CharacterCreation.PlayerUnit import PlayerUnit
from ..Items.Weapons.Lance import Lance
from ..Items.Weapons.Sword import Sword


class Sain(PlayerUnit):
    def __init__(self):
        PlayerUnit.__init__(self)
        self._class = "Cavalier"
        self.starting_items = [Lance(), Sword()]

    def setTraits(self):
        self._stats["HP"] = 19
        self._stats["STR"] = 8
        self._stats["DEF"] = 6
        self._stats["RES"] = 0
        self._stats["SPD"] = 6
        self._stats["SKL"] = 4
        self._stats["MOV"] = 7

        self._growthRates["HP_Growth"] = 0.80
        self._growthRates["STR_Growth"] = 0.60
        self._growthRates["DEF_Growth"] = 0.20
        self._growthRates["RES_Growth"] = 0.20
        self._growthRates["SPD_Growth"] = 0.40
        self._growthRates["SKL_Growth"] = 0.35
