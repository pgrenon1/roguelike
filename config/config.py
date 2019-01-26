import tcod as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
MAP_WIDTH = 80
MAP_HEIGHT = 45

COLORS = {
    'dark_wall': libtcod.Color(255,255,255),
    'dark_ground': libtcod.Color(0,0,0)
}

DEFAULT_FONT = 'data/fonts/lucida10x10_gs_tc.png'

libtcod.console_set_custom_font(DEFAULT_FONT, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'libtcod tutorial revised', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

KEY = libtcod.Key()
MOUSE = libtcod.Mouse()

