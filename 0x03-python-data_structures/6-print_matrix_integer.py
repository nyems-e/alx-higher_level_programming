#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for seq in matrix:
            if len(seq) == 3:
                print("{:d} {:d} {:d}".format(*seq))
            elif len(seq) == 2:
                print("{:d} {:d}".format(*seq))
            elif len(seq) == 1:
                print("{:d}".format(*seq))
            else:
                print("")
