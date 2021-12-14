import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from src.weapons import weaponClass as wc

class BaseCharacter():
    def __init__(self) :
        self.name = str()
        
        #Graphics used for interfaces
        self.pictures = {
            "portrait"      : None,
            "banner"        : None,
            "abilities"     : [None, None, None],
            "passives"      : [None, None, None],
            "constellations": [None, None, None, None, None, None]
            }

        self.rarity = 4
        self.level = 1

        #self.baseStats = dict()
        #self.statIncreases = list() #Liste de dictionnaires taille max 90
        self.statsAtLevel = {
            "Health Points"     : [0 for _ in range(90)], # x90
            "Attack"            : [0 for _ in range(90)], # x90
            "Defense"           : [0 for _ in range(90)], # x90
            "Critical Rate"     : [0 for _ in range(90)], # x90
            "Critical Damage"   : [0 for _ in range(90)], # x90
            "Energy Mastery"    : [0 for _ in range(90)], # x90
            "Energy Recharge"   : [0 for _ in range(90)], # x90
            "Physical Damage"   : [0 for _ in range(90)], # x90
            "Physical Resitance": [0 for _ in range(90)], # x90
            "Geo Damage"        : [0 for _ in range(90)], # x90
            "Geo Resitance"     : [0 for _ in range(90)], # x90
            "Pyro Damage"       : [0 for _ in range(90)], # x90
            "Pyro Resitance"    : [0 for _ in range(90)], # x90
            "Cryo Damage"       : [0 for _ in range(90)], # x90
            "Cryo Resitance"    : [0 for _ in range(90)], # x90
            "Hydro Damage"      : [0 for _ in range(90)], # x90
            "Hydro Resitance"   : [0 for _ in range(90)], # x90
            "Anemo Damage"      : [0 for _ in range(90)], # x90
            "Anemo Resitance"   : [0 for _ in range(90)], # x90
            "Dendro Damage"     : [0 for _ in range(90)], # x90
            "Dendro Resitance"  : [0 for _ in range(90)], # x90
            "Electro Damage"    : [0 for _ in range(90)], # x90
            "Electro Resitance" : [0 for _ in range(90)], # x90
        }

        self.attackSpeed = 0
        self.chargedAttackSpeed = 0
        
        self.baseAbilities = dict() #champs : basicAttack; elementalAbility; elementalBurst
        self.abilityIncreases = list();

        self.passives = list() #length = 3; liste de dict contenant notemment la condition d'unlock

        self.constellation = list()
        self.artifacts = dict() #unused for now
        self.weapon = wc.BaseWeapon("none", "none") #weapon instance

        self.levelMaterials     = list()
        self.ascensionMaterials = list()
        self.abilityMaterials   = list()

        pass

    def getStatAtLevel(self, level) -> dict:
        if level > 90:
            level = 90
        elif level < 1:
            level = 1

        ret = dict()
        ret["hp"] = self.statsAtLevel["hp"][level-1]
        ret["atk"] = self.statsAtLevel["atk"][level-1]
        ret["def"] = self.statsAtLevel["def"][level-1]
        ret["crit rate"] = self.statsAtLevel["crit rate"][level-1]
        ret["crit dmg"] = self.statsAtLevel["crit dmg"][level-1]

        return ret

    def getStats(self) -> dict:
        return self.getStatsAtLevel(self, self.level)