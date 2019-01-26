import json
from components.fighter import *
from components.mover import *


NAMED_COMPONENTS = {'fighter': Fighter, 'mover': Mover}

# maybe have a more generic function that loads these items when needed
# A repertory contains templates of entities (player, monsters, items, etc)


class ProcessDirector:
    def __init__(self):
        self.allClasses = []

    def construct(self, builderName):
        targetClass = getattr(idClasses, builderName)
        instance = targetClass()
        self.allClasses.append(instance)


def LoadDataSet(repertory, entity):
    with open(repertory) as f:
        data = json.load(f)
        return data[entity]


def GetEntityData(data):
    _newData = {"attributes": {}, "components": {}}
    # print(type(_newData))

    # TO BE IMPLEMENTED :
    # loop through all data recursively
#      #assign components as needed
# def myprint(d):
#   for k, v in d.items():
#     if isinstance(v, dict):
#       myprint(v)
#     else:
#       print("{0} : {1}".format(k, v))
    for key in data:
        if key != "components":
            _newData["attributes"][key] = data[key]
            # print(_newData)
        else:
            for value in _newData["components"]:
                if value == "mover":
                    _newData["components"]["mover"].append(Mover())
                elif value == "fighter":
                    _tempComponent = data["components"]["fighter"]
                    _newData["components"]["fighter"].append(Fighter(
                        _tempComponent["hp"], _tempComponent["defense"], _tempComponent["power"]))
                else:
                    print(value + "does not exist")

    return _newData

# Initialize a component without knowing what the component is
# Fill the component parameters

# def assign_components(components):
#     for component in components:
