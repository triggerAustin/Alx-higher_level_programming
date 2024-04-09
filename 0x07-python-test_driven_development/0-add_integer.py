#!/usr/bin/python3

def add_integer(a, b=98):
    """
        Addition function for two integers

        Args:
            @a: first integer, has to be integer or float
            @b: second integer, defaulted to 98, has to be integer or float

        Return:
            returns the sum of both numbers
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
