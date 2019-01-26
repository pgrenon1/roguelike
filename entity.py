from config.config import *


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        # Attributes
        self.char = data['attributes']['character']
        self.color = config.COLORS[data['attributes']['color']]
        self.name = data['attributes']['name']
        self.description = data['attributes']['description']
        self.blocks = data['attributes']['blocks']
        # Componenents

        if ('mover' in data['components']):
            self.mover = data['components']['mover']
            if self.mover:
                self.mover.owner = self
        if ('fighter' in data['components']):
            self.fighter = data['components']['fighter']
            if self.fighter:
                self.fighter.owner = self

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy


def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity

    return None
