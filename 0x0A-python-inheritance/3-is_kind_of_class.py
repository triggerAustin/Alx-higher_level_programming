#!/usr/bin/python3

"""
module defines a method is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if is instance of class or any inherited class in a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
