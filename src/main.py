import processor
import components as c
# import level
import config
from factory import Factory
from game_map import GameMap

import collections
import esper
import tcod
import pickle


class SceneManager:

    def __init__(self, state='menu'):
        tcod.console_set_custom_font(
            fontFile=config.FONT_PATH,
            flags=config.FONT_FLAG
        )
        self.root_console = tcod.console_init_root(
            w=config.SCREEN_WIDTH,
            h=config.SCREEN_HEIGHT,
            title=config.TITLE,
            renderer=tcod.RENDERER_GLSL
        )
        self.scenes = {
            'menu': MainMenu(),
            'game': Game(),
        }
        self.current_scene = self.scenes[state]
        Scene.manager = self

    def change_scene(self, state):
        self.current_scene = self.scenes[state]

    def run(self):
        while not tcod.console_is_window_closed():
            self.current_scene.update()


class Scene:
    manager = None

    def update(self):
        raise NotImplementedError


class Game(Scene):
    def __init__(self, world=None, game_map=None):
        self.world = world
        self.game_map = game_map
        self.factory = Factory(self, "data/entities.json")
        if world is None:
            self.world = esper.CachedWorld()
        if game_map is None:
            self.game_map = GameMap(
                config.MAP_WIDTH, config.MAP_HEIGHT, self.world, self.factory)
        self.astar = tcod.path.AStar(self.game_map)

        self.processor_group = processor.PROCESSOR_GROUP
        self.change_processors('player_turn')

        self.fov_recompute = True
        self.message = collections.deque()
        self.action = {}
        self.mouse = tcod.Mouse()

        self.con = tcod.console.Console(
            width=config.MAP_WIDTH,
            height=config.MAP_HEIGHT
        )
        # self._render_unexplored_map()

        self.panel = tcod.console.Console(
            width=config.SCREEN_WIDTH,
            height=config.PANEL_HEIGHT
        )

    def _create_level(self):
        player = self.factory.instantiate_entity(
            'player', config.MAP_WIDTH//2, config.MAP_HEIGHT//2)
        # lvl = level.Level(**level_type)
        # lvl.make_blueprint()
        # lvl.make_map()
        # lvl.place_entities(create_player)
        # for entity in lvl.entities:
        #     if len(entity) <= 1:
        #         self.world.create_entity(entity)
        #     else:
        #         self.world.create_entity(*entity)
        # self.start_pos = lvl.get_start_position()
        # self.game_map = lvl.game_map

    # def _render_unexplored_map(self):
    #     self.con.ch[:] = 219
    #     self.con.fg[:] = (15, 10, 5)
    #     self.con.bg[:] = (15, 10, 5)

    def change_processors(self, state):
        self.world._processors = self.processor_group[state]
        for processor_instance in self.processor_group[state]:
            processor_instance.world = self.world
            processor_instance.scene = self

    def update(self):
        self.world.process()


class MainMenu(Scene):
    def __init__(self):
        self.world = esper.World()
        self._add_processors()
        self.action = {}

    def _add_processors(self):
        processors = (
            processor.RenderTitle(),
            processor.InputTitle(),
            # processor.Console(),
            processor.StateTitle()
        )
        for num, proc in enumerate(processors):
            self.world.add_processor(proc, priority=num)
            proc.scene = self

    def update(self):
        self.world.process()


class Option(Scene):
    def update(self):
        raise NotImplementedError


if __name__ == '__main__':
    app = SceneManager(state='menu')
    app.run()
