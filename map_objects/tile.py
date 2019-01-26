class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """

    def __init__(self, meta_blocks):
        self.meta_blocks = meta_blocks
        self.entities = []
