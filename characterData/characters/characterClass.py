#from abc import abstractmethod
from . import weaponClass as wc

class BaseCharacter():
    def __init__(self) :
        self.level = 1

        self.baseStats = dict()
        self.statIncreases = list() #Liste de dictionnaires taille max 90

        self.attackSpeed = 0
        self.chargedAttackSpeed = 0
        
        self.baseAbilities = dict() #champs : basicAttack; elementalAbility; elementalBurst
        self.abilityIncreases = list();

        self.passives = list() #length = 3; liste de dict contenant notemment la condition d'unlock

        self.constellation = list()
        self.artifacts = dict() #unused for now
        self.weapon = wc.BaseWeapon("none", "none") #weapon instance

        self.ascensionMaterials = list()
        self.abilityMaterials   = list()

        pass

    def getStatsAtLevel(self, level):
        if level > 90:
            level = 90
        elif level < 1:
            level = 0

        ret = dict()
        ret["hp"] = self.baseStats["hp"]
        ret["atk"] = self.baseStats["atk"]
        ret["def"] = self.baseStats["def"]
        ret["crit rate"] = self.baseStats["crit rate"]
        ret["crit dmg"] = self.baseStats["crit dmg"]

        for i in range(1,level):
            ret["hp"] += self.statIncreases[i-1]["hp"]
            ret["atk"] += self.statIncreases[i-1]["atk"]
            ret["def"] += self.statIncreases[i-1]["def"]
            ret["crit rate"] += self.statIncreases[i-1]["crit rate"]
            ret["crit dmg"] += self.statIncreases[i-1]["crit dmg"]

        return ret

    def getStats(self):
        return self.getStatsAtLevel(self, self.level)

    def set_statIncreases(self, hpIncreases, atkIncreases, defIncreases, critRateIncreases, critDmgIncreases):
        self.statIncreases = [
            {
                "hp" : hpIncreases[i],
                "atk" : atkIncreases[i],
                "def" : defIncreases[i],
                "crit rate" : critRateIncreases[i],
                "crit dmg" : critDmgIncreases[i],
            }
            for i in range(89)
        ]