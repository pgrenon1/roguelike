import esper
from components.speed import Speed
from components.position import Position
from components.movement import Movement
from components.block import Block
from components.damage_dealer import DamageDealer
from components.damage import Damage
from components.spawner import Spawner
from components.spawner_event import SpawnerEvent
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

            #self.world.remove_component(ent, SpawnerEvent)
