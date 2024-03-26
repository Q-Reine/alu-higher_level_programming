#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class square inherits from rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

