#!/usr/bin/python3
def no_c(my_string):
    if 'c' in my_string:
        n = my_string.remove(c)
        return n
    elif 'C' in my_string:
        n = my_string.remove(c)
        return n
    else:
        return my_string
