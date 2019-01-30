from config import ENTITY_DATA
from loader_functions.instantiator import *
from components import Position


def find_request_components(request):
    requestData = query_dataset(config.ENTITY_DATA, request)
    requestedComponents = get_entity_data(requestData)
    
    return requestedComponents


def instantiate_entity(world, query, x, y):

    entityComponents = find_request_components(query)
    new_entity = world.create_entity()
    world.add_component(new_entity, Position(x, y))
    for i in entityComponents:
        world.add_component(new_entity, entityComponents[i])
    # print(new_entity)
    return new_entity
