import esper
from components.speed import Speed
from components.position import Position
from components.render import Render
from components.dna import Dna
from components.generate_dna import GenerateDna
from components.movement import Movement
from components.block import Block
from components.death import Death
from components.remains import Remains
from render_functions import RenderOrder
import engine


class DeathProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (death, ren) in self.world.get_components(Death, Render):
            ren.character = ren.corpse_character
            ren.render_order = RenderOrder.REMAINS
            engine.WORLD.add_component(ent, Remains)
            engine.WORLD.add_component(ent, GenerateDna)

            block = engine.WORLD.try_component(ent, Block)
            if block:
                engine.WORLD.remove_component(ent, type(next(block)))

            # movement = engine.WORLD.try_component(ent, Movement)
            # if movement:
            #     engine.WORLD.remove_component(ent, type(next(movement)))

            engine.WORLD.remove_component(ent, Death)
