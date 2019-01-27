import esper
from components.speed import Speed
from components.position import Position
from components.dropsdna import DropsDna
from components.block import Block
import engine


class DropDnaProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (drops, dna, pos) in self.world.get_components(DropsDna, Dna, Position):
            pass
