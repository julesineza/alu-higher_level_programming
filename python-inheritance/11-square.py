#!/usr/bin/python3
"""
Module that defines a Square class inheriting from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initialize a square with validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)