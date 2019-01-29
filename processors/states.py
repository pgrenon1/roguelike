import esper
import tcod

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
            if all(key in ['move', 'pickup'] for key in self.scene.action.keys()):
                self.scene.change_processors('enemy_turn')

            # might not end up using any of these!
            # if self.scene.action.get('show_inventory'):
            #     self.scene.change_processors('show_inventory')

            # if self.scene.action.get('drop_inventory'):
            #     self.scene.change_processors('drop_inventory')

            # if self.scene.action.get('next_level'):
            #     player = self.scene.action.get('next_level')[0]
            #     inventory = self.scene.action.get('next_level')[1]
            #     self.scene.manager.next_level(
            #         player_entity=player,
            #         item_entities=inventory
            #     )

            # if self.scene.action.get('show_level_up'):
            #     self.scene.change_processors('level_up')

            # if self.scene.action.get('show_character_screen'):
            #     self.scene.change_processors('character_screen')


class StateEnemyTurn(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    # vu que c'est le dernier process du PROCESSORGROUP du enemyturn, Reliquish the turn!
    def process(self):
        self.scene.change_processors('player_turn')
