#!/usr/bin/python3
"""creating a class with private attribute"""


class Square:
    """Representation of a square.
    with no type or value verification"""
    def __init__(self, size):
        """private attribute size"""
        self.__size = size
