#!/usr/bin/python3

def square_stuff(num):
    return (num**2)


def square_matrix_simple(matrix=[]):
    return ([list(map(square_stuff, i) for i in matrix)])
