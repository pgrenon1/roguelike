import tcod as libtcod
from loader_functions.instantiator import *
from loader_functions.fetcher import *
from enum import Enum
import components
from components import *
import random


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 60
PANEL_HEIGHT = 10

MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT
FULLSCREEN = False
VERBOSE_MODE = False

MASTER_SEED = None
LIBTCOD_RANDOM = None

FOV_RADIUS = 15
FOV_ALGORITHM = libtcod.FOV_SHADOW
FOV_LIGHT_WALLS = True

COLORS = {
    'none': libtcod.Color(0, 0, 0),
    'dark_wall': libtcod.Color(255, 255, 255),
    'dark_ground': libtcod.Color(0, 50, 10),
    'player': libtcod.Color(0, 255, 255),
    'npc': libtcod.Color(100, 25, 80),
    'wall': libtcod.Color(192, 192, 192),
    'tree': libtcod.Color(34, 139, 34),
    'treebg': libtcod.Color(0, 30, 0),
    'wallbg': libtcod.Color(10, 10, 10),
    'dead': libtcod.Color(100, 20, 10)
}


class RenderOrder(Enum):
    REMAINS = 1
    ITEM = 2
    ACTOR = 3


ENTITY_DATA = load_dataset('data/entities.json')
data_list = fill_data_list('components')

MASTER_COMPONENT_DATASET = create_master_component_dataset(data_list)

DEFAULT_FONT = 'data/fonts/terminal16x16_gs_ro.png'
# console_map_ascii_code_to_font("∞", fontCharX, fontCharY)

TICK = 0

KEY = libtcod.Key()
# MOUSE = libtcod.Mouse()
