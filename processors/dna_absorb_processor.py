import esper
import engine
from components.dna import Dna
from components.dna_absorber import DnaAbsorber


class DnaAbsorberProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (absorb, position) in self.world.get_components(Dna, DnaAbsorber):
            pass
