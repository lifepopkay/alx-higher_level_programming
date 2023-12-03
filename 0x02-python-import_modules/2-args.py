#!/usr/bin/python3

if __name__ == "main":
    from sys import argv

    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    for i, arg in enumerate(argv[1:]):
        print("{}: {}"format(i, arg))
