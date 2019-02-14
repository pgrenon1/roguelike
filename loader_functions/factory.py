import pyclbr
import enum
import sys
import inspect
import json
import config
from components import *


class Factory:
    def __init__(self, scene, path="data/entities.json"):
        self.scene = scene
        self.annotations = self.get_annotations(module_name="components")
        self.database = self.load_json(path)
        # self.components_templates = self.get_component_templates()
        self.validate_data(self.database)
        self.entities_blueprints = self.construct_entities_blueprint()

    def get_annotations(self, module_name="components"):
        module = pyclbr.readmodule(module_name)
        # del module["Enum"]
        # del module["RenderOrder"]
        class_to_annotations = {}
        for class_object in module:
            clazz = getattr(sys.modules[module_name], class_object)
            # if type(clazz) is enum.EnumMeta:
            #     render_order_options = [e.name for e in clazz]
            # else:
            class_name = class_object
            signature = inspect.getfullargspec(clazz)

            if not signature.annotations:
                class_to_annotations[class_object] = {}
            else:
                class_to_annotations[class_object] = signature.annotations

        return class_to_annotations

    def load_json(self, path):
        with open(path) as f:
            data = json.load(f)
            return data

    def validate_data(self, raw):
        pass

    def construct_entities_blueprint(self):
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
        components = self.entities_blueprints[entity_name]
        self.scene.world.add_component(new_entity, Position(x, y))
        for component in components:
            self.scene.world.add_component(new_entity, component)

        return new_entity
