import libtcodpy as libtcod
from game_states import GameStates
from render_functions import RenderOrder

class Destructible():

    events = [] 

    def __init__(self):
        pass

    def process(self):
        pass

    def destroy(self):
        self.owner.char = self.owner.data['corpse_char']
        self.owner.color = libtcod.dark_red
        self.owner.name = 'remains of ' + self.owner.name
        self.owner.render_order = RenderOrder.CORPSE
        
        if(self.owner.data['has_dna']):
            print("This drops DNA")
