import tcod as libtcod
from scene_gameplay import Gameplay
from scene_menu import MainMenu
from config import *

# I'm importing scene here or else Gameplay() will require an argument for some reason
from scene import Scene


class SceneManager:
    """This class manages scenes. In toptea's implementation, it's called "Director
    It basically allows us to change scenes and run them. 
    When adding a new scene, for example a main menu, it should be added in self.scenes"""

    def __init__(self, state='menu'):
        print("Scene manager initialized")

        libtcod.console_set_custom_font(DEFAULT_FONT, 2)
        self.state = state

        self.root_console = libtcod.console_init_root(
            SCREEN_WIDTH, SCREEN_HEIGHT, 'ROGUELIKE', FULLSCREEN, renderer=libtcod.RENDERER_GLSL)

        libtcod.sys_set_fps(60)
        self.scenes = {
            # We currently only have gameplay, no menues or anything like that, but we would add them here.
            'menu': MainMenu(),
            'gameplay': Gameplay()
        }

        self.current_scene = self.scenes[state]
        Scene.manager = self

    def change_scene(self, state):
        self.current_scene = self.scenes[state]

    def run(self):
        while not libtcod.console_is_window_closed():

            self.current_scene.update()
