import pyclbr
import enum
import sys
import inspect
import json
from components import *
from config import RenderOrder


class Factory:
    def __init__(self, scene, path="data/entities.json"):
        self.scene = scene
        self.annotations = self.get_annotations(module_name="components")
        self.database = self.load_json(path)
        self.validate_data(self.database)
        # self.templates = self.construct_templates()
        self.blueprints = self.construct_blueprints()
        self.update_index()

    def get_annotations(self, module_name="components"):
        module = pyclbr.readmodule(module_name)
        class_to_annotations = {}
        for class_object in module:
            clazz = getattr(sys.modules[module_name], class_object)
            class_name = class_object
            signature = inspect.getfullargspec(clazz)

            if not signature.annotations:
                class_to_annotations[class_object] = {}
            else:
                class_to_annotations[class_object] = signature.annotations

        return class_to_annotations

    def load_json(self, path):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            return data

    def validate_data(self, raw):
        pass

    def construct_blueprints(self):
        entities = {}
        for entity in self.database:
            components = self.database[entity]
            comp_instances = []
            for component in components:
                attributes_template = self.annotations[component]
                attributes_dict = components[component]
                constructor = globals()[component]
                instance = constructor(**attributes_dict)
                comp_instances.append(instance)
            entities[entity] = comp_instances
        return entities

    def instantiate_entity(self, entity_name, x, y):
        new_entity = self.scene.world.create_entity()
        components = self.blueprints[entity_name]
        self.scene.world.add_component(new_entity, Position(x, y))
        for component in components:
            self.scene.world.add_component(new_entity, component)

        return new_entity

    def update_index(self):
        print("Updating components index")
        components_annotations = self.annotations
        # skipping import statements
        del components_annotations["RenderOrder"]
        for component in components_annotations:
            # print(component)
            if components_annotations[component] != {}:
                for arg in components_annotations[component]:

                    # These first types are dirty dirty exceptions that have to do with our colors.
                    # In the creator, they will be selects. We hardcode them for now.
                    # For now, all non-primitives non-natives will be handled this way
                    for key in components_annotations[component].keys():
                        if "color" in key:
                            components_annotations[component][key] = 'col'

                    # These should never(?) change. They are not dirty.
                    # Unless we find some way to encode python types in json! :-O
                    # Here the important problem that this is solving is that you can't explicitly encode a type in JSON
                    # So we modify the dictionary's data and we interpret it on the other side, aka in the creator.
                    if components_annotations[component][arg] is int:
                        components_annotations[component][arg] = 'int'
                    elif components_annotations[component][arg] is str:
                        components_annotations[component][arg] = 'str'
                    elif components_annotations[component][arg] is bool:
                        components_annotations[component][arg] = 'bool'
                    elif isinstance(components_annotations[component][arg], enum.EnumMeta):
                        components_annotations[component][arg] = components_annotations[component][arg].__dict__[
                            '_member_names_']

        with open("./data/component_index.json", "w") as index_file:
            json.dump(components_annotations, index_file)
