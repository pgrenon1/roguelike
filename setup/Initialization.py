'''
We initialize the console and get all dependencies in this class.
We can refer to it
'''

import libtcodpy as libtcod
import setup.CONFIG

#############################################
# Initialization & Main Loop
#############################################


def InitializeConsole():
   libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
   libtcod.console_init_root(setup.CONFIG.SCREEN_WIDTH, setup.CONFIG.SCREEN_HEIGHT, 'python/libtcod tutorial', False)
   libtcod.sys_set_fps(setup.CONFIG.LIMIT_FPS)
   con = libtcod.console_new(setup.CONFIG.SCREEN_WIDTH, setup.CONFIG.SCREEN_HEIGHT)