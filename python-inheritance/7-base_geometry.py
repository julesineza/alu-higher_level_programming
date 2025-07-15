#!/usr/bin/python3

"""Base Geometry class"""

class BaseGeometry :
    """area function returns an expection message"""
    def area(self):
        """"uses Expection to return the message """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """uses isinstance to check if value is an integer and also checks if value is less or equal to 0 and
        raises errors"""
        if type(value) != int :
            raise TypeError("<name> must be an integer")
        if value <= 0 :
            raise ValueError("<name> must be greater than 0")
        

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))