#!/usr/bin/python3
"""
Module to print sorted list
"""


class MyList(list):
    """
    Class that inherits from list
    """

    def print_sorted(self):
        """
        prints a sorted list
        """
        sorted_list = list.copy()
        sorted_list.sort()
        print(sorted_list)
