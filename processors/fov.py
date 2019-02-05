import esper
import components as c
import tcod as libtcod
import config


class Fov(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()
        self.radius = config.FOV_RADIUS
        self.light_walls = config.FOV_LIGHT_WALLS
        self.algo = config.FOV_ALGORITHM
        # libtcod.map_new(config.MAP_WIDTH, config.MAP_HEIGHT)
        # self.update_map()

    def get_player_position(self):
        iterable = self.world.get_components(
            c.PlayerTurn,
            c.Position
        )
        for _, (_, pos) in iterable:
            yield pos

    def update_map(self):
        libtcod.map_clear(self.scene.game_map, True, True)
        for ent, (pos) in list(self.world.get_component(c.Position)):
            libtcod.map_set_properties(
                self.scene.game_map, pos.x, pos.y, False, True)

    def process(self):
        if self.scene.fov_recompute:
            self.update_map()
            for pos in self.get_player_position():
                libtcod.map_compute_fov(
                    self.scene.game_map,
                    x=pos.x,
                    y=pos.y,
                    radius=self.radius,
                    light_walls=self.light_walls,
                    algo=self.algo,
                )
                # fov_bool_array = self.scene.game_map.fov
                # self.scene.game_map.explored[fov_bool_array] = True
