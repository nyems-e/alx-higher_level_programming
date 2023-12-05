#!/usr/bin/python3
def no_c(my_string):
    new_s = ''
     for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_s += i
     return (new_s)
