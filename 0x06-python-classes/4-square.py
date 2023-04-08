#!/usr/bin/python3
"""a class that returns the area of a square"""


class Square:
    """ use setter to place the attributes of the
    class and getter to retrieve the values from
    the class. add a private attribute size and
    public attribute area"""

    def __init__(self, size=0):
        """ initialize the data"""
        self.__size = size

    @property
    def size(self):
        """ initialize getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2
