#!/usr/bin/python3

"""write file getts the filename and the text to be written in the file then writes to that files"""

def write_file(filename="", text=""):

    """we use with -> with open to write to a file and len() to get the length of the text parameter"""

    with open(filename , mode="w" , encoding="utf-8") as myfile:
        myfile.write(text)
    return(len(text))
      