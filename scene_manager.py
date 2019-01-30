import tcod as libtcod
from scene_gameplay import Gameplay
from config import *

# I'm importing scene here or else Gameplay() will require an argument for some reason
from scene import Scene


class SceneManager:
    """This class manages scenes. In toptea's implementation, it's called "Director"""

    def __init__(self, state='gameplay'):
        print("Scene manager initialized")
        libtcod.console_set_custom_font(DEFAULT_FONT, 2)

        self.root_console = libtcod.console_init_root(
            SCREEN_WIDTH, SCREEN_HEIGHT, 'ROGUELIKE', FULLSCREEN, renderer=libtcod.RENDERER_GLSL)
        # libtcod.sys_set_renderer(3)
        # self.con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
        #libtcod.console_s(0, 0, 100, 100)

        self.scenes = {
            # We currently only have gameplay, no menues or anything like that, but we would add them here.
            'gameplay': Gameplay()

        }

        self.current_scene = self.scenes[state]
        Scene.manager = self

    def change_scene(self, state):
        self.current_scene = self.scenes[state]

    def run(self):
        while not libtcod.console_is_window_closed():
            self.current_scene.update()
