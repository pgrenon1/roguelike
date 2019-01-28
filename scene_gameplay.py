import esper
from scene import Scene


class Gameplay(Scene):
    def __init__(self, world):
        self.world = world

        if world is None:
            esper.CachedWorld()
