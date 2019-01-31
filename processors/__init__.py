""" I think this is the right way to import many classes from a file. import * seems like a dirty way to import all.
 J'pense qu'en théorie faudrait pas importer des classes qu'on a pas besoin. Au début pour le dev ça peut aider, mais
 par souci de clarté, et peut-être plus tard par souci d'optimisation, on devrait juste se limiter aux classes qu'on
 a besoin d'importer
"""
from .states import (
    StatePlayerTurn,
    StateEnemyTurn
)
from .death import Death
from .input_handler import InputPlayer
from .render import RenderConsole
from .render import RenderPanel
from .move_player import MovePlayer
import config


PROCESSOR_GROUP = {
    'player_turn': [
        RenderPanel(),
        # computing FOV should be here
        RenderConsole(),
        InputPlayer(),
        MovePlayer(),
        # giving the player experience should be here if we ever do that
        Death(),
        # picking up stuff should be here
        # changing level such as a dungeon level should be here, aka stairs
        # checking "out game" player actions that involve the console should be here, that means going full screen, save and exit, etc
        # rendering the panel should be here, stats, logs, etc
        StatePlayerTurn()
    ],
    'enemy_turn': [
        Death(),
        StateEnemyTurn()
    ]
}
