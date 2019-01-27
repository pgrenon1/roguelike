import esper
from components.speed import Speed
from components.position import Position
from components.render import Render
from components.dna import Dna
from components.block import Block
from components.death import Death
import engine


class DeathProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (death, ren) in self.world.get_components(Death, Render):
            if(death):
                ren.character = ren.corpse_character
                #engine.WORLD.remove_component(ent, Movement)
