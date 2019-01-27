import esper
from components.speed import Speed
from components.position import Position
from components.movement import Movement
from components.block import Block
import engine


class MovementProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (mov, pos) in self.world.get_components(Movement, Position):
            dx = pos.x + mov.x
            dy = pos.y + mov.y
            for other_ent, (other_pos, blo) in self.world.get_components(Position, Block):
                if other_pos.x == dx and other_pos.y == dy:
                    if blo.blocks:
                        
                        engine.WORLD.remove_component(ent, Movement)
                        return

            pos.x = dx
            pos.y = dy
            engine.WORLD.remove_component(ent, Movement)