"""Just getting the camera object started here. Not implemented in game, just trying to populate an array that updates as the player moves.
We then would loop through that array to do the rendering. We would not writing entities directly anymore"""


class Camera():

    def __init__(self, viewport_width, viewport_height, world, mode):
        self.viewport_width = 10
        self.viewport_height = 10
        self.world = world

        # Say, if we wanted different rendering modes : sprites, ascii, dizzy, bw,
        # we could maybe do it through this variable
        self.mode = None

        # We store everything we want to render in this list
        self.camera_data = []

    def refresh_camera():
        # We refresh the camera on each pass
        pass

    def move_camera(target_x, target_y):
        # The target will most of the time be the player coordinates, unless some special effect occurs, I guess?
        pass

    def render_camera():
        pass
        # We would loop through self.camera_data and render these things to the screen

    def update():
        print("Camera updated")
