import esper
from components.speed import Speed
from components.position import Position
from components.generate_dna import GenerateDna
from components.dna import Dna
from components.block import Block
import engine


class GenerateDnaProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (gendna) in self.world.get_component(GenerateDna):
            # generate dna
            _generatedDna = {'dna': {'dna_data': 'dna data, baby!'}}
            engine.WORLD.add_component(ent, Dna(_generatedDna))
            engine.WORLD.remove_component(ent, GenerateDna)
