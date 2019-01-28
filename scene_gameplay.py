import esper
import processors
from scene import Scene

from components.render import Render
from components.position import Position


class Gameplay(Scene):
    def __init__(self, world=None):
        print("Gameplay scene initialized")
        self.processor_group = processors.PROCESSOR_GROUP
        self.world = world

        if world is None:
            """We can use esper.CachedWorld to get the last world that was assigned to esper (not 100% sure)"""
            """We should set self.world = esper.World() to whatefver is the first scene we start with I think"""
            # esper.CachedWorld()
            self.world = esper.World()

        self.add_processors()
        self.change_processors('player_turn')

        # !!PLACEHOLDER ENTITY
        # JUST FOR TESTING THE ARCHITECTURE!!
        self.world.create_entity(Render({
            'render': {
                "character": "@",
                "corpse_character": "%",
                "render_order": "ACTOR",
                "color": "player",
                "background_color": "none"
            }}),
            Position(0, 0))

    def change_processors(self, state):
        self.world_processors = self.processor_group[state]
        for processor_instance in self.processor_group[state]:
            processor_instance.world = self.world
            processor_instance.scene = self

    def add_processors(self):
        for num, state in enumerate(self.processor_group):
            for proc in self.processor_group[state]:
                # missing priority argument here, not sure how to get it to work
                self.world.add_processor(proc)
                proc.scene = self

    def update(self):
        self.world.process()
