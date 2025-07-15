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
        if isinstance(value,int):
            raise TypeError(f"{name}must be an integer")
        if value <= 0 :
            raise ValueError(f"{name} must be greater than 0")
        
