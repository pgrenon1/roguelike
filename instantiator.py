import json

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
    return data[query]


def get_entity_data(data):
    """We create a dataset to be used as an argument to be used when creating a new entity"""
    _newData = {}

    for key in data:
        for value in data:
            _componentType = Factory(value)
            #print(_entityType)
            args = {}

            for param in data[value]:

                args[param] = data[value][param]
              #  print(args)
            _newComponent = _componentType(args)
    #print(_newData)
    return _newComponent

# Initialize a component without knowing what the component is
# Fill the component parameters
