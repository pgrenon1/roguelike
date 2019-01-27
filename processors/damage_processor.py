from components.health import Health
from components.damage import Damage
from components.death import Death
from components.metadata import Metadata
import engine
import esper


class DamageProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (dam, hp) in self.world.get_components(Damage, Health):
            hp.current_health -= dam.damage
            engine.WORLD.remove_component(ent, Damage)
            print(hp.current_health)
            if (hp.current_health == 0):
                engine.WORLD.add_component(ent, Death())
