# This should possibly be somewhere that isn't config.
import config
import enum
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
        # self.speed = speed


class Dna:
    def __init__(self, component):
        # The DNA is just a holder that contains ONE component chosen on generation
        self.component = component


class Metadata:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Remains:
    def __init__(self):
        pass


class Spawner:
    def __init__(self):
        self.children = []
        self.child_type = 'child'


class Child:
    def __init__(self):
        self.parent = None


class Decay:
    def __init__(self):
        pass


class Renderable:
    def __init__(self, character: str, corpse_character: str, foreground_color: str, background_color: str, render_order: int):
        self.character = character
        # config.COLORS[args['Renderable']['color']]
        self.foreground_color = config.COLORS[foreground_color]
        self.background_color = config.COLORS[background_color]
        # self.background_color: libtcod.color = config.COLORS[args['Renderable']
        #                                                      ['background_color']]
        self.corpse_character = corpse_character
        self.render_order = config.RenderOrder[render_order].value
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


class AiRandomCalm:
    def __init__(self):
        pass


class AiRandomAgitated:
    def __init__(self, attacks: bool):
        self.attacks = attacks


class AiPredator:
    def __init__(self, radius: int):
        self.target = None
        self.radius = radius


class AiChild:
    def __init__(self):
        pass


class GenerateDna:
    def __init__(self):
        pass


class Light:
    def __init__(self, radius: int):
        self.radius = radius


class Hard:
    def __init__(self):
        pass


class Wood:
    def __init__(self):
        pass
