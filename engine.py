import tcod as libtcod
from input_handlers import handle_keys
from config import config
from render_functions import clear_all, render_all
import game_objects
import action_handler
from entity import get_blocking_entities_at_location
from death_functions import *


# libtcod.sys_(30,30)
#libtcod.console_init_root(400, 400, "", True)


def run_game():

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(
            libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)
        render_all(config.con, game_objects.entities, game_objects.game_map,
                   config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.COLORS)

        libtcod.console_flush()

        clear_all(config.con, game_objects.entities)

        # TO BE WRAPPED OUT
        action = handle_keys(config.KEY)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        player_turn_results = []

        if move:
            dx, dy = move
            destination_x = game_objects.player.x + dx
            destination_y = game_objects.player.y + dy

            # if not gameobjects.game_map.is_blocked(destination_x, destination_y):
            target = get_blocking_entities_at_location(
                game_objects.entities, destination_x, destination_y)

            if target:
                attack_results = game_objects.player.fighter.attack(target)
                player_turn_results.extend(attack_results)
            else:
                game_objects.player.move(dx, dy)

                fov_recompute = True

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        for player_turn_result in player_turn_results:
            message = player_turn_result.get('message')
            dead_entity = player_turn_result.get('dead')

            if message:
                print(message)

            if dead_entity:
                if dead_entity == game_objects.player:
                    message, game_state = kill_player(dead_entity)
                else:
                    message = kill_monster(dead_entity)

                print(message)
        # TO BE WRAPPED OUT
