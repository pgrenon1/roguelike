# This should possibly be somewhere that isn't config.
from config import *
import sys
import inspect
import ast

# GETTING ALL THE COMPONENTS


class Block:
    def __init__(self, args):
        pass


class Dnaabsorber:
    def __init__(self, args):
        pass


class Damagedealer:
    def __init__(self, args):
        self.damage = args['damagedealer']['damage']


class Dna:
    def __init__(self, args):
        self.dna_raw = args
        self.dna_data = args['dna']['dna_data']


class Metadata:
    def __init__(self, args):
        self.name = args['metadata']['name']
        self.description = args['metadata']['description']


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Remains:
    def __init__(self):
        pass


class Spawner:
    def __init__(self, args):
        pass


class Speed:
    def __init__(self, args):
        self.speed = args['speed']


class Renderable:
    def __init__(self, args):
        self.character = args['renderable']['character']
        self.color = args['renderable']['color']
        self.background_color = args['renderable']['background_color']
        self.corpse_character = args['renderable']['corpse_character']
        #self.render_order = RenderOrder['renderable']['render_order'].value
#        self.foreground_color = args['render']['foreground_color']


class Movable:
    def __init__(self):
        pass


class PlayerTurn:
    def __init__(self):
        pass


class Airandomwalk:
    def __init__(self, args):
        pass


class Damage:
    def __init__(self, damage):
        self.damage = damage


class Death:
    def __init__(self):
        pass


class Generatedna:
    def __init__(self):
        pass


class Health:
    def __init__(self, args):
        self.max_health = args['health']['max_health']
        self.current_health = args['health']['current_health']


class Movement:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Spawnerevent:
    def __init__(self, args):
        pass
