import components as c
import config
import esper
import tcod as libtcod
import textwrap
import config


"""Le processeur pour render. more details below"""


class RenderConsole(esper.Processor):

    scene = None
    # targeting est pour une state spéciale qui n'est pas encore implemented
    # def __init__(self, targeting=False):

    def __init__(self):
        super().__init__()
        self.width = config.MAP_WIDTH
        self.height = config.MAP_HEIGHT
        self.entities = []

    def get_entities(self):
        iterable = list(self.world.get_components(c.Renderable, c.Position))
        iterable.sort(key=lambda row: row[1][0].render_order)
        for entity, (rend, pos) in iterable:
            yield entity, (rend, pos)

    def process(self):
        self.entities = self.get_entities()
        self.reveal_all()
        self.render_map()
        self.render_entity()
        self.blit_console()

        # self.flush_console()
        self.clear_entity()

    def reveal_all(self):
        if self.scene.action.get('switch_reveal_all'):
            self.scene.reveal_all = not self.scene.reveal_all

    def render_map(self):
        if self.scene.fov_recompute:
            # libtcod.console_clear(self.scene.con)
            for x in range(0, self.scene.game_map.width):
                for y in range(0, self.scene.game_map.height):
                    for fov_map in self.scene.fovs:
                        if libtcod.map_is_in_fov(fov_map, x, y):
                            libtcod.console_put_char(
                                self.scene.con, x, y, chr(250), libtcod.BKGND_ADD)
                    if libtcod.map_is_in_fov(self.scene.game_map, x, y):
                        libtcod.console_put_char(
                            self.scene.con, x, y, chr(250), libtcod.BKGND_ADD)
                    elif self.scene.game_map.explored.item((y, x)):
                        libtcod.console_put_char(
                            self.scene.con, x, y, ' ', libtcod.BKGND_ADDALPHA(0.5))

    def render_entity(self):
        entity_number = 0
        for entity, (rend, pos) in self.entities:
            entity_number += 1
            if not self.scene.reveal_all:
                for fov_map in self.scene.fovs:
                    if libtcod.map_is_in_fov(fov_map, pos.x, pos.y):
                        bg = rend.background_color + libtcod.darkest_grey
                        fg = rend.color + libtcod.darkest_grey
                        libtcod.console_put_char_ex(
                            self.scene.con, pos.x, pos.y, rend.character, fg, bg)

                if libtcod.map_is_in_fov(self.scene.game_map, pos.x, pos.y):
                    bg = rend.background_color + libtcod.darkest_grey
                    fg = rend.color + libtcod.darkest_grey
                    libtcod.console_put_char_ex(
                        self.scene.con, pos.x, pos.y, rend.character, fg, bg)
                elif self.scene.game_map.explored.item((pos.y, pos.x)):
                    if not self.world.has_component(entity, c.Movable):
                        libtcod.console_put_char_ex(
                            self.scene.con, pos.x, pos.y, rend.character, rend.color,  rend.background_color)

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
        for (rend, pos) in self.entities:
            # if self.scene.game_map.fov[pos.y, pos.x]: NO FOV YET
            # write an empty char, ca c'est pour pas avoir une genre de trainée.
            # ca change rien si personne bouge, mais si qqun bouge, on doit l'effacer de là ou il était
            self.scene.con.print_(
                x=pos.x, y=pos.y, string=' ', bg_blend=libtcod.BKGND_NONE)


