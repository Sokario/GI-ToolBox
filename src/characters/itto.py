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

        hpIncreases = [0 for i in range(89)]
        atkIncreases = [0 for i in range(89)]
        defIncreases = [0 for i in range(89)]
        critRateIncreases = [0 for i in range(89)]
        critDmgIncreases = [0 for i in range(89)]

        

        self.set_statIncreases(hpIncreases, atkIncreases, defIncreases, critRateIncreases, critDmgIncreases)

        
        #TODO
