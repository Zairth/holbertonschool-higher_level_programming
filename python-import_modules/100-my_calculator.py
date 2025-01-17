#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argv_len = len(argv) - 1

    if argv_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = ".format(argv[1], argv[2], argv[3]), end="")
    if argv[2] == "+":
        print("{}".format(add(int(argv[1]), int(argv[3]))))
    elif argv[2] == "-":
        print("{}".format(sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == "*":
        print("{}".format(mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == "/":
        print("{}".format(div(int(argv[1]), int(argv[3]))))