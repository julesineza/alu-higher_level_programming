#!usr/bin/python3
def uppercase(str):
    upper = ""
    for i in range(len(str)):
        if 97 >= ord(str[i]) <= 122:
            str[i] = ord(str[i]) - 32
            upper = upper + chr(str[i])
        else:
            upper = upper + str[i]

    return upper         
