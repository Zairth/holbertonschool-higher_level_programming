#!/usr/bin/python3

for i in range(0, 26):
    if i % 2 == 0:
        k = chr(122 - i)
    else:
        k = chr(90 - i)
    print("{}".format(k), end="")
