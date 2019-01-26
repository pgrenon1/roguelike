import engine
from instantiator import *


def main():
    engine.run_game()


if __name__ == '__main__':
    playerData = LoadDataSet('data/gameobjects/entities.json','player')
    player = GetEntityData(playerData)
    main()
