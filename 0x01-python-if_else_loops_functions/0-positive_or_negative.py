#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (True):
    match number:
        case number > 0:
            print("{} is positive".format(number))
        case number = 0:
            print("{} is zero".format(number))
        case _:
            print("{} is negative".format(number))
