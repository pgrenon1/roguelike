import tcod as libtcod
from config import config
from entity import Entity
from map_objects.game_map import GameMap
from components.mover import Mover
from components.fighter import Fighter
from instantiator import *
from map_objects.tile import Tile


# Initialize player entities
playerData = LoadDataSet('data/gameobjects/entities.json', 'player')
player = Entity(int(config.SCREEN_HEIGHT / 2),
                int(config.SCREEN_HEIGHT / 2), GetEntityData(playerData))


# An immobile entity that blocks
npcData = LoadDataSet('data/gameobjects/entities.json', 'npc')
npc = Entity(int(config.SCREEN_HEIGHT / 2 - 5),
             int(config.SCREEN_HEIGHT / 2), GetEntityData(npcData))


# Create the arrays of tiles
game_map = GameMap(config.MAP_WIDTH, config.MAP_HEIGHT)


wallData = LoadDataSet('data/gameobjects/entities.json', 'wall')
# Populate it with basic entites like walls


def CreateMapEntities():
    mapEntities = []

    for x in range(0, 5):
        wall = Entity(x, 1, GetEntityData(wallData))
        mapEntities.append(wall)
        game_map.tiles[x][1].entities.append(wall)

    return mapEntities


# Initialize a simple map
mapEntities = CreateMapEntities()

# Initialize entity groups
entities = [npc, player] + mapEntities
