import components as c
import esper
import random


class MoveEnemy(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        # if self.scene.action != {}:
        self.move_enemies()

    def get_enemies(self):
        enemies = self.world.get_components(
            c.EnemyTurn,
            c.Renderable,

            c.Stats,
            # since I only have this case, I'm using this one, but it should be more general
            # and we should check for movement Ai in the process itself I guess
            c.Position,
            c.AiRandomWalk,
        )

        for enemy, (_, _, _, en_pos, ai) in enemies:

            yield enemy, (en_pos, ai)

    def move_enemies(self):
        for enemy, (en_pos, ai) in self.get_enemies():
            if isinstance(ai, c.AiRandomWalk):
                new_x = en_pos.x + random.randint(-1, 1)
                new_y = en_pos.y + random.randint(-1, 1)

            en_pos.x = new_x
            en_pos.y = new_y

