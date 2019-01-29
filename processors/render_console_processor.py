import esper
import tcod as libtcod
from components.render import Render
from components.position import Position


class RenderConsole(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        self.render_entity()
        self.blit_console()
        self.flush_console()
        self.clear_entity()

    def blit_console(self):
        pass

    def flush_console(self):
        libtcod.console_flush()

    def clear_entity(self):
        pass

    def get_entities(self):
        iterable = list(self.world.get_components(Render, Position))
        for _, (rend, pos) in iterable:
            yield (rend, pos)

        # We need to sort these for rendering order of course
        #iterable.sort(key=lambda row: row[1][0].render_order)

    def render_entity(self):
        # self.get_entities()
        for(rend, pos) in self.get_entities():
            #     print("!!!!!!!*!@&(*@!^!@&*!@%&^!@^&%@!&*%^!@")
            print(pos.x, pos.y)
            print(rend.character)
        #     # self.scene.con.print
