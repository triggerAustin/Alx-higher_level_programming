#!/usr/bin/python3
"""defines a class square"""

class Square:
    """
    class square with size attribute
    Atrribute:
        size: size of one side of square
    """

    def __init__(self, size=0):
        """
        constructor for class initializes __size to size
        
        Args:
            size: should be more than 0 and type int
        """

        self.__size = size
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        method to calculate Area

        Args:
            self:class instance

        Return:
            Area: area of the square
        """
        return self.__size * self.__size
