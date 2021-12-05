#from abc import abstractmethod
from . import weaponClass as wc

class BaseCharacter():
    def __init__(self) :
        self.level = 1

        self.baseStats = dict()
        #self.statIncreases = list() #Liste de dictionnaires taille max 90
        self.statsAtLevel = dict() #dict de listes

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

    def getStatAtLevel(self, level) -> dict:
        if level > 90:
            level = 90
        elif level < 1:
            level = 0

        ret = dict()
        ret["hp"] = self.statsAtLevel["hp"][level-1]
        ret["atk"] = self.statsAtLevel["atk"][level-1]
        ret["def"] = self.statsAtLevel["def"][level-1]
        ret["crit rate"] = self.statsAtLevel["crit rate"][level-1]
        ret["crit dmg"] = self.statsAtLevel["crit dmg"][level-1]

        return ret

    def getStats(self) -> dict:
        return self.getStatsAtLevel(self, self.level)