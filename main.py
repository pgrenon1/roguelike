#import engine
import sys
import config
import random
import tcod as libtcod
from scene_manager import SceneManager


def main():
    pass
    # engine.run_game()
    # engine.WORLD.process()


if __name__ == '__main__':
    """We setup the randomness of the game as soon as we run it for now"""
    if len(sys.argv) > 1:
        random.seed(int(sys.argv[1]))
        config.LIBTCOD_RANDOM = libtcod.random_new_from_seed(int(sys.argv[1]))
        config.MASTER_SEED = int(sys.argv[1])
    else:
        randomseed = random.randint(0, 1000)
        LIBTCOD_RANDOM = libtcod.random_new()
        config.MASTER_SEED = randomseed
        random.seed(randomseed)

    app = SceneManager(state='gameplay')
    app.run()
    # main()
