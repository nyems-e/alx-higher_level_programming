#!/usr/bin/python3
"""
Module file
"""


def is_same_class(obj, a_class):
    """
    Function

    Args:
        obj (obj): object 1
        a_class (obj): object 2

    Returns:
        bool: if same True else False
    """

    return type(obj) is a_class
