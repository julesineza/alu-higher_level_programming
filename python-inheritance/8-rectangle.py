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
        

class Rectangle(BaseException):
    """Rectangle class inherits from BaseGeometry """
    def __init__(self, *args,width, height):
        """ Rectangle intitilization and validation of width and height through integer_validator from BaseGeometry"""
        super().__init__(*args)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width=width
        self.__height=height
        
