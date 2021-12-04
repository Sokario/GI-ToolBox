from characterClass import *

class Itto(BaseCharacter):
    def __init__(self):
        super().__init__()

        baseStats = dict()
        baseStats["hp"] = 1001
        baseStats["atk"] = 18
        baseStats["def"] = 75
        baseStats["crit rate"] = 0.05
        baseStats["crit dmg"] = 0.5
        self.baseStats = baseStats

        statIncreases = [dict() for i in range(89)]

        self.statIncreases = statIncreases
        #TODO
