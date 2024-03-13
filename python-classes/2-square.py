#!/usr/bin/python3
""" Defines a class square"""


class Square:
    """ class square defines a square by size """
    def __init__(self, size=0):
        """ initializes the object square
          Args:
            size (int): size of a side of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
