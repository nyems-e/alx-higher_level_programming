#!/usr/bin/python3
#-*- coding:utf-8 -*-
""" Square Class

Defines square attributes
"""

class Square:
    """Class that defines a square shape"""
    def __init__(self, size):
        """___init__ method for square class.

        Args:
        size(:obj:`int'): size of square
        """
        self.__size = size
