import tcod as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
MAP_WIDTH = 40
MAP_HEIGHT = 40
FULLSCREEN = False

COLORS = {
    'dark_wall': libtcod.Color(255, 255, 255),
    'dark_ground': libtcod.Color(0, 10, 10),
    'player': libtcod.Color(255, 255, 255)
}

DEFAULT_FONT = 'data/fonts/terminal16x16_gs_ro.png'


libtcod.console_set_custom_font(DEFAULT_FONT, 2)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'ROGUELIKE', FULLSCREEN)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

KEY = libtcod.Key()
MOUSE = libtcod.Mouse()
