import json
import config


def Factory(class_name):
    # print(config.MASTER_COMPONENT_DATASET)
    return config.MASTER_COMPONENT_DATASET[class_name]


# # maybe have a more generic function that loads these items when needed
# # A repertory contains templates of entities (player, monsters, items, etc)

def load_dataset(repertory):
    """We load the JSON containing all the data, we specify the entity we
    want it to check for. Store it in a variable"""

    with open(repertory) as f:
        data = json.load(f)
        # print(data)
        return data


def query_dataset(data, query):
    # print(data[query])
    return data[query]


def get_entity_data(data):
    """We create a dataset to be used as an argument to be used when creating a new entity"""
    _newData = {}

    for key in data:
        _componentType = Factory(key)
        args = {}
        for param in data[key]:

            args[key] = data[key]

        if args:
            _newComponent = _componentType(args)
        else:
            _newComponent = _componentType()

        _newData[key] = _newComponent
    return _newData

# # Initialize a component without knowing what the component is
# # Fill the component parameters
