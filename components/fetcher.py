import os
import instantiator

clean_component_list = []
master_component_dataset = {}


def fetch_directory_components():
    global clear_component_list
    component_list = os.listdir('components')
    for component_string in component_list:
        if "__" not in component_string:

            clean_component_list.append(component_string.strip('.py'))
    return clean_component_list


def create_master_component_dataset(comp_list):
    pass
#    for component_string in comp_list:
