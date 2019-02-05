import components as c
import esper
import random
import tcod as libtcod


class MoveEnemy(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        # if self.scene.action != {}:
        self.move_enemies()

    def get_enemies(self):
        enemies = self.scene.world.get_components(
            c.EnemyTurn,
            c.Renderable,
            # since I only have this case, I'm using this one, but it should be more general
            # and we should check for movement Ai in the process itself I guess
            c.Position,
            c.Stats,
            c.AiRandomWalk,
        )

        for enemy, (_, _, en_pos, stats, ai) in enemies:

            yield enemy, (en_pos, stats, ai)

    def get_player(self):
        player = self.scene.world.get_components(
            c.Position,
            c.PlayerTurn,
            c.Renderable
        )

        return player

    def get_other_entities(self):

        iterable = self.scene.world.get_components(
            c.Collidable,
            c.Position,

            c.Stats
        )

        for other, (_, pos, stats) in iterable:
            yield other, (pos, stats)

    def move_enemies(self):
        for enemy, (en_pos, stats, ai) in self.get_enemies():

                # We check the movement Ai, is this AiRandomWalk?
            if isinstance(ai, c.AiRandomWalk):
                new_x = en_pos.x + random.randint(-1, 1)
                new_y = en_pos.y + random.randint(-1, 1)

                self.collide_on_entities(enemy, stats, en_pos.x, en_pos.y)

            en_pos.x, en_pos.y = new_x, new_y

    def collide_on_entities(self, en_ent, en_stats, en_x, en_y):
        is_collided = False
        for other, (other_pos, other_stats) in self.get_other_entities():
            if (en_x, en_y) == (other_pos.x, other_pos.y) and en_ent != other:
                is_collided = True

                # not doing any damage calculation at the moment since it's not really implemented

                # damage = en_stats.damage - other_stats.defense
                # Check if it's this object's parent, if so, we want to avoid hurting it!
                if self.scene.world.has_component(en_ent, c.Child):
                    childComp = self.scene.world.component_for_entity(
                        en_ent, c.Child)
                    if childComp.parent == other:
                        en_stats.health -= 1
                        self.scene.messages.append((
                            "The moth (*) moved too close to the light (O)", libtcod.yellow))
                    else:
                        other_stats.health -= 1

        return is_collided
