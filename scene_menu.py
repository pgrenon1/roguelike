import tcod as libtcod
import esper
import processors
import config
from scene import Scene
from helpers import *
from processors.console_processor import ConsoleProcessor
from processors.main_title_processor import *


class MainMenu(Scene):

    def __init__(self):
        print("MainMenu Initialized")
        self.world = esper.World()
        self._add_processors()
        self.action = {}
        # self.panel = libtcod.console.Console(
        #     config.SCREEN_WIDTH,
        #     config.PANEL_HEIGHT
        # )

    def _add_processors(self):
        processors = {
            RenderTitleProcessor(),
            InputTitleProcessor(),
            ConsoleProcessor(),
            MainTitleProcessor(),

        }

        for num, proc in enumerate(processors):
            self.world.add_processor(proc, priority=num)
            proc.scene = self

    def update(self):
        self.world.process()
