#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    l_dig = 0
elif number > 0:
    l_dig = int(str(number)[-1])
else:
    l_dig = -1 * (int(str(number)[-1]))
if l_dig == 0:
    sent = "and is 0"
elif l_dig > 5:
    sent = "and is greater than 5"
elif l_dig < 6 and l_dig != 0:
    sent = "and is less than 6 and not 0"
print(f'Last digit of {number:d} is {l_dig:d} {sent}')
