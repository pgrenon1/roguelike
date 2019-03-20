import esper
import components as c
import tcod as libtcod
import config
import random


class Fov(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()
        self.radius = config.FOV_RADIUS
        self.light_walls = config.FOV_LIGHT_WALLS
        self.algo = config.FOV_ALGORITHM
        self.lights = []
        self.framerates = []
        # libtcod.map_new(config.MAP_WIDTH, config.MAP_HEIGHT)
        # self.update_map()

    def update_lights(self):
        for light in self.world.get_component(c.Light):
            if not light in self.lights:
                self.lights.append(light)
                self.scene.fovs.append(libtcod.map_new(
                    config.MAP_WIDTH, config.MAP_HEIGHT))

    def get_player_position(self):
        iterable = self.world.get_components(
            c.PlayerTurn,
            c.Position
        )

        print("playerpos count : " + str(len(iterable)))
        for _, (_, pos) in iterable:
            yield pos

    def get_lights_positions(self):
        iterable = self.world.get_components(
            c.Light,
            c.Position
        )

        print("lights count : " + str(len(iterable)))
        for _, (li, pos) in iterable:
            yield (li, pos)

    def update_map(self, fov_map):
        self.scene.game_map.transparent[:] = True
        for ent, (pos, col) in list(self.world.get_components(c.Position, c.Collidable)):
            self.scene.game_map.transparent[pos.y, pos.x] = False

    def process(self):
        # milis = libtcod.sys_elapsed_milli()
        if self.scene.fov_recompute:
            self.update_map(self.scene.game_map)
            for pos in self.get_player_position():
                libtcod.map_compute_fov(
                    self.scene.game_map,
                    x=pos.x,
                    y=pos.y,
                    radius=self.radius,
                    light_walls=self.light_walls,
                    algo=self.algo,
                )
            fov_bool_array = self.scene.game_map.fov
            self.scene.game_map.explored[fov_bool_array] = True
        # self.update_lights()
        # for fov_map in self.scene.fovs:
        #     self.update_map(fov_map)
        #     for light, pos in self.get_lights_positions():
        #         libtcod.map_compute_fov(
        #             fov_map,
        #             x=pos.x,
        #             y=pos.y,
        #             radius=light.radius + random.randint(0, 1),
        #             light_walls=self.light_walls,
        #             algo=self.algo)
        #         fov_bool_array = self.scene.game_map.fov
        #         self.scene.game_map.explored[fov_bool_array] = True
        # self.framerates.append(libtcod.sys_elapsed_milli() - milis)
        # print(sum(self.framerates)/len(self.framerates))
