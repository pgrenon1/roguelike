from config.config import ENTITY_DATA
from instantiator import *
import engine
from components.position import Position


def find_request_components(request):
    requestData = query_dataset(config.ENTITY_DATA, request)
    requestedComponents = get_entity_data(requestData)

    return requestedComponents


def instantiate_entity(query, x, y):
    entityComponents = find_request_components(query)
    new_entity = engine.WORLD.create_entity()
    engine.WORLD.add_component(new_entity, Position(x, y))
    for i in entityComponents:
        engine.WORLD.add_component(new_entity, entityComponents[i])
        # print(entityComponents[i])
    return new_entity
