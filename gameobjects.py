import tcod as libtcod
from config import config
from entity import Entity
from map_objects.game_map import GameMap
from components.mover import Mover
from components.fighter import Fighter
from instantiator import *


# Initialize player entities
playerData = QueryDataSet(config.ENTITY_DATA,'player')
player = Entity(int(config.SCREEN_HEIGHT / 2),
                int(config.SCREEN_HEIGHT / 2), GetEntityData(playerData))


# An immobile entity that blocks
npcData = QueryDataSet(config.ENTITY_DATA,'npc')
npc = Entity(int(config.SCREEN_HEIGHT / 2 - 5),
             int(config.SCREEN_HEIGHT / 2), GetEntityData(npcData))

# Initialize entity groups
entities = [npc, player]
game_map = GameMap(config.MAP_WIDTH, config.MAP_HEIGHT)
