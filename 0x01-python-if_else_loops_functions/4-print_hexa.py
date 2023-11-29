#!/usr/bin/python3
for num in range(0, 99):
    print("{num_A:d} = {hex_n}".format(
        hex_n=hex(num), num_A=num), end="\n")
