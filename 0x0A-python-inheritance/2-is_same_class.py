#!/usr/bin/python3
"""
This module defines a function is_same_class
"""

def is_same_class(obj, a_class):
    """
    Function checks if obj is exactly an instance of a_class
    Args:
        obj: instance of a class
        a_class: class to compare to obj
    Returns:
        True if obj is exactly an instance of a_class, otherwise False
    """
    obj_class = type(obj)
    if obj_class == a_class:
        return True
    return False
