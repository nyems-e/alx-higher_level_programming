#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if any(matrix):
        for i in matrix:
            print("{} {} {}".format(*i))
