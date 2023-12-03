#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) == 4:
        a = argv[1]
        b = argv[3]
        op = argv[2]

        if op != '+' and op != '-' and op != '*' and op != '/':
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
        else:
            if op == '+':
                print(f"{a} {op} {b} = {add(a,b)}")
            elif op == '*':
                print(f"{a} {op} {b} = {mul(a,b)}")
            elif op == '/':
                print(f"{a} {op} {b} = {div(a,b)}")
            else:
                print(f"{a} {op} {b} = {sub(a,b)}")
    else:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
