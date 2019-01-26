import tcod as libtcod
from input_handlers import handle_keys
from config import config
from render_functions import clear_all, render_all
import gameobjects
import action_handler


#libtcod.sys_(30,30)
#libtcod.console_init_root(400, 400, "", True)


def run_game():

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)
        render_all(config.con, gameobjects.entities, gameobjects.game_map,
                   config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.COLORS)

        libtcod.console_flush()

        clear_all(config.con, gameobjects.entities)

        # TO BE WRAPPED OUT
        action = handle_keys(config.KEY)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move


        if action_handler.exit:

            if not gameobjects.game_map.is_blocked(gameobjects.player.x + dx, gameobjects.player.y + dy):
                gameobjects.player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        # TO BE WRAPPED OUT
