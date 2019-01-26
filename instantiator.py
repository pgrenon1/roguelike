import json
from components.mover import *

#maybe have a more generic function that loads these items when needed
#A repertory contains templates of entities (player, monsters, items, etc)

def LoadDataSet(repertory,entity):
    with open(repertory) as f:
        data = json.load(f)
        print(data[entity])
        return data[entity]



def GetEntityData(data):
    _attributes = {}
    _components = []



    for key in data:
        if key != "components":
            _attributes[key] = data[key]
        else:
            #We scan for components
            for value in data["components"]:
                if value == "mover":
                    _components.append(Mover())
                elif key == "other":
                    print("other")


    print(_attributes,_components)
    return _attributes, _components

#Initialize a component without knowing what the component is
#Fill the component parameters

