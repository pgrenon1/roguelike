from .tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(False) for y in range(self.height)]
                 for x in range(self.width)]

        return tiles

    def is_blocked(self, x, y):
        tile = self.tiles[x][y]
        if tile.meta_blocks:
            return True
        for entity in tile.entities:
            if entity.blocks:
                return True
        return False

    def check_block_sight(self, x, y):
        tile = self.tiles[x][y]
        for entity in tile.entities:
            if entity.block_sight:
                return True
        return False
