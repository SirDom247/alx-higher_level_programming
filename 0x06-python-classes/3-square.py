#!/usr/bin/python3
""" creating a public and private attribute
within a class"""


class Square:
    """class that returns the square
    of a private instance"""
    def __init__(self, size=0):
        """private instance size
        with exception handlers
        for typeError if size is not an int
        valueError if size < 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public instance area
        returns the square of size"""
        return self.__size ** 2
