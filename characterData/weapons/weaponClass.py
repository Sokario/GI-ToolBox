
class BaseWeapon():
    def __init__(self, name, type) -> None:
        self.type = type
        self.name = name
        
        self.primary = list()#"stat" : string, "value" : int aux 90 differents niveaux