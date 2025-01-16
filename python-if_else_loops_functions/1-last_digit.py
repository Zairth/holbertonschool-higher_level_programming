#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")
last_digit = number
if last_digit < 0:
    last_digit *= -1
last_digit %= 10
print("{} and is".format(last_digit), end=" ")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
elif last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0")
