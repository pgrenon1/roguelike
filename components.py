from render_functions import RenderOrder


class Block:
    def __init__(self, args):
        pass


class DnaAbsorber:
    def __init__(self, args):
        pass


class DamageDealer:
    def __init__(self, args):
        self.damage = args['damage_dealer']['damage']


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
        self.character = args['render']['character']
        self.color = args['render']['color']
        self.background_color = args['render']['background_color']
        self.corpse_character = args['render']['corpse_character']
        self.render_order = RenderOrder[args['render']['render_order']].value
        # self.foreground_color = args['render']['foreground_color']


class Movable:
    def __init__(self):
        pass


class PlayerTurn:
    def __init__(self):
        pass


class AiRandomwalk:
    def __init__(self, args):
        pass


class Damage:
    def __init__(self, damage):
        self.damage = damage


class Death:
    def __init__(self):
        pass


class Dna:
    def __init__(self, args):
        self.dna_raw = args
        self.dna_data = args['dna']['dna_data']


class GenerateDna:
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


class SpawnerEvent:
    def __init__(self, args):
        pass
