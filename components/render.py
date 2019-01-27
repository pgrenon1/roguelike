from render_functions import RenderOrder


class Render:
    def __init__(self, args):
        self.character = args['render']['character']
        self.corpse_character = args['render']['corpse_character']
        self.render_order = RenderOrder[args['render']['render_order']].value
