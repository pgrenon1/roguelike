import tcod as libtcod
from input_handlers import handle_keys
from config import config
from render_functions import clear_all, render_all
import game_objects
import action_handler
from entity import get_blocking_entities_at_location
from death_functions import *
import esper
from components.velocity import Velocity
from components.position import Position
from processors.movement_processor import MovementProcessor
from processors.rendering_processor import RenderingProcessor


# libtcod.sys_(30,30)
#libtcod.console_init_root(400, 400, "", True)


def run_game():

    global WORLD

    # create world
    WORLD = esper.World()

    # create and add processors
    movement_processor = MovementProcessor()
    WORLD.add_processor(movement_processor)

    # create testing entities and add components to them
    player = WORLD.create_entity()
    WORLD.add_component(player, Velocity(x=0.9, y=1.2))
    WORLD.add_component(player, Position(x=5, y=5))

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(
            libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)
        render_all(config.con, game_objects.entities, game_objects.game_map,
                   config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.COLORS)

        libtcod.console_flush()

        clear_all(config.con, game_objects.entities)

        action_handler.handle_player_actions()
