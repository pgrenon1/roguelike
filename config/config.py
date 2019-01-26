import tcod as libtcod

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 50
MAP_WIDTH = 10
MAP_HEIGHT = 10

COLORS = {
    'dark_wall': libtcod.Color(255,255,255),
    'dark_ground': libtcod.Color(0,0,50)
}

DEFAULT_FONT = 'data/fonts/terminal16x16_gs_ro.png'

libtcod.console_set_custom_font(DEFAULT_FONT, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'ROGUELIKE', True)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

KEY = libtcod.Key()
MOUSE = libtcod.Mouse()
