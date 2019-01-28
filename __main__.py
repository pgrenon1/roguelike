import engine
import sys
import config
import random
import tcod as libtcod


def main():
    engine.run_game()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        random.seed(int(sys.argv[1]))
        config.LIBTCOD_RANDOM = libtcod.random_new_from_seed(int(sys.argv[1]))
        config.MASTER_SEED = int(sys.argv[1])
    else:
        randomseed = random.randint(0, 1000)
        LIBTCOD_RANDOM = libtcod.random_new()
        config.MASTER_SEED = randomseed
        random.seed(randomseed)

    main()
