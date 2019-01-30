import components as c
import config
import esper
import tcod as libtcod

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
            # JE SAIS PAS NON PLUS POURQUOI IL UTILISE PRINT_ YA VRAIMENT BEAUCOUP DE DIFFERENTES FACON DE PRINT DES CHAR ON DIRAIT
            self.scene.con.print_(
                x=pos.x, y=pos.y, string=rend.character, bg_blend=libtcod.BKGND_NONE)

    def blit_console(self):
        self.scene.con.blit(
            dest=self.scene.manager.root_console,
            width=self.width,
            height=self.height
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
