#!/usr/bin/python3
""" A class Square definition"""


class Square:
    """ class square defines a square by size """
    def __init__(self, size):
        """ initializes the object square
          Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
