import esper
import components as c
import tcod
import config


class FOV(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()
        self.radius = 40
        self.light_walls = config.FOV_LIGHT_WALLS
        self.algo = config.FOV_ALGORITHM

    def get_player_position(self):
        iterable = self.world.get_components(
            c.PlayerTurn,
            c.Position
        )
        for _, (_, pos) in iterable:
            yield pos

    def process(self):
        if self.scene.fov_recompute:
            for pos in self.get_player_position():
                tcod.map_compute_fov(
                    self.scene.game_map,
                    x=pos.x,
                    y=pos.y,
                    radius=self.radius,
                    light_walls=self.light_walls,
                    algo=self.algo,
                )
                fov_bool_array = self.scene.game_map.fov
                self.scene.game_map.explored[fov_bool_array] = True
