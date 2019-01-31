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


# from components.render import Render
# from components.position import Position


class Gameplay(Scene):
    def __init__(self, world=None, game_map=None):
        print("Gameplay scene initialized")
        self.processor_group = processors.PROCESSOR_GROUP

        self.game_map = game_map
        self.panel = libtcod.console.Console(
            config.SCREEN_WIDTH,
            config.PANEL_HEIGHT
        )
        self.messages = []

        self.world = world
        if world is None:
            """We can use esper.CachedWorld to get the last world that was assigned to esper (not 100% sure)"""
            """We should set self.world = esper.World() to whatefver is the first scene we start with I think"""
            # esper.CachedWorld()
            self.world = esper.World()

        if self.game_map is None:
            self._create_level()

        self.add_processors()
        self.change_processors('player_turn')
        self.action = {}  # mon seul ajout so far, c'est necessaire pour que tout les processors

        # aillent accès à quelle key vient d'être pressed et qu'est-ce que cette clef veut dire. i.e. une action typique ressemble à { 'move' : (0,1)}
    global room
    room = Rect(20, 20, 10, 15)
    global noise

    # !!PLACEHOLDER ENTITY
    # JUST FOR TESTING THE ARCHITECTURE!!
    """Tout les components sont maintenant dans un seul file."""

    def _create_level(self):

        noise = libtcod.noise_new(2, 5.0, 0.9, random=config.LIBTCOD_RANDOM)

        for x in range(0, config.MAP_WIDTH):
            for y in range(0, config.MAP_HEIGHT):
                if x == config.MAP_WIDTH//2 and y == config.MAP_HEIGHT//2:
                    player = instantiate_entity(self.world, 'player', x, y)
                elif x in range(room.x1, room.x2) and y in range(room.y1, room.y2):
                    if x not in range(room.x1+1, room.x2-1):
                        wall = instantiate_entity(self.world, 'wall', x, y)
                    if y not in range(room.y1+1, room.y2-1):
                        wall = instantiate_entity(self.world, 'wall', x, y)
                else:
                    val = libtcod.noise_get_fbm(
                        noise, [x, y], 32.0, libtcod.NOISE_PERLIN)
                    # print(val)
                    if val > 0.8 and val < 1:
                        tree = instantiate_entity(self.world, 'tree', x, y)
        # libtcod.sys_set_renderer(2)

        self.populate_world()

        self.con = libtcod.console.Console(
            width=config.MAP_WIDTH,
            height=config.MAP_HEIGHT
        )

        # print(libtcod.sys_get_renderer())

    #"""Placeholder class for instantiating one of each entity declared in the entities.JSON file"""
    def populate_world(self):
        for entity in config.ENTITY_DATA:
            if(entity != 'player'):
                instantiate_entity(self.world, entity, random.randint(
                    0, config.MAP_WIDTH), random.randint(0, config.MAP_HEIGHT))

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
