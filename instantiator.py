import json
from components.fighter import *
from components.mover import *
from config import config


def Factory(class_name):
    return config.MASTER_COMPONENT_DATASET[class_name]


# maybe have a more generic function that loads these items when needed
# A repertory contains templates of entities (player, monsters, items, etc)

def load_dataset(repertory):
    """We load the JSON containing all the data, we specify the entity we
    want it to check for. Store it in a variable"""

    with open(repertory) as f:
        data = json.load(f)
        return data


def query_dataset(data, query):
    """Query the dataset you loaded with LoadDataSet"""
<<<<<<< HEAD
=======
    # print(data[query])
>>>>>>> 507b127d2fd26955e07ccb2ea6dea1b7654c3a0b
    return data[query]


def fetch_all_components():
    pass


def get_entity_data(data):
    """We create a dataset to be used as an argument to be used when creating a new entity"""
    _newData = {"attributes": {}, "components": {}}

    for key in data:
        if key != "components":
            _newData["attributes"][key] = data[key]
        else:
            for value in data["components"]:
                _entityType = Factory(value)
                args = {}

                for param in data["components"][value]:
                    args[param] = data["components"][value][param]
                _newComponent = _entityType(args)
                print("!!!!")
                print(_newComponent)
                _newData['components'][value] = _newComponent
    return _newData

# Initialize a component without knowing what the component is
# Fill the component parameters
