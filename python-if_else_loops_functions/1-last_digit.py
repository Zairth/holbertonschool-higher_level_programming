#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
if number < 0:
    number *= -1
number %= 10
print("{0} and is".format(number), end=" ")
if number > 5:
    print("greater than 5")
elif number == 0:
    print("0")
else:
    print("less than 6 and not 0")
