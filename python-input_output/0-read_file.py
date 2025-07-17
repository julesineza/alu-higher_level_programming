#!/usr/bin/python3

"""a function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """use with and read mode to read the file that was given"""
    with open(filename,encoding="utf-8") as myfile:
        return myfile.read()


