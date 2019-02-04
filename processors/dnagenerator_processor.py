import esper
import components as c


class DnaGeneratorProcessor(esper.Processor):
    scene = None

    def __init__(self):
        super().__init__()

    def process(self):
        pass
        # for ent, (gendna) in self.scene.world.get_component(GenerateDna):
        #     # generate dna
        #     _generatedDna = {'dna': {'dna_data': 'dna data, baby!'}}
        #     self.scene.world.add_component(ent, Dna(_generatedDna))
        #     self.scene.world.remove_component(ent, GenerateDna)
