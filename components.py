# This should possibly be somewhere that isn't config.
from config import *
import sys
import inspect
import ast

# GETTING ALL THE COMPONENTS


class Collidable:
    def __init__(self):
        pass


class Stats:
    def __init__(self, args):
        self.max_health = args['Stats']['max_health']
        self.health = args['Stats']['health']
        self.defense = args['Stats']['defense']
        self.damage = args['Stats']['damage']


class Dna:
    def __init__(self, component):
        # The DNA is just a holder that contains ONE component chosen on generation
        self.component = component


class DnaAbsorber:
    def __init__(self):
        pass


class Metadata:
    def __init__(self, args):
        self.name = args['Metadata']['name']
        self.description = args['Metadata']['description']


class Position:
    def __init__(self, x, y):
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
    def __init__(self, args):
        if RepresentsInt(args['Renderable']['character']):
            self.character = chr(int(args['Renderable']['character']))
        else:
            self.character = args['Renderable']['character']
        self.color = config.COLORS[args['Renderable']['color']]
        self.background_color = config.COLORS[args['Renderable']
                                              ['background_color']]
        self.corpse_character = args['Renderable']['corpse_character']
        self.corpse_color = config.COLORS['dead']
        self.render_order = config.RenderOrder[args['Renderable']
                                               ['render_order']].value
        self.is_visible = True
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


"""It might be possible and preferable to use inheritance to make the move_enemy simpler!"""


class AiRandomCalm:
    def __init__(self):
        pass


class AiRandomAgitated:
    def __init__(self, args):
        self.attacks = args['AiRandomAgitated']['attacks']


class AiPredator:
    def __init__(self, args):
        self.target = None
        self.range = args['AiPredator']['range']


class AiChild:
    def __init__(self):
        pass


class Death:
    def __init__(self):
        pass


class GenerateDna:
    def __init__(self):
        pass


class Light:
    def __init__(self, args):
        self.radius = args['Light']['radius']

# These are just a set of components that don't do much. Just using them to test Absorb + Generation


class Hard:
    def __init__(self):
        pass


class Wood:
    def __init__(self):
        pass


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
