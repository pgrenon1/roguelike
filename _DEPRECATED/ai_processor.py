import esper
from components import (
    Speed,
    Position,
    Movement,
    AiRandomwalk,
    DamageDealer,
    Damage,
    Block
)
import engine
import random
# from loader_functions.entity_factory import instantiate_entity
import config


class AiProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def get_walkers(self):
        iterable = self.scene.world.get_components(
            c.Position,
            c.AiRandomwalk

        )

        for ent, (pos, ai) in iterable:
            yield (ent, pos, ai)

    def process(self):
        pass
