import numpy as np

def get_regular_materials_gem(element):
    returnVal = dict()

    ############################### 0 J'usqu'a lvl 20 ####### 1 pour passer 21
    returnVal["gem sliver count"] = [0 for i in range(19)] + [(element, 1)]
    ################################## 0 jusqu'au lvl 40 ###### 3 pour passer 41 ###### 
    returnVal["gem fragment count"] = [0 for i in range(39)]   + (element, 3) +        [0 for i in range(9)] + (element, 6)
    
    return {\
        "gem fragment count" : [0 for i in range(39)] + (element, 3) + [0 for i in range(9)] + (element, 6),\
    }

def get_regular_materials_monster(monster):
    return {\
    }

def get_regular_materials_resource(resource):
    return {\
    }

def get_regular_materials_boss(boss):
    return {\
    }

def get_regular_materials(element, monster, resource, boss):
    return {\
        "gem" : get_regular_materials_gem(element),
        "monster material" : get_regular_materials_monster(monster),
        "natural resource" : get_regular_materials_resource(resource),
        "boss material"    : get_regular_materials_boss(boss),
        }

itto_materials = {\
    "gem sliver count" : [("geo",0) for i in range(19)] + [("geo", 1)], """0 J'usqu'a lvl 20; 1 pour passer 21""" \
    "gem fragment count" : ["" for i in range(19)] + "geo", \
}


character_materials = {\
    "itto" : get_regular_materials("geo", "slime"),\
}