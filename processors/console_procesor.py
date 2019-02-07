import esper


class ConsoleProcessor(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        if self.scene.action.get('exit'):
            sys.exit()
