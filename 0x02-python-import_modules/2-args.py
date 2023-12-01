#!/usr/bin/python3

if __name__ == "__main__":
    import sys.argv as sa

    n = len(sa) - 1

    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))

    for i, arg in enumerate(n):
        print(f"{i}: {arg}")
