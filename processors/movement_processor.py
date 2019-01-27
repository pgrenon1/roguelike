import esper
from components.speed import Speed
from components.position import Position
from components.movement import Movement
import engine


class MovementProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (mov, pos) in self.world.get_components(Movement, Position):
            pos.x += mov.x
            pos.y += mov.y
            engine.WORLD.remove_component(ent, Movement)
