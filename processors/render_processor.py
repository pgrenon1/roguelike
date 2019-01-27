import esper
import tcod as libtcod
from components.render import Render
from components.position import Position


class RenderProcessor(esper.Processor):
    def __init__(self, console, clear_color):
        super().__init__()
        self.console = console
        self.clear_color = clear_color

    def process(self):
        libtcod.console_clear(self.console)
        for ent, (ren, pos) in self.world.get_components(Render, Position):
            libtcod.console_put_char(
                self.console, pos.x, pos.y, "@", self.clear_color)
        libtcod.console_flush()
