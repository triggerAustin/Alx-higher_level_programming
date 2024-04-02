#!/usr/bin/python3
"""define a class square"""

class Square:
    """
        class of a square with size attr

        Attributes:
            size: size of one side of square
    """

    def __init__(self, size = 0, pos = (0, 0)):
        """
        constructor initializes __size to size

        Args:
            size: initialized to 0
        """
        
        self.__size = size
        self.__position = pos

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

    @property
    def position(self):
        """
        to get the position of the square

        Return: position
        """

        return self.__position

    @position.setter
    def position(self, pos):
        """        to set the attr position

        Args:
            position: tuple of x, y co-ordinates

        Raises:
            TypeError: size has to be int
            ValueError: size has to be >= 0
        """

        self.__position = pos

        if not isinstance(pos, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(pos[0], int) or not isinstance(pos[1], int):
            raise TypeError("poition must be a tuple of 2 positive integers")
        if pos[0] < 0 or pos[0] < 0:
            raise TypeError("poition must be a tuple of 2 positive integers")
        self.__position = pos

    def my_print(self):
        """
        to draw a square of area size ** size
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * self.__size)
