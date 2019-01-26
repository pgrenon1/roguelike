import tcod as libtcod
from instantiator import *

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 70
MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT - 20
FULLSCREEN = False

COLORS = {
    'dark_wall': libtcod.Color(255, 255, 255),
    'dark_ground': libtcod.Color(0, 10, 10),
    'player': libtcod.Color(255, 255, 255)
}

ENTITY_DATA = load_dataset('data/gameobjects/entities.json')
COMPONENT_LIST_DATA = fetch_all_components()

DEFAULT_FONT = 'data/fonts/terminal16x16_gs_ro.png'


libtcod.console_set_custom_font(DEFAULT_FONT, 2)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'ROGUELIKE', FULLSCREEN)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
# console_map_ascii_code_to_font("∞", fontCharX, fontCharY)

KEY = libtcod.Key()
MOUSE = libtcod.Mouse()
