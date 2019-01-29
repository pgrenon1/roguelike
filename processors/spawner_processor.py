import esper
from components import (
    Speed,
    Position,
    Movement,
    Block,
    DamageDealer,
    Damage,
    Spawner,
    SpawnerEvent
)
import engine
from loader_functions.entity_factory import *
import random


class SpawnerProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (spawner, pos) in self.world.get_components(SpawnerEvent, Position):
            # print(pos)
            instantiate_entity(
                'npcwalk',
                pos.x + random.choice([-1, 1]),
                pos.y+random.choice([-1, 1]))

            self.world.remove_component(ent, SpawnerEvent)
