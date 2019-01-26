import tcod as libtcod
from config import config
from entity import Entity
from map_objects.game_map import GameMap
from components.mover import Mover


# Initialize player entities
player_mover_component = Mover()
player = Entity(int(config.SCREEN_HEIGHT / 2),
                int(config.SCREEN_HEIGHT / 2), '@', libtcod.white, "Player", blocks=True, mover=player_mover_component)

# An immobile entity that blocks
npc = Entity(int(config.SCREEN_HEIGHT / 2 - 5),
             int(config.SCREEN_HEIGHT / 2), '@', libtcod.yellow, "OTHER ALVARO", blocks=True)


# Initialize entity groups
entities = [npc, player]

game_map = GameMap(config.MAP_WIDTH, config.MAP_HEIGHT)
