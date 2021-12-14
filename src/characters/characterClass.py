import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from src.weapons import weaponClass as wc

class BaseCharacter():
    def __init__(self) :
        self._name = str()
        
        #Graphics used for interfaces
        self._pictures = {
            "portrait"      : None,
            "banner"        : None,
            "abilities"     : [None, None, None],
            "passives"      : [None, None, None],
            "constellations": [None, None, None, None, None, None]
            }

        self._rarity = 4
        self._level = 1

        #self.baseStats = dict()
        #self.statIncreases = list() #Liste de dictionnaires taille max 90
        self._baseStats = {
            "Health"                : [0 for _ in range(90)], # x90
            "Attack"                : [0 for _ in range(90)], # x90
            "Defense"               : [0 for _ in range(90)], # x90
            "Critical Rate"         : [0 for _ in range(90)], # x90
            "Critical Damage"       : [0 for _ in range(90)], # x90
            "Energy Mastery"        : [0 for _ in range(90)], # x90
            "Energy Recharge"       : [0 for _ in range(90)], # x90
            "Physical Damage"       : [0 for _ in range(90)], # x90
            "Physical Resistance"   : [0 for _ in range(90)], # x90
            "Geo Damage"            : [0 for _ in range(90)], # x90
            "Geo Resistance"        : [0 for _ in range(90)], # x90
            "Pyro Damage"           : [0 for _ in range(90)], # x90
            "Pyro Resistance"       : [0 for _ in range(90)], # x90
            "Cryo Damage"           : [0 for _ in range(90)], # x90
            "Cryo Resistance"       : [0 for _ in range(90)], # x90
            "Hydro Damage"          : [0 for _ in range(90)], # x90
            "Hydro Resistance"      : [0 for _ in range(90)], # x90
            "Anemo Damage"          : [0 for _ in range(90)], # x90
            "Anemo Resistance"      : [0 for _ in range(90)], # x90
            "Dendro Damage"         : [0 for _ in range(90)], # x90
            "Dendro Resistance"     : [0 for _ in range(90)], # x90
            "Electro Damage"        : [0 for _ in range(90)], # x90
            "Electro Resistance"    : [0 for _ in range(90)], # x90
        }

        self.attackSpeed = 0
        self.chargedAttackSpeed = 0
        
        self.baseAbilities = dict() #champs : basicAttack; elementalAbility; elementalBurst
        self.abilityIncreases = list();

        self.constellation = list()
        self.artifacts = dict() #unused for now
        self.weapon = wc.BaseWeapon("none", "none") #weapon instance

        self.levelMaterials     = list()
        self.ascensionMaterials = list()
        self.abilityMaterials   = list()

        pass

    # Name property
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    # Pictures property
    @property
    def portrait(self) -> str:
        return self._pictures["portrait"]

    @portrait.setter
    def portrait(self, value: str):
        self._pictures["portrait"] = value

    @property
    def banner(self) -> str:
        return self._pictures["banner"]

    @banner.setter
    def banner(self, value: str):
        self._pictures["banner"] = value

    @property
    def abilities(self) -> list:
        return self._pictures["abilities"]

    @abilities.setter
    def abilities(self, values: tuple([int, int, int])):
        self._pictures["abilities"] = values

    @property
    def passives(self):
        return self._pictures["passives"]

    @passives.setter
    def passives(self, values):
        self._pictures["passives"] = values

    @property
    def constellations(self):
        return self._pictures["constellations"]

    @constellations.setter
    def constellations(self, values):
        self._pictures["constellations"] = values
    
    # Rarity property
    @property
    def rarity(self) -> int:
        return self._rarity

    @rarity.setter
    def rarity(self, value: int):
        assert (value >= 4), "Character rarity can't < 4"
        self._rarity = value

    # Level property
    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        assert (1 <= value <= 90), "Character level need to be between 1 and 90"
        self._level = value

    # BaseStats property
    @property
    def health(self) -> int:
        return self._baseStats["Health"][self._level - 1]

    @health.setter
    def health(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Health"][level - 1] = value

    @property
    def attack(self) -> int:
        return self._baseStats["Attack"][self._level - 1]

    @attack.setter
    def attack(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Attack"][level - 1] = value

    @property
    def defense(self) -> int:
        return self._baseStats["Defense"][self._level - 1]

    @defense.setter
    def defense(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Defense"][level - 1] = value

    @property
    def rCrit(self) -> int:
        return self._baseStats["Critical Rate"][self._level - 1]

    @rCrit.setter
    def rCrit(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Critical Rate"][level - 1] = value
    
    @property
    def dCrit(self) -> int:
        return self._baseStats["Critical Damage"][self._level - 1]

    @dCrit.setter
    def dCrit(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Critical Damage"][level - 1] = value

    @property
    def mEnergy(self) -> int:
        return self._baseStats["Energy Mastery"][self._level - 1]

    @mEnergy.setter
    def mEnergy(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Energy Mastery"][level - 1] = value

    @property
    def rEnergy(self) -> int:
        return self._baseStats["Energy Recharge"][self._level - 1]

    @rEnergy.setter
    def rEnergy(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Energy Recharge"][level - 1] = value

    @property
    def dPhy(self) -> int:
        return self._baseStats["Physical Damage"][self._level - 1]

    @dPhy.setter
    def dPhy(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Physical Damage"][level - 1] = value

    @property
    def rPhy(self) -> int:
        return self._baseStats["Physical Resistance"][self._level - 1]

    @rPhy.setter
    def rPhy(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Physical Resistance"][level - 1] = value
    
    @property
    def dGeo(self) -> int:
        return self._baseStats["Geo Damage"][self._level - 1]

    @dGeo.setter
    def dGeo(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Geo Damage"][level - 1] = value

    @property
    def rGeo(self) -> int:
        return self._baseStats["Geo Resistance"][self._level - 1]

    @rGeo.setter
    def rGeo(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Geo Resistance"][level - 1] = value

    @property
    def dPyro(self) -> int:
        return self._baseStats["Pyro Damage"][self._level - 1]

    @dPyro.setter
    def dPyro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Pyro Damage"][level - 1] = value

    @property
    def rPyro(self) -> int:
        return self._baseStats["Pyro Resistance"][self._level - 1]

    @rPyro.setter
    def rPyro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Pyro Resistance"][level - 1] = value

    @property
    def dCryo(self) -> int:
        return self._baseStats["Cryo Damage"][self._level - 1]

    @dCryo.setter
    def dCryo(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Cryo Damage"][level - 1] = value

    @property
    def rCryo(self) -> int:
        return self._baseStats["Cryo Resistance"][self._level - 1]

    @rCryo.setter
    def rCryo(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Cryo Resistance"][level - 1] = value

    @property
    def dHydro(self) -> int:
        return self._baseStats["Hydro Damage"][self._level - 1]

    @dHydro.setter
    def dHydro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Hydro Damage"][level - 1] = value

    @property
    def rHydro(self) -> int:
        return self._baseStats["Hydro Resistance"][self._level - 1]

    @rHydro.setter
    def rHydro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Hydro Resistance"][level - 1] = value

    @property
    def dAnemo(self) -> int:
        return self._baseStats["Anemo Damage"][self._level - 1]

    @dAnemo.setter
    def dAnemo(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Anemo Damage"][level - 1] = value

    @property
    def rAnemo(self) -> int:
        return self._baseStats["Anemo Resistance"][self._level - 1]

    @rAnemo.setter
    def rAnemo(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Anemo Resistance"][level - 1] = value

    @property
    def dDendro(self) -> int:
        return self._baseStats["Dendro Damage"][self._level - 1]

    @dDendro.setter
    def dDendro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Dendro Damage"][level - 1] = value

    @property
    def rDendro(self) -> int:
        return self._baseStats["Geo Resistance"][self._level - 1]

    @rDendro.setter
    def rDendro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Dendro Resistance"][level - 1] = value

    @property
    def dElectro(self) -> int:
        return self._baseStats["Electro Damage"][self._level - 1]

    @dElectro.setter
    def dElectro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Electro Damage"][level - 1] = value

    @property
    def rElectro(self) -> int:
        return self._baseStats["Geo Resistance"][self._level - 1]

    @rElectro.setter
    def rElectro(self, value: int, level: int = 0):
        assert (0 <= value <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        self._baseStats["Geo Resistance"][level - 1] = value

    #Global baseStats property
    @property
    def stats(self) -> dict:
        return self._baseStats

    @property
    def baseStats(self, level: int = 0) -> dict:
        print(level)
        assert (0 <= level <= 90), "Character level need to be between 1 and 90"
        level = level if level != 0 else self._level
        print(level)
        for key in self._baseStats.keys():
            print(len(self._baseStats[key]))
        return {key: self._baseStats[key][level - 1] for key in self._baseStats.keys()}
