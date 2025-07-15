#!/usr/bin/python3

"""inherits_from is a function that checks the object is an instance of, or if the object is an 
instance of a class that inherited from, the specified class
returns True is true and false otherwise"""

def inherits_from(obj, a_class) :
    """Uses is insubcalss to check if the object is an instance of a class that inherited (directly or indirectly) from the specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
