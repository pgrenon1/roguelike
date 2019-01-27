import esper
from components.speed import Speed
from components.position import Position
from components.dropsdna import DropsDna
from components.dna import Dna
from components.block import Block
import engine


class GenerateDna(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        pass