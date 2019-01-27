import esper
from components.speed import Speed
from components.position import Position


class MovementProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (vel, pos) in self.world.get_components(Speed, Position):
            pass
            # pos.x += vel.x
            # pos.y += vel.y
            # print("Current Position: {}".format((int(pos.x), int(pos.y))))
