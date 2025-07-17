#!/usr/bin/python3

"""function that creates an Object from a “JSON file"""

import json
def load_from_json_file(filename):
    """uses json.parse to convert data fromthe filename to an object """
    with open(filename,mode="r",encoding="utf-8") as myfile:
        data=myfile.read()
        json.parse(data)