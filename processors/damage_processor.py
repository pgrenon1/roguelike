from components.health import Health
from components.damage import Damage
from components.death import Death
from components.metadata import Metadata
import engine


class DamageProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (dam, hp) in self.world.get_components(Damage, Health):
            hp.current_health -= dam.damage
            # print(engine.WORLD.try_component(ent, Metadata))
            if (hp.current_health == 0):
                engine.WORLD.add_component(ent, Death())
