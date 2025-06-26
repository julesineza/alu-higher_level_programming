#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last-dig=number[-1]
if Last-dig > 5:
    print(f"Last digit of {number} is {Last-dig} and is greater than")
elif Last-dig == 0:
    print(f"Last digit of {number} is {Last-dig} and is 0")
else:
    print(f"Last digit of {number} is {Last-dig} and is less than 6 and not 0")
