class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x, y, char, color, , blocks=False, turn_taker=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.blocks = blocks
        self.turn_taker = turn_taker

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
