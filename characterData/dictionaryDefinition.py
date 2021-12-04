"""import numpy as np

def get_regular_materials_gem(element):
    returnVal = dict()

    ############################### 0 J'usqu'a lvl 20 ####### 1 pour passer 21
    returnVal["gem sliver count"] = np.zeros(19, dtype = np.int64).tolist() + [(element, 1)]
    ################################## 0 jusqu'au lvl 40 ###### 3 pour passer 41 ###### 0 jusqu'a 50 ########## 6 de 50 à 51 
    returnVal["gem fragment count"] = [0 for i in range(39)]   + [(element, 3)] +        [0 for i in range(9)] + [(element, 6)]
    ###############################
    returnVal["gem "] = 0
    
    return returnVal

def get_regular_materials_monster(monster):
    return {\
    }

def get_regular_materials_resource(resource):
    return {\
    }

def get_regular_materials_boss(boss):
    return {\
    }

def create_regular_material_dict(element, monster, resource, boss):
    return {\
        "gem"              : get_regular_materials_gem(element),
        "monster material" : get_regular_materials_monster(monster),
        "natural resource" : get_regular_materials_resource(resource),
        "boss material"    : get_regular_materials_boss(boss),
        }"""

character_materials = {\
    "itto" : create_regular_material_dict("geo", "slime", "scarabuto", "loup de faille dore"),\
}

if __name__ == "__main__" :
    print(np.zeros(9, dtype = np.int64).tolist())