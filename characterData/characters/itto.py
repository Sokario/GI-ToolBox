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
        statIncreases[0:19]  = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[20]    = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[21:39] = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[40]    = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[41:49] = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[50]    = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[51:59] = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[60]    = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[61:69] = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[70:79] = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[80]    = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        statIncreases[81:89] = {"hp" : 0, "atk" : 0, "def" : 0, "crit rate" : 0, "crit dmg" : 0}
        self.statIncreases = statIncreases

        
        #TODO
