"""Commented this out so I can isolate what I was working on"""
import os
from loader_functions.instantiator import *
from pydoc import locate
import sys
import inspect
from config import *
import importlib
from components import *

"""We use this class to dynamically fetch all the components in the component directory
We then create a master list that we can use when attaching components by using the JSON FILES"""


def fill_data_list(name):
    import pyclbr
    data_list = []
    module_name = name
    module_info = pyclbr.readmodule(module_name)
    # print(module_info)

    for item in module_info.values():
        if(item.name != "Enum"):
            data_list.append(item.name)
    return data_list


# refactor this shittttttttt


def create_master_component_dataset(comp_list):
    component_dataset = {}
    for comp_name in comp_list:
        if(comp_name != "RenderOrder"):
            component_dataset[comp_name] = getattr(
                sys.modules['components'], comp_name)

        # implement a way to make sure this list is clean

    return component_dataset
