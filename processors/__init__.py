""" I think this is the right way to import many classes from a file. import * seems like a dirty way to import all.
 J'pense qu'en théorie faudrait pas importer des classes qu'on a pas besoin. Au début pour le dev ça peut aider, mais
 par souci de clarté, et peut-être plus tard par souci d'optimisation, on devrait juste se limiter aux classes qu'on
 a besoin d'importer
"""
from .states_processor import (
    StatePlayerTurn,
    StateEnemyTurn
)
from .death_processor import Death
from .input_handler_processor import InputPlayer
from .render_processor import (
    RenderConsole,
    RenderPanel,
    RenderTooltip
)
from .fov_processor import Fov
from .move_player_processor import MovePlayer
from .dna_absorb_processor import DnaAbsorberProcessor
from .move_enemy_processor import MoveEnemy
from .spawner_processor import SpawnerProcessor

import config


PROCESSOR_GROUP = {
    'player_turn': [

        Fov(),

        RenderConsole(),
        InputPlayer(),
        MovePlayer(),
        SpawnerProcessor(),
        DnaAbsorberProcessor(),
        # DnaGeneratorProcessor(),
        # giving the player experience should be here if we ever do that
        Death(),
        # picking up stuff should be here
        # changing level such as a dungeon level should be here, aka stairs
        # checking "out game" player actions that involve the console should be here, that means going full screen, save and exit, etc
        # rendering the panel should be here, stats, logs, etc
  
        RenderPanel(),
        RenderTooltip(),
        StatePlayerTurn()
    ],
    'enemy_turn': [
        # RenderPanel(),
        MoveEnemy(),
        Death(),
        SpawnerProcessor(),
        StateEnemyTurn()
    ]

}
