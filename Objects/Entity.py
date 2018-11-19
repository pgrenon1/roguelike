import libtcodpy as libtcod
import setup.Initialization

class Entity:
    # this is a generic object: the player, a monster, an item, the stairs...
    # it's always represented by a character on screen.
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def draw(self):
        # set the color and then draw the character that represents this object at its position
        libtcod.console_set_default_foreground(setup.Initialization.con, self.color)
        libtcod.console_put_char(setup.Initialization.con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self):
        # erase the character that represents this object
        libtcod.console_put_char(setup.Initialization.con, self.x, self.y, ' ', libtcod.BKGND_NONE)