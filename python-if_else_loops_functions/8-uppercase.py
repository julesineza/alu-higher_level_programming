#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in range(len(str)):

        if 97 <= ord(str[i]) <= 122:
            upper = upper + chr(ord(str[i]) - 32)
        else:
            upper = upper + str[i]
            print("{}".format(upper))
