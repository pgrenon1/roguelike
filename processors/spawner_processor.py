import esper
import components as c
import random
import config
from loader_functions.entity_factory import instantiate_entity


class SpawnerProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def get_spawners(self):
        spawners = self.world.get_components(
            c.Position,
            c.Spawner
        )

        for spawner, (pos, spawn) in spawners:
            yield spawner, (pos, spawn)

    def spawn_children(self):
        for spawner, (pos, spawn) in self.get_spawners():

            instantiate_entity(self.scene.world, 'npcwalk', pos.x + random.randint(-1, 1),
                               pos.y + random.randint(-1, 1))

    def process(self):
        if(config.TICK % 10 == 0):
            self.spawn_children()

        # self.world.remove_component(ent, SpawnerEvent)
