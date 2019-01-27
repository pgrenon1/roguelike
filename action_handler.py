from input_handlers import *
from config import config
import engine
from components.position import Position
from components.movement import Movement
from components.ai_randomwalk import Ai_randomwalk


def handle_player_turn_results(player_turn_results):
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


def handle_player_actions():
    action = handle_keys(config.KEY)

    if action:

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        player_turn_results = []

        if move:
            player_position_component = engine.WORLD.component_for_entity(
                engine.player, Position)

            dx, dy = move
            destination_x = player_position_component.x + dx
            destination_y = player_position_component.y + dy

            engine.WORLD.add_component(engine.player, Movement(dx, dy))
            engine.WORLD.add_component(engine.npc, Ai_randomwalk(None))

            # does is that spot blocked

            # is that thing a fighter

            # # if not gameobjects.game_map.is_blocked(destination_x, destination_y):
            # target = get_blocking_entities_at_location(
            #     game_objects.entities, destination_x, destination_y)

            # if target:
            #     attack_results = game_objects.player.fighter.attack(target)
            #     player_turn_results.extend(attack_results)
            # else:
            #     game_objects.player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        engine.WORLD.process()

        handle_player_turn_results(player_turn_results)
