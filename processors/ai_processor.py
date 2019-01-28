import esper
from components.speed import Speed
from components.position import Position
from components.movement import Movement
from components.ai_randomwalk import AiRandomwalk
import engine
import random
from loader_functions.entity_factory import instantiate_entity
from components.damage_dealer import DamageDealer
from components.damage import Damage
from components.block import Block
import config


class AiProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent,  (ai, pos) in self.world.get_components(AiRandomwalk, Position):
            # Seems to me like the AI should use the movement component, since that one
            # checks for block? Or else we'd be duplicating code
            # I think the AIprocessor should be a place where we use the components attached to the NPC
            # this AI is attached to.
            # It doesn't make sense to make things move in this class, it's against the design of the system I think?

            """ ouais j'avais pas verifier ce processor. je l'aurais fait comme tu dit en effet. ça aurait du pas être une interaction
            avec le component Position, mais bien juste d'ajouter un Movement flag
            la fonction get_components va pouvoir servir ici pas juste à faire interagir des pairs de components,
            ca peut aussi prendre n'importe quel nombre d'arguments, so tu peux get tout les components.
            maintenant, ça va etre de determiner comment stocker et coder les comportements. genre est-ce que le ai_processor
            va contenir un genre de switch case? il me semble que ça serait bizarre? maybe not"""

            dx = 0
            dy = 0

            if pos.x >= config.MAP_WIDTH:
                dx -= 1
            elif pos.x <= 0:
                dx += 1
            elif pos.y >= config.MAP_HEIGHT:
                dy -= 1
            elif pos.y <= 0:
                dy += 1
            else:
                dx += random.randint(-1, 1)
                dy += random.randint(-1, 1)

            self.world.add_component(ent, Movement(dx, dy))
        # else:
        #    pass
            # for other_ent, (other_pos, blo) in self.world.get_components(Position, Block):
            #     if other_pos.x == dx and other_pos.y == dy:
            #         if blo:
            #             damage = engine.WORLD.component_for_entity(ent,
            #                                                        DamageDealer).damage
            #             if damage:
            #                 engine.WORLD.add_component(
            #                     other_ent, Damage(damage))
            #         return
            # pos.x = dx
            # pos.y = dy

            # engine.WORLD.remove_component(ent, AiRandomwalk)
