"""This class will contain generic helpers that are meant to help us with our programming, debugging, etc"""
import config


def debug(arg):
    if(config.VERBOSE_MODE):
        print(arg)
