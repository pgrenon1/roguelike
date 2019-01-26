import json
from components.fighter import *
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


     #TO BE IMPLEMENTED :
     #loop through all data recursively
     #assign components as needed

    for key in data:
        if key != "components":
            _attributes[key] = data[key]
        else:

            #We scan for components
            for value in data["components"]:
                if value == "mover":
                    _components.append(Mover())
                elif value == "fighter":
                    _tempComponent = data["components"]["fighter"]
                    _components.append(Fighter(_tempComponent["hp"]
                                               ,_tempComponent["defense"]
                                               ,_tempComponent["power"]))
                else:
                    print(value + "does not exist")

    return _attributes, _components

#Initialize a component without knowing what the component is
#Fill the component parameters

