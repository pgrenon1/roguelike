import components as c
import esper
import tcod as libtcod

"""Checks for an action in the scene, if that action is a "move", use it to move. see input handler
 for mor info on how the scene's action variable is populated """


class MovePlayer(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        if self.scene.action.get('move'):
            player_c = self.world.get_components(
                c.PlayerTurn,
                c.Movable,
                c.Position,
                c.Stats,
                # eventuellement on aura besoin des autres components du player pour faire des choses avec comme collision avec autre chose
                c.Metadata
                # components.Stats
            )
            # ici on ajoutera après player_pos metadata pour le nom + stats pour le damage etc.
            for player, (_, _, player_pos, player_stats, player_metadata) in player_c:
                new_x = player_pos.x + self.scene.action.get('move')[0]
                new_y = player_pos.y + self.scene.action.get('move')[1]

                """We might never use this, because All is Entity"""
                # # check for collision on map
                # if not self.scene.game_map.walkable[new_y, new_x]:
                #     break

                # check for collision on other entities,
                if self.collide_on_entity(player, new_x, new_y, player_stats, player_metadata):
                    # if the player collided with something, don't move the player
                    break

                # self.scene.fov_compute = True
                player_pos.x = new_x
                player_pos.y = new_y
                #self.scene.messages = []
                self.scene.messages.append(
                    "We moved to {}, {}".format(new_x, new_y))

    def collide_on_entity(self, entity, new_x, new_y, player_stats, player_metadata):
        collidable_c = self.world.get_components(
            c.Collidable,
            c.Position,
            c.Metadata,
            c.Stats
        )

        is_collided = False
        for other_entity, (_, other_pos, other_metadata, other_stats) in collidable_c:
            # If it's not the same entity and if the new position would be the position of the other entity
            if entity != other_entity and new_x == other_pos.x and new_y == other_pos.y:
                is_collided = True
                damage = player_stats.damage - other_stats.defense

                if damage > 0:
                    other_stats.health -= damage
                #     self.scene.message.append(
                #         (
                #             '{0} attacks {1} for {2} hit points.'.format(
                #                 desc.name.capitalize(),
                #                 other_desc.name,
                #                 str(damage),
                #             ),
                #             tcod.white
                #         )
                #     )
                # else:
                #     self.scene.message.append(
                #         (
                #             '{0} attacks {1} but does no damage.'.format(
                #                 desc.name.capitalize(),
                #                 other_desc.name
                #             ),
                #             tcod.white
                #         )
                #     )
        return is_collided
