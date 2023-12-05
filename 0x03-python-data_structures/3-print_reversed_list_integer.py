#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        acc = my_list[::-1]
        for i in acc:
            print("{:d}".format(i))        
