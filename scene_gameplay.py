import tcod as libtcod
import esper
import processors
import config
from scene import Scene
import components as c
from map_generation.tile import Tile
from map_generation.rect import Rect
from map_generation.game_map import GameMap
# from loader_functions.entity_factory import *
import random
import collections
from loader_functions.factory import Factory


# from components.render import Render
# from components.position import Position


class Gameplay(Scene):
    """This is the gameplay scene. It's managed by the scene_manager.py
    """

    def __init__(self, world=None, game_map=None):
        print("Gameplay scene initialized")

        self.game_map = game_map

        self.world = world

        self.con = libtcod.console.Console(
            width=config.SCREEN_WIDTH,
            height=config.SCREEN_HEIGHT - config.PANEL_HEIGHT
        )

        self.panel = libtcod.console.Console(
            config.SCREEN_WIDTH,
            config.PANEL_HEIGHT
        )

        self.tooltip = libtcod.console.Console(
            config.SCREEN_WIDTH,
            config.SCREEN_HEIGHT
        )

        self.visible_entities = []

        # This is just a simple data type with a pop func
        self.messages = collections.deque()

        if world is None:
            """We can use esper.CachedWorld to get the last world that was assigned to esper (not 100% sure)"""
            """We should set self.world = esper.World() to whatefver is the first scene we start with I think"""
            # esper.CachedWorld()
            self.world = esper.CachedWorld()

        self.processor_group = processors.PROCESSOR_GROUP
        self.current_processor_group = None
        self.change_processors('player_turn')

        self.factory = Factory(self, "data/entities.json")

        if self.game_map is None:
            self.game_map = GameMap(
                config.MAP_WIDTH, config.MAP_HEIGHT, self.world, self.factory)

        self.reveal_all = False
        self.show_debug = True
        self.fovs = []
        libtcod.console_set_default_background(
            self.con, libtcod.Color(15, 15, 15))

        self.number_of_entities = 0  # this is updated in render.py, check render_entity()
        self.fov_recompute = True
        self.action = {}
        self.mouse = libtcod.Mouse()
        self.astar = libtcod.path.AStar(self.game_map.walkable)

    def check_world_processor(self, state):
        return state == self.current_processor_group

    def change_processors(self, state):
        print("Changing to {} processor group".format(state))
        self.current_processor_group = state

        self.world._processors = self.processor_group[state]
        for processor_instance in self.processor_group[state]:
            processor_instance.world = self.world
            processor_instance.scene = self

    # def add_processors(self):
    #     for num, state in enumerate(self.processor_group):
    #         for proc in self.processor_group[state]:
    #             # missing priority argument here, not sure how to get it to work
    #             self.world.add_processor(proc, priority=num)
    #             proc.scene = self

    def update(self):
        self.world.process()
        # Once we process the world, we render it
        libtcod.console_flush()
