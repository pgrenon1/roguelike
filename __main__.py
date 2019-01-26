import engine
from Instantiator import *


def main():
    engine.run_game()


if __name__ == '__main__':
    playerData = LoadDataSet('data/gameobjects/entities.json','Player')
    player = Instantiate(playerData)
    main()
