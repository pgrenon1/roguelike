import tcod as libtcod
from input_handlers import handle_keys
from config import config
from render_functions import clear_all, render_all
import gameobjects
import action_handler

#libtcod.sys_force_fullscreen_resolution(400,400)
#libtcod.console_init_root(400, 400, "", True)


def run_game():

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)
        render_all(config.con, gameobjects.entities, gameobjects.game_map, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.COLORS)
        libtcod.console_flush()

        clear_all(config.con, gameobjects.entities)


        if action_handler.exit:
            return True

        if action_handler.fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
