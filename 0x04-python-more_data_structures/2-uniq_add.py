#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_q = set(my_list)
    result = 0

    for i in n_q:
        result += i
    return result
