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
        if not isinstance(value,int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0 :
            raise ValueError(f"{name} must be greater than 0")
        

class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Validates and sets private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
