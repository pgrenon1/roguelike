import esper

import components as c
import tcod as libtcod


class DnaAbsorberProcessor(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def get_absorbers(self):
        iterable = self.scene.world.get_components(
            c.Position,
            c.DnaAbsorber
        )

        for ent, (pos, dna_abs) in iterable:
            yield (ent, pos, dna_abs)

    def get_dna(self):
        iterable = self.scene.world.get_components(
            c.Position,
            c.Dna,
            c.Metadata
        )
        for other_ent, (pos, dna, meta) in iterable:
            yield (other_ent, pos, dna, meta)

    def try_removing(self, entity, component):
        if self.world.has_component(entity, component):
            self.world.remove_component(entity, component)

    def absorb_other(self, entity, x, y):
        for other_ent, otherpos, dna, meta in self.get_dna():
            if((x, y) == (otherpos.x, otherpos.y)) and other_ent != entity:
                # We add the component contained in the enemy's dna here
                self.scene.world.add_component(entity, dna)
                # And we remove it
                self.try_removing(other_ent, c.Dna)

                self.scene.messages.append(
                    ("Absorbed " + meta.name.lower() + "'s DNA", libtcod.lightest_chartreuse))

    def process(self):
        for ent, pos, dna in self.get_absorbers():
            self.absorb_other(ent, pos.x, pos.y)
