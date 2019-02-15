import esper

import components as c
import tcod as libtcod
import config


class DnaAbsorberProcessor(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def get_absorbers(self):
        iterable = self.scene.world.get_components(
            c.Position,
            c.DnaAbsorber,
            c.Metadata
        )

        for ent, (pos, dna_abs, meta) in iterable:
            yield (ent, pos, dna_abs, meta)

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

    def absorb_other(self, absorber_entity, absorber_x, absorber_y, absorber_meta):
        for absorbed_entity, absorbed_pos, absorbed_dna, absorbed_meta in self.get_dna():
            if((absorber_x, absorber_y) == (absorbed_pos.x, absorbed_pos.y)) and absorbed_entity != absorber_entity:
                # We add the component contained in the enemy's dna here
                # The reality is that we should NOT add the component directly
                # But pass it into a dictionary with some value, and eventually add it to the player if a certain value is reached
                # For now, however, this is a nice proof of concept
                self.scene.world.add_component(
                    absorber_entity, absorbed_dna.component)
                # And we remove it
                self.try_removing(absorbed_entity, c.Dna)
                self.try_removing(absorbed_entity, c.GenerateDna)
                # print(len(self.scene.world.components_for_entity(entity)))
                if absorber_entity in self.scene.visible_entities:

                    self.scene.messages.append(
                        (absorber_meta.name.capitalize() + " absorbed " + absorbed_meta.name.capitalize() + "'s DNA", libtcod.lightest_chartreuse))

    def process(self):
        for ent, pos, dna, meta in self.get_absorbers():
            self.absorb_other(ent, pos.x, pos.y, meta)
