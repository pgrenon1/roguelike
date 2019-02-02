# import esper

# from components import (
#     Speed,
#     Position,
#     Render,
#     Dna,
#     GenerateDna,
#     Movement,
#     Block,
#     Death,
#     Remains,
#     RenderOrder,
#     AiRandomwalk
# )

# from render_functions import RenderOrder
# import engine


# class DeathProcessor(esper.Processor):
#     def __init__(self):
#         super().__init__()

    



#     # This is a duplicate func  from dna_absorb. We might wanna decline
#     # from a top class?
#     def try_removing(self, entity, component):
#         if self.world.has_component(entity, component):
#             self.world.remove_component(entity, component)

#     def process_death(self):
#         for ent, (death, ren) in self.world.get_components(Death, Render):
#             ren.character = ren.corpse_character
#             ren.render_order = RenderOrder.REMAINS.value

#             if self.world.has_component(ent, AiRandomwalk):
#                 self.world.remove_component(ent, AiRandomwalk)

#             self.world.add_component(ent, Remains())
#             self.world.add_component(ent, GenerateDna())

#             block = engine.WORLD.try_component(ent, Block)
#             if block:
#                 engine.WORLD.remove_component(ent, type(next(block)))

#             # Not really sure how to stop the movement of a corpse
#             # I think our approach on moven needs to be rethought

#             # movement = engine.WORLD.try_component(ent, AiRandomwalk)
#             # if movement:
#             #     engine.WORLD.remove_component(ent, type(next(movement)))

#             engine.WORLD.remove_component(ent, Death)

#     def process(self):
#         self.process_death()
#         self.process_dnageneration()
