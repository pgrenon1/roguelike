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
        player_pos = (self.width//2, self.height//2)
        player = self.factory.instantiate_entity(
            'player', *player_pos)

        rooms = self.create_rooms(5)

        # print(rooms)
        for x in range(0, self.width):
            for y in range(0, self.height):
                in_room = False
                if (x, y) != player_pos:
                    for room in rooms:
                        if x == room.x1 and y in range(room.y1, room.y2+1) \
                                or x == room.x2 and y in range(room.y1, room.y2+1) \
                                or y == room.y1 and x in range(room.x1+1, room.x2) \
                                or y == room.y2 and x in range(room.x1+1, room.x2):
                            wall = self.factory.instantiate_entity(
                                'wall', x, y)
                            in_room = True
                    if not in_room:
                        val = libtcod.noise_get_fbm(
                            noise, [x+50, y+50], 15, libtcod.NOISE_PERLIN)

                        if val > 0.95:
                            tree = self.factory.instantiate_entity(
                                'tree', x, y)

    def create_rooms(self, number):
        rooms = []
        while len(rooms) < number:
            w = random.randint(6, 15)
            h = random.randint(6, 15)
            x = random.randint(0, config.MAP_WIDTH - w)
            y = random.randint(0, config.MAP_HEIGHT - h)
            new_room = Rect(x, y, w, h)
            if any(room.intersect(new_room) for room in rooms):
                continue
            rooms.append(new_room)
        return rooms
