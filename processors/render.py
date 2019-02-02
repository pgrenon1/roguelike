import components as c
import config
import esper
import tcod as libtcod
import textwrap

"""Le processeur pour render. more details below"""


class RenderConsole(esper.Processor):

    scene = None
    # targeting est pour une state spéciale qui n'est pas encore implemented
    # def __init__(self, targeting=False):

    def __init__(self):
        super().__init__()
        # self.targeting = targeting
        self.width = config.MAP_WIDTH
        self.height = config.MAP_HEIGHT

    def get_entities(self):
        # not optimal, but it works! === not Phil's comment!
        iterable = list(self.world.get_components(c.Renderable, c.Position))
        # I confess I don't understand row[1][0] yet
        """J'AI COMMENT OUT CETTE PARTIE TO MAKE IT WORK, SORRY!!!!"""
        iterable.sort(key=lambda row: row[1][0].render_order)
        for _, (rend, pos) in iterable:
            yield (rend, pos)

    def process(self):
        # self.render_map() NO MAP YET.
        self.render_entity()
        # if self.targeting:
        #     self.render_target_cursor()
        self.blit_console()
        self.flush_console()
        self.clear_entity()

    # checks enverything that has a rend and pos and renders it
    def render_entity(self):
        for (rend, pos) in self.get_entities():
            # if self.scene.game_map.fov[pos.y, pos.x]:
            # self.scene.con.default_fg = rend.fg
            # self.scene.con.default_bg = rend.bg
            # # JE SAIS PAS NON PLUS POURQUOI IL UTILISE PRINT_ YA VRAIMENT BEAUCOUP DE DIFFERENTES FACON DE PRINT DES CHAR ON DIRAIT
            # self.scene.con.print_(
            #     x=pos.x, y=pos.y, string=rend.character, bg_blend=rend.BKGND_NONE)
            libtcod.console_put_char_ex(
                self.scene.con, pos.x, pos.y, rend.character, rend.color, rend.background_color)

    def blit_console(self):
        self.scene.con.blit(
            dest=self.scene.manager.root_console,
            width=self.width,
            height=self.height-config.PANEL_HEIGHT
        )

    def flush_console(self):
        libtcod.console_flush()

    def clear_entity(self):
        for (rend, pos) in self.get_entities():
            # if self.scene.game_map.fov[pos.y, pos.x]: NO FOV YET
            # write an empty char, ca c'est pour pas avoir une genre de trainée.
            # ca change rien si personne bouge, mais si qqun bouge, on doit l'effacer de là ou il était
            self.scene.con.print_(
                x=pos.x, y=pos.y, string=' ', bg_blend=libtcod.BKGND_NONE)


class RenderPanel(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()
        self.display_message = []
        self.msg_width = config.SCREEN_WIDTH
        self.msg_height = config.PANEL_HEIGHT - 1
        self.msg_x = 3
        self.idx = []
        self.col = []
        self.idx_ = [self.idx.append(x) for x in range(self.msg_height)]
        self.col_ = [self.col.append(libtcod.Color(
            10*(y), y, 255)) for y in range(0, 255, 255//self.msg_height)]

    def render_message(self):
        if len(self.scene.messages) > 0:
            while self.scene.messages:

                message, color = self.scene.messages.popleft()
                new_msg_lines = textwrap.wrap(message, self.msg_width)
        # for line in self.scene.messages:

                for line in new_msg_lines:
                    if len(self.display_message) == self.msg_height-1:
                        self.display_message.pop(0)
                    self.display_message.append((line, color))
        for y, (message, color) in enumerate(self.display_message):

            color_map = libtcod.color_gen_map(self.col, self.idx)
            self.scene.panel.default_fg = color_map[y]

            libtcod.console_print_ex(
                self.scene.panel, self.msg_x, y+1, libtcod.BKGND_NONE, libtcod.LEFT,  message)

    def blit_panel(self):
        self.scene.panel.blit(
            dest=self.scene.manager.root_console,
            dest_x=0,
            dest_y=config.SCREEN_HEIGHT - config.PANEL_HEIGHT,
            src_x=0,
            src_y=0,
            width=self.msg_width,
            height=config.PANEL_HEIGHT,
            fg_alpha=1.0,
            bg_alpha=1.0,
            key_color=None)
        self.scene.panel.default_bg = libtcod.darkest_blue
        self.scene.panel.clear()

    def process(self):

        self.render_message()
        self.blit_panel()
