# import tcod as libtcod
# from enum import Enum


# class RenderOrder(Enum):
#     REMAINS = 1
#     ITEM = 2
#     ACTOR = 3


# def render_all(con, entities, game_map, screen_width, screen_height, colors):
#     # Draw all the tiles in the game map
#     for y in range(game_map.height):
#         for x in range(game_map.width):
#             libtcod.console_set_char_background(
#                 con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

#     entities_in_render_order = sorted(
#         entities, key=lambda x: x.render_order.value)

#     # Draw all entities in the list
#     for entity in entities_in_render_order:
#         draw_entity(con, entity)

#     libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


# def clear_all(con, entities):
#     for entity in entities:
#         clear_entity(con, entity)


# def draw_entity(con, entity):
#     libtcod.console_set_default_foreground(con, entity.color)
#     libtcod.console_put_char(con, entity.x, entity.y,
#                              entity.char, libtcod.BKGND_NONE)


# def clear_entity(con, entity):
#     # erase the character that represents this object
#     libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
