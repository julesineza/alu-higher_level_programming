#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = 0
    for nums in my_list:
        if nums > biggest:
            biggest = nums
    print("Max: {:d}".format(biggest))
