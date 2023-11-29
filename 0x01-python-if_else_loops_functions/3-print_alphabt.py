#!/usr/bin/python3
for uni_code in range(97, 123):
    if uni_code != 101 and uni_code != 113:
        print("{}".format(chr(uni_code)), end="")
