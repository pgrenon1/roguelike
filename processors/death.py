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

        if self.world.has_component(ent, c.GenerateDna):
            # We generate the DNA right before adding it
            current_components = self.world.components_for_entity(ent)
            for component in current_components:
                if not isinstance(component, (c.Renderable, c.Position, c.Metadata, c.Stats, c.AiRandomAgitated, c.AiRandomCalm, c.AiPredator, c.GenerateDna, c.Decay, c.Dna)):
                    clean_components.append(component)
                    # print(clean_components)
                    # print(clean_components)

            if(len(clean_components) > 0):
                # We just get all the components that aren't the forbidden ones and we pass it as an argument to DNA.
                # DNA is basically just a 1 slot inventory that remains have.
                drop_dna = random.choice(clean_components)
                self.world.add_component(ent, c.Dna(drop_dna))
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
            rend.color = rend.corpse_color

            rend.render_order = config.RenderOrder.REMAINS.value

            self.handleSpawners()
            # We remove the absorber ability from the corpse, just in case
            self.try_removing(ent, c.DnaAbsorber)

            # we process dna generation at this point, right before we start removing components
            self.process_dnageneration(ent)

            self.try_removing(ent, c.Collidable)
            self.try_removing(ent, c.Movable)
            self.try_removing(ent, c.PlayerTurn)
            self.try_removing(ent, c.EnemyTurn)
            self.try_removing(ent, c.Spawner)
            self.try_removing(ent, c.Child)

            # We check if this entity is someone's children, if so, we remove it

    def get_spawners(self):
        iterable = []
        iterable = self.scene.world.get_components(
            c.Spawner,
            c.Stats
        )
        for ent, (spawner_component, spawner_stats) in iterable:
            yield ent, (spawner_component, spawner_stats)

    def get_children(self):
        iterable = []
        iterable = self.scene.world.get_components(
            c.Child,
            c.Stats
        )

        for ent, (child_component, stats) in iterable:
            yield ent, (child_component, stats)

    def handleSpawners(self):

        # Is this entity a parent?

        # We remove the children entity from the parent list, so it can spawn an additional one
        # We check that the parent of this thing is not dead also
        for spawner, (spawner_component, spawner_stats) in self.get_spawners():
            for child, (child_component, child_stats) in self.get_children():
                if child_stats.health <= 0 and child in spawner_component.children:
                    spawner_component.children.remove(child)
                if spawner_stats.health <= 0:
                    child_stats.health = 0

    def process(self):
        self.process_death()
        # print("processing death")
