#from abc import abstractmethod

class BaseCharacter():
    def __init__(self) :
        self.level = 1

        self.baseStats = dict()
        self.statIncreases = list() #Liste de dictionnaires taille max 90
        
        self.baseAbilities = dict() #champs : basicAttack; elementalAbility; elementalBurst
        self.abilityIncreases = list();

        self.passives = list() #length = 3; liste de dict contenant notemment la condition d'unlock

        self.constellation = list()
        self.artifacts = dict() #unused for now
        self.weaponType = Weapon() #weapon instance

        self.ascensionMaterials = list()
        self.abilityMaterials   = list()

        pass


    def getStatsAtLevel(self, level):

        pass


    def getStats(self):
        return self.getStatsAtLevel(self, self.level)