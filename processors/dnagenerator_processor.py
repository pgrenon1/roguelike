import esper
from components import (
    Speed,
    Position,
    GenerateDna,
    Dna,
    Block
)
import engine


class DnaGeneratorProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (gendna) in self.world.get_component(GenerateDna):
            # generate dna
            _generatedDna = {'dna': {'dna_data': 'dna data, baby!'}}
            engine.WORLD.add_component(ent, Dna(_generatedDna))
            engine.WORLD.remove_component(ent, GenerateDna)
