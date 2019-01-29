"""Commented this out so I can isolate what I was working on"""
# import os
# from loader_functions.instantiator import *
# from pydoc import locate
# import sys
# import inspect

# clean_component_list = []
# master_component_dataset = {}

# """We use this class to dynamically fetch all the components in the component directory
# We then create a master list that we can use when attaching components by using the JSON FILES"""
# exceptions = ['__', "fetcher", "event"]


# def fetch_directory_components(directory):
#     global clear_component_list
#     component_list = os.listdir(directory)
#     for component_string in component_list:
#         # dunno how to do this in a for loop with an exception list, we need to figure it out
#         # and "event" not in component_string:
#         if "__" not in component_string and "fetcher" not in component_string:
#             clean_component_list.append(component_string[:-3])
#     return clean_component_list

# # refactor this shittttttttt


# def create_master_component_dataset(comp_list):
#     for component_string in comp_list:
#         my_class_module = locate('components.' + component_string)
#         my_class = inspect.getmembers(my_class_module, inspect.isclass)
#         # print(my_class)
#         master_component_dataset[component_string] = my_class[0][1]

#         # implement a way to make sure this list is clean

#     #print("master component dataset :  " , master_component_dataset)
#     return master_component_dataset
