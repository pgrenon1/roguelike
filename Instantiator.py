import json



#maybe have a more generic function that loads these items when needed
def LoadDataSet(dataset,entity):
    with open(dataset) as f:
        data = json.load(f)
        return data[entity]


def Instantiate(data):
    for key in data:
        print(data[key])
