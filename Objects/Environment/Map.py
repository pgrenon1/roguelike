# class Map():
#     def __init__(self, width, height, type):
#         self.width = width;
#         self.height = height;
#         self.type = type;

#     def GenerateMap():
#         global map
    
#         #fill map with "unblocked" tiles
#         map = [
#             [Tile(False) for y in range(MAP_HEIGHT)]
#             for x in range(MAP_WIDTH) 
#         ]
    
#         #place two pillars to test the map
#         map[30][22].blocked = True
#         map[30][22].block_sight = True
#         map[50][22].blocked = True
#         map[50][22].block_sight = True

#     def Render():
#         global color_light_wall
#         global color_light_ground
 
#         #go through all tiles, and set their background color
#         for y in range(MAP_HEIGHT):
#             for x in range(MAP_WIDTH):
#                 wall = map[x][y].block_sight
#                 if wall:
#                     libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
#                 else:
#                     libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)