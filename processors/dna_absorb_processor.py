import esper

import components as c


class DnaAbsorberProcessor(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def get_absorbers(self):
        iterable = self.scene.world.get_components(
            c.Position,
            c.DnaAbsorber

        )

        for ent, (pos, dna) in iterable:
            yield (ent, pos, dna)

    def absorb_other(self, entity, x, y):

        for other_ent, pos, dna in self.get_absorbers():
            if((x, y) == (pos.x, pos.y)):
                self.scene.messages = []
                self.scene.messages.append("Allo")

    def process(self):
        for ent, pos, dna in self.get_absorbers():
            self.absorb_other(ent, pos.x, pos.y)

        # for ent, (position, dnaabsorber) in self.scene.world.get_components(Position, DnaAbsorber):
        #     for otherent, (otherposition, otherdna) in self.scene.world.get_components(Position, Dna):

        #         if((position.x, position.y) == (otherposition.x, otherposition.y)):

        #             self.scene.world.add_component(ent, Dna(otherdna.dna_raw))
        #             entity_name = scene.world.component_for_entity(
        #                 ent, Metadata)
        #             dna_nam = self.scene.world.component_for_entity(
        #                 ent, Dna)
        #             self.scene.messages.append(entity_name.name,
        #                                        "picked up some dna containing", dna_nam.dna_data)
        #             self.scene.world.remove_component(otherent, Dna)
