#!/usr/bin/python3
"""
Addition Module
"""


def add_integer(a, b=98):
    """
    Function that adds two integers

    Args:
        a (number): Float or Integer
        b (:obj:number, optional): Optional Float or Integer

    Raises:
        TypeError: not float or integer

    Returns:
        float:int: Integer or float
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    if (float("nan") == a or float("nan") == b):
        raise TypeError("Nan is not a number")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