class RenderTooltip(esper.Processor):

    def __init__(self):
        super().__init__()
        self.mouse_x = 0
        self.offset_x = 1
        self.offset_y = 1
        self.mouse_y = 0
        self.mouse_px = 0
        self.mouse_py = 0
        self.draw_x = 0
        self.draw_y = 0
        self.width = 1
        self.height = 1
        self.show_tooltip = config.SHOW_TOOLTIP
        self.current_message = []

    def get_entities(self):
        entities = self.world.get_components(
            c.Position,
            c.Metadata,
            c.Renderable
        )

        for entity, (pos, meta_data, _) in entities:
            yield (entity, pos, meta_data)

    def get_entity_information(self):
        # ents = []
        for ent, pos, meta_data in self.get_entities():
            if(pos.x, pos.y) == (self.mouse_x, self.mouse_y):
                # ents.append(ent)
                # # We make sure we're only describing the entity on top.
                # Not sure how doe
                # if(ent == ents[0]):

                self.current_message.append(meta_data.name)
                self.current_message.append(meta_data.description)
                self.width = len(meta_data.description)
                self.height = len(self.current_message)

    def handle_tooltip_offset(self, mouse_x, mouse_y):
        """This changes the orientation of the tooltip depending on which side of the screen we're in.
           Prevents it from going outside of the screen"""
        if mouse_x > config.SCREEN_WIDTH//2:
            mouse_x = mouse_x - self.width
            mouse_x = mouse_x + self.offset_x

        mouse_y = mouse_y + self.offset_y

        return mouse_x, mouse_y

    def handle_mouse_position(self):
        """ . We need to transform pixel coordinates into tiles.
            . We also need to limit the coordinates to ones in the screen
            . We also need to know what the last pixel coordinate was before the current update"""

        self.mouse_x = int((libtcod.mouse_get_status().x //
                            config.CHARACTER_RESOLUTION_WIDTH/2))

        self.mouse_y = int((libtcod.mouse_get_status().y //
                            config.CHARACTER_RESOLUTION_HEIGHT/2))

        self.mouse_px = int((libtcod.mouse_get_status().dx //
                             config.CHARACTER_RESOLUTION_WIDTH/2))
        self.mouse_py = int((libtcod.mouse_get_status().dy //
                             config.CHARACTER_RESOLUTION_HEIGHT/2))

        if(self.mouse_x > config.SCREEN_WIDTH):
            self.mouse_x = config.SCREEN_WIDTH
        elif(self.mouse_x < 0):
            self_mouse_x = 0
        elif(self.mouse_y > config.SCREEN_HEIGHT):
            self.mouse_y = config.SCREEN_HEIGHT
        elif(self.mouse_y < 0):
            self.mouse_y = 0

    def render_tooltip(self):
        self.get_entity_information()

        self.draw_x, self.draw_y = self.handle_tooltip_offset(
            self.mouse_x, self.mouse_y)

        line_y = 0
        for message in self.current_message:
            libtcod.console_print_ex(
                self.scene.tooltip, 0, line_y, libtcod.BKGND_NONE, libtcod.LEFT, message)
            line_y += 1

        if self.mouse_x != self.mouse_px or self.mouse_y != self.mouse_py:
            self.current_message = []
            y = 0

    def reveal_tooltip(self):
        if self.scene.mouse.rbutton_pressed:
            self.show_tooltip = not self.show_tooltip

    def blit_tooltip(self):
        self.scene.tooltip.blit(
            dest=self.scene.manager.root_console,
            dest_x=self.draw_x,
            dest_y=self.draw_y,
            src_x=0,
            src_y=0,
            width=self.width,
            height=self.height,
            fg_alpha=0.9,
            bg_alpha=0.8,
            key_color=None)
        self.scene.tooltip.default_bg = libtcod.pink
        self.scene.tooltip.clear()

    def process(self):
        # self.get_entities()
        # self.get_entity_information()

        self.reveal_tooltip()
        if(self.show_tooltip):
            self.handle_mouse_position()
            self.render_tooltip()
            self.blit_tooltip()


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
            fg_alpha=1,
            bg_alpha=1,
            key_color=None)
        self.scene.panel.default_bg = libtcod.darkest_blue
        self.scene.panel.clear()

    def show_debug(self):
        if self.scene.action.get('switch_show_debug'):
            self.scene.show_debug = not self.scene.show_debug

            # @staticmethod
    def _render_fps_counter(self, console):
        if(self.scene.show_debug):
            console.default_fg = libtcod.white
            console.print_(
                x=config.MAP_WIDTH - 20, y=2,
                string="tick: {}".format(config.TICK), bg_blend=libtcod.BKGND_NONE)
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
            console.print_(
                x=config.MAP_WIDTH - 20, y=7,
                string="seed: {}".format(config.MASTER_SEED),
                bg_blend=libtcod.BKGND_NONE
            )

    def process(self):

        self.render_message()
        self._render_fps_counter(self.scene.panel)
        self.show_debug()
        self.blit_panel()
