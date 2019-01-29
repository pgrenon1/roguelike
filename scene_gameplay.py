import esper
import processors
from scene import Scene


class Gameplay(Scene):
    def __init__(self, world=None):
        print("Gameplay scene initialized")
        self.world = world

        self.processor_group = processors.PROCESSOR_GROUP
        self.change_processors('player_turn')

        if world is None:
            """We can use esper.CachedWorld to get the last world that was assigned to esper (not 100% sure)"""
            """We should set self.world = esper.World() to whatefver is the first scene we start with I think"""
            # esper.CachedWorld()
            self.world = esper.World()

    def change_processors(self, state):
        self.world_processors = self.processor_group[state]
        for processor_instance in self.processor_group[state]:
            processor_instance.world = self.world
            processor_instance.scene = self

    def update(self):
        self.world.process()
