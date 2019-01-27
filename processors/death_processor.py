import esper
from components.speed import Speed
from components.position import Position
from components.render import Render
from components.dna import Dna
from components.block import Block
from components.death import Death
from components.remains import Remains
import engine


class DeathProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (death, ren) in self.world.get_components(Death, Render):
            ren.character = ren.corpse_character
            engine.WORLD.add_component(ent, Remains)
            if engine.WORLD.try_component(ent, Block):
                engine.WORLD.remove_component(ent, Block)

            engine.WORLD.remove_component(ent, Death)
