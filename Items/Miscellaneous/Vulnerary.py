class Vulnerary:
    def __init__(self):
        self.name = "Vulnerary"
        self.HP_restore = 10

    def getName(self):
        return self.name

    def useItem(self, health: int):
        return health + self.HP_restore
