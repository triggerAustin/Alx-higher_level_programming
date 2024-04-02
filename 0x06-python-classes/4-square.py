#!/usr/bin/python3
"""define a class square"""

class Square:
    """
        class of a square with size attr

        Attributes:
            size: size of one side of square
    """

    def __init__(self, size = 0):
        """
        constructor initializes __size to size

        Args:
            size: initialized to 0
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

    @property
    def size(self):
        """
        to get the size of the side of a square

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        to set the property __size to size

        Args:
            size: size of one side of square

        Raises:
            TypeError: size has to be int
            ValueError: size has to be >= 0
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


