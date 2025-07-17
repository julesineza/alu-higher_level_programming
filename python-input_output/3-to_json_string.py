#!/usr/bin/python3
import json
"""a function that returns the JSON representation of an object (string)"""
def to_json_string(my_obj):
    """uses json.dumps to jsonify the my_obj parameter"""
    return json.dumps(my_obj)