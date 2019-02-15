import tcod as libtcod
# from loader_functions.instantiator import *
# from loader_functions.fetcher import *
from enum import Enum
import random


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
PANEL_HEIGHT = 10
# Gives us the width of the characters we're using. Since they're square, we just need one of the two (width,height)
# If needed, just comment out and add WIDTH to the first one.
CHARACTER_RESOLUTION_WIDTH = libtcod.sys_get_char_size()[0]
CHARACTER_RESOLUTION_HEIGHT = libtcod.sys_get_char_size()[1]

PIXEL_SCREEN_WIDTH = SCREEN_WIDTH * CHARACTER_RESOLUTION_WIDTH
PIXEL_SCREEN_HEIGHT = SCREEN_HEIGHT * CHARACTER_RESOLUTION_HEIGHT

MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT
FULLSCREEN = False
VERBOSE_MODE = False

MASTER_SEED = None
LIBTCOD_RANDOM = None

FOV_RADIUS = 15
FOV_ALGORITHM = libtcod.FOV_BASIC
FOV_LIGHT_WALLS = True

SHOW_TOOLTIP = False

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


# ENTITY_DATA = load_dataset('data/entities.json')
# data_list = fill_data_list('components')

# MASTER_COMPONENT_DATASET = create_master_component_dataset(data_list)

DEFAULT_FONT = 'data/fonts/terminal16x16_gs_ro.png'
# console_map_ascii_code_to_font("∞", fontCharX, fontCharY)

TICK = 0

KEY = libtcod.Key()
# MOUSE = libtcod.Mouse()
