#!/usr/bin/python3

"""is_kinf_of_class is a function that checks the object is an instance of, or if the object is an 
instance of a class that inherited from, the specified class
returns True is true and false otherwise"""
def is_kind_of_class(obj, a_class) :
    """Uses is insatnace to check if obj is an instance of a_class or even 
    if its an object of an instance of a class that was inherited"""
    return isinstance(obj,a_class)
