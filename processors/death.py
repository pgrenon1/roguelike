import components as c
import config
import esper
import tcod as libtcod
import random


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

    # def get_generators(self):
    #     iterable = self.scene.world.get_components(
    #         c.Position,
    #         c.GenerateDna
    #     )

    #     for ent, (pos, dna) in iterable:
    #         yield (ent, pos, dna)

    def process_dnageneration(self, ent):
        # We will store all components contained by the entity, except Renderable, position, metadata and stats here
        clean_components = []

        if self.world.has_component(ent, c.Dna):
            # We generate the DNA right before adding it
            current_components = self.world.components_for_entity(ent)
            for component in current_components:
                if not (component, (c.Renderable, c.Position, c.Metadata, c.Stats)):
                    clean_components.append(component)

            if(len(clean_components) > 0):
                drop_dna = random.choice(clean_components)
                dna_data = {'Dna': {'dna_data': drop_dna}}
                self.world.add_component(ent, c.Dna(dna_data))
            else:
                pass

    def try_removing(self, entity, component):
        if self.world.has_component(entity, component):
            self.world.remove_component(entity, component)

    def process_death(self):
        for ent, rend, desc, stats in self.get_dead_entities():
                # print(rend.character)
            rend.character = '%'
            # rend.foreground_color = libtcod.dark_red
            rend.render_order = config.RenderOrder.REMAINS.value

            # We remove the absorber ability from the corpse, just in case
            self.try_removing(ent, c.DnaAbsorber)
            # we process dna generation at this point, right before we start removing components
            self.process_dnageneration(ent)

            self.try_removing(ent, c.Collidable)
            # self.try_removing(ent, c.Stats)
            self.try_removing(ent, c.Movable)
            self.try_removing(ent, c.PlayerTurn)
            self.try_removing(ent, c.EnemyTurn)
            self.world.add_component(ent, c.Decay())
            # self.scene.message.append(
            #     ('{} is dead!'.format(desc.name.capitalize()), tcod.orange)
            # )

    def process(self):
        self.process_death()
        # print("processing death")
