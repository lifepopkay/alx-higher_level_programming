#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_key = list(a_dictionary.keys())
    list_key.sort()
    for key in list_key:
        print(f'{key}: {a_dictionary.get(key)}')
