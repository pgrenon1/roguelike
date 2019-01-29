import tcod as libtcod
from input_handlers import handle_keys
import config
import action_handler
from death_functions import *
import esper
import sys
from components import (
    Renderable,
    Position,
    GenerateDna,
    DnaAbsorber,
    Block,
    Metadata
)
# from processors.movement_processor import MovementProcessor
# from processors.render_processor import RenderProcessor
# from processors.ai_processor import AiProcessor
# from processors.damage_processor import DamageProcessor
# from processors.death_processor import DeathProcessor
# from processors.dnagenerator_processor import DnaGeneratorProcessor
# from processors.dna_absorb_processor import DnaAbsorberProcessor
# from processors.spawner_processor import SpawnerProcessor
# from config import random
# from loader_functions.instantiator import *
# from loader_functions.entity_factory import *
from render_functions import RenderOrder
from rect import *
from config import COLORS


global TICK
TICK = 0

WORLD = esper.World()
global player
global npc


def run_game():

    world_created = False
    while not libtcod.console_is_window_closed():

        libtcod.sys_check_for_event(
            libtcod.EVENT_KEY_PRESS, config.KEY, config.MOUSE)

        libtcod.console_blit(config.con, 0, 0, config.SCREEN_WIDTH,
                             config.SCREEN_HEIGHT, 0, 0, 0)

        if not world_created:
            create_world()
            world_created = True

        render_all()

        action_handler.handle_player_actions()


def render_all():
    libtcod.console_clear(config.con)
    entities = []
    for ent, (ren, pos) in WORLD.get_components(Render, Position):
        entities.append(ent)

    sorted_entities = sorted(
        entities, key=lambda x: WORLD.component_for_entity(x, Render).render_order, reverse=True)

    for enti in sorted_entities:
        posi = WORLD.component_for_entity(enti, Position)
        rend = WORLD.component_for_entity(enti, Render)

        libtcod.console_put_char_ex(
            config.con, posi.x, posi.y, rend.character,
            COLORS[rend.color], COLORS[rend.background_color])

    libtcod.console_flush()


def create_world():
    print("create")
    # create world
    # WORLD = esper.World()
    global player
    # create and add processors
    movement_processor = MovementProcessor()
    WORLD.add_processor(movement_processor)

    # render_processor = RenderProcessor(config.con, libtcod.BKGND_NONE)
    # WORLD.add_processor(render_processor)

    ai_processor = AiProcessor()
    WORLD.add_processor(ai_processor)

    damage_processor = DamageProcessor()
    WORLD.add_processor(damage_processor)

    death_processor = DeathProcessor()
    WORLD.add_processor(death_processor)

    generate_dna_processor = DnaGeneratorProcessor()
    WORLD.add_processor(generate_dna_processor)

    absorb_dna_processor = DnaAbsorberProcessor()
    WORLD.add_processor(absorb_dna_processor)

    spawner_processor = SpawnerProcessor()
    WORLD.add_processor(spawner_processor)

    player = instantiate_entity(
        'player', config.MAP_WIDTH//2, config.MAP_HEIGHT//2)
    npc2 = instantiate_entity(
        'npc2', 4 + config.MAP_WIDTH//2, 5 + config.MAP_HEIGHT//2)
    npc = instantiate_entity(
        'npc', 1 + config.MAP_WIDTH//2, 2 + config.MAP_HEIGHT//2)

    noise = libtcod.noise_new(2, 5.0, 0.9)

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
                val = libtcod.noise_get_fbm(
                    noise, [x, y], 32.0, libtcod.NOISE_PERLIN)
                # print(val)
                if val > 0.8 and val < 1:
                    tree = instantiate_entity('tree', x, y)

   # entities = player,
    npc3 = instantiate_entity('npcdrop', 0, 1)

    # WORLD.process()

    # world_created = True
