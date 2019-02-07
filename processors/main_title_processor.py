import esper
import tcod as libtcod
import config


class MainTitleProcessor(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        if self.scene.action != {}:

            if self.scene.action.get('new_game'):
                self.scene.manager.change_scene('gameplay')


class RenderTitleProcessor(esper.Processor):
    scene = None

    def __init__(self):
        self.title = "WELCOME TO MUT8"
        self.subtitle = "PRESS ANY ALPHANUMERICAL KEY (lol)"
        super().__init__()

    def process(self):
        self.scene.manager.root_console_default_fg = libtcod.white
        self.scene.manager.root_console.print_(
            x=(config.SCREEN_WIDTH - len(self.title)) // 2,
            y=config.SCREEN_HEIGHT // 2 - 4, string=self.title)
        self.scene.manager.root_console.print_(
            x=(config.SCREEN_WIDTH - len(self.title)) // 2 - len(self.title)//2,
            y=config.SCREEN_HEIGHT // 2, string=self.subtitle)
        libtcod.console_flush()


class InputTitleProcessor(esper.Processor):
    def __init__(self):
        self.key = libtcod.Key()
        self.mouse = libtcod.Mouse()
        super().__init__()

    def process(self):
        libtcod.sys_wait_for_event(
            mask=libtcod.EVENT_ANY,
            k=self.key,
            m=self.mouse,
            flush=False
        )

        if libtcod.EVENT_KEY_PRESS and self.key.pressed:
            if self.key.c:
                self.scene.action = {'new_game': True}
