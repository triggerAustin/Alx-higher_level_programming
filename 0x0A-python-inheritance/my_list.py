#!/usr/bin/python3
"""
This module defines a function is same class
"""

def is_same_class(obj, a_class):
    """
    function checks if obj is exactly an instance of a_class
    Args:
        obj: instance of a class
        a_class: class to compare to obj
    """
    if isinstance(obj, a_class):
        return (True)
    False
