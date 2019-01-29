import esper
import engine
from components import (
    Dna,
    DnaAbsorber,
    Position,
    Metadata
)


class DnaAbsorberProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (position, dnaabsorber) in self.world.get_components(Position, DnaAbsorber):
            for otherent, (otherposition, otherdna) in self.world.get_components(Position, Dna):
                if((position.x, position.y) == (otherposition.x, otherposition.y)):

                    engine.WORLD.add_component(ent, Dna(otherdna.dna_raw))
                    entity_name = engine.WORLD.component_for_entity(
                        ent, Metadata)
                    dna_nam = engine.WORLD.component_for_entity(
                        ent, Dna)
                    print(entity_name.name,
                          "picked up some dna containing", dna_nam.dna_data)
                    engine.WORLD.remove_component(otherent, Dna)
