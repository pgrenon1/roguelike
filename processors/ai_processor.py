import esper
from components.speed import Speed
from components.position import Position
from components.movement import Movement
from components.ai_randomwalk import AiRandomwalk
import engine
import random
from loader_functions.entity_factory import instantiate_entity
import config


class AiProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent,  (mov, pos) in self.world.get_components(AiRandomwalk, Position):
          # if pos.x >=0 and pos.x < config.MAP_WIDTH and pos.y > 0 and pos.y < config.MAP_HEIGHT:
                pos.x += random.randint(-1, 1)
                pos.y += random.randint(-1, 1)
            #else:
            #    pass
                

                engine.WORLD.remove_component(ent, AiRandomwalk)
