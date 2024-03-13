#!/usr/bin/python3
""" Defines a square"""


class Square:
    """ class square defines a square by size """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): position of the square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

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
        """ sets the value of __size
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

    def my_print(self):
        """
       Prints graphic representaion of square instance
        """
        if self.size == 0:
            print("")
            return
        for i in range(self.size):
            print("\n" * self.position[1], end="")
            print(" " * self.position[0] + "#" * self.size)

    @property
    def position(self):
        """gets the current position of square instance.
           Returns:The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Sets the value for position
               Args:
                 value (tuple): The position of the square
            Returns: None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
