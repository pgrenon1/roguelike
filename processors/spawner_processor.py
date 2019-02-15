import esper
import components as c
import random
import config
# from loader_functions.entity_factory import instantiate_entity
import tcod as libtcod


class SpawnerProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def get_spawners(self):
        spawners = self.world.get_components(
            c.Position,
            c.Spawner,
            c.Stats,
            c.Metadata
        )

        for spawner, (pos, spawn, stats, metadata) in spawners:
            yield spawner, (pos, spawn, stats, metadata)

    def spawn_children(self):

        for spawner, (pos, spawn, stats,  metadata) in self.get_spawners():
            # we check if the entity has less than 3 children. This could be an arg, of course.
            if len(spawn.children) < 3:

                # child = instantiate_entity(self.scene.world, spawn.child_type, pos.x + random.randint(-2, 2),
                #                            pos.y + random.randint(-2, 2))
                spawn.children.append(child)

                childComponent = c.Child()
                childComponent.parent = spawner

                self.scene.world.add_component(child, childComponent)
                if child in self.scene.visible_entities:
                    self.scene.messages.append((
                        "A moth (*) came out of {}".format(metadata.name), libtcod.yellow))

    def process(self):
        if(config.TICK % 10 == 0):
            self.spawn_children()

        # self.world.remove_component(ent, SpawnerEvent)
