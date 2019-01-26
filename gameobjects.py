import tcod as libtcod
from config import config
from entity import Entity
from map_objects.game_map import GameMap
from components.mover import Mover
from components.fighter import Fighter
from instantiator import *


# Initialize player entities
playerData = LoadDataSet('data/gameobjects/entities.json', 'player')
# player = GetEntityData(playerData)

player_mover_component = Mover()
player_fighter_component = Fighter(100, 0, 1)
player = Entity(int(config.SCREEN_HEIGHT / 2),
                int(config.SCREEN_HEIGHT / 2), GetEntityData(playerData))


# An immobile entity that blocks
npc_fighter_component = Fighter(2, 0, 0)
npc = Entity(int(config.SCREEN_HEIGHT / 2 - 5),
             int(config.SCREEN_HEIGHT / 2), '@', libtcod.yellow, "OTHER ALVARO", blocks=True, fighter=npc_fighter_component)

# Initialize entity groups
entities = [npc, player]
game_map = GameMap(config.MAP_WIDTH, config.MAP_HEIGHT)
