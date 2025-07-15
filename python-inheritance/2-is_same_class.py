#!/usr/bin/python3

"""Is came_class checks ifthe object is exactly an instance of the specified class """
def is_same_class(obj, a_class):
    """Uses isinctance to check if a_class is an instnce of obj if true returns true else returns false"""
    return type(obj) is a_class

