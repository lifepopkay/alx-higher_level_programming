#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) == 4:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])

        if op != '+' and op != '-' and op != '*' and op != '/':
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)

        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
