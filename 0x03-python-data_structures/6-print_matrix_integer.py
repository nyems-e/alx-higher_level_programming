#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for seq in matrix:
            if seq:
                print("{:d} {:d} {:d}".format(*seq))
            else:
                print("")
