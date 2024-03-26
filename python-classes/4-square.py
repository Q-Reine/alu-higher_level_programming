#!/usr/bin/python3
""" Defines a class Square"""


class Square:
    """ class square defines a square by size:
    size must be an integer
    size must not be negative
    """
    def __init__(self, size=0):
        """ Initializes the object square
          Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.size = size

    def area(self):
        """calculates the area of a square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """ gets the value of __size
         Returns:
            The size of the square
         """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of __size
         value (int): the value of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
