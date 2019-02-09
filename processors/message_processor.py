import components as c
import esper
import config


class Message(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def populate_visibles(self):
        iterable = self.world.get_component(c.Renderable)

        for ent, ren in iterable:
            if ren.is_visible:
                config.VISIBLES.append(ren)

    def process(self):
        config.VISIBLES = []
        self.populate_visibles()


# Not implemented, but this should take care of checking if the entity is visible, format the message, etc.
def sendMessage(message, color, subjects):
    self.scene.messages.append(message, color)
