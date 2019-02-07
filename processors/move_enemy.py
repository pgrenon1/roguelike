import components as c
import random
import esper
import math
import tcod


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
                            tcod.white
                        )
                    )
                else:
                    self.scene.messages.append(
                        (
                            '{0} attacks {1} but does no damage.'.format(
                                entity_meta.name.capitalize(),
                                other_meta.name
                            ),
                            tcod.white
                        )
                    )
                return None
            # Bump
            else:
                self.scene.messages.append(
                    (
                        '{0} bumped into {1}.'.format(
                            entity_meta.name.capitalize(),
                            other_meta.name),
                        tcod.white
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

    def move_predator(self):
        pass
        # If no target try acquire target
        g_player = self.world.get_components(
            c.PlayerTurn,
            c.Movable,
            c.Position,
            c.Describable,
            c.Stats
        )
        

            # If no target do random_calm
        # Get destination to go toward target
        # Check for collision

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
                entity, c.AiRandomCalm)

            # If multiple, takes first
            if ai_random_agitated:
                self.move_random_agitated(
                    entity, entity_pos, entity_meta, entity_stats, ai_random_agitated.attacks)
            elif ai_random_calm:
                self.move_random_calm(entity, entity_pos)
            elif ai_predator:
                self.move_predator(
                    entity, entity_pos, entity_meta, entity_stats, ai_predator.range)

        # for player, (_, _, player_pos, player_desc, player_stats) in player:
        #     for enemy, (_, _, enemy_pos, enemy_desc, enemy_stats, enemy_status) in enemy:

        #         # if enemy is within range, move towards the player
        #         if self.find_distance(player_pos, enemy_pos) <= 5:
        #             new_y, new_x = self.move_toward(enemy_pos, player_pos)

        #             # under status
        #             if enemy_status.paralyse or enemy_status.freeze:
        #                 new_x, new_y = enemy_pos.x, enemy_pos.y

        #             if enemy_status.confuse:
        #                 new_x = enemy_pos.x + random.randint(-1, 1)
        #                 new_y = enemy_pos.y + random.randint(-1, 1)

        #                 if not self.scene.game_map.walkable[new_y, new_x]:
        #                     break

        #             # check for collision on player
        #             if new_x == player_pos.x and new_y == player_pos.y:
        #                 damage = enemy_stats.power - player_stats.defense

        #                 if damage > 0:
        #                     player_stats.hp -= damage
        #                     self.scene.message.append(
        #                         (
        #                             '{0} attacks {1} for {2} hit points.'.format(
        #                                 enemy_desc.name.capitalize(),
        #                                 player_desc.name,
        #                                 str(damage)
        #                             ),
        #                             tcod.white
        #                         )
        #                     )
        #                 else:
        #                     self.scene.message.append(
        #                         (
        #                             '{0} attacks {1} but does no damage.'.format(
        #                                 enemy_desc.name.capitalize(),
        #                                 player_desc.name
        #                             ),
        #                             tcod.white
        #                         )
        #                     )
        #                 return None

        #             # check for collision on other entities
        #             gen_c = self.world.get_components(c.Collidable, c.Position)
        #             for other_ent, (_, other_pos) in gen_c:
        #                 b1 = enemy != other_ent
        #                 b2 = new_x == other_pos.x
        #                 b3 = new_y == other_pos.y
        #                 if b1 and b2 and b3:
        #                     self.scene.message.append(
        #                         ('enemy bumped into each other!', tcod.white))
        #                     return None

        #             # set enemy new x,y position
        #             enemy_pos.x = new_x
        #             enemy_pos.y = new_y

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
