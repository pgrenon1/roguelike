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
        iterable = list(self.world.get_components(c.Renderable, c.Position))
        iterable.sort(key=lambda row: row[1][0].render_order)
        for _, (rend, pos) in iterable:
            yield (rend, pos)

    def process(self):
        self.reveal_all()
        self.render_map()
        self.render_entity()
        # if self.targeting:
        #     self.render_target_cursor()
        self.blit_console()
        self.flush_console()
        self.clear_entity()

    def reveal_all(self):
        if self.scene.action.get('switch_reveal_all'):
            self.scene.reveal_all = not self.scene.reveal_all

    def render_map(self):
        if self.scene.fov_recompute:
            libtcod.console_clear(self.scene.con)
            for x in range(0, self.scene.game_map.width):
                for y in range(0, self.scene.game_map.height):
                    for fov_map in self.scene.fovs:
                        if libtcod.map_is_in_fov(fov_map, x, y):
                            libtcod.console_put_char(
                                self.scene.con, x, y, chr(250), libtcod.BKGND_ADD)
                    if libtcod.map_is_in_fov(self.scene.game_map, x, y):
                        libtcod.console_put_char(
                            self.scene.con, x, y, chr(250), libtcod.BKGND_ADD)

    def render_non_moving(self):
        pass

    def update_non_moving(self):
        pass

    def render_entity(self):
        entity_number = 0
        for (rend, pos) in self.get_entities():
            entity_number += 1
            if not self.scene.reveal_all:
                for fov_map in self.scene.fovs:
                    if libtcod.map_is_in_fov(fov_map, pos.x, pos.y):
                        libtcod.console_put_char_ex(
                            self.scene.con, pos.x, pos.y, rend.character, rend.color, rend.background_color)
                if libtcod.map_is_in_fov(self.scene.game_map, pos.x, pos.y):
                    libtcod.console_put_char_ex(
                        self.scene.con, pos.x, pos.y, rend.character, rend.color, rend.background_color)
            else:
                libtcod.console_put_char_ex(
                    self.scene.con, pos.x, pos.y, rend.character, rend.color, rend.background_color)
        self.scene.number_of_entities = entity_number

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
            # Mayabe format the most current action in some special way, like with "[{}]".format(var) or something
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

    # @staticmethod
    def _render_fps_counter(self, console):
        console.default_fg = libtcod.grey
        console.print_(
            x=config.MAP_WIDTH - 20, y=3,
            string='fps: %3d fps' % (libtcod.sys_get_fps()),
            bg_blend=libtcod.BKGND_NONE,
        )
        console.print_(
            x=config.MAP_WIDTH - 20, y=4,
            string='last frame: %2d ms' % (
                libtcod.sys_get_last_frame_length() * 1000.0,
            ),
            bg_blend=libtcod.BKGND_NONE,
        )
        console.print_(
            x=config.MAP_WIDTH - 20, y=5,
            string='elapsed: %4.2fs' % (libtcod.sys_elapsed_seconds()),
            bg_blend=libtcod.BKGND_NONE,
        )
        console.print_(
            x=config.MAP_WIDTH - 20, y=6,
            string='entities: %d' % (self.scene.number_of_entities),
            bg_blend=libtcod.BKGND_NONE
        )

    def process(self):
        self.blit_panel()
        self.render_message()
        self._render_fps_counter(self.scene.panel)
