#!/usr/bin/python3

""" function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""

def append_write(filename="", text="") :
    """uses mode=a to append to a file and not overright the file"""

    with open(filename, mode='a', encoding="utf-8") as myfile :
        myfile.write(text)
    return len(text)