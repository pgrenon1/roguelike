from dataclasses import dataclass
import esper
import tcod


"""Une classe qui est filled par le InputPlayer pour wrapper toutes les possibilitées de combinaisons genre alt+a
si tu print une instance de cette classe en appuyant sur RIGHT_ARROW, ça donne Key(vk=16, ch='\x00', pressed=True, alt=False, ctrl=False, meta=False, shift=False)
vk c'est le numero de la key, ch c'est le character (\x00 means empty string). le reste c'est des bools pour les combinaisons
un keyword qui utilise le module dataclasses. tout ce que ca fait c'est que ca ajoute un __init__ typé à la classe qui suit."""


@dataclass
class Key:
    vk: int = 65
    ch: str = chr(0)
    pressed: bool = True
    alt: bool = False
    ctrl: bool = False
    meta: bool = False
    shift: bool = False

    def __key(self):
        return (
            self.vk, self.ch, self.pressed,
            self.alt, self.ctrl, self.meta,
            self.shift
        )

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())


""" La class qui handle les input du joueur. Elle prend l'information de la classe Key() et la match dans un dictionnaire key_code
à une "action". la string de l'action genre "move" est associée à un set de variable, des fois des coords, des fois un bool, etc. """


class InputPlayer(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()
        self.key = tcod.Key()
        self.mouse = tcod.Mouse()
        self.key_code = {
            Key(vk=tcod.KEY_ENTER, ch='\r'): {'take_stairs': True},
            Key(vk=tcod.KEY_ENTER, ch='\r', alt=True): {'fullscreen': True},
            Key(vk=tcod.KEY_ESCAPE, ch='\x1b'): {'save_and_exit': True},
            Key(vk=tcod.KEY_LEFT, shift=True): {'move': (-1, -1)},
            Key(vk=tcod.KEY_RIGHT, shift=True): {'move': (1, -1)},
            Key(vk=tcod.KEY_LEFT, ctrl=True): {'move': (-1, 1)},
            Key(vk=tcod.KEY_RIGHT, ctrl=True): {'move': (1, 1)},
            Key(vk=tcod.KEY_UP): {'move': (0, -1)},
            Key(vk=tcod.KEY_DOWN): {'move': (0, 1)},
            Key(vk=tcod.KEY_LEFT): {'move': (-1, 0)},
            Key(vk=tcod.KEY_RIGHT): {'move': (1, 0)},
            Key(vk=tcod.KEY_KP0): {'move': (0, 0)},
            Key(vk=tcod.KEY_KP1): {'move': (-1, 1)},
            Key(vk=tcod.KEY_KP2): {'move': (0, 1)},
            Key(vk=tcod.KEY_KP3): {'move': (1, 1)},
            Key(vk=tcod.KEY_KP4): {'move': (-1, 0)},
            Key(vk=tcod.KEY_KP5): {'move': (0, 0)},
            Key(vk=tcod.KEY_KP6): {'move': (1, 0)},
            Key(vk=tcod.KEY_KP7): {'move': (-1, -1)},
            Key(vk=tcod.KEY_KP8): {'move': (0, -1)},
            Key(vk=tcod.KEY_KP9): {'move': (1, -1)},
            Key(vk=tcod.KEY_F1): {'next_level': (None, None)},
            Key(vk=tcod.KEY_F5): {'reveal_all': True},
            Key(vk=tcod.KEY_F12): {'screenshot': True},
            Key(ch='a'): {},
            Key(ch='b'): {'move': (-1, 1)},
            Key(ch='c'): {'show_character_screen': True},
            Key(ch='d'): {'drop_inventory': True},
            Key(ch='e'): {},
            Key(ch='f'): {},
            Key(ch='g'): {'pickup': True},
            Key(ch='h'): {'move': (-1, 0)},
            Key(ch='i'): {'show_inventory': True},
            Key(ch='j'): {'move': (0, 1)},
            Key(ch='k'): {'move': (0, -1)},
            Key(ch='l'): {'move': (1, 0)},
            Key(ch='m'): {},
            Key(ch='n'): {'move': (1, 1)},
            Key(ch='o'): {'switch_show_debug': True},
            Key(ch='p'): {},
            Key(ch='q'): {},
            Key(ch='r'): {'switch_reveal_all': True},
            Key(ch='s'): {},
            Key(ch='t'): {},
            Key(ch='u'): {'move': (1, -1)},
            Key(ch='v'): {},
            Key(ch='w'): {},
            Key(ch='x'): {},
            Key(ch='y'): {'move': (-1, -1)},
            Key(ch='z'): {},
            Key(ch='.'): {'move': (0, 0)},
        }

    def process(self):
        # check for an event of type EVENT_ANY, parce que eventuellement on va faire qqch avec la souris
        # self.key = tcod.console_wait_for_keypress(flush=False)
        tcod.sys_wait_for_event(
            mask=tcod.EVENT_ANY,
            k=self.key,
            m=self.mouse,
            # je sais pas c'est quoi, mais la Doc de libtcod dit "flush: This should always be false." ...
            flush=False
        )

        # populate an in intance of key with the result of the event
        user_input = Key(
            vk=self.key.vk,
            ch=chr(self.key.c),
            alt=(self.key.lalt or self.key.ralt),
            ctrl=(self.key.lctrl or self.key.lctrl),
            meta=(self.key.lmeta or self.key.rmeta),
            shift=self.key.shift, pressed=self.key.pressed,
        )

        if tcod.EVENT_KEY_PRESS and user_input in self.key_code:
            # if the event is a key press and recognized in the dictionary "key_code", translate it to its action
            # l'action est stocké dans scene parce qu'elle peut être utilisée par différents processors, see move_player.py for example
            self.scene.action = self.key_code[user_input]
        else:
            self.scene.action = {}  # if the event is null, empty the action variable
        # this assigns the current mouse data in the mouse variable in the scene, for use in other processors
        self.scene.mouse = self.mouse
