import esper
import engine
from components.dna import Dna


class DnaAbsorberProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (dna) in self.world.get_components(Dna):
            print(dna.dna_data)
