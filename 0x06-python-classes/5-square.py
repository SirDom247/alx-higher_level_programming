#!/usr/bin/python3
"""that prints the area of a square"""


class Square:
    """a class with a private attribute
    size and public attributes area and my_print
    that prints a square"""

    def __init__(self, size=0):
        """initialize the data"""
        self.__size = size

    @property
    def size(self):
        """getter for private instance size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for the private attribute size
        set size to the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
