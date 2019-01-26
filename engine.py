import tcod as libtcod
from input_handlers import handle_keys
from config import config
from render_functions import clear_all, render_all
import gameobjects
import action_handler
from entity import get_blocking_entities_at_location


def run_game():
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(
            libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)
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
            destination_x = gameobjects.player.x + dx
            destination_y = gameobjects.player.y + dy

            if not gameobjects.game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(
                    gameobjects.entities, destination_x, destination_y)

                if target:
                    print('You kick the ' + target.name +
                          ' in the shins, much to its annoyance!')
                else:
                    gameobjects.player.move(dx, dy)

                    fov_recompute = True

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        # TO BE WRAPPED OUT
