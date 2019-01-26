import json
from components.fighter import *
from components.mover import *


def Factory(class_name):
    components = {"fighter":Fighter, "mover":Mover}
    return components[class_name]
    

# maybe have a more generic function that loads these items when needed
# A repertory contains templates of entities (player, monsters, items, etc)

def LoadDataSet(repertory, entity):
    with open(repertory) as f:
        data = json.load(f)
        return data[entity]


def GetEntityData(data):
    _newData = {"attributes": {}, "components": {}}

    for key in data:
        if key != "components":
            _newData["attributes"][key] = data[key]
        else:
            for value in data["components"]:
                _entityType = Factory(value)
                args = {}

                for param in data["components"][value]:
                    args[param] =  data["components"][value][param]
                _newComponent = _entityType(args)
                _newData['components'][value] = _newComponent

            print(_newData)

    return _newData

# Initialize a component without knowing what the component is
# Fill the component parameters