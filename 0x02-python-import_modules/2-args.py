#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(f"{len(sys.argv)} arguments")
else:
    print(f"{len(sys.argv)} arguments")

    for i, arg in enumerate(sys.argv):
        print(f"{i}: {arg}")

