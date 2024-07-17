#!/usr/bin/python3

"""
This module contains a method to look up methods and attr of an object
"""


def lookup(obj):
    """
    Return list of attributes or methods
    args:
        obj - object containing said attributes
    Returns:
        list of attr or methods
    """

    return dir(obj)
