import components as c
import random
import esper
import math
import tcod as libtcod
import config


class MoveEnemy(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        if self.scene.action != {}:
            self.move_enemies()

    def move_random_agitated(self, entity, entity_pos, entity_meta, entity_stats, attacks):
        # Get destination position
        new_x = entity_pos.x + random.randint(-1, 1)
        new_y = entity_pos.y + random.randint(-1, 1)

        # Check for collision
        collided_with = self.collide_on_other(
            entity, new_x, new_y)
        for other, (other_meta, other_stats) in collided_with:
            # Attack
            if attacks:
                self.do_damage(entity_meta, entity_stats,
                               other_meta, other_stats)
                return None
            # Bump
            else:
                if entity in config.VISIBLES:
                    self.scene.messages.append(
                        (
                            '{0} bumped into {1}.'.format(
                                entity_meta.name.capitalize(),
                                other_meta.name),
                            libtcod.white
                        )
                    )
                return None
        # set enemy new x,y position
        entity_pos.x = new_x
        entity_pos.y = new_y

    def move_random_calm(self, entity, entity_pos):
        # Get destination position
        if random.randint(0, 1) == 0:
            new_x = entity_pos.x
            new_y = entity_pos.y
        else:
            new_x = entity_pos.x + random.randint(-1, 1)
            new_y = entity_pos.y + random.randint(-1, 1)

        # Check for collision
        if bool(next(self.collide_on_other(entity, new_x, new_y), False)):
            return None

        # set enemy new x,y position
        entity_pos.x = new_x
        entity_pos.y = new_y

    def move_predator(self,  entity, entity_pos, entity_meta, entity_stats, range):
        others = self.world.get_components(
            c.Movable,
            c.Position,
            c.Metadata,
            c.Stats,
        )
        # Attack anything that moves
        has_target = False
        for other, (_, other_pos, other_meta, other_stats) in others:
            if other != entity and self.find_distance(other_pos, entity_pos) <= range:
                has_target = True
                # Get destination to go toward target
                new_y, new_x = self.move_toward(entity_pos, other_pos)

                # Check for collision
                collided_with = self.collide_on_other(
                    entity, new_x, new_y)
                for collided, (collided_meta, collided_stats) in collided_with:
                    self.do_damage(entity_meta, entity_stats,
                                   collided_meta, collided_stats)
                    return None

                entity_pos.x = new_x
                entity_pos.y = new_y
        if not has_target:
            self.move_random_calm(entity, entity_pos)

    def do_damage(self, entity_meta, entity_stats, other_meta, other_stats):
        damage = entity_stats.damage - other_stats.defense
        if damage > 0:
            other_stats.health -= damage
            self.scene.messages.append(
                (
                    '{0} attacks {1} for {2} hit points.'.format(
                        entity_meta.name.capitalize(),
                        other_meta.name,
                        str(damage)
                    ),
                    libtcod.white
                )
            )
        else:
            self.scene.messages.append(
                (
                    '{0} attacks {1} but does no damage.'.format(
                        entity_meta.name.capitalize(),
                        other_meta.name
                    ),
                    libtcod.white
                )
            )

    def move_enemies(self):
        entities = self.world.get_components(
            c.EnemyTurn,
            c.Movable,
            c.Position,
            c.Metadata,
            c.Stats,
        )

        for entity, (_, _, entity_pos, entity_meta, entity_stats) in entities:
            # Get Ais
            ai_random_agitated = self.scene.world.component_for_entity(
                entity, c.AiRandomAgitated)
            ai_random_calm = self.scene.world.component_for_entity(
                entity, c.AiRandomCalm)
            ai_predator = self.scene.world.component_for_entity(
                entity, c.AiPredator)

            # If multiple, takes first
            if ai_predator:
                self.move_predator(
                    entity, entity_pos, entity_meta, entity_stats, ai_predator.range)
            elif ai_random_agitated:
                self.move_random_agitated(
                    entity, entity_pos, entity_meta, entity_stats, ai_random_agitated.attacks)
            elif ai_random_calm:
                self.move_random_calm(entity, entity_pos)

    def collide_on_other(self, entity, new_x, new_y):
        other_components = self.world.get_components(
            c.Collidable, c.Position, c.Metadata, c.Stats)
        for other_entity, (_, other_pos, other_meta, other_stats) in other_components:
            if new_x == other_pos.x and new_y == other_pos.y and entity != other_entity:
                yield other_entity, (other_meta, other_stats)
        return None

    @staticmethod
    def find_distance(pos, other_pos):
        dx = other_pos.x - pos.x
        dy = other_pos.y - pos.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def move_toward(self, pos, other_pos):
        path = self.scene.astar.get_path(
            pos.y, pos.x, other_pos.y, other_pos.x)
        new_y, new_x = path[0]
        return new_y, new_x
