#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")
    else:
        print("{} arguments:".format(count))
        for i, item in enumerate(argv[1:], start=1):
            print(f"{i}: {item}")
