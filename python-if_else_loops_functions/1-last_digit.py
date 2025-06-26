#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last-dig=abs(number)%10
    last-dig=last-dig * -1
else:
    last-dig=number%10
if last-dig > 5:
    print(f"Last digit of {number} is {Last-dig} and is greater than")
elif last-dig == 0:
    print(f"Last digit of {number} is {Last-dig} and is 0")
else:
    print(f"Last digit of {number} is {Last-dig} and is less than 6 and not 0")
