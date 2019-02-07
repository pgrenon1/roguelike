import tcod as libtcod
import esper
import processors
import config
from scene import Scene
import components as c
from map_generation.tile import Tile
from map_generation.rect import Rect
from map_generation.game_map import GameMap
from loader_functions.entity_factory import *
import random
import collections


# from components.render import Render
# from components.position import Position


class Gameplay(Scene):
    """This is the gameplay scene. It's managed by the scene_manager.py
    """

    def __init__(self, world=None, game_map=None):
        #helpers.debug("Gameplay scene initialized")
        self.processor_group = processors.PROCESSOR_GROUP

        self.game_map = game_map

        self.con = libtcod.console.Console(
            width=config.SCREEN_WIDTH,
            height=config.SCREEN_HEIGHT
        )

        self.panel = libtcod.console.Console(
            config.SCREEN_WIDTH,
            config.PANEL_HEIGHT
        )

        # This is just a simple data type with a pop func
        self.messages = collections.deque()

        self.world = world
        if world is None:
            """We can use esper.CachedWorld to get the last world that was assigned to esper (not 100% sure)"""
            """We should set self.world = esper.World() to whatefver is the first scene we start with I think"""
            # esper.CachedWorld()
            self.world = esper.CachedWorld()

        if self.game_map is None:
            self.game_map = libtcod.map_new(
                config.MAP_WIDTH, config.MAP_HEIGHT)
            GameMap(config.MAP_WIDTH, config.MAP_HEIGHT, self.world)

        self.reveal_all = False
        self.show_debug = False
        self.fovs = []
        libtcod.console_set_default_background(
            self.con, libtcod.Color(15, 15, 15))

        self.number_of_entities = 0  # this is updated in render.py, check render_entity()
        self.fov_recompute = True
        self.add_processors()
        self.change_processors('player_turn')
        self.action = {}
        self.mouse = libtcod.Mouse()

    def change_processors(self, state):
        self.world_processors = self.processor_group[state]
        for processor_instance in self.processor_group[state]:
            processor_instance.world = self.world
            processor_instance.scene = self

    def add_processors(self):
        for num, state in enumerate(self.processor_group):
            for proc in self.processor_group[state]:
                # missing priority argument here, not sure how to get it to work
                self.world.add_processor(proc)
                proc.scene = self

    def update(self):
        # print("Processing world")
        self.world.process()
