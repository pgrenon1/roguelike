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
            c.Dna
        )
        for other_ent, (pos, dna) in iterable:
            yield (other_ent, pos, dna)

    def absorb_other(self, entity, x, y):
        for other_ent, otherpos, dna in self.get_dna():
            if((x, y) == (otherpos.x, otherpos.y)) and other_ent != entity:
                self.scene.messages.append(("Absorbed DNA", libtcod.lightest_chartreuse))

    def process(self):
        for ent, pos, dna in self.get_absorbers():
            self.absorb_other(ent, pos.x, pos.y)
