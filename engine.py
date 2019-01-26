import tcod as libtcod
from config import config

from entity import Entity
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import clear_all, render_all


def main():

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    player = Entity(int(config.config.SCREEN_HEIGHT / 2), int(config.SCREEN_HEIGHT / 2), '@', libtcod.white)
    npc = Entity(int(config.SCREEN_HEIGHT / 2 - 5), int(config.SCREEN_HEIGHT / 2), '@', libtcod.yellow)

    entities = [npc, player]

    libtcod.console_set_custom_font(
        'data/fonts/lucida10x10_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, 'libtcod tutorial revised', False)


    con = libtcod.console_new(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

    game_map = GameMap(config.MAP_WIDTH, config.MAP_HEIGHT)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, colors)


        libtcod.console_flush()

        clear_all(con, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move

            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
