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
from components.ai_randomwalk import AiRandomwalk
import engine


class DeathProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (death, ren) in self.world.get_components(Death, Render):
            ren.character = ren.corpse_character
            ren.render_order = RenderOrder.REMAINS.value

            if self.world.has_component(ent, AiRandomwalk):
                self.world.remove_component(ent, AiRandomwalk)

            self.world.add_component(ent, Remains())
            self.world.add_component(ent, GenerateDna())

            block = engine.WORLD.try_component(ent, Block)
            if block:
                engine.WORLD.remove_component(ent, type(next(block)))

            # Not really sure how to stop the movement of a corpse
            # I think our approach on moven needs to be rethought

            # movement = engine.WORLD.try_component(ent, AiRandomwalk)
            # if movement:
            #     engine.WORLD.remove_component(ent, type(next(movement)))

            engine.WORLD.remove_component(ent, Death)
