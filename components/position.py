class Position:
    def __init__(self, args):
        print(args)
        self.x = args['position']['x']
        self.y = args['position']['y']
