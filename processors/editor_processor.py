import esper
import components as c
import tcod as libtcod
import config
import random
import numpy
import itertools


class Editor(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()
        self.noise = libtcod.noise_new(
            4, 1.0, 0.9, random=config.LIBTCOD_RANDOM)
        self.offset = 1

    def process(self):
        m = self.scene.ed_matrix
        self.offset += 0.1
        for index, e in numpy.ndenumerate(m):
            if e:
                libtcod.console_put_char_ex(
                    self.scene.editor, index[0], index[1], e, libtcod.gray * (libtcod.noise_get_fbm(
                        self.noise, [index[0]+self.offset, index[1]], 15, libtcod.NOISE_PERLIN)+1), libtcod.black)
