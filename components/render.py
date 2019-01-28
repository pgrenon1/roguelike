from render_functions import RenderOrder


class Render:
    def __init__(self, args):
        self.character = args['render']['character']
        self.color = args['render']['color']
        self.background_color = args['render']['background_color']
        self.corpse_character = args['render']['corpse_character']
        self.render_order = RenderOrder[args['render']['render_order']].value
