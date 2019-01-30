import components as c
import config
import esper
import tcod as libtcod


class Death(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def get_dead_entities(self):
        iterable = self.world.get_components(
            c.Renderable,
            c.Metadata,
            c.Stats
        )
        for ent, (rend, meta, stats) in iterable:
            if stats.health <= 0:
                yield (ent, rend, meta, stats)

    def process(self):
        # print("processing death")
        for ent, rend, desc, stats in self.get_dead_entities():
            # print(rend.character)
            rend.character = '%'
            # rend.foreground_color = libtcod.dark_red
            rend.render_order = config.RenderOrder.REMAINS.value
            self.try_removing(ent, c.Collidable)
            # self.try_removing(ent, c.Stats)
            self.try_removing(ent, c.Movable)
            self.try_removing(ent, c.PlayerTurn)
            self.try_removing(ent, c.EnemyTurn)
            # self.scene.message.append(
            #     ('{} is dead!'.format(desc.name.capitalize()), tcod.orange)
            # )

    def try_removing(self, entity, component):
        if self.world.has_component(entity, component):
            self.world.remove_component(entity, component)
