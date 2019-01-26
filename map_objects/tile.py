class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """

    def __init__(self, meta_blocks):
        self.meta_blocks = meta_blocks
        self.entities = []
        self.block_sight = self.check_block_sight()

        # By default, if a tile is blocked, it also blocks sight
        # if block_sight is None:
        #     block_sight = blocked

        # self.block_sight = block_sight

    def check_block_sight(self):
        for entity in self.entities:
            if entity.block_sight:
                return True
        return False
