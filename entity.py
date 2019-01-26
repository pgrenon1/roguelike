class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        print(data[0]['character'])

        # self.char = data['attributes']['character']
        # self.name = data['attributes']['name']
        # self.description = data['attributes']['description']
        # self.blocks = data['attributes']['blocks']
        # self.mover = data['components']['mover']

    # def __init__(self, x, y, char, color, name, description, blocks=False, mover=None, fighter=None):
    #     self.x = x
    #     self.y = y
    #     self.char = char
    #     self.color = color
    #     self.name = name
    #     self.blocks = blocks
    #     self.mover = mover
    #     self.fighter = fighter

    #    if self.mover:
    #         self.mover.owner = self

    #     if self.fighter:
    #         self.fighter.owner = self

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy


def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity

    return None
