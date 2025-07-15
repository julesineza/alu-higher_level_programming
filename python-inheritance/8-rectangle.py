#!/usr/bin/python3

"""Renctangle class """

class Rectangle(BaseException):
    """Rectangle class inherits from BaseGeometry """
    def __init__(self,width, height):
        """ Rectangle intitilization and validation of width and height through integer_validator from BaseGeometry"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width=width
        self.__height=height
        
