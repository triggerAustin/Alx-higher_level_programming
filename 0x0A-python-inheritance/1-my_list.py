#!/usr/bin/python3

"""
This module describes a class
has a fn prints a sorted list
"""


class MyList(list):
    """
    instance method that prints a sorted list
    """
    def print_sorted(self):
        """
        prints a sorted list: ascending
        """
        print(sorted(self))
