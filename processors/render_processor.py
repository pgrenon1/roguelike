import esper
import tcod as libtcod
from components.render import Render
from components.position import Position
from render_functions import RenderOrder
import engine
from config import COLORS


class RenderProcessor(esper.Processor):
    def __init__(self, console, clear_color):
        super().__init__()
        self.console = console
        self.clear_color = clear_color

    def process(self):
        libtcod.console_clear(self.console)

        entities = []
        for ent, (ren, pos) in self.world.get_components(Render, Position):
            entities.append(ent)
            # print(ren.render_order)

        sorted_entities = sorted(
            entities, key=lambda x: self.world.component_for_entity(x, Render).render_order)

        for enti in sorted_entities:
            posi = self.world.component_for_entity(enti, Position)
            rend = self.world.component_for_entity(enti, Render)
            libtcod.console_put_char_ex(
                self.console, posi.x, posi.y, rend.character,
                COLORS[rend.color], COLORS[rend.background_color])

        libtcod.console_flush()
