from .tile import Tile
# from loader_functions.entity_factory import *
from .rect import Rect
import tcod as libtcod
import random
import numpy
import config
from loader_functions.factory import Factory


class GameMap(libtcod.map.Map):
    def __init__(self, width, height, world, factory):
        self.factory = factory
        self.width = width
        self.height = height
        self.world = world
        self.explored = numpy.zeros((height, width), dtype=bool, order='C')
        self.create_level()
        super().__init__(width, height)

    def create_level(self):
        room = Rect(20, 20, 10, 15)

        global noise
        noise = libtcod.noise_new(4, 1.0, 0.9, random=config.LIBTCOD_RANDOM)

        player = self.factory.instantiate_entity(
            'player', self.width//2, self.height//2)

        # for x in range(0, self.width):
        #     for y in range(0, self.height):
        #         if x == self.width//2 and y == self.height//2:
        #             player = instantiate_entity(
        #                 self.world, 'player', x, y)
        #         elif x in range(room.x1, room.x2) and y in range(room.y1, room.y2):
        #             if x not in range(room.x1+1, room.x2-1):
        #                 wall = instantiate_entity(
        #                     self.world, 'wall', x, y)
        #             if y not in range(room.y1+1, room.y2-1):
        #                 wall = instantiate_entity(
        #                     self.world, 'wall', x, y)
        #         else:
        #             val = libtcod.noise_get_fbm(
        #                 noise, [x+50, y+50], 15, libtcod.NOISE_PERLIN)

        #             if val > 0.95:
        #                 tree = instantiate_entity(
        #                     self.world, 'tree', x, y)
        # self.populate_world()

    def populate_world(self):
        for entity in config.ENTITY_DATA:
            if(entity != 'player'):
                instantiate_entity(self.world, entity, random.randint(
                    10, config.MAP_WIDTH - 10), random.randint(10, config.MAP_HEIGHT - 10))
