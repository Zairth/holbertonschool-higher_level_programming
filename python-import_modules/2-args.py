#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    if len == 0:
        print("{} arguments.".format(len))
    else:
        print("{} arguments:".format(len))
        for i in range(1, len + 1):
            print("{}: {}".format(i, sys.argv[i]))
