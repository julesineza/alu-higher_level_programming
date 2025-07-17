#!/usr/bin/python3

"""a function that returns the JSON representation of an object (string)"""

import json

def to_json_string(my_obj):
    """uses json.dumps to jsonify the my_obj parameter"""
    return json.dumps(my_obj)