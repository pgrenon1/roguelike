import esper
from components import (
    Speed,
    Position,
    Movement,
    Block,
    DamageDealer,
    Damage
)
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
                    if blo:
                        damage = engine.WORLD.component_for_entity(ent,
                                                                   DamageDealer).damage
                        if damage:
                            engine.WORLD.add_component(
                                other_ent, Damage(damage))
                    engine.WORLD.remove_component(ent, Movement)
                    return

            pos.x = dx
            pos.y = dy
            engine.WORLD.remove_component(ent, Movement)
