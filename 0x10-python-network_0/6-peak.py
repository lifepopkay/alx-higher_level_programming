#!/usr/bin/python3
# Write a function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    num = 0
    if list_of_integers is not None:
        for i in list_of_integers:
            if i > num:
                num = i
        return num
