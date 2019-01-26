import tcod as libtcod
from config import config
from entity import Entity
from map_objects.game_map import GameMap



#Initialize individual entities
player = Entity(int(config.SCREEN_HEIGHT / 2), int(config.SCREEN_HEIGHT / 2), '@', libtcod.white)
npc = Entity(int(config.SCREEN_HEIGHT / 2 - 5), int(config.SCREEN_HEIGHT / 2), '@', libtcod.yellow)




#Initialize entity groups
entities = [npc, player]

game_map = GameMap(config.MAP_WIDTH, config.MAP_HEIGHT)

