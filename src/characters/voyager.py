import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from src.characters.characterClass import BaseCharacter

class Voyager(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Voyager"
        
        #Graphics used for interfaces
        self.pictures["portrait"]           = "voyager.png"
        self.pictures["banner"]             = "voyager_party.png"
        self.pictures["abilities"][0]       = "sword.png"
        self.pictures["abilities"][1]       = "sword.png"
        self.pictures["abilities"][2]       = "sword.png"
        self.pictures["passives"][0]        = "sword.png"
        self.pictures["passives"][1]        = "sword.png"
        self.pictures["passives"][2]        = "sword.png"
        self.pictures["constellations"][0]  = "sword.png"
        self.pictures["constellations"][1]  = "sword.png"
        self.pictures["constellations"][2]  = "sword.png"
        self.pictures["constellations"][3]  = "sword.png"
        self.pictures["constellations"][4]  = "sword.png"
        self.pictures["constellations"][5]  = "sword.png"

        #Enregistrement des statistiques au niveau 1
        self.rarity = 5
        baseStats = dict()
        baseStats["hp"] = 1001
        baseStats["atk"] = 18
        baseStats["def"] = 75
        baseStats["crit rate"] = 0.05
        baseStats["crit dmg"] = 0.5
        self.baseStats = baseStats

        #Enregistrement des increases au niveau de personnage i+1 (0 au rang 0)

        hpIncreases = [1001 for _ in range(89)]
        atkIncreases = [18 for _ in range(89)]
        defIncreases = [75 for _ in range(89)]
        critRateIncreases = [0.05 for _ in range(89)]
        critDmgIncreases = [0.50 for _ in range(89)]

        hpIncreases[1:19]  = [2597 for _ in range(1, 19)]
        hpIncreases[20]    = 3455
        hpIncreases[21:39] = [5170 for _ in range(21, 39)]
        hpIncreases[40]    = 5779
        hpIncreases[41:49] = [6649 for _ in range(41, 49)]
        hpIncreases[50]    = 7462
        hpIncreases[51:59] = [8341 for _ in range(51, 59)]
        hpIncreases[60]    = 8951
        hpIncreases[61:69] = [9838 for _ in range(61, 69)]
        hpIncreases[70]    = 10448
        hpIncreases[71:79] = [11345 for _ in range(71, 79)]
        hpIncreases[80]    = 11954
        hpIncreases[81:89] = [12858 for _ in range(81, 89)]

        atkIncreases[1:19]  = [46 for _ in range(1, 19)]
        atkIncreases[20]    = 61
        atkIncreases[21:39] = [91 for _ in range(21, 39)]
        atkIncreases[40]    = 102
        atkIncreases[41:49] = [117 for _ in range(41, 49)]
        atkIncreases[50]    = 132
        atkIncreases[51:59] = [147 for _ in range(51, 59)]
        atkIncreases[60]    = 158
        atkIncreases[61:69] = [174 for _ in range(61, 69)]
        atkIncreases[70]    = 185
        atkIncreases[71:79] = [200 for _ in range(71, 79)]
        atkIncreases[80]    = 211
        atkIncreases[81:89] = [227 for _ in range(81, 89)]

        defIncreases[1:19]  = [194 for _ in range(1, 19)]
        defIncreases[20]    = 258
        defIncreases[21:39] = [386 for _ in range(21, 39)]
        defIncreases[40]    = 431
        defIncreases[41:49] = [496 for _ in range(41, 49)]
        defIncreases[50]    = 557
        defIncreases[51:59] = [622 for _ in range(51, 59)]
        defIncreases[60]    = 668
        defIncreases[61:69] = [734 for _ in range(61, 69)]
        defIncreases[70]    = 779
        defIncreases[71:79] = [846 for _ in range(71, 79)]
        defIncreases[80]    = 892
        defIncreases[81:89] = [959 for _ in range(81, 89)]

        critRateIncreases[40:49]  = [0.098 for _ in range(40, 49)]
        critRateIncreases[50:69]  = [0.146 for _ in range(50, 69)]
        critRateIncreases[70:79]  = [0.194 for _ in range(70, 79)]
        critRateIncreases[80:89]  = [0.242 for _ in range(80, 89)]

        self.statsAtLevel = {
            "hp" : hpIncreases,
            "atk" : atkIncreases,
            "def" : defIncreases,
            "crit rate" : critRateIncreases,
            "crit dmg" : critDmgIncreases,
        }

        
        #TODO
