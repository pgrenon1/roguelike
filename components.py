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


class Health:
    def __init__(self, args):
        self.max_health = args['health']['max_health']
        self.current_health = args['health']['current_health']


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
