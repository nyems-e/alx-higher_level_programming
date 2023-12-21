#!/usr/bin/python3
""" 
This a square module descibing the square class
"""


class Square:
    """
    This a square module descibing the square class

    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        """
        This is the __init__ method

        Args: 
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
