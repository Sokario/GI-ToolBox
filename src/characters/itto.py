from characterClass import BaseCharacter

class Itto(BaseCharacter):
    def __init__(self):
        super().__init__()

        #Enregistrement des statistiques au niveau 1

        baseStats = dict()
        baseStats["hp"] = 1001
        baseStats["atk"] = 18
        baseStats["def"] = 75
        baseStats["crit rate"] = 0.05
        baseStats["crit dmg"] = 0.5
        self.baseStats = baseStats

        #Enregistrement des increases au niveau de personnage i+1 (0 au rang 0)

        hpIncreases = [1001 for i in range(89)]
        atkIncreases = [18 for i in range(89)]
        defIncreases = [75 for i in range(89)]
        critRateIncreases = [0.05 for i in range(89)]
        critDmgIncreases = [0.50 for i in range(89)]

        hpIncreases[1:19]  = 2597
        hpIncreases[20]    = 3455
        hpIncreases[21:39] = 5170
        hpIncreases[40]    = 5779
        hpIncreases[41:49] = 6649
        hpIncreases[50]    = 7462
        hpIncreases[51:59] = 8341
        hpIncreases[60]    = 8951
        hpIncreases[61:69] = 9838
        hpIncreases[70]    = 10448
        hpIncreases[71:79] = 11345
        hpIncreases[80]    = 11954
        hpIncreases[81:89] = 12858

        atkIncreases[1:19]  = 46
        atkIncreases[20]    = 61
        atkIncreases[21:39] = 91
        atkIncreases[40]    = 102
        atkIncreases[41:49] = 117
        atkIncreases[50]    = 132
        atkIncreases[51:59] = 147
        atkIncreases[60]    = 158
        atkIncreases[61:69] = 174
        atkIncreases[70]    = 185
        atkIncreases[71:79] = 200
        atkIncreases[80]    = 211
        atkIncreases[81:89] = 227

        defIncreases[1:19]  = 194
        defIncreases[20]    = 258
        defIncreases[21:39] = 386
        defIncreases[40]    = 431
        defIncreases[41:49] = 496
        defIncreases[50]    = 557
        defIncreases[51:59] = 622
        defIncreases[60]    = 668
        defIncreases[61:69] = 734
        defIncreases[70]    = 779
        defIncreases[71:79] = 846
        defIncreases[80]    = 892
        defIncreases[81:89] = 959

        critRateIncreases[40:49]  = 0.098
        critRateIncreases[50:69]  = 0.146
        critRateIncreases[70:79]  = 0.194
        critRateIncreases[80:89]  = 0.242

        self.statsAtLevel({
            "hp" : hpIncreases,
            "atk" : atkIncreases,
            "def" : defIncreases,
            "crit rate" : critRateIncreases,
            "crit dmg" : critDmgIncreases,
        })

        
        #TODO
