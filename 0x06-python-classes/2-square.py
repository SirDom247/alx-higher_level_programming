#!/usr/bin/python3
"""creating a square class with exceptions"""


class Square:
    """class with an integer attribute size.
    size must be a private attribute
    exceptions for TypeError and ValueError must
    be included in instance with custom messages"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            """handle exceptions then initialize data"""
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
