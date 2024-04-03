#!/usr/bin/python3
"""Square class definition"""

class Square:
    """Square class body"""

    def __init__(self, size):
        """Square constructor
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Square getter for __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Square setter for __size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """Print stdout the square with the character"""
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
