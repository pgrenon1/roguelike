from config.config import ENTITY_DATA
from instantiator import *
import engine


def find_request_components(request):
    requestData = query_dataset(config.ENTITY_DATA, request)
    requestedComponents = get_entity_data(requestData)

    return requestedComponents


def instantiate_entity(query):
    entityComponents = find_request_components(query)
    new_entity = engine.WORLD.create_entity()
    for i in entityComponents:
        engine.WORLD.add_component(new_entity, entityComponents[i])
        # print(entityComponents[i])
    return new_entity
