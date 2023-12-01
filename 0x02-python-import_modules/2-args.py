#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 1:
        print(f"{len(sys.argv)} arguments")
else:
    print(f"{len(sys.argv)} arguments")

    for i, arg in enumerate(sys.argv):
        print(f"{i}: {arg}")
