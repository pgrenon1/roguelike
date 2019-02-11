import esper
import tcod
import config

"""Ces process sont responsables de dire à la scene de changer d'un ProcessorGroup à un autre, c'est le turn based system basically
Je crois que c'est legit de les avoir dans un seul file même si c'est deux states"""


class StatePlayerTurn(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        # Process this only if the action is not empty
        if self.scene.action != {}:
            # all() True - If all elements in an iterable are true. False - If any element in an iterable is false
            # si la key est move ou pickup, reliquish the turn!
            if all(key in ['move'] for key in self.scene.action.keys()):
                self.scene.change_processors('enemy_turn')

        config.TICK += 1


class StateEnemyTurn(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    # vu que c'est le dernier process du PROCESSORGROUP du enemyturn, Reliquish the turn!
    def process(self):
        if(self.scene.action != {}):
            self.scene.change_processors('player_turn')


class StateExamining(esper.Processor):

    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        if self.scene.mouse.rbutton_pressed and self.scene.action != {}:
            self.scene.change_processors('player_turn')
