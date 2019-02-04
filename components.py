# This should possibly be somewhere that isn't config.
from config import *
import sys
import inspect
import ast

# GETTING ALL THE COMPONENTS


class Collidable:
    def __init__(self):
        pass


class DnaAbsorber:
    def __init__(self):
        pass


class Stats:
    def __init__(self, max_health: int, health: int, defense: int, damage: int):
        self.max_health = max_health
        self.health = health
        self.defense = defense
        self.damage = damage
        self.speed = speed


# class Dna:
#     def __init__(self, args):
#         """This should just be created at run time, because the components of a entity might change"""
#         self.dna_raw = args
#         self.dna_data = args['Dna']['dna_data']


class Metadata:
    def __init__(self, name: str, description: str):
        self.name: str = args['Metadata']['name']
        self.description: str = args['Metadata']['description']


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Remains:
    def __init__(self):
        pass


class Spawner:
    def __init__(self):
        pass


class Renderable:
    def __init__(self, character: str, corpse_character: str, color: str, background_color: str, render_order: int):
        self.character = character
        # config.COLORS[args['Renderable']['color']]
        self.color = color
        self.background_color = background_color
        # self.background_color: libtcod.color = config.COLORS[args['Renderable']
        #                                                      ['background_color']]
        self.corpse_character = corpse_character
        self.render_order = render_order
        # config.RenderOrder[args['Renderable']['render_order']].value
#        self.foreground_color = args['render']['foreground_color']


class Movable:
    def __init__(self):
        pass


class PlayerTurn:
    def __init__(self):
        pass


class EnemyTurn:
    def __init__(self):
        pass


class AiRandomWalk:
    def __init__(self):
        pass


class GenerateDna:
    def __init__(self):
        pass


class SpawnerEvent:
    def __init__(self):
        pass
