import config
# We need to learn how to do this correctly
from processors.ai_processor import AiProcessor
from processors.damage_processor import DamageProcessor
from processors.death_processor import DeathProcessor
from processors.dna_absorb_processor import DnaAbsorberProcessor
from processors.movement_processor import MovementProcessor
from processors.render_processor import RenderProcessor
from processors.spawner_processor import SpawnerProcessor
from processors.render_console_processor import RenderConsole
from scene_manager import SceneManager

PROCESSOR_GROUP = {
    'player_turn': [
        RenderProcessor(config.con, config.COLORS['none']),
        RenderConsole(),
        MovementProcessor(),
        DeathProcessor()
    ],
    'enemy_turn': [
        # Most likely we need to separate this into EnemyMovementProcessor()
        MovementProcessor()

    ]
}
