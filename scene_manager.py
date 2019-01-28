import tcod as libtcod


class SceneManager:
    """This class manages scenes. In toptea's implementation, it's called "Director"""

    def __init__(self, state='gameplay'):
        self.scenes = {
            'gameplay': Gameplay()
        }
        self.current_scene = self.scenes[state]

    def change_scene(self, state):
        self.current_scene = self.scenes[state]

    def run(self):
        while not libtcod.console_is_window_closed():
            self.current_scene.update()
