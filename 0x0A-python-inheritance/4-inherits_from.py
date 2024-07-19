#!/usr/bin/python3

"""
This module contains a fn inherits_from
"""


def inherits_from(obj, a_class):
    """
    check if obj is instance of subclass of a class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
