#!/usr/bin/python3
"""
Module details
"""


class BaseGeometry():
    """
    My class
    """

    def area(self):
        """
        Function area

        Raises:
            Exception: all the time
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function integer_validator
        Args:
            name (str): string
            value (int): intger

        Raises:
            TypeError: when not int
            ValueError: when below 1
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
