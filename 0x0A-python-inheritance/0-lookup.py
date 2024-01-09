#!/usr/bin/python3
"""
Module to print class attributes
"""


def lookup(obj):
    """
    function returns list of available attributes and methods

    Args:
        obj (object): Object to print contents of

    Returns:
        list: List of attributes
    """
    return dir(obj)
