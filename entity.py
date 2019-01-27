# from config.config import *
from render_functions import RenderOrder


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        # print(data)
        # Attributes
#         self.char = data['character']
#         self.color = config.COLORS[data['color']]
#         self.render_order = RenderOrder[data['render_order']]
#         self.name = data['name']
#         self.description = data['description']
#         self.blocks = data['blocks']
#         # Componenents

#         if ('mover' in data['components']):
#             self.mover = data['components']['mover']
#             if self.mover:
#                 self.mover.owner = self
#         if ('fighter' in data['components']):
#             self.fighter = data['components']['fighter']
#             if self.fighter:
#                 self.fighter.owner = self

#     def move(self, dx, dy):
#         # Move the entity by a given amount
#         self.x += dx
#         self.y += dy


# def get_blocking_entities_at_location(entities, destination_x, destination_y):
#     for entity in entities:
#         if entity.blocks and entity.x == destination_x and entity.y == destination_y:
#             return entity

#     return None
