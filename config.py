import tcod as libtcod
from loader_functions.instantiator import *
from loader_functions.fetcher import *
import random

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 70
MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT - 20
FULLSCREEN = False

MASTER_SEED = None


COLORS = {
    'none': libtcod.black,
    'dark_wall': libtcod.Color(255, 255, 255),
    'dark_ground': libtcod.Color(0, 50, 10),
    'player': libtcod.Color(0, 255, 255),
    'npc': libtcod.Color(100, 25, 80),
    'wall': libtcod.Color(192, 192, 192),
    'tree': libtcod.Color(34, 139, 34),
    'treebg': libtcod.Color(0, 30, 0),
    'wallbg': libtcod.dark_grey
}

ENTITY_DATA = load_dataset('data/entities.json')
data_list = fetch_directory_components('components')
MASTER_COMPONENT_DATASET = create_master_component_dataset(data_list)

DEFAULT_FONT = 'data/fonts/terminal16x16_gs_ro.png'


libtcod.console_set_custom_font(DEFAULT_FONT, 2)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'ROGUELIKE', FULLSCREEN)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
# console_map_ascii_code_to_font("∞", fontCharX, fontCharY)

KEY = libtcod.Key()
MOUSE = libtcod.Mouse()
