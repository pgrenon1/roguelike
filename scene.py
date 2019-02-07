class Scene:
    """Base class for all scenes. Example scenes : Main Menu, Gameplay"""
    manager = None

    def update(self):
        raise NotImplementedError
