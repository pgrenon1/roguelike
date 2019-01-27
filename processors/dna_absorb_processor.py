import esper
import engine
from components.dna import Dna
from components.dna_absorber import DnaAbsorber
from components.position import Position


class DnaAbsorberProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (position, dnaabsorber) in self.world.get_components(Position, DnaAbsorber):
            for otherent, (otherposition, otherdna) in self.world.get_components(Position, Dna):
                if((position.x, position.y) == (otherposition.x, otherposition.y)):
                    print("You picked up some dna ", otherdna)
                    engine.WORLD.remove_component(otherent, Dna)

            # for i in engine.WORLD.components_for_entity(ent):
            #     print(i)
