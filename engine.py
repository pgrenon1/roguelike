import tcod as libtcod
from input_handlers import handle_keys
from config import config
from render_functions import clear_all, render_all
# import game_objects
import action_handler
# from entity import get_blocking_entities_at_location
from death_functions import *
import esper
from components.speed import Speed
from components.position import Position
from processors.movement_processor import MovementProcessor
from processors.render_processor import RenderProcessor
from components.render import Render
from components.metadata import Metadata
from instantiator import *

# libtcod.sys_(30,30)
#libtcod.console_init_root(400, 400, "", True)


def run_game():

    global WORLD

    # create world
    WORLD = esper.World()

    # create and add processors
    movement_processor = MovementProcessor()
    WORLD.add_processor(movement_processor)

    render_processor = RenderProcessor(config.con, libtcod.BKGND_NONE)
    WORLD.add_processor(render_processor)

    # create testing entities and add components to them
    playerData = query_dataset(config.ENTITY_DATA, 'player')
    playerComponents = get_entity_data(playerData)
    
    player = WORLD.create_entity()
 
    WORLD.add_component(player, playerComponents['position'])
    WORLD.add_component(player, playerComponents['render'])
    WORLD.add_component(player, playerComponents['metadata'])
    WORLD.add_component(player, playerComponents['speed'])

    entities = player
    
    while not libtcod.console_is_window_closed():
        WORLD.process()

        libtcod.sys_check_for_event(
            libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)

        libtcod.console_blit(config.con, 0, 0, config.SCREEN_WIDTH,
                             config.SCREEN_HEIGHT, 0, 0, 0)


        # render_all(config.con, entities, game_map,
        #            config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.COLORS)

        # libtcod.console_flush()

        # clear_all(config.con, entities)

        # action_handler.handle_player_actions()
