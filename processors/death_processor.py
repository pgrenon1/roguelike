import esper
from components.speed import Speed
from components.position import Position
from components.render import Render
from components.dna import Dna
from components.block import Block
import engine


class DeathProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (pos, ren) in self.world.get_components(Position, Render):
            ren.character = ren.corpse_character
            
