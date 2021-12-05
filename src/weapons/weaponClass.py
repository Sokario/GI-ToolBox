
class BaseWeapon():
    def __init__(self, name, type) -> None:
        self.type = type
        self.name = name

        self.refinement = 0
        
        self.attack = 0
        self.stat = list()#"stat" : string, "value" : float aux 90 differents niveaux

        self.effect = None