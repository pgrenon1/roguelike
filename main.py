# import engine
import sys
import config
import random
import tcod as libtcod
from scene_manager import SceneManager
import getopt
import argparse
from helpers import *


def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('-s', dest='seed', action='store')
    args = parser.parse_args()

    if args.verbose:
        config.VERBOSE_MODE = True
        '''A function that allows us to print only when we need to ;)'''
        debug("****VERBOSE MODE ACTIVE FOR THIS INSTANCE****")

    if args.seed:
        seed = int(args.seed)
        config.MASTER_SEED = seed

        debug("This game will have a deterministic seed")
        debug(seed)
        config.LIBTCOD_RANDOM = libtcod.random_new_from_seed(seed)
        random.seed(config.MASTER_SEED)

    else:
        randomseed = random.randint(0, 10000)
        config.MASTER_SEED = randomseed
        debug("This game will have a random seed")
        #config.LIBTCOD_RANDOM = libtcod.random_new()

    app = SceneManager(state='gameplay')
    app.run()
    # main()


if __name__ == '__main__':
    """We setup the randomness of the game as soon as we run it for now"""
    main(sys.argv[1:])
