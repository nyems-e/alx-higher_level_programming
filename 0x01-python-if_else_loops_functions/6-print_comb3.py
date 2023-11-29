#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i == 8 and x == 9:
            print("{:d}{:d}".format(i, x),end = "\n")
        elif i != x and i < x:
            print("{:d}{:d}".format(i, x), end=", ")
print("\n")


