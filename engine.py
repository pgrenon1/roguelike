import tcod as libtcod
from input_handlers import handle_keys
from config import config
import action_handler
from death_functions import *
import esper
import sys
from components.speed import Speed
from components.position import Position
from processors.movement_processor import MovementProcessor
from processors.render_processor import RenderProcessor
from processors.ai_processor import AiProcessor
from processors.damage_processor import DamageProcessor
from processors.death_processor import DeathProcessor
from processors.generatedna_processor import GenerateDnaProcessor
from processors.dna_absorb_processor import DnaAbsorberProcessor
from components.render import Render
from config import random
from components.generate_dna import GenerateDna
from components.dna_absorber import DnaAbsorber
from components.block import Block
from components.metadata import Metadata
from loader_functions.instantiator import *
from loader_functions.entity_factory import *
from render_functions import RenderOrder
from rect import *


# libtcod.sys_(30,30)
# libtcod.console_init_root(400, 400, "", True)


def run_game():

    global WORLD
    global player
    global npc

    # create world
    WORLD = esper.World()

    # create and add processors
    movement_processor = MovementProcessor()
    WORLD.add_processor(movement_processor)

    render_processor = RenderProcessor(config.con, libtcod.BKGND_NONE)
    WORLD.add_processor(render_processor)

    ai_processor = AiProcessor()
    WORLD.add_processor(ai_processor)

    damage_processor = DamageProcessor()
    WORLD.add_processor(damage_processor)

    death_processor = DeathProcessor()
    WORLD.add_processor(death_processor)

    generate_dna_processor = GenerateDnaProcessor()
    WORLD.add_processor(generate_dna_processor)

    absorb_dna_processor = DnaAbsorberProcessor()
    WORLD.add_processor(absorb_dna_processor)

    player = instantiate_entity('player', 0, 0)
    npc2 = instantiate_entity('npc2', 1, 0)
    npc = instantiate_entity('npc', 1, 1)

    noise = libtcod.noise_new(2)
    libtcod.noise_set_type(noise, libtcod.NOISE_SIMPLEX)

    room = Rect(20, 20, 10, 15)
    # test
    # level generation DUMMY
    for x in range(0, config.MAP_WIDTH):
        for y in range(0, config.MAP_HEIGHT):
            if x in range(room.x1, room.x2) and y in range(room.y1, room.y2):
                if x not in range(room.x1+1, room.x2-1):
                    wall = instantiate_entity('wall', x, y)
                if y not in range(room.y1+1, room.y2-1):
                    wall = instantiate_entity('wall', x, y)
            else:
                val = noise.get_point(x, y)
                # print(val)
                if val > 0.4:
                    tree = instantiate_entity('tree', x, y)

   # entities = player,
    npc3 = instantiate_entity('npcdrop', 0, 1)

    while not libtcod.console_is_window_closed():
        WORLD.process()

        libtcod.sys_check_for_event(
            libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)

        libtcod.console_blit(config.con, 0, 0, config.SCREEN_WIDTH,
                             config.SCREEN_HEIGHT, 0, 0, 0)

        # WORLD.process()

        action_handler.handle_player_actions()
