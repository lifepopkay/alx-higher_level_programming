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
        else:
            if op == '+':
                print(f"{a} {op} {b} = {a + b}")
            elif op == '*':
                print(f"{a} {op} {b} = {a * b}")
            elif op == '/':
                print(f"{a} {op} {b} = {a / b}")
            else:
                print(f"{a} {op} {b} = {a - b}")
    else:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
