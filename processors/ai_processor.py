import esper
from components.speed import Speed
from components.position import Position
from components.movement import Movement
from components.ai_randomwalk import Ai_randomwalk
import engine
import random
from loader_functions.entity_factory import instantiate_entity


class AiProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent,  (mov, pos) in self.world.get_components(Ai_randomwalk, Position):
            pos.x += random.randint(-1, 1)
            pos.y += random.randint(-1, 1)

            engine.WORLD.remove_component(ent, Ai_randomwalk)
